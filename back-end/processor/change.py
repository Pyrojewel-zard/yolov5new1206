# -*- coding = utf-8 -*-
# @Time : 2021/12/15 13:55
# @Author : lml
# @File : 1.py
# @Software : PyCharm
from PIL import  ImageFilter

class MyGaussianBlur(ImageFilter.Filter):
  name = "GaussianBlur"   # 高斯模糊

  def __init__(self, radius=2, bounds=None):
    self.radius = radius
    self.bounds = bounds

  def filter(self, image):
    if self.bounds:
      clips = image.crop(self.bounds).gaussian_blur(self.radius)
      image.paste(clips, self.bounds)
      return image
    else:
      return image.gaussian_blur(self.radius)

