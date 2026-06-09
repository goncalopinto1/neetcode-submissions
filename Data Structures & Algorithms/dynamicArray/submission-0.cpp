class DynamicArray {
private:
    int* data;
    int length;
    int capacity;
public:

    DynamicArray(int capacity) : capacity(capacity), length(0){
        data = new int[capacity]();
    }

    int get(int i) {
        if(isValid(i)){
            return data[i];
        }
        return -1;
    }

    void set(int i, int n) {
        if(isValid(i)) {
            data[i] = n;
        }
    }

    void pushback(int n) {
        if(length == capacity) {
            capacity *= 2;

            int* newData = new int[capacity]();

            for(int i = 0; i < length; i++) {
                newData[i] = data[i];
            }

            delete[] data;

            data = newData;
        }

        data[length++] = n;    
    }

    int popback() {
       int removed = data[length - 1];
       length--;
       return removed;
    }

    void resize() {
        capacity *= 2;
        int* newCapacity = new int[capacity]();

        for(int i = 0; i < length; i++){
            newCapacity[i] = data[i];
        }

        delete[] data;

        data = newCapacity;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }

    bool isValid(int i) {
        if(i >= 0 && i < length) {
            return true;
        }
        return false;
    }
};
