import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303
lsm303 = Adafruit_LSM303.LSM303()
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_63(rst=RST, i2c_adress=0x3d)
disp.begin()
disp.clear()
disp.display()
width-disp.width
height=disp.height
image.new('1', (width, height))
padding = 2
shape_width = 20
top = padding
bottom = height - padding
while True:
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  draw.text((0,0), 'Accel X={0}'.format(accel_x), font=font, fill=225)
  draw.text((0,0), 'Accel Y={0}'.format(accel_y), font=font, fill=225)
  draw.text((0,0), 'Accel Z={0}'.format(accel_z), font=font, fill=225)
  display.clear()
      
