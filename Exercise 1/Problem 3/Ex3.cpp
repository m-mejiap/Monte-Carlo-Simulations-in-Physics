//Head.
#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

//Variable declaration.
int N; //Number of steps.
int M; //Number of repetitions.
int l = 1;
double tau; //Maximum time.

//Method declaration.
double Random_Sailor_Walk(double t);

//Main.
int main(){
    ofstream outfile;
    outfile.open("data3.dat");
    tau = pow(10,7);
    for(int i=0; i<1000; i++){
       outfile<<Random_Sailor_Walk(tau)<<endl;
    }
    outfile.close();
    return 0; 
}

//Methods.
double Random_Sailor_Walk(double t){
    int x = 0;
    int y = 0;
    int sum = 0;
    double p = double(rand()) / double(RAND_MAX);
    while(t>0){
        if(x == 1000){
            break;
            return t;
        }
        if(sum == 100){
            p = double(rand()) / double(RAND_MAX);
            sum = 0;
        }
        if(p < 0.25){
            x += l;
        }
        if(p > 0.75){
            x -= l;
        }
        if(p >= 0.25 && p <= 0.50){
            y += l;
        }
        if(p > 0.50 && p <= 0.75){
            y -= l;
        }
        t -= 1;
        sum += 1;
    }
}