#!/usr/bin/python

from time import sleep, strftime
from datetime import datetime
import picamera
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import Adafruit_MCP230XX
import Adafruit_CharLCD as LCD

#VIDEO_DAYS = 5
FRAMES_PER_HOUR = 6
#FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS
ROTATION = 90

lcd = LCD.Adafruit_CharLCDPlate()
lcd.backlight(lcd.ON)

def capture_frame(path, frame):
    lcd.clear()
    lcd.message('Shooting #%03d' % frame)
    with picamera.PiCamera() as cam:
        cam.rotation(ROTATION)
        time.sleep(2)
        cam.capture('%s/frame%03d.jpg' % (path, frame))

#create directory with date
date = datetime.now().strftime('%b %d')
directory = '/home/pi/%s' % date
if not os.path.exists(directory):
    os.makedirs(directory)

# Capture the images
while True:
    # Note the time before the capture
    start = time.time()
    capture_frame(directory, frame)
    # Wait for the next capture. Note that we take into
    # account the length of time it took to capture the
    # image when calculating the delay
    while True:
        seconds_to_next = int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
        if seconds_to_next <= 0:
            break
        lcd.clear()
        lcd.message('taken: %03d' % frame)
        lcd.message('next: %s' % str(datetime.timedelta(seconds=seconds_to_next)))
        time.sleep(1)
