import cv2
from PIL import Image
from pytesseract import image_to_string

CURRENT_FRAME_FLAG = 1

videocap = cv2.VideoCapture('949.mp4')
success, image = videocap.read()
height, width, colors = image.shape
count = 0;
success = True
s = ''

while True:
  videocap.set(CURRENT_FRAME_FLAG, count*30)

  success, image = videocap.read()
  if success==False:
    break

  image = image[465:486, 160:906]
  s1 = image_to_string(Image.fromarray(image), lang='rus')

  if s!=s1:
    print s1
    s = s1
  
  count += 1


