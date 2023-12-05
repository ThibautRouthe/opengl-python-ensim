# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:38:04 2023

@author: e2104605
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

poly = [
        [0.0,1.0],
        [1.0,1.0],
        [1.0,0.0],
        [0.0,0.0],
        ]

# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0,0.0,0.0)
    # Render scene
    drawPoly()

    # Swap buffers
    glutSwapBuffers()
    
def drawPoly():
    glBegin(GL_POLYGON)
    for vertex in poly:
        glVertex2f(vertex[0],vertex[1])
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