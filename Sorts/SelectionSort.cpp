
#include <stdio.h>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <random>
#include <chrono>
using namespace std;
void selectionSort(int* a, int size){
    for (int i=0; i<size; ++i){
        int min = INT_MAX;
        int minDex = 0;
        for (int j=i; j<size; ++j){
            if (a[j]<=min){
                min = a[j];
                minDex = j;
            }
        }
        int temp = a[i];
        a[i] = a[minDex];
        a[minDex] = temp;
    }
}
int main()
{
    int size = 10000;
    int array [size];
    for (int i=0; i<size; ++i){
        array[i] = rand()%10000-5000;
    }
    auto start = std::chrono::_V2::high_resolution_clock::now();
    selectionSort(array, size);
    auto stop = std::chrono::_V2::high_resolution_clock::now();
    cout<<"Runtime: ";
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
    cout << duration.count() << endl;
    return 0;
}
