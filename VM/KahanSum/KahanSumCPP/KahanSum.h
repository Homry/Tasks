#ifndef UNIT_KAHANSUM_H
#define UNIT_KAHANSUM_H
double KahanSum(double*& array, int n){
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
#endif //UNIT_KAHANSUM_H
