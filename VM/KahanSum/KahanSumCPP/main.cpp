#include <iostream>
#include <vector>
#include <iomanip>
#include "KahanSum.h"



int main(){
    int n;
    setlocale(LC_ALL, "Russian");
    std::cout << "Введите количество элементов двойной точности" << std::endl;
    std::cin >> n;
    std::vector<double> array;
    double* arr = new double [n];
    for (int i = 0; i < n; i++){
        std::cout << "Введите " << i + 1 << " элемент" << std::endl;
        std::cin >> arr[i];
        array.push_back(arr[i]);
    }

    /*std::cout << std::endl;
    for (int i = 0; i < n; i++){
        std::cout << std::fixed<<std::setprecision(20) << arr[i] << std::endl;
        std::cout << std::fixed<<std::setprecision(20) << array[i] << std::endl;
    }*/

    std::cout << std::fixed<<std::setprecision(20) << KahanSum(arr, n) << std::endl;
    return 0;
}

