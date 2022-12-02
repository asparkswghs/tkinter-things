
#!/usr/bin/env python3
# Copyright (c) 2022 Austen Sparks
# Licensed Under the MIT License
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 400
canvas_center = canvas_width/2
bottom_diameter = canvas_height/2
middle_diameter = bottom_diameter/2
top_diameter = middle_diameter/2
# Added Variables
bottom = [
    canvas_center-bottom_diameter/2, canvas_height-bottom_diameter,
    canvas_center+bottom_diameter/2, canvas_height
    ]
middle = [
    canvas_center-middle_diameter/2, canvas_height-bottom_diameter-middle_diameter,
    canvas_center+middle_diameter/2, canvas_height-bottom_diameter
    ]
top = [
    canvas_center-top_diameter/2, canvas_height-bottom_diameter-middle_diameter-top_diameter,
    canvas_center+top_diameter/2, canvas_height-bottom_diameter-middle_diameter
    ]

# Create canvas
screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

# Add shapes here!
screen.create_oval(bottom[0], bottom[1], bottom[2], bottom[3], fill = '#d3d3d3', outline = '')
screen.create_oval(middle[0], middle[1], middle[2], middle[3], fill = '#d3d3d3', outline = '')
screen.create_oval(top[0], top[1], top[2], top[3], fill = '#d3d3d3', outline = '')



# Add shapes to canvas
mainloop()
