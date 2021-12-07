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
max_x = 1
time = 0
l = 128
h=64  
disp.begin()
pixelList = []
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,l,h), outline=0, fill=0)
while True:

  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
  accel_x=abs(accel_x)
  print(accel_x)
  redo = 0
  y=round((accel_x/max_x)*64)
  
  pixelList.append(accel_x)
  
  
  if len(pixelList) > l:
    pixelList.pop(0)
    
  if accel_x > max_x:
    max_x = accel_x
    y=round((accel_x/max_x)*64)
  if time >= 128:
    draw.rectangle((0,0,l,h), outline=0, fill=0)
    while redo <= len(pixelList):
        draw.rectangle((redo, round((int(pixelList[redo])/max_x) * 64) ,1,1), outline=225,fill=225)
        redo += 1
  else:
    draw.rectangle((time,y,1,1), outline=1, fill=1)
    print("time is:" +str(y)+"\nY is: "+str(y))
    time += 1
    
  disp.image(image)
