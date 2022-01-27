import os
import time
import picamera


print("start")
initial_count = 0
dir = "../pictures"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('../pictures/image_'+str(initial_count+1) + '.jpg')
print("done")
