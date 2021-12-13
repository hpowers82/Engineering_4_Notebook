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
width = 128 ## first input in print is width
height = 64  ##  second input in print is height
disp.begin()
pixelList = []
for i in range(128):
 pixelListList.append(0)
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
def getY(pixelList,redo):
 # y=round((int(pixelList[redo])/int(max(pixelList))*64)
  y=round(64*((int(pixelList[redo])/int(max(pixelList)))))
  return y
while True:
  time += 1
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
  accel_x=abs(accel_x)
  print(accel_x)
  redo = 0 
  pixelList.append(accel_x)
  pixelList.pop(0)
  
  while redo < 128:
    getY()
    draw.rectangle((redo,y,redo,y), outline=225,fill=225)
  redo += 1



      
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
    
  disp.image(image)
