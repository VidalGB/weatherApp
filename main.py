#Python3.9.2
# -*- coding: utf-8 -*-

#Imports
import requests
import json
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import sys
import os
import csv

#Path search
def path(relativePath):
  try:
    bacePath = sys._MEIPASS
  except Exception:
    bacePath = os.path.abspath(".")
  return os.path.join(bacePath, relativePath)


#Read and write files functions
def read(obj):
  with open (path('data/data.csv'), 'r', encoding="utf-8") as file:
    content = csv.reader(file, delimiter = ';')
    for line in content:
      if line[0] == obj:
        return line[1]
  file.close()

def write(obj, writer):
  save = []
  n = 0
  with open (path('data/data.csv'), 'r', encoding="utf-8") as file:
    content = csv.reader(file, delimiter = ';')
    for line in content:
      if line[0] == obj:
        del line[1]
        del line[0]
      save.append(line)
    for element in save:
      if element == []:
        del save[n]
      n += 1
  with open (path('data/data.csv'), 'w', newline = '') as file:
    write = csv.writer(file, delimiter = ';')
    write.writerows(save)
    write.writerow([obj, writer])
  file.close()

#Main class app
class app(MDApp):
  #Gobal variables
  global screenManager
  screenManager = ScreenManager()

  def __init__(self, *args, **kwargs):
    MDApp.__init__(self, *args, **kwargs)
    self.title = 'Weather App'
    self.icon = None
    self.theme_cls.primary_palette = 'Orange'
    self.theme_cls.accent_palette = 'Orange'
    self.theme_cls.theme_style = read('color')
    self.theme_cls.material_style = "M3"

  def build(self):
    screenManager.add_widget(Builder.load_file('./data/screens/main.kv'))
    return screenManager

  def on_start(self):
    print('on_start')
  
  def on_stop(self):
    print('on_stop')
  
#Check main script
if __name__ == '__main__':
  app().run()
