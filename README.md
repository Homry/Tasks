# Tasks



# В папке VM предоставленны задания по лабораторным работам
## rotateTriangle - лабораторная работа №1
## predator-prey model - лабораторная работа №2 (можель хищник-жертва)

## Алгоритм Кэхэна!

#### Запуск cpp проекта

```
cd VM/KahanSum/KahanSumCPP
cmake CMakeLists.txt 
make && ./lab_3
```

#### Запуск юнит-тестов cpp
```
cd VM/KahanSum/KahanSumCPP_unitTest/
cmake CMakeLists.txt 
make && ./unit
```

#### Запуск py проекта
```
cd VM/KahanSum/KahanSumPy
python3 main.py
```

#### Запуск юнит-тестов py
```
cd VM/KahanSum/KahanSumPy
python3 test.py -v
```

## Добавление своих тестов
- Для добавления собственных тестов вы можете изменить количество чисел в тестиреумом массиве `arr` и предполагаемое значени `res` или написать собственную функцию `test3`, например, где тело функции будет аналогично представленным, но с собственными значениями, для python тестов `test.py`
```
 def test1(self):
        arr = [0.987654321, 0.369]
        res = 1.356654321
        self.assertEqual(KahanSum(arr), res)
```

- Так же вы можете изменить размер и значение тестируемого массива `arr` и предполагаемое значени `res`, а так же размер массива внутри функции `BOOST_REQUIRE(KahanSum(arr, 3) == res);`. Для написания собственного теста необходимо скопировать представленный блок, изменить данные как описывалось выше, а так же можно изменить номер теста в `  std::cout << "Test 2 not OK" << std::endl;` и ` std::cout << "Test 2 OK" << std::endl;`.
```
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
```
