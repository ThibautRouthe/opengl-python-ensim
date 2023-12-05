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
import random


# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    drawConnectedLines()

    # Swap buffers
    glutSwapBuffers()
    
def poly():
    p = []
    while len(p)<random.uniform(3,10):
        p.append([random.uniform(-1, 1),random.uniform(-1, 1)])
    return p

def point():
    p = []
    while len(p)<random.uniform(1,20):
        p.append([random.uniform(-1, 1),random.uniform(-1, 1)])
    return p

def circle():
    p = []
    radiants = np.linspace(0, 2 * np.pi, 32)
    for radiant in radiants :
        p.append([math.cos(radiant), math.sin(radiant)])
    return p

def lines():
    p = []
    while len(p)<10:
        p.append([[random.uniform(-1, 1),random.uniform(-1, 1)],[random.uniform(-1, 1),random.uniform(-1, 1)]])
    return p

    
def drawPoly():
    verteces = poly()
    glBegin(GL_POLYGON)
    glColor3f(random.random(),random.random(),random.random())
    for vertex in verteces:
        glVertex2f(vertex[0],vertex[1])
    glEnd()

def drawPoints():
    points = point()
    glPointSize(5.0)
    glEnable(GL_POINT_SMOOTH)
    for p in points:
        glColor3f(random.random(),random.random(),random.random())
        glBegin(GL_POINTS)
        glVertex2f(p[0],p[1])
        glEnd()

def drawCircles():
    points = circle()
    pointsize = 0
    glEnable(GL_POINT_SMOOTH)
    for point in points:
        pointsize += 1
        glPointSize(pointsize)
        glColor3f(random.random(),random.random(),random.random())
        glBegin(GL_POINTS)
        glVertex2f(point[0]/1.25,point[1]/1.25)
        glEnd()
        
def drawLines(lines):
    linewidth = 0
    for line in lines:
        linewidth += 1
        glLineWidth(linewidth)
        glBegin(GL_LINES)
        for l in line :
            glColor3f(random.random(),random.random(),random.random())
            glVertex2f(l[0],l[1])
        glEnd()
        
def drawConnectedLines(lines):
    glLineWidth(5.0)
    glColor3f(random.random(),random.random(),random.random())
    for line in lines:
        glBegin(GL_LINE_STRIP)
        for l in line :
            glVertex2f(l[0],l[1])
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