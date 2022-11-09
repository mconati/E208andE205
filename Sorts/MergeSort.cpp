/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

bool isSorted(int *array, int size){
    bool sorted = true;
    for (int i=0; i<size-1; ++i){
        if (array[i]>array[i+1]){
            sorted=false;
        }
    }
    return sorted;
}

int min(int a, int b){
    if (a>b){
        return b;
    }
    return a;
}

int * mergeSort(int* array, int size, int* arr2){
    if (size==1){
        return arr2;
    } else {
        int midPoint = size/2;
        int* left =  mergeSort(array, midPoint, arr2);
        int* right = mergeSort(&array[midPoint], size-midPoint, &arr2[midPoint]);
        int a = 0;
        int b = 0;
        int i = 0;

        while (a<midPoint && b<(size-midPoint)){
            if (min(left[a], right[b]) == left[a]){
                array[i] = left[a];
                a++;
            } else{
                array[i] = right[b];
                b++;
            }
            i++;
        }
        while (a<midPoint){
            array[i] = left[a];
            a++;
            i++;
        }
        while (b<(size-midPoint)){
            array[i] = right[b];
            b++;
            i++;
        }
        return array;
    }
}
int main()
{
    int size = 1000000;
    int array [size];
    int arr2 [size];
    for (int i=0; i<size; ++i){
        array[i] = rand()%size;
        arr2[i] = array[i];
    }
    cout<<'\n';
    auto start = chrono::high_resolution_clock::now();
    int* newArray = mergeSort(array, size, arr2);
    auto stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
    cout<<"Runtime: "<<duration.count()<<" microseconds"<<endl;
    cout<<'\n'<<"Sorted: "<<isSorted(newArray, size);
    
    return 0;
}
