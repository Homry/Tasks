#ifndef UNIT_TEST_H
#define UNIT_TEST_H

#include "unitTest.h"
#include "../KahanSumCPP/KahanSum.h"

class test: public unitTest{
public:
    void check() override{
        double* arr = new double [2];
        arr[0] = 0.987654321;
        arr[1] = 0.369;
        double res = 1.356654321;
        bool check = true;
        try {
            BOOST_REQUIRE(KahanSum(arr, 2) == res);
            delete arr;
        }
        catch (...) {
            std::cout << "Test 1 not OK" << std::endl;
            check = false;
        }
        if (check){
            std::cout << "Test 1 OK" << std::endl;
        } else{
            check = true;
        }

        arr = new double [3];
        arr[0] = 13.258;
        arr[1] = 158.269852;
        arr[2] = 0.00000001;
        res = 171.52785201;
        try {
            BOOST_REQUIRE(KahanSum(arr, 3) == res);
            delete arr;
        }
        catch (...) {
            std::cout << "Test 2 not OK" << std::endl;
            check = false;
        }
        if (check){
            std::cout << "Test 2 OK" << std::endl;
        } else{
            check = true;
        }
    }

};

#endif //UNIT_TEST_H
