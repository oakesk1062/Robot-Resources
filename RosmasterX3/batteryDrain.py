#!/usr/bin/env python3
#coding=utf-8

#written by KO 2/17/23 - To run as startup application to check that data can be read/wrote to robot, otherwise restart needed
import time
from Rosmaster_Lib import Rosmaster
import os

time.sleep(5)
bot = Rosmaster()
bot.create_receive_threading()
test = True
while test:
    vol = bot.get_battery_voltage()
    #f = open("~/Rosmaster/Sample/batteryDrain.txt","w")
    #f = open("batteryDrain.txt","w")
   #f.write(str(bot.get_battery_voltage()) + " Out of ~12 " + "\n")
   # f.close()
   # os.system("gedit ~/Rosmaster/Sample/batteryDrain.txt")
    #os.system("gedit batteryDrain.text")
    if vol<11.7:
        if vol>11.1:
            bot.set_colorful_lamps(0xff,0,255,0)
            bot.set_beep(100)
            test = False
        else:
            bot.set_colorful_lamps(0xff,255,0,0)
            bot.set_beep(200)
    else:
        bot.set_colorful_lamps(0xff,0,0,255)
        time.sleep(30)

del bot