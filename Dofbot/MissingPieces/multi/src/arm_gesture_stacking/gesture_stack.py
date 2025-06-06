# !/usr/bin/env python
# coding: utf-8
import cv2
import numpy as np
import random
import time
from Arm_Lib import Arm_Device
import threading

import demjson
import pygame 
from aip import AipBodyAnalysis
from aip import AipSpeech
from PIL import Image, ImageDraw, ImageFont

class gesture_stack:
    def __init__(self):

        self.Arm = Arm_Device()
        self.color_name = None
        self.image = None

        self.look_at = [90, 164, 18, 0, 90, 90]
        self.p_top = [90, 80, 50, 50, 270]

        self.p_Yellow = [65, 22, 64, 56, 270]
        self.p_Red = [118, 19, 66, 56, 270]

        self.p_Green = [136, 66, 20, 29, 270]
        self.p_Blue = [44, 66, 20, 28, 270]

        self.p_gray = [90, 52, 37, 29, 270]

        self.p_layer_4 = [90, 76, 40, 17, 270]
        self.p_layer_3 = [90, 65, 44, 17, 270]
        self.p_layer_2 = [90, 65, 25, 36, 270]
        self.p_layer_1 = [90, 48, 35, 30, 270]

        self.p_push_over_1 = [90, 90, 5, 0, 90, 150]
        self.p_push_over_2 = [90, 90, 0, 50, 90, 150]

        self.g_state_arm = 0
        self.started = 0
        self.g_layer = 0

        self.yellow_grabbed = 0
        self.red_grabbed = 0
        self.green_grabbed = 0
        self.blue_grabbed = 0

        self.Count_One = 0
        self.Count_Two = 0
        self.Count_Three = 0
        self.Count_Four = 0
        self.Count_Fist = 0

    
    # knock down the blocks
    # 推倒积木块
    def push_over_block(self):
        self.Arm.Arm_serial_servo_write6_array(self.p_push_over_1, 1000)
        time.sleep(1.2)
        self.Arm.Arm_serial_servo_write6_array(self.p_push_over_2, 1000)
        time.sleep(1.1)
        self.Arm.Arm_serial_servo_write6_array(self.look_at, 1000)
        time.sleep(1)
        self.g_layer = 0

    def put_down_block(self, layer):
        if layer == 1:
            self.arm_move(self.p_layer_1, 1000)
            self.arm_clamp_block(0) 
            self.Arm.Arm_serial_servo_write6_array(self.look_at, 1000)
        elif layer == 2:
            self.arm_move(self.p_layer_2, 1000)
            self.arm_clamp_block(0)
            self.Arm.Arm_serial_servo_write6_array(self.look_at, 1000)
        elif layer == 3:
            self.arm_move(self.p_layer_3, 1000)
            self.arm_clamp_block(0) 
            self.Arm.Arm_serial_servo_write6_array(self.look_at, 1000)
        elif layer == 4:
            self.arm_move(self.p_layer_4, 1000)
            time.sleep(.1)
            self.arm_clamp_block(0) 
            self.Arm.Arm_serial_servo_write6_array(self.look_at, 1000)

    def ctrl_arm_move(self, index):
        self.g_layer = self.g_layer + 1
        if self.g_layer >= 5:
            self.g_layer = 1
        self.arm_clamp_block(0)

        if index == 1:
            self.number_action(1)
            self.put_down_block(self.g_layer)
        elif index == 2:
            self.number_action(2)
            self.put_down_block(self.g_layer)
        elif index == 3:
            self.number_action(3)
            self.put_down_block(self.g_layer)
        elif index == 4:
            self.number_action(4)
            self.put_down_block(self.g_layer)
        elif index == 5:
            self.push_over_block()
        self.g_state_arm = 0

    # Define the function of moving the manipulator, and control the motion of No. 1-5 servos at the same time, p=[S 1, S 2, S 3, S 4, S 5]
    # 定义移动机械臂函数,同时控制1-5号舵机运动，p=[S1,S2,S3,S4,S5]
    def arm_move(self, p, s_time = 500):
        for i in range(5):
            id = i + 1
            if id == 5:
                time.sleep(.1)
                self.Arm.Arm_serial_servo_write(id, p[i], int(s_time*1.2))
            elif id == 1 :
                self.Arm.Arm_serial_servo_write(id, p[i], int(3*s_time/4))
            else:
                self.Arm.Arm_serial_servo_write(id, p[i], int(s_time))
            time.sleep(.01)
        time.sleep(s_time/1000)
    
    # Define the function of clamping blocks, enable=1: clamp, =0: release
    # 定义夹积木块函数，enable=1：夹住，=0：松开
    def arm_clamp_block(self, enable):
        if enable == 0:
            self.Arm.Arm_serial_servo_write(6, 60, 400)
        else:
            self.Arm.Arm_serial_servo_write(6, 135, 400)
        time.sleep(.5)

    #Definition of digital functions
    # 数字功能定义
    def number_action(self, index):
        if index == 1:
            # Grab the yellow blocks
            # 抓取黄色的积木块
            self.arm_move(self.p_top, 1000)
            self.arm_move(self.p_Yellow, 1000)
            self.arm_clamp_block(1)
    #         time.sleep(.5)
            self.arm_move(self.p_top, 1000)
        elif index == 2:
            # Grab the red blocks
            # 抓取红色的积木块
            self.arm_move(self.p_top, 1000)
            self.arm_move(self.p_Red, 1000)
            self.arm_clamp_block(1)
            self.arm_move(self.p_top, 1000)
        elif index == 3:
            # Grab the green blocks
            # 抓取绿色的积木块
            self.arm_move(self.p_top, 1000)
            self.arm_move(self.p_Green, 1000)
            self.arm_clamp_block(1)
            self.arm_move(self.p_top, 1000)
        elif index == 4:
            # Grab the blue blocks
            # 抓取蓝色的积木块
            self.arm_move(self.p_top, 1000)
            self.arm_move(self.p_Blue, 1000)
            self.arm_clamp_block(1)
            self.arm_move(self.p_top, 1000)

    def start_move_arm(self, index):
        # Open the robot arm control thread
        # 开启机械臂控制线程
        if self.g_state_arm == 0:
            closeTid = threading.Thread(target = self.ctrl_arm_move, args = [index])
            closeTid.setDaemon(True)
            closeTid.start()
            
            self.g_state_arm = 1

    def bgr8_to_jpeg(self, value, quality=75):
        return bytes(cv2.imencode('.jpg', value)[1])


    def reset_state(self):
        self.started = 0

    def Gesture_Action(self, frame):
        if self.started == 0:
            # For specific gestures, please see the official offer https://ai.baidu.com/ai-doc/BODY/4k3cpywrv
            # 具体手势请看官方提供 https://ai.baidu.com/ai-doc/BODY/4k3cpywrv
            self.hand = {'One':'数字1','Two':'数字2','Three':'数字3','Four':'数字4',
                        'Five':'数字5', 'Six':'数字6','Seven':'数字7',
                        'Eight':'数字8','Nine':'数字9','Fist':'拳头','Ok':'OK',
                        'Prayer':'祈祷','Congratulation':'作揖','Honour':'作别',
                        'Heart_single':'比心心','Thumb_up':'点赞','Thumb_down':'Diss',
                        'ILY':'我爱你','Palm_up':'掌心向上','Heart_1':'双手比心1',
                        'Heart_2':'双手比心2','Heart_3':'双手比心3','Rock':'Rock',
                        'Insult':'竖中指','Face':'脸'}

            """ Human Analysis APPID AK SK """
            self.APP_ID = '24840713'
            self.API_KEY = 'WMvYkrI7omD8OyGlwqjHQMRK'
            self.SECRET_KEY = 'XAKxY0NyCL1QIfIRjEi8ScsPjGjsANuX'

            self.client = AipBodyAnalysis(self.APP_ID, self.API_KEY, self.SECRET_KEY)

            self.Arm.Arm_serial_servo_write6_array(self.look_at, 1000)
            time.sleep(1.2)


            self.Arm.Arm_Buzzer_On(1)
            s_time = 300
            self.Arm.Arm_serial_servo_write(4, 10, s_time)
            time.sleep(s_time/1000)
            self.Arm.Arm_serial_servo_write(4, 0, s_time)
            time.sleep(s_time/1000)
            self.Arm.Arm_serial_servo_write(4, 10, s_time)
            time.sleep(s_time/1000)
            self.Arm.Arm_serial_servo_write(4, 0, s_time)
            time.sleep(s_time/1000)
            self.started = 1
        
        """ 调用手势识别 call gesture recognition """
        raw = str(self.client.gesture(self.bgr8_to_jpeg(frame)))
        text = demjson.decode(raw)
        try:
            res = text['result'][0]['classname']
        except:
            img = frame
        else:
    #         print('Recognition result：' + hand[res])
    
            if res == 'One': # 1 
                self.Count_One = self.Count_One + 1
                
                self.Count_Two = 0
                self.Count_Three = 0
                self.Count_Four = 0
                self.Count_Fist = 0
                img = cv2.putText(frame, res, (450, 50),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                
                if self.Count_One >= 3:
                    if self.yellow_grabbed == 0:
                        print('Recognition result：' + self.hand[res])
                        self.Arm.Arm_Buzzer_On(1)
                        self.start_move_arm(1)
                        self.yellow_grabbed = 1
            elif res == 'Two': # 2 
                self.Count_Two = self.Count_Two + 1
    
                self.Count_One = 0
                self.Count_Three = 0
                self.Count_Four = 0
                self.Count_Fist = 0
                img = cv2.putText(frame, res, (450, 50),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

                if self.Count_Two >= 3: 
                    if self.red_grabbed == 0:
                        print('Recognition result：' + self.hand[res])
                        self.Arm.Arm_Buzzer_On(1)
                        self.start_move_arm(2)
                        self.red_grabbed = 1
            elif res == 'Three':
                self.Count_Three = self.Count_Three + 1
   
                self.Count_One = 0
                self.Count_Two = 0
                self.Count_Four = 0
                self.Count_Fist = 0
                img = cv2.putText(frame, res, (450, 50),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

                if self.Count_Three >= 3:
                    if self.green_grabbed == 0:
                        print('Recognition result：' + self.hand[res])
                        self.Arm.Arm_Buzzer_On(1)
                        self.start_move_arm(3)
                        self.green_grabbed = 1
            elif res == 'Four': # 4 
                self.Count_Four = self.Count_Four + 1
                
                self.Count_One = 0
                self.Count_Two = 0
                self.Count_Three = 0
                self.Count_Fist = 0
                img = cv2.putText(frame, res, (450, 50),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

                if self.Count_Four >= 3:
                    if self.blue_grabbed == 0:
                        print('Recognition result：' + self.hand[res])
                        self.Arm.Arm_Buzzer_On(1)
                        self.start_move_arm(4)
                        self.blue_grabbed = 1
            elif res == 'Fist':
                self.Count_Fist = self.Count_Fist + 1

                self.Count_One = 0
                self.Count_Two = 0
                self.Count_Three = 0
                self.Count_Four = 0
                img = cv2.putText(frame, res, (450, 50),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

                if self.Count_Fist >= 3:
                    print('Recognition result：' + self.hand[res])
                    self.Arm.Arm_Buzzer_On(1)
                    
                    self.Count_One = 0
                    self.Count_Two = 0
                    self.Count_Three = 0
                    self.Count_Four = 0
                    self.Count_Fist = 0
                    self.yellow_grabbed = 0
                    self.red_grabbed = 0
                    self.green_grabbed = 0
                    self.blue_grabbed = 0
                    self.start_move_arm(5)
            else:
                img = frame
        return img


    def start_gesture(self, img):
        self.image = self.Gesture_Action(img)
        return self.image

