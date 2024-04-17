#include<iostream>
using namespace std;
int main(){
        int box1,box2,box3,bag;
    cout<<"Enter the size of the first box : ";
    cin>>box1;
    cout<<"Enter the size of the second box : ";
    cin>>box2;
    cout<<"Enter the size of the third box : ";
    cin>>box3;
    cout<<"Enter the size of the bag : ";
    cin>>bag;
    int p = box1+box2+box3;
     if(box1<=bag && box2<=bag && box3 <=bag){
            if(p<=bag){
                cout<<"Minimum requirement of bag = 1";
            }
            else if(box1+box2<=bag || box1+box3 <=bag || box2+box3<=bag){
                cout<<"Minimum requirement of bag = 2";
            }
            else{
                cout<<"requirement of bag= 3 ";
            }
    }
    else{
        cout<<"Please Enter Valid Box-Size ";
    }


    return 0;
}

