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

disp.begin()
disp.clear()
disp.display()

width=disp.width
height = disp.height
image = Image.new('1', (width,height))
draw=ImageDraw.Draw(image)
padding = 2
shape_width = 20
top = padding
bottom = height-padding

font = ImageFont.load_default()
while True:
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
 # draw.text((x,top+20), 'Accel X='+str(accel_x), font=font, fill=225)
  draw.text((x,top+20), "y: " + (str(round(accel_y / 107, 3))), font=font, fill=225)
  #draw.text((x,top+20), 'Accel Y='+str(accel_y), font=font, fill=225)
 # draw.text((x,top+40), 'Accel Z='+str(accel_z), font=font, fill=225)
  #time.sleep(.5)
  disp.image(image)

