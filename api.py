
from pymemcache.client import base
from flask import Flask, request

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def index():
    # POST request
    if request.method == 'POST':
        client = base.Client(('127.0.0.1', 11211))
        data = request.get_json()
        print("Incoming...")
        windBearing = data["winddir"]
        windDirection = "N"
        if windBearing >= 0 and windBearing <= 22 or windBearing >= 337 and windBearing <= 360:
            windDirection = "N"
        elif windBearing >= 23 and windBearing <= 67:
            windDirection = "NE"
        elif windBearing >= 68 and windBearing <= 112:
            windDirection = "E"
        elif windBearing >= 113 and windBearing <= 157:
            windDirection = "SE"
        elif windBearing >= 158 and windBearing <= 202:
            windDirection = "S"
        elif windBearing >= 203 and windBearing <= 247:
            windDirection = "SW"
        elif windBearing >= 248 and windBearing <= 292:
            windDirection = "W"
        elif windBearing >= 293 and windBearing <= 336:
            windDirection = "Nw"

        client.set('windDir', windDirection)
        client.set('windSpd', round(data["windspeedmph"]))
        client.set('windSpdGust', round(data["windgustmph"]))
        client.set('temp', round(data["tempc"]))
        client.set('humidity', round(data["humidity"]))

        
        return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')