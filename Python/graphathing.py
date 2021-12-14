import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303
import time

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

redo = 0
y=0
oldMax=0
pixelList = []
for i in range(128):
 pixelList.append(0)

disp.begin()

font = ImageFont.load_default()
draw = ImageDraw.Draw(image)

while True:
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
  accel_x=abs(accel_x)
  #print(accel_x)
  pixelList.append(accel_x)
  pixelList.pop(0)
  #print(pixelList)
  #y=round(pixelList[127]/max(pixelList)*64,0)
  #print(y)
  if oldMax > max(pixelList):
   for x in range(3):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x,top+20), "resetting."+"."*redo, font=font, fill=225)
    redo += 1
   disp.image(image)
   time.sleep(2)
   draw.rectangle((0,0,width,height), outline=0, fill=0)
  elif redo < 128:
    y=round(pixelList[redo]/max(pixelList)*64,0)
    draw.rectangle((redo,y,redo,y), outline=225,fill=225)
    redo += 1
    print(redo)
    print(y)
  redo = 0
  oldMax=max(pixelList)
  disp.image(image)
  time.sleep(.1)


      
  # time < 128:
   # redo = 128
#    #for i in range(time):
 #     if pixelList[redo] = 0
  #    getY()
   #   draw.rectangle((redo,y,redo,y), outline=225,fill=225)
 #     redo += 1
 #   redo = 0
    
 # if len(pixelList) >= 128:
 #   draw.rectangle((0,0,disp.width,disp.height), outline=0, fill=0)
  #  redo = 0
   # for i in 128:
   #     findY()
    #    draw.rectangle((redo,y,redo,y), outline=225,fill=225)
     #   redo += 1
  oldMax=max(pixelList)
