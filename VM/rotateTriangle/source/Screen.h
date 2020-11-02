#ifndef ROTATETRIANGLE_SCREEN_H
#define ROTATETRIANGLE_SCREEN_H

#include "RigidBody.h"
#include <GL/glut.h>
#include <math.h>
#include <ctime>

[[maybe_unused]] RigidBody body;
double DeltaTime;

void drawTriangle(){
    glBegin(GL_TRIANGLES);
    glColor3f(0.52,0.44,1.0);// Сделали боковую сторону фиолетовой
    glVertex3f( 1.0, -1.0,-1.0);
    glVertex3f(1.0, -1.0,1.0);
    glVertex3f(0.0, 1.0, 0.0);
    glEnd();
    /*glVertex3f(body.widthBlock, -1*body.depthBlock, -1*body.heightBlock);
    glVertex3f(-body.widthBlock, -1*body.depthBlock, body.heightBlock);
    glVertex3f(-body.widthBlock*0, -body.depthBlock, body.heightBlock*0);
    glEnd();*/


    glBegin(GL_TRIANGLES);
    glColor3f(1.0,0.84,0.0);  // Сделали боковую сторону желтой
    glVertex3f( 1.0,-1.0, 1.0);
    glVertex3f(-1.0,-1.0, 1.0);
    glVertex3f(0.0,1.0,0.0);
    glEnd();

    glBegin(GL_TRIANGLES);
    glColor3f(0.94,0.5,0.5);// Сделали сторону  розовой
    glVertex3f(-1.0,-1.0,1.0);
    glVertex3f(-1.0, -1.0,-1.0);
    glVertex3f(0.0,1.0,0.0);
    glEnd();

    glBegin(GL_TRIANGLES);
    glColor3f(0.0,1.0,0.0);  // Сделали сторону  светло зеленой
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f(1.0,-1.0,-1.0);
    glVertex3f(0.0, 1.0,0.0);
    glEnd();

    glBegin(GL_QUADS);// основание пирамиды
    glColor3f(1.0,0.51,0.28); // сделали основание рыжим
    glVertex3f( 1.0,-1.0, 1.0);
    glVertex3f(-1.0,-1.0, 1.0);
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f( 1.0,-1.0,-1.0);
    glEnd();
};


void Idle() {
    long Time;
    static long OldTime = -1;
    static long StartTime;
    if (OldTime == -1)
        StartTime = OldTime = clock();
    else {
        Time = clock();
        DeltaTime = (double)(Time - OldTime) / CLOCKS_PER_SEC;
        OldTime = clock();
    }
    glutPostRedisplay();
    body.solveRungeKutta(DeltaTime);
};

void screen(){
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glPushMatrix();
    glTranslated(0.5, 0.5, sqrt(2)/8);
    //glTranslated(body.x.x, body.x.y, body.x.z);
    glRotatef(2*acos(body.q.r)*180/M_PI,  body.q.i, body.q.j, body.q.k);
    glPolygonMode(GL_FRONT, GL_FILL);
    drawTriangle();
    glPopMatrix();
    glFlush();
    glutSwapBuffers();
}

void Reshape(int W, int H) {
    glViewport(0, 0, W, H);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(15.0, ((float)W)/((float)H), 10.0, 100.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0, 30, 0, 0, 0, 0, 0, 0, 1);
}

void init(){
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH);
    glutInitWindowSize(1920, 1080);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("result");
    glutReshapeFunc(Reshape);
    glutDisplayFunc(screen);
    glutIdleFunc(Idle);
    glClearColor(0, 0, 0, 0);
    glEnable(GL_DEPTH_TEST);
    glShadeModel(GL_SMOOTH);
    glutMainLoop();
}


#endif //ROTATETRIANGLE_SCREEN_H
