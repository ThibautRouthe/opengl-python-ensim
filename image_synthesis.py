# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:38:04 2023

@author: e2104605
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

poly = [
        [0.0,1.0],
        [1.0,1.0],
        [1.0,0.0],
        [0.0,0.0],
        ]

def circle():
    p = []
    radiants = np.linspace(0, 2 * np.pi, 32)
    for radiant in radiants :
        p.append([math.cos(radiant), math.sin(radiant)])
    return p

# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0,0.0,0.0)
    # Render scene
    drawPoints(circle())

    # Swap buffers
    glutSwapBuffers()
    
def drawPoly(verteces):
    glBegin(GL_POLYGON)
    for vertex in verteces:
        glVertex2f(vertex[0],vertex[1])
    glEnd()

def drawPoints(points):
    glPointSize(15.0)
    for point in points:
        glBegin(GL_POINTS)
        glVertex2f(point[0],point[1])
        glEnd()

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

# Begin event loop
glutMainLoop()