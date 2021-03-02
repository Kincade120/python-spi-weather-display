#!/usr/bin/python3

import os
import time
import sys
sys.path.append('./drive')
import json

import SPI
import SSD1305

from pymemcache.client import base

# from octorest import OctoRest
from PIL import ImageFont, Image, ImageDraw

from datetime import datetime

def makeFont(name, size):
    font_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'fonts',
            name
        )
    )
    return ImageFont.truetype(font_path, size)


def main():
    client = base.Client(('127.0.0.1', 11211))
    client.set('windDir', "N")
    client.set('windSpd', 0)
    client.set('windSpdGust', 0)
    client.set('temp', 0)
    client.set('humidity', 0)
    
    try:
        RST = None 
        DC = 24
        SPI_PORT = 0
        SPI_DEVICE = 0

        disp = SSD1305.SSD1305_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

        disp.begin()

        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = 0
        top = padding
        bottom = height-padding
        x = 0

        font = makeFont("04B_08__.TTF", 8)
        
        
        while True:
                    draw.rectangle((0,0,width,height), outline=0, fill=0)
                    now = datetime.now()
                    draw.text((x, top), now.strftime("%d-%m-%Y, %H:%M:%S"), font=font, fill=255)
                    draw.text((x, top + 8), "Wind Direction : " + str(client.get('windDir').decode('UTF-8')), font=font, fill=255)
                    draw.text((x, top + 16), "Wind: " + str(client.get('windSpd').decode('UTF-8')) + "m/ph Gust:" + str(client.get('windSpdGust').decode('UTF-8')) + "m/ph", font=font, fill=255)
                    draw.text((x, top + 25), "Temp: " + str(client.get('temp').decode('UTF-8')) + "c Humidity: " + str(client.get('humidity').decode('UTF-8')) + "%", font=font, fill=255)
                    disp.image(image)
                    disp.display()
                    time.sleep(1)

    except KeyboardInterrupt:
        pass
    except ValueError as err:
        print(f"Error: {err}")
    except KeyError as err:
        print(f"Error: Please ensure the {err} environment variable is set")
 
if __name__ == '__main__':
    main()
