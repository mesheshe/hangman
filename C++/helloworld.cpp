//// Online C++ compiler to run C++ program online
//#include <iostream>
//#include <vector>
//using namespace std;
//
//int main() {
//    long long n,maxweight,temp;
//    cin >> n >> maxweight;
//    vector<int> v;
//    for (long long i = 0; i < n; i++){
//        cin >> temp;
//        if (v.size() == 0){
//            v.push_back(temp);
//        }
//        else{
//            vector<int>::iterator itt = v.begin();
//            while (itt != v.end() && *itt < temp){
//                itt++;
//            }
//            v.insert(itt,temp);
//        }
//    }
//    long long count = 0;
//    long long sum = 0;
//    vector<int>::iterator it = v.begin();
//    for (it; it != v.end(); it++){
//        int temp = sum;
//        temp+= *it;
//        if (temp <= maxweight){
//            sum += *it;
//        }
//        else{
//            count ++;
//            sum = *it;
//        }
//    }
//    cout << count + 1;
//}
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    cout << "hello"<<endl;
    cout<< "Please enter your name: ";
    string name;
    cin >> name;
    cout << "Your name is "<< name ; 
    return 0;
}