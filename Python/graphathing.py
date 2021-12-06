import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()
x=0
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
padding = 2
shape_width = 20
top = padding
bottom = height-padding

pos_x = 0
max_x = 0
disp.begin()
pixelList = []
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
#128, 64

while True:
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
  
  pos_x += accel_x
  
  #y = round((max_x/64) * pos_x)
  
  # pixelList = pixelList + y
  if len(pixelList) > 128:
    pixelList.pop(0)

  if pos_x > max_x:
    max_x = pos_x
    redo = time
    while redo < 0:
      draw.rectangle((0,0,width,height), outline=0, fill=0)
      display.pixel((redo-1),round(max_x/64) * pos_x)
      y = round((max_x/64) * pos_x)
                            
  display.pixel(time, y)

  display.pixel(timer,
  draw.text((x,top+20), "y: " + (str(round(accel_y / 107, 3))), font=font, fill=225)
  #draw.text((x,top+20), 'Accel Y='+str(accel_y), font=font, fill=225)
 # draw.text((x,top+40), 'Accel Z='+str(accel_z), font=font, fill=225)
  #time.sleep(.5)
  disp.image(image)
