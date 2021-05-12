#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Node{
    public:
        char data;
        Node *next;
};

class LinkedList{
    private:
        Node *head;
        int size;  
    public:
        LinkedList(){
            head = nullptr;
            char cha = 'z';
            for (int i = 0; i < 26; i++){
                Node* newNode = new Node;
                newNode->data = cha;
                newNode->next = head;
                head = newNode;
                cha--;
            }
            size = 26;
        }

        Node* get_head(){
            return head;
        }
        
        int get_size(){
            return size;
        }

        void printLL(){  // output the linked list given the head
            cout << "Word Bank:" << endl;
            Node* node = head;
            while (node != nullptr){
                cout << node->data << "  ";
                node = node->next;
            }
            cout<<endl;
        }

        bool remove(char ch){
            // implement the remove letter
            // take into account the case where the letter is not there. 
            if (ch == head ->data && head->next == nullptr){
                head->data = (char)0;
                size--;
                return true;
            }else if (size == 0){
                return false; 
            }
            if (ch == head->data){ 
                Node* temp = head;
                head = head->next;
                delete temp;
                size--;
                return true; 
            }else{
                Node* prev = head;
                Node* curr = prev->next;
                while (curr != nullptr && curr->data != ch){
                    prev = curr;
                    curr = prev->next;
                }
                if(curr != nullptr && curr->data == ch){
                    prev->next = curr->next;
                    delete curr;
                    size--;
                    return true;
                }
            }
            return false;            
        }
};

ostream& operator << (ostream& cout, map<char, vector<int>> &m);
// Print out map
ostream& operator << (ostream& cout, vector<int> &v);
// Print out vector
int hangmanGame();
// Main game
int hangman(int z);
// Drawing the actual stick figure 
bool guessALetter(string &guess, LinkedList &list, map<char, vector<int>> &keyValuePair); 
// returns true if letter is valid, otherwise returns false
string stringToDashes(string word);
// passed by reference so is void needed
void dashesToString(string &word, char, vector <int> &pos);
// index that matches user guess will be how many dashes will be counted
// what if more than one pos exist that match it.  
void wordIndexLibrary(string &word, map<char, vector<int>> &m);
// done but kinda iffy.
// main() should be where I do the function calls, game should be played in the functions.    

int main(){
    hangmanGame();
    return 0;    
}

int hangmanGame(){
    LinkedList li;
    int z = 0; //represents error
    string guess, guessMyWord = "bad cat"; //"cat in the hat!!!";
    map<char, vector<int>> m;
    wordIndexLibrary(guessMyWord, m);
    guess = stringToDashes(guessMyWord);
    guessMyWord = guess; 
    for(auto &n: m){
        dashesToString(guessMyWord, n.first , n.second);
    }
    while (guessMyWord != guess && z != 9){
        bool y = guessALetter(guess, li, m);
        if  (!y){
            z = hangman(z);
        }
    }
    if(guessMyWord == guess){
        cout << guess<<endl<<"Well done you have finished the game"<<endl;
    }else{
        cout << "Better luck next time"<<endl;
    }
    return 0;
}

bool guessALetter(string &guess, LinkedList &list, map<char, vector<int>> &keyValuePair){
    char ch;
    list.printLL();
    cout << guess << endl;
    cout << "Guess a letter: ";
    cin >> ch;
    while (!list.remove(ch)){
        cout << "Not in Word Bank! Guess again: ";
        cin >> ch;
    }
    for (auto &n: keyValuePair){
        if (n.first == ch){
            dashesToString(guess, n.first, n.second);
            return true;
        }
    }
    return false;
}

void dashesToString(string &word, char ch, vector <int> &pos){
    //i have a sorted list of indexes. So I just have to count the number of dashes and letters
    int dashnLetCount = 0, j = 0;

    for (int i = 0; i < word.length(); i++){    
        if ((int)word[i] == 95 || ((int)word[i] > 64 && (int)word[i] < 123)){
            if (dashnLetCount == pos[j]){
                word[i] = ch;
                j++;
            }
            dashnLetCount++;    
        }
    }
}

void wordIndexLibrary(string &word, map<char, vector<int>> &m){
    int subForSpace = 0;
    for (int i = 0; i < word.length(); i++){
        char ch = word[i];
        if (word[i] == ' ') subForSpace++;
        if ((int)ch > 64 && (int)ch < 123){ // between A-z
            if (m.find(ch) == m.end()){
                vector<int> v;
                v.push_back(i - subForSpace);
                m.insert(make_pair(ch, v));
            }else m[ch].push_back(i-subForSpace);
        }
    }
}

string stringToDashes(string word){
    string w = "";
    for (int i = 0; i < word.length(); i++){
        if ((int)word[i] > 64 && (int)word[i] < 123){
            w+= " _ ";
        }else if (word[i] == ' '){
            w+= " ";
        }else
            w += word[i];
    }
    return w;
}

int hangman(int z){
    switch(z){
        case 0:
            cout << " O " << endl;
            return 1;
        case 1:
            cout << " O " << endl;
            cout << " | " << endl;
            return 2;
        case 2:
            cout << " O " << endl;
            cout << "/|\\ " << endl;
            return 3;
        case 3:
            cout << " O " << endl;
            cout << "/|\\ " << endl;
            cout << " ' " << endl;
            return 4;
        case 4:
            cout << " O   " << endl;
            cout << "/|\\ " << endl;
            cout << "/'   " << endl;
            return 5;
        case 5:
            cout << " O   " << endl;
            cout << "/|\\ " << endl;
            cout << "/'   " << endl;
            return 6;
        case 6:
            cout << " O   " << endl;
            cout << "/|\\ " << endl;
            cout << "/'\\ " << endl;
            return 7;
        case 7:
            cout << " O/  " << endl;
            cout << "/|\\ " << endl;
            cout << "/'\\ " << endl;
            return 8;
        default:
            cout << "Game Over"<<endl;
            return 9;
    }
    return 0;
}

ostream& operator << (ostream& cout, map<char, vector<int>> &m){
    for (auto &x: m){
        cout << x.first << ": " <<x.second;
    }
    return cout;
}

ostream& operator << (ostream& cout, vector<int> &v){
    for (int i = 0; i < v.size() - 1; i++){
        cout << v[i] << ", ";
    }
    cout<<v[v.size() - 1]<<endl;
    return cout;
}