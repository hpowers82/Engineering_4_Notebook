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
l = 128
h=64  
disp.begin()
pixelList = []
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
if time < l:
  draw.rectangle((0,0,l,h), outline=0, fill=0)
while True:
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
  accel_x=abs(accel_x)
  draw.rectangle((time + 1, 0, 1, height), outline=0, fill=0)
  pixelList.append(accel_x)
  if len(pixelList) > l:
    pixelList.pop(0)

  if accel_x > max_x:
    max_x = accel_x
    redo = 0
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    while redo <= time:
      display.drawPixel((redo),(round(max_x/h) * int(pixelList[redo])))
      redo += 1
  else:  
    y = round((max_x/h) * pos_x)
    display.drawPixel(time,y)
  time += 1
  if time > 128:
    time = 0
  disp.image(image)
