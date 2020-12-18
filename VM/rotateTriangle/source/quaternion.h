#ifndef ROTATETRIANGLE_QUATERNION_H
#define ROTATETRIANGLE_QUATERNION_H
#include <cmath>

class quaternion {
public:
    double i;
    double j;
    double k;
    double r;
    quaternion(){
        this->r = 0;
        this->k = 0;
        this->i = 0;
        this->j = 0;
    };

    quaternion normalize(){
        quaternion res;
        double len = sqrt( this->r* this->r+ this->i* this->i+ this->j* this->j+ this->k* this->k);
        res.r = this->r/len;
        res.i = this->i/len;
        res.j = this->j/len;
        res.k = this->k/len;
        return res;
    };

    static quaternion mult_quat_to_quat(const quaternion & q1, const quaternion & q2){
        quaternion res;
        res.r = q1.r*q2.r - q1.i*q2.i - q1.j*q2.j - q1.k*q2.k;
        res.i = q1.r*q2.i + q1.i*q2.r + q1.j*q2.k - q1.k*q2.j;
        res.j = q1.r*q2.j - q1.i*q2.k + q1.j*q2.r + q1.k*q2.i;
        res.k = q1.r*q2.k + q1.i*q2.j - q1.j*q2.i + q1.k*q2.r;
        return res;
    };
};


#endif //ROTATETRIANGLE_QUATERNION_H
