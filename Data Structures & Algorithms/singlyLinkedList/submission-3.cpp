class LinkedList {
private:
    struct node {
        int value;
        node* next;
    };

    int size;
    node* linkedList;
public:
    LinkedList() {
        linkedList = new node();
        linkedList = nullptr;
        size = 0;
    }

    int get(int index) {
        if(index >= 0 && index < size) {
            node* track = linkedList;
            for(int i = 0; i < index; i++){
                track = track->next;
            }
            return track->value;
        }
        return -1;
    }

    void insertHead(int val) {
        node* newNode = new node();
        newNode->value = val;
        newNode->next = linkedList;

        linkedList = newNode;
        size++;
    }
    
    void insertTail(int val) {
        node* t = linkedList;
        
        if(t == nullptr) {
            node* newValue = new node();
            newValue->value = val;
            newValue->next = nullptr;

            linkedList = newValue;

            size++;

            return;
        }

        while(t->next != nullptr){
            t = t->next;
        }

        node* newValue = new node();
        newValue->value = val;
        newValue->next = nullptr;

        t->next = newValue;

        size++;
    }

    bool remove(int index) {
        if(index >= 0 && index < size){
            node* t = linkedList;
            if(index == 0) {
                node* remove = linkedList;
                linkedList = linkedList->next;
                delete remove;

                size--;

                return true;
            }

            for(int i = 0; i < index - 1; i++){
                t = t->next;
            }

            node* remove = t->next;
            t->next = remove->next;
            delete remove;

            size--;

            return true;
        }
        return false;
    }

    vector<int> getValues() {
        vector<int> values;
        node* t = linkedList;
        for(int i = 0; i < size; i++){
            values.push_back(t->value);
            t = t->next;
        }

        return values;
    }
};
