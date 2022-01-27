import os
from time import sleep
import picamera
from random import choice
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
effects = ['none', 'negative', 'sketch', 'denoise', 'emboss', 'oilpaint', 'hatch', 'gpen', 'pastel', 'watercolor', 'film', 'blur', 'saturation']
done = []
initial_count=0
dir = "../pictures"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1

for x in range(5):
	y=(choice([i for i in range(13) if i not in done]))
	done.append(y)
	camera.image_effect = effects[y]
	camera.capture('../pictures/image_'+str(initial_count+x+1) + '.jpg')
print("done")
