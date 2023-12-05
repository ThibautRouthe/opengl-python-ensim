# Template code to run OpenGL with Python

# Importing the necessary Modules
from OpenGL.GL import *
from OpenGL.GLUT import *
# from OpenGL.GLU import *

# Disply callback function
def display():
    # Reset background
    glClear(GL_COLOR_BUFFER_BIT)

    # Render scene
    render_Scene()

    # Swap buffers
    glutSwapBuffers()  

# Scene render function
def render_Scene():
    
    glEnable(GL_POINT_SMOOTH)
    # Set current color to red
    glColor3f(1.0,0.0,0.0)

    glPointSize(5.0)
    
    # Draw a red square
    glBegin(GL_POINTS)
    glVertex2f(0.15, 0.15)
    glEnd()
    
    # Set current color to red
    glColor3f(0.0,1.0,0.0)

    glPointSize(10.0)
    
    # Draw a red square
    glBegin(GL_POINTS)
    glVertex2f(-0.3, 0.15)
    glEnd()
    
    # Set current color to red
    glColor3f(0.0,0.0,1.0)

    glPointSize(20.0)
    
    # Draw a red square
    glBegin(GL_POINTS)
    glVertex2f(-0.2, -0.2)
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
