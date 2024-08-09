#include<windows.h>
#include <GL/glut.h>

void init(void)
{
	glClearColor(1.0, 1.0, 1.0, 0.0);	// Set display window colour to white
	// The four arguments are the red, green, blue, and alpha (transparency) values respectively.

	glMatrixMode(GL_PROJECTION);		// Set projection parameters
	//This mode is used for projection transformations, which define the camera's lens.
	// It controls how objects are projected from 3D space into the 2D screen space. This typically involves defining perspective
	//or orthographic projections.
	gluOrtho2D(0.0, 400.0, 0.0, 400.0);//Defines a 2D orthographic projection matrix,
	//setting up a coordinate system where the bottom-left corner is (0, 0) and the top-right corner is (400, 400)
}

void drawShapes(void)
{
	glClear(GL_COLOR_BUFFER_BIT);	// Clear display window

	//Set colour to black
	glColor3f(0.0, 0.0, 0.0);
	//Adjust the point size
	glPointSize(5.0);

	//Set colour to red
	glColor3f(1.0, 0.0, 0.0);

	// Draw an outlined triangle
	glBegin(GL_LINES);

		glVertex2i(0, 200);
		glVertex2i(400, 200);

		glVertex2i(200, 400);
		glVertex2i(200,0);



	glEnd();

	glFlush();	// Process all OpenGL routines
}

int main(int argc, char* argv[])
{
	glutInit(&argc, argv);						// Initalise GLUT
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);	// Set display mode
	//single frame buffer
	//In this mode, all rendering is done directly to the visible buffer, meaning the image is drawn directly on the screen.

	glutInitWindowPosition(50, 100);				// Set window position
	glutInitWindowSize(400, 300);					// Set window size
	glutCreateWindow("An Example OpenGL Program");	// Create display window

	init();							// Execute initialisation procedure
	glutDisplayFunc(drawShapes);		// Send graphics to display window
	glutMainLoop();					// Display everything and wait

	return 0;
}
