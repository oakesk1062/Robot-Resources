#!/usr/bin/env python3
#coding=utf-8

#written by KO 2/17/23 - To run as startup application to check that data can be read/wrote to robot, otherwise restart needed

import time
from Rosmaster_Lib import Rosmaster
import os

time.sleep(5)
bot = Rosmaster()
bot.create_receive_threading()
#vol = bot.get_battery_voltage()
test = bot.get_version()

#if vol>1:
if test>0:
    #set color of back lights to green
    bot.set_colorful_lamps(0xff,0,255,0)
    bot.set_beep(100)
    time.sleep(2)
    bot.set_colorful_lamps(0xff,0,0,0)
    bot.set_beep(100)
    f = open("Rosmaster/Sample/batteryCheck.txt","w")
    f.write(str(bot.get_battery_voltage()) + " Out of ~12 " + "\n" + "Shutdown required at 9.6")
    f.close()
    os.system("gedit ~/Rosmaster/Sample/batteryCheck.txt")
    #os.system("gedit ~/Rosmaster/Sample/lowBatteryPrompt.txt")
    #print(bot.get_battery_voltage())
    #print("Out of ~12")
    #print("Restart required at 9.6")
    #if bot.get_battery_voltage()<10:
     #   os.system("gedit ~/Rosmaster/Sample/lowBatteryPrompt.txt")
else:
    os.system("gedit ~/Rosmaster/Sample/restartPrompt.txt")

del bot
