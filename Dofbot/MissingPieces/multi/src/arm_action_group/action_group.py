# !/usr/bin/env python
# coding: utf-8

import time
from Arm_Lib import Arm_Device


class action_group:
    def __init__(self):
        self.Arm = Arm_Device()
        self.started = 0

    #Set the action group state
    #设置动作组状态
    def set_state(self, state):
        self.started = state

    #Read the running state of the action group
    #读取动作组运行状态
    def read_state(self):
        return self.started

    # Define the function of moving the manipulator, and control the motion of No. 1-5 servos at the same time, p=[S1, S2, S3, S4, S5]
    # 定义移动机械臂函数,同时控制1-5号舵机运动，p=[S1,S2,S3,S4,S5]
    def arm_move(self, p, s_time = 500):
        for i in range(5):
            id = i + 1
            if id == 5:
                time.sleep(.1)
                self.Arm.Arm_serial_servo_write(id, p[i], int(s_time*1.2))
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

    #Start running custom action group
    #开始运行自定义动作组
    def start_action(self, index):
        if self.started == 1:
            self.custom_action_group(index)
            self.started = 0

    #Custom action group, number=1~8
    #自定义动作组，number=1~8
    def custom_action_group(self, number):
        # Corresponding to Basic Experiment 9, clip blocks to define variable parameters at different positions
        # 对应基础实验9，夹积木定义不同位置的变量参数
        if number == 1:
            p_mould = [90, 130, 0, 0, 90]
            p_top = [90, 80, 50, 50, 270]
            p_Brown = [90, 53, 33, 36, 270]

            p_Yellow = [65, 22, 64, 56, 270]
            p_Red = [117, 19, 66, 56, 270]

            p_Green = [136, 66, 20, 29, 270]
            p_Blue = [44, 66, 20, 28, 270]
            # Move the robotic arm to a position ready to grab
            # 让机械臂移动到一个准备抓取的位置
            self.arm_clamp_block(0)
            if self.started == 1:
                self.arm_move(p_mould, 1000)
            if self.started == 1:
                time.sleep(1)
            # Grab a block from the position of the gray block and place it on the position of the yellow block.
            # 从灰色积木块位置抓取一块积木放到黄色积木块的位置上。
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Brown, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Yellow, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)

            if self.started == 1:
                self.arm_move(p_mould, 1000)
            if self.started == 1:
                time.sleep(1)
            # Grab a block from the gray block and place it on the red block.
            # 从灰色积木块位置抓取一块积木放到红色积木块的位置上。
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Brown, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Red, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_up()
            if self.started == 1:
                self.arm_move(p_mould, 1100)

            if self.started == 1:
                time.sleep(1)
            # Grab a block from the gray block position and place it on the green block position.
            # 从灰色积木块位置抓取一块积木放到绿色积木块的位置上。
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Brown, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Green, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_up()
                self.arm_move(p_mould, 1100)

            if self.started == 1:
                time.sleep(1)
            # Grab a block from the gray block position and place it on the blue block position.
            # 从灰色积木块位置抓取一块积木放到蓝色积木块的位置上。
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Brown, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Blue, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_up()
                self.arm_move(p_mould, 1100)

            if self.started == 1:
                time.sleep(1)
        #Corresponding to basic experiment 10, nature porter
        #对应基础实验10，大自然搬运工
        elif number == 2:
            # Define variable parameters in different positions
            # 定义不同位置的变量参数
            p_mould = [90, 130, 0, 0, 90]
            p_top = [90, 80, 50, 50, 270]

            p_Yellow = [65, 22, 64, 56, 270]
            p_Red = [117, 19, 66, 56, 270]

            p_Green = [136, 66, 20, 29, 270]
            p_Blue = [44, 66, 20, 28, 270]


            p_layer_4 = [90, 72, 49, 13, 270]
            p_layer_3 = [90, 66, 43, 20, 270]
            p_layer_2 = [90, 63, 34, 30, 270]
            p_layer_1 = [90, 53, 33, 36, 270]


            # Move the robotic arm to a position ready to grab
            # 让机械臂移动到一个准备抓取的位置
            if self.started == 1:
                self.arm_clamp_block(0)
                self.arm_move(p_mould, 1000)
            if self.started == 1:
                time.sleep(1)

            # Move the blocks on the fourth floor to the yellow area
            # 搬运第四层的积木块到黄色区域
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_layer_4, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Yellow, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)
            if self.started == 1:
                self.arm_move_up()
                self.arm_move(p_mould, 1100)

            # time.sleep(1)

            # Move the blocks on the third floor to the red area
            # 搬运第三层的积木块到红色区域
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_layer_3, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Red, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_up()
                self.arm_move(p_mould, 1100)

            # time.sleep(1)

            # Move the blocks of the second layer to the green area
            # 搬运第二层的积木块到绿色区域
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_layer_2, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Green, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)


            if self.started == 1:
                self.arm_move_up()
                self.arm_move(p_mould, 1100)

            # time.sleep(1)

            # Move the blocks of the first layer to the blue area
            # 搬运第一层的积木块到蓝色区域
            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_layer_1, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move(p_top, 1000)
            if self.started == 1:
                self.arm_move(p_Blue, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_up()
                self.arm_move(p_mould, 1100)

            # time.sleep(1)
        # Corresponding to basic experiment 11, stacking Arhats
        # 对应基础实验11，叠罗汉
        elif number == 3:
            # Define variable parameters in different positions
            # 定义不同位置的变量参数
            p_mould = [90, 130, 0, 0, 90]
            p_top = [90, 80, 50, 50, 270]

            p_layer_4 = [90, 76, 40, 17, 270]
            p_layer_3 = [90, 65, 44, 17, 270]
            p_layer_2 = [90, 65, 25, 36, 270]
            p_layer_1 = [90, 48, 35, 30, 270]

            p_Yellow = [65, 22, 64, 56, 270]
            p_Red = [118, 19, 66, 56, 270]

            p_Green = [136, 66, 20, 29, 270]
            p_Blue = [44, 66, 20, 28, 270]

            # Move the robotic arm to a position ready to grab
            # 让机械臂移动到一个准备抓取的位置
            if self.started == 1:
                self.arm_clamp_block(0)
            if self.started == 1:
                self.arm_move_h(p_mould, 1000)
            if self.started == 1:
                time.sleep(1)

            # Hold the blocks in the yellow area and stack them to the bottommost position in the middle.
            # 夹取黄色区域的方块堆叠到中间最底层的位置。
            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_Yellow, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_layer_1, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_h(p_mould, 1100)

            # time.sleep(1)

            # Stack the squares in the red area to the second layer in the middle.
            # 夹取红色区域的方块堆叠到中间第二层的位置。

            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_Red, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_layer_2, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_h(p_mould, 1100)
            # Stack the squares in the green area to the third layer in the middle.
            # 夹取绿色区域的方块堆叠到中间第三层的位置。
            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_Green, 1000)
            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_layer_3, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_h(p_mould, 1100)

            # time.sleep(1)

            # Stack the squares in the blue area to the fourth layer in the middle.
            # 夹取蓝色区域的方块堆叠到中间第四层的位置。
            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_Blue, 1000)

            if self.started == 1:
                self.arm_clamp_block(1)

            if self.started == 1:
                self.arm_move_h(p_top, 1000)
            if self.started == 1:
                self.arm_move_h(p_layer_4, 1000)
            if self.started == 1:
                self.arm_clamp_block(0)
                time.sleep(.1)

            if self.started == 1:
                self.arm_move_h(p_mould, 1100)

            # time.sleep(1)

        # Corresponding to basic experiment 6, move up and down, left and right
        # 对应基础实验6，上下左右动
        elif number == 4:
            if self.started == 1:
                self.Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 1000)
            if self.started == 1:
                time.sleep(1)


            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 0, 1000)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 180, 1000)
                time.sleep(1)

            # Control the left and right movement of the No. 1 servo
            # 控制1号舵机左右运动
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(1, 180, 500)
                time.sleep(.5)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(1, 0, 1000)
                time.sleep(1)

            # Control the servo to return to the initial position
            # 控制舵机恢复初始位置
            if self.started == 1:
                self.Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 1000)
                time.sleep(1.5)
        #Corresponding to basic experiment 7, dancing
        #对应基础实验7，跳舞
        elif number == 5:
            time_1 = 500
            time_sleep = 0.5
            if self.started == 1:
                self.Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 1000)
                time.sleep(1)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 180-120, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 120, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 60, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 180-135, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 135, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 45, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 180-120, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 120, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 60, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 90, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 90, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 90, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 180-80, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 80, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 80, time_1)
                time.sleep(time_sleep)



            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 180-60, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 60, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 60, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 180-45, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 45, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 45, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(2, 90, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 90, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 90, time_1)
                time.sleep(.001)
                time.sleep(time_sleep)



            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 20, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(6, 150, time_1)
                time.sleep(.001)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 90, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(6, 90, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 20, time_1)
                time.sleep(.001)
                self.Arm.Arm_serial_servo_write(6, 150, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(4, 90, time_1)
                time.sleep(.001)
                self.Arm.Arm_serial_servo_write(6, 90, time_1)
                time.sleep(.001)
                self.Arm.Arm_serial_servo_write(1, 0, time_1)
                time.sleep(.001)
                self.Arm.Arm_serial_servo_write(5, 0, time_1)
                time.sleep(time_sleep)



            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 180, time_1)
                time.sleep(.001)
                self.Arm.Arm_serial_servo_write(4, 0, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(6, 180, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(6, 0, 1000)
                time.sleep(time_sleep)



            if self.started == 1:
                self.Arm.Arm_serial_servo_write(6, 90, 1000)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(1, 90, time_1)
                time.sleep(.001)
            if self.started == 1:
                self.Arm.Arm_serial_servo_write(5, 90, time_1)
                time.sleep(time_sleep)

            if self.started == 1:
                self.Arm.Arm_serial_servo_write(3, 90, time_1)
                time.sleep(.001)
                self.Arm.Arm_serial_servo_write(4, 90, time_1)
                time.sleep(time_sleep)

        elif number == 6: #自定义动作造型 custom action sculpt
            self.Arm.Arm_serial_servo_write6(90, 180, 0, 0, 90, 155, 1000)
        elif number == 7: #自定义动作造型 custom action sculpt
            self.Arm.Arm_serial_servo_write6(90, 0, 90, 90, 90, 180, 1000)
        elif number == 8: #自定义动作造型 custom action sculpt
            self.Arm.Arm_serial_servo_write6(90, 134, 43, 13, 90, 180, 1000)
        self.started = 0


    # Define the function of moving the manipulator, and control the motion of No. 1-5 servos at the same time, p=[S 1, S 2, S 3, S 4, S 5]
    # 定义移动机械臂函数,同时控制1-5号舵机运动，p=[S1,S2,S3,S4,S5]
    def arm_move_h(self, p, s_time = 500):
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


    # Robot arm moves up
    # 机械臂向上移动
    def arm_move_up(self):
        self.Arm.Arm_serial_servo_write(2, 90, 1500)
        self.Arm.Arm_serial_servo_write(3, 90, 1500)
        self.Arm.Arm_serial_servo_write(4, 90, 1500)
        time.sleep(.1)
