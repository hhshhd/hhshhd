from OpenGL.GL import *
from OpenGL.GLUT import *
def draw():
    glBegin(GL_LINES)
    glColor4f(1.0,1.0,0.0,0.0)
    glVertex3f(-0.8,-0.8,0.0)
    glVertex3f(0.8,0.8,0.0)

    glColor4f(0.0,1.0,1.0,0.0)
    glVertex3f(-0.8,0.8,0.0)
    glVertex3f(0.8,-0.8,0.0)


    glEnd()

    glBegin(GL_QUADS)
    glColor4f(1.0, 0.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.366, -0.5)
    glColor4f(0.0, 1.0, 0.0, 1.0)       
    glVertex3f(-0.5, 0.366, -0.5)       
    glColor4f(0.0, 0.0, 1.0, 1.0)   
    glVertex3f(0.5, 0.336, -0.5)
    glColor4f(1.0, 0.0, 1.0, 0.0)   
    glVertex3f(0.5, -0.336, 0.5) 
    
    glEnd()                            
    
    glFlush()

if __name__ == "__main__":
    glutInit()                           
    glutCreateWindow('Quidam Of OpenGL')
    glutDisplayFunc(draw)                
    glutMainLoop()         
