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

void swap(int * array, int first, int second){
    int temp = array[first];
    array[first] = array[second];
    array[second] = temp;
}
bool isSorted(int *array, int size){
    bool sorted = true;
    for (int i=0; i<size; ++i){
        if (array[i]>array[i+1]){
            sorted=false;
        }
    }
    return sorted;
}

void bubbleSort(int target[], int indexes[], int size) {
    for (int i=0; i<size; ++i){
        for (int j=1; j<size+1; ++j){
            int prev = target[j-1];
            int cur = target[j];
            if (prev>cur){
                int temp = prev;
                int temp2 = indexes[j-1];
                target[j-1] = cur;
                indexes[j-1] = indexes[j];
                target[j] = temp;
                indexes[j] = temp2;
            }
        }
    }
}

int pivotPicker(int* array, int size){
    int vals [5];
    int indexes [5];
    for (int i=0; i<5; ++i) {
        indexes[i] = rand()%size;
        vals[i] = array[indexes[i]];
    }
    bubbleSort(vals, indexes, 5);
    return indexes[2];
}

void quickSort(int* array, int size){

    if (size>=2){
    int pivot = 0;


    for (int i=1; i<size; ++i){
        if (array[i]<array[pivot]){
            swap(array, pivot, i);
            swap(array, i, pivot+1);
            pivot++;
     }
    }

    quickSort(array, pivot);
    int * array2 = &array[pivot+1];
    quickSort(array2, size-pivot-1);
    }
}



int main()
{
    int size = 1000000;
    int array [size];
    for (int i=0; i<size; ++i){
        array[i] = rand()%size;
    }
    auto start = std::chrono::_V2::high_resolution_clock::now();
    quickSort(array, size);
    auto stop = std::chrono::_V2::high_resolution_clock::now();
    cout<<"Runtime: ";
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
    cout << duration.count() << endl;
    cout<<'\n'<<"Sorted: "<<isSorted(array, 10);
    return 0;
}