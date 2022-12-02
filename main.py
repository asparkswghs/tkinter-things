#!/usr/bin/env python
# Copyright (c) 2022 Austen Sparks
# Licensed Under the MIT License
# 
from tkinter import *

root = Tk()

# Variables
# Sourced from https://en.wikipedia.org/wiki/Flag_of_Norway#Legal_definition
#  Colors
blue = '#00205b'
red = '#ba0c2f'
white = '#ffffff'
# Units
size = [16,22] # Flag is 16:22
scale = 20
h = size[0]*scale # Should be 320
w = size[1]*scale # Should be 440
# Portions, multiplied by the scale
# For  drawing of shapes
p_horiz = [6*scale,1*scale,2*scale,1*scale,12*scale]
p_vert =  [6*scale,1*scale,2*scale,1*scale,6*scale]
# Shapes
white_vert = [
    p_horiz[0], 0,
    w - p_horiz[4], h
    ]
white_horiz = [
    0, p_vert[0],
    w, h - p_vert[4]
    ]
blue_vert = [
    p_horiz[0] + p_horiz[1], 0,
    p_horiz[0] + p_horiz[1] + p_horiz[2], h
    ]
blue_horiz = [
    0, p_vert[0] + p_vert[1],
    w, h - p_vert[4] - p_vert[3]
    ]

# Create canvas
# Change the background color if you need to!
screen = Canvas(root, width = w, height = h, bg = red)
screen.pack()

# Add shapes here!
# White
screen.create_rectangle(white_vert[0], white_vert[1], white_vert[2], white_vert[3], fill = white, outline = '')
screen.create_rectangle(white_horiz[0], white_horiz[1], white_horiz[2], white_horiz[3], fill = white, outline = '')
# Blue
screen.create_rectangle(blue_vert[0], blue_vert[1], blue_vert[2], blue_vert[3], fill = blue, outline = '')
screen.create_rectangle(blue_horiz[0], blue_horiz[1], blue_horiz[2], blue_horiz[3], fill = blue, outline = '')

# Add shapes to canvas
mainloop()
