#ifndef ROTATETRIANGLE_RIGIDBODY_H
#define ROTATETRIANGLE_RIGIDBODY_H
#include "matrix.h"
#include "quaternion.h"
#include "vector3D.h"

namespace{
    const int STATE_SIZE = 13;
};

class RigidBody {
public:
    double mass;
    matrix Ibody;
    matrix Ibodyinv;
    vector3D x;
    quaternion q;
    vector3D P;
    vector3D L;
    matrix Iinv;
    matrix R;
    vector3D v;
    vector3D omega;
    vector3D force;
    vector3D torque;
    double height;
    double width;
    double length;
    RigidBody (){
        this->mass=2;
        this->width = 1.5;
        this->length = 1.5;
        //this->height = sqrt(pow(this->edge, 2) - pow(sqrt(pow(this->width, 2) + pow(this->length, 2)) / 2, 2));
        this->height = 1.5;
        matrix Ib_inv;
        Ib_inv.position[0][0] = 20/((this->length * this->length + this->width * this->width) * this->mass);
        Ib_inv.position[0][1] = 0;
        Ib_inv.position[0][2] = 0;
        Ib_inv.position[1][0] = 0;
        Ib_inv.position[1][1] = 20/(this->mass*((3 / 4) * this->height * this->height + this->width * this->width));
        Ib_inv.position[1][2] = 0;
        Ib_inv.position[2][0] = 0;
        Ib_inv.position[2][1] = 0;
        Ib_inv.position[2][2] = 20/(this->mass*((3 / 4) * this->height * this->height + this->length * this->length));
        this->Ibodyinv = Ib_inv;
        this->x.x = 1;
        this->x.y = 1;
        this->x.z = 1;
        this->q.r = 0.5;
        this->q.i = 0.5;
        this->q.j = 0.5;
        this->q.k = 0.5;
        this->P.x = 0;
        this->P.y = 0;
        this->P.z = 0;
        this->L.x = 15;
        this->L.y = 10;
        this->L.z = 5;
        this->force.x=0;
        this->force.y=0;
        this->force.z=0;
        this->torque.x=0;
        this->torque.y=0;
        this->torque.z=0;
    };

    void State_to_Array(double *y){
        *y++ = this->x.x;
        *y++ = this->x.y;
        *y++ = this->x.z;
        *y++ = this->q.r;
        *y++ = this->q.i;
        *y++ = this->q.j;
        *y++ = this->q.k;
        *y++ = this->P.x;
        *y++ = this->P.y;
        *y++ = this->P.z;
        *y++ = this->L.x;
        *y++ = this->L.y;
        *y++ = this->L.z;
    };


    void Array_to_State(double *y){
        this->x.x = *y++;
        this->x.y = *y++;
        this->x.z = *y++;
        this->q.r = *y++;
        this->q.i = *y++;
        this->q.j = *y++;
        this->q.k = *y++;
        this->P.x = *y++;
        this->P.y = *y++;
        this->P.z = *y++;
        this->L.x = *y++;
        this->L.y = *y++;
        this->L.z = *y++;
        this->v.x = this->P.x/this->mass;
        this->v.y = this->P.y/this->mass;
        this->v.z = this->P.z/this->mass;
        this->R = matrix::quaternion_to_matrix(this->q.normalize());
        this->Iinv = matrix::multMatAndMat(matrix::multMatAndMat(this->R, this->Ibodyinv), this->R.transposition());
        this->omega = matrix::matXvec(this->Iinv, this->L);
    };

    void Compute_Force_and_Torque(){};


    void ddt_State_to_Array(double *ydot){
        *ydot++ = this->v.x/50;
        *ydot++ = this->v.y/50;
        *ydot++ = this->v.z/10;
        quaternion rotation_quat;
        rotation_quat.r = 0;
        rotation_quat.i = this->omega.x/10;
        rotation_quat.j = this->omega.y/10;
        rotation_quat.k = this->omega.z/10;
        quaternion temp = quaternion::mult_quat_to_quat(rotation_quat,this->q);
        quaternion res;
        res.r=0.5*temp.r;
        res.i=0.5*temp.i;
        res.j=0.5*temp.j;
        res.k=0.5*temp.k;
        *ydot++ = res.r;
        *ydot++ = res.i;
        *ydot++ = res.j;
        *ydot++ = res.k;
        *ydot++ = this->force.x;
        *ydot++ = this->force.y;
        *ydot++ = this->force.z;
        *ydot++ = this->torque.x;
        *ydot++ = this->torque.y;
        *ydot++ = this->torque.z;
    };


    static void MUL_Y_DOUBLE(double *y, double numb){
        for(int i = 0; i<STATE_SIZE; i++){
            y[i]*=numb;
        }
    };
    
    void solveRungeKutta(double h){
        double yinit[STATE_SIZE];
        State_to_Array(yinit);
        double k_1[STATE_SIZE];
        dydt(yinit,k_1);
        MUL_Y_DOUBLE(k_1, h);
        double temp[STATE_SIZE];
        for(int i = 0; i<STATE_SIZE; i++){
            temp[i] = k_1[i];
            temp[i] *= (1.0/2.0);
            temp[i] += yinit[i];
        }
        double k_2[STATE_SIZE];
        dydt(temp,k_2);
        MUL_Y_DOUBLE(k_2, h);
        for(int i = 0; i<STATE_SIZE; i++){
            temp[i] = k_2[i];
            temp[i] *= (1.0/2.0);
            temp[i] += yinit[i];
        }
        double k_3[STATE_SIZE];
        dydt(temp,k_3);
        MUL_Y_DOUBLE(k_3, h);
        for(int i = 0; i<STATE_SIZE; i++){
            temp[i] = k_3[i];
            temp[i] += yinit[i];
        }
        double k_4[STATE_SIZE];
        dydt(temp,k_4);
        MUL_Y_DOUBLE(k_4, h);
        double res[STATE_SIZE];
        for(int i = 0; i<STATE_SIZE; i++){
            res[i] = yinit[i] + (k_1[i] * (1.0/6.0)) + (k_2[i] * (1.0/3.0))+ (k_3[i] * (1.0/3.0))+ (k_4[i] * (1.0/6.0));

        }
        Array_to_State(res);
    };

    void dydt(double *y, double *ydot){
        Array_to_State(y);
        Compute_Force_and_Torque();
        ddt_State_to_Array(ydot);
    };

};
#endif //ROTATETRIANGLE_RIGIDBODY_H
