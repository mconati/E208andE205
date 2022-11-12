

#include <iostream>
using namespace std;
#include <chrono>

bool isSorted(int *array, int size){
    bool sorted = true;
    for (int i=0; i<size; ++i){
        if (array[i]>array[i+1]){
            sorted=false;
        }
    }
    return sorted;
}

void bubbleSort(int target[], int size) {
    for (int i=0; i<size; ++i){
        for (int j=1; j<size+1; ++j){
            int prev = target[j-1];
            int cur = target[j];
            if (prev>cur){
                int temp = prev;
                target[j-1] = cur;
                target[j] = temp;
            }
        }
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
    bubbleSort(array, size);
    auto stop = std::chrono::_V2::high_resolution_clock::now();
    cout<<"Runtime: ";
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
    cout << duration.count() << endl;
    cout<<'\n'<<"Sorted: "<<isSorted(array, 10);
    return 0;
}

