# Python weather display

Takes data from my wsview weather station data interface ( https://github.com/Kincade120/wsview-weather-station-interface ) ad displays it on an OLED screen.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install requriements.txt
```

## Usage

There are two services in the application, the first is the flask api in api.py. The second is the spi controller in main.py. 

I used a cheap OLED spi display from Waveshare (https://www.waveshare.com/2.23inch-oled-hat.htm)

![alt text](https://i.imgur.com/9f5DbV8l.jpg)

```bash
screen -S api
python api.py 
```

Detach with Ctrl+A+D

```bash
screen -S display
python main.py 
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

