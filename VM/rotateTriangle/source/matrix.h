#ifndef ROTATETRIANGLE_MATRIX_H
#define ROTATETRIANGLE_MATRIX_H
#include "quaternion.h"
#include "vector3D.h"

class matrix {
public:
    double position[3][3]{};
    matrix& operator=(matrix obj){
        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++) {
                this->position[i][j] = obj.position[i][j];
            }
        }
    };

    static matrix multMatAndMat(matrix A, matrix B){
        matrix res;
        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++){
                res.position[i][j] = 0;
                for(int k = 0; k<3; k++){
                    res.position[i][j]+=A.position[i][k]*B.position[k][j];
                }
            }
        }
        return res;
    };

    matrix transposition(){
        matrix transpose;
        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++){
                transpose.position[i][j] = this->position[j][i];
            }
        }
        return transpose;
    };

    static matrix quaternion_to_matrix(const quaternion & q){
        matrix result;
        result.position[0][0] = 1-2*q.j*q.j-2*q.k*q.k;
        result.position[0][1] = 2*q.i*q.j-2*q.r*q.k;
        result.position[0][2] = 2*q.i*q.k+2*q.r*q.j;
        result.position[1][0] = 2*q.i*q.j+2*q.r*q.k;
        result.position[1][1] = 1-2*q.i*q.i-2*q.k*q.k;
        result.position[1][2] = 2*q.j*q.k-2*q.r*q.i;
        result.position[2][0] = 2*q.i*q.k-2*q.r*q.j;
        result.position[2][1] = 2*q.j*q.k+2*q.r*q.i;
        result.position[2][2] = 1-2*q.i*q.i-2*q.j*q.j;
        return result;
    };

    quaternion matrix_to_quaternion(){
        quaternion q;
        double tr,s;
        tr = this->position[0][0]+ this->position[1][1] + this->position[2][2];
        if(tr>=0){
            s = sqrt(tr + 1);
            q.r = 0.5*s;
            s = 0.5/s;
            q.i = (this->position[2][1] - this->position[1][2])*s;
            q.j = (this->position[0][2] - this->position[2][0])*s;
            q.k = (this->position[1][0] - this->position[0][1])*s;
        } else{
            int i = 0;
            if(this->position[1][1] > this->position[0][0]){
                i=1;
            }
            if(this->position[2][2] > this->position[i][i]) {
                i = 2;
            }
            switch(i){
                case 0 :
                    s = sqrt((this->position[0][0]-(this->position[1][1] + this->position[2][2]))+1);
                    q.i = 0.5*s;
                    s = 0.5/s;
                    q.j = (this->position[0][1]+ this->position[1][0])*s;
                    q.k = (this->position[2][0]+ this->position[0][2])*s;
                    q.r = (this->position[2][1] - this->position[1][2])*s;
                    break;
                case 1:
                    s = sqrt((this->position[1][1] -(this->position[2][2] + this->position[0][0]))+1);
                    q.j = 0.5*s;
                    s = 0.5/s;
                    q.k = (this->position[1][2] + this->position[2][1])*s;
                    q.i = (this->position[0][1] + this->position[1][0])*s;
                    q.r = (this->position[0][2] - this->position[2][0])*s;
                    break;
                case 2:
                    s = sqrt((this->position[2][2] - (this->position[0][0] + this->position[1][1]))+1);
                    q.k = 0.5*s;
                    s = 0.5/s;
                    q.i = (this->position[2][0] + this->position[0][2])*s;
                    q.j = (this->position[1][2] + this->position[2][1])*s;
                    q.k = (this->position[1][0] - this->position[0][1])*s;
            }
        }
        return q;
    };

    static vector3D matXvec(matrix A, vector3D vec){
        vector3D res;
        res.x=A.position[0][0]*vec.x + A.position[0][1]*vec.y + A.position[0][2]*vec.z;
        res.y=A.position[1][0]*vec.x + A.position[1][1]*vec.y + A.position[1][2]*vec.z;
        res.z=A.position[2][0]*vec.x + A.position[2][1]*vec.y + A.position[2][2]*vec.z;
        return res;
    };
};


#endif //ROTATETRIANGLE_MATRIX_H
