raspicam-timelapse-lcd
======================

Use the Adafriut Lcd Controller for taking Raspberry Pi camera stills for making a time lapse video.
This project is inspired on [rpi-timelapse](https://github.com/dps/rpi-timelapse)


## Hardware

* Raspberry Pi
* Raspberry Pi Camera
* [Adafruit Lcd Controller](http://www.adafruit.com/products/1110)

## Software Requirements

* Rasbian OS (should work also on others)
* Adafriut Lcd Libraries (should be included in here in the future)
* Python modules: (wip...)

## Install

```
$ git clone https://github.com/kappy/raspicam-timelapse-lcd.git
$ cd raspicam-timelapse-lcd
$ sudo chmod +x tl.py
$ sudo ./tl.py
```

You'll find the photos taken inside a date folder on your home

## Run on boot

```
cp tl /etc/init.d/tl
$ sudo chmod +x /etc/init.d/tl
$ sudo chmod +x /etc/init.d/lcd
```
