#ifndef UNIT_KAHANSUM_H
#define UNIT_KAHANSUM_H
#include <iostream>
#include <cmath>
double KahanSum(double* array, int n){
    double res = 0.0;
    double error = 0.0;
    double numb;
    double current;
    for (int i = 0; i < n; i++){
        numb = array[i] - error;
        current = res + numb;
        error = (current - res) - numb;
        res = current;
    }
    return res;
}

double NeumaierSum(double* arr, int n){
    double res = 0.0;
    double error = 0.0;
    double t;
    for (int i = 0; i < n; i++){
        t = res + arr[i];
        if (fabs(res) >= fabs(arr[i])){
            error += (res - t) + arr[i];
        } else{
            error += (arr[i] - t) + res;
        }
        res = t;
    }
    return res + error;
}

double KleinSum(double* arr, int n) {
    double res = 0.0;
    double cs = 0.0;
    double ccs = 0.0;
    double error = 0.0;
    double cc = 0.0;
    double t;
    for (int i = 0; i < n; i++) {
        t = res + arr[i];
        if (fabs(res) >= fabs(arr[i])) {
            error = (res - t) + arr[i];
        } else {
            error = (arr[i] - t) + res;
        }
        res = t;
        t = cs + error;
        if (fabs(cs) >= fabs(error)){
            cc = (cs - t) + error;
        } else {
            cc = (error - t) + cs;
        }
        cs = t;
        ccs = ccs + cc;
    }
    //std::cerr << std::fixed<<std::setprecision(20) << res + cs + ccs << std::endl;
    return res + cs + ccs;
}


#endif //UNIT_KAHANSUM_H
