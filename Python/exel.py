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

disp.begin()

font = ImageFont.load_default()
draw = ImageDraw.Draw(image)


while True:
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
  draw.text((x,top), "Accel X:"+ (str(round(accel_x / 107, 3))), font=font, fill=225)
  draw.text((x,top+20), "Accel Y: " + (str(round(accel_y / 107, 3))), font=font, fill=225)
  draw.text((x,top+40), 'Accel Z:'+(str(round(accel_z / 107, 3))), font=font, fill=225)
  disp.image(image)
  disp.display()

