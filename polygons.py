# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:33:53 2023

@author: e2104605
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math
import random



# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_triangle_fan()

    # Swap buffers
    glutSwapBuffers()
    
def poly(points):
    p = []
    radiants = np.linspace(0, 2 * np.pi, points+1)
    radiants = radiants[:-1]
    for radiant in radiants :
        p.append([math.cos(radiant), math.sin(radiant)])
    return p
    
def draw_triangle():
    center = [0,0]
    verteces = poly(12)
    triangles=[]
    i=0
    triangle=[]
    for i in range(len(verteces) - 1):
        vertex = verteces[i:i+2]
        triangle.append(vertex[0])
        triangle.append(vertex[1])
        triangle.append(center)
        triangles.append(triangle)
        triangle = []
    
    triangle.append(verteces[-1])
    triangle.append(verteces[0])
    triangle.append(center)
    triangles.append(triangle)
            
    for t in triangles:
        glBegin(GL_TRIANGLES)
        glColor3f(random.random(),random.random(),random.random())
        for v in t:
            glVertex2f(v[0],v[1])
        glEnd()
        
def draw_triangle_strip():
    center = [0,0]
    verteces = poly(8)
    triangle = []
    for i in range(len(verteces) - 1):
        vertex = verteces[i:i+2]
        triangle.append(vertex[0])
        triangle.append(vertex[1])
        triangle.append(center)
        
    triangle.append(verteces[-1])
    triangle.append(verteces[0])
    triangle.append(center)
        
    glBegin(GL_TRIANGLES)
    glColor3f(random.random(),random.random(),random.random())
    i=0
    for t in triangle:
        glVertex2f(t[0],t[1])
        i+=1
        if(i%3 == 0):
            glColor3f(random.random(),random.random(),random.random())
            
    glEnd()
    
def draw_triangle_fan():
    center = [0,0]
    verteces = poly(8)
    verteces.append(verteces[0])
    verteces.insert(0, center)
    
    print(verteces)
        
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(random.random(),random.random(),random.random())
    i=0
    for t in verteces:
        glVertex2f(t[0],t[1])
        i+=1
        if(i%2 == 0):
            glColor3f(random.random(),random.random(),random.random())
            
    glEnd()
    
    
    
print("start")
# Initialize GLUT
glutInit()

# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)

# Create the window and give it a title
glutCreateWindow("My First OpenGL Window")

# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)

# Define callbacks
glutDisplayFunc(display)

print("loop")

# Begin event loop
glutMainLoop()