class Node {
public:
    int value;
    Node* next;

    Node(int val) : value(val), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;
    Node* tail;

public:
    LinkedList() : head(nullptr), tail(nullptr) {

    }

    int get(int index) {
        Node* curr = head;
        int i = 0;
        while(curr != nullptr) {
            if(i == index) {
                return curr->value;
            }
            curr = curr->next;
            ++i;
        }

        return -1; // Index out of bounds
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        if(head == nullptr) {
            head = tail = newNode;
        }
        else {
            newNode->next = head;
            head = newNode;
        }
    }
    
    void insertTail(int val) {
        // Node* newNode = new Node(val);
        Node* newNode = new Node(val);

        if(head == nullptr) {
            head = tail = newNode;
        }
        else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    // 1 2 3 4
    bool remove(int index) {

        // Empty List
        if(head == nullptr || index < 0) {
            return false;
        }

        // List with one node
        Node* tmp = head;
        if(index == 0) {
            head = head->next;
            if(head == nullptr) {
                tail = nullptr;
            }
            delete tmp;
            return true;
        }

        for(int i = 0; tmp != nullptr && i < index - 1; ++i) {
            tmp = tmp->next;
        }

        if(tmp == nullptr || tmp->next == nullptr) {
            return false;
        }

        Node* next = tmp->next->next;
        delete tmp->next;
        tmp->next = next;
        if(tmp->next == nullptr) {
            tail = tmp;
        }

        return true;
    }

    vector<int> getValues() {
        vector<int> vals;
        Node* curr = head;
        while(curr != nullptr) {
            vals.push_back(curr->value);
            curr = curr->next;
        }

        return vals;
    }
};