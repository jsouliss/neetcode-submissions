class DynamicArray {
public:
private:
    int* arr;
    int length;
    int capacity;
public:
    DynamicArray(int capacity) : capacity(capacity), length(0) {
        if(capacity > 0) {
            arr = new int[capacity];
        } 
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if(length == capacity) {
            resize();
        }
        arr[length] = n;
        length++;
    }

    int popback() {
        int val = arr[length - 1];
        if(length > 0) {
            --length;       
        }
        return val;
    }

    void resize() {
        capacity = capacity * 2;
        int* newArr = new int[capacity];

        // Copy values from arr to newArray
        for(int i = 0; i < length; ++i) {
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};