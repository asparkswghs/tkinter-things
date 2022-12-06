from tkinter import *

root = Tk()

# Constant values
canvas_width = 400
canvas_height = 600
center_width = canvas_width /2
center_height= canvas_height /2

head_radius = canvas_width/4
body_width = head_radius * 2
body_height = canvas_height/3
num_feet = 3
foot_radius = body_width / (num_feet * 2)
body_color = "red"

eye_radius = head_radius/4
eye_offset = eye_radius * 1.5
eye_color = "white"
pupil_radius = eye_radius/2.5
pupil_left_offset = eye_radius
pupil_right_offset = pupil_radius * 5
pupil_color = "blue"

# Create canvas
screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

# Create circles from their center coordinate
def create_circle(x, y, r, fill='black', outline='', canvas=screen):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=fill, outline=outline)
def create_square(x, y, r, fill='black', outline='', canvas=screen):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=outline)

# Write program here

# Head
create_circle(center_width, center_height-body_height/2, head_radius, fill=body_color)
create_square(center_width,center_height, head_radius,fill=body_color)

# Bottom Fringe
pos_sub = body_width /num_feet
for i in range(num_feet):
    pos_x = center_width + pos_sub
    create_circle(pos_x,center_height+body_height/2,foot_radius, fill=body_color)
    pos_sub -= body_width /num_feet

# Eyes
create_circle(center_width-eye_offset,body_height,eye_radius,fill=eye_color)
create_circle(center_width+eye_offset,body_height,eye_radius,fill=eye_color)
create_circle(center_width-pupil_left_offset,body_height,pupil_radius,fill=pupil_color)
create_circle(center_width+pupil_right_offset,body_height,pupil_radius,fill=pupil_color)


# Add shapes to canvas
mainloop()
