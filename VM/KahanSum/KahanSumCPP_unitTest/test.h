#ifndef UNIT_TEST_H
#define UNIT_TEST_H

#include "unitTest.h"
#include "../KahanSumCPP/KahanSum.h"

class test: public unitTest{
public:
    void check() override{
        bool check = true;
        double arr[] = {-0.215658663043966,
                      -0.492527580913462,
                      -0.269875306398424,
                      0.117401836814101,
                      -0.047543415743381,
                      -0.843888416760003,
                      -0.769400926489953,
                      -0.109353029101274,
                      -0.451327447567128,
                      -0.373765041670001,
                      -0.57417096415687,
                      0.445267247389472,
                      -0.144024127341733,
                      -0.423780798926874,
                      0.005243344612406,
                      -0.025707503513994,
                      -0.37992314391242,
                      0.37525536424463,
                      -0.346477672992113};
        double res = -4.52425624547099;
        try {
            BOOST_REQUIRE(KleinSum(arr, 19) == res);
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
        double arr1[] = {-0.215658663043966,
                        -0.492527580913462,
                        -0.269875306398424,
                        0.117401836814101,
                        -0.047543415743381,
                        -0.769400926489953,
                        -0.109353029101274,
                        -0.451327447567128,
                        -0.373765041670001,
                        -0.843888416760003,
                        -0.57417096415687,
                        0.445267247389472,
                        -0.423780798926874,
                        0.005243344612406,
                        -0.144024127341733,
                        -0.025707503513994,
                        -0.37992314391242,
                        0.37525536424463,
                        -0.346477672992113};
        try {
            BOOST_REQUIRE(KleinSum(arr1, 19) == res);
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

class test2: public unitTest{
public:
    void check() override{
        bool check = true;
        double arr2[] = {1, 1.0E-20, 1, -(1.0E-20)};
        double res = 2;
        try {
            BOOST_REQUIRE(NeumaierSum(arr2, 4) == res);
        }
        catch (...) {
            std::cout << "Test 3 not OK" << std::endl;
            check = false;
        }
        if (check){
            std::cout << "Test 3 OK" << std::endl;
        } else{
            check = true;
        }
    }
};

#endif //UNIT_TEST_H
