
from lib import getMRZFromImg, mrzToText, getMRZData
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", required=True, help="path to images directory")
args = vars(ap.parse_args())

imgpath  = args['i']

img = None
img  = getMRZFromImg(imgpath=imgpath)

# import cv2 
# outp = imgpath.split('/')[1]
# cv2.imwrite(outp, img)
if img is not None: 
  text = mrzToText(img)
  data, ty  = getMRZData(text)

  print(data)
