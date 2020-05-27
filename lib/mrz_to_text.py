import cv2
import pytesseract as pt


def mrzToText(img=None, imgpath=""):

  image = img if img is not None else cv2.imread(imgpath)
  config = ('-l eng --oem 1 --psm 3')
  config = ("-l mrz --psm 6 -c  tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789><"
                      " -c load_system_dawg=F -c load_freq_dawg=F ")

  text = pt.image_to_string(image, config=config)

  return text
