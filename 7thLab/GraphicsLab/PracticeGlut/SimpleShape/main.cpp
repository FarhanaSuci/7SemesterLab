#include<GL/glut.h>
#include<windows.h>
void init(void)
{
    glClearColor(0.0,0.0,0.0,0.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0,1.0,0.0,1.0,-10.0,10.0);

}
void DrawShape()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0,0.0,0.0);
    glBegin(GL_TRIANGLES);
    glVertex3f(0.1,0.3,0.0);
    glVertex3f(0.5,0.3,0.0);
    glVertex3f(0.3,0.8,0.0);
    glEnd();
    glColor3f(0.0,0.0,1.0);
    glBegin(GL_QUADS);
    glVertex3f(0.6,0.3,0.0);
    glVertex3f(.95,0.3,0.0);
    glVertex3f(0.95,0.8,0.0);
    glVertex3f(0.6,0.8,0.0);
    glEnd();
    glFlush();
}
int main(int a, char** b)
{

 glutInit(&a,b);
 glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
 glutInitWindowPosition(10,10);
 glutInitWindowSize(600,600);
 glutCreateWindow("Suchi");
 init();
 glutDisplayFunc(DrawShape);
 glutMainLoop();
 return 0;
}




