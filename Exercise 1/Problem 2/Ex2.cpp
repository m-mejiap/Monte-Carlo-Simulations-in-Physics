//Head.
#include <fstream>
#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES
using namespace std;

//Variable declaration.
double N; //Number of steps.
double l; //Step lenght.
double l1; //Possible step lenght.
double l2; //Possible step lenght.

//Method declaration.
double Random_2D_Cont_Walk(int N, double l1, double l2);

//Main.
int main(){
    ofstream outfile;
    outfile.open("data2.dat");
    l1 = 1;
    l2 = 2;
    for(int i=0; i<5; i++){
        N = 50.0;
        for(int j=0; j<7; j++){
            outfile<<N<<", "<<Random_2D_Cont_Walk(N,l1,l2)<<", "<<l1<<", "<<l2<<endl;
            N += 50;
        }
        l1 += 1;
        l2 += 1;
    }
    outfile.close();
    return 0; 
}

//Methods.
double Random_2D_Cont_Walk(int N, double l1, double l2){
    double r2 = 0.0;
    int x = 0.0;
    int y = 0.0;
    double M = 100;
    for(int j=0; j<M; j++){
        for(int i=0; i<N; i++){
            double pl = double(rand()) / double(RAND_MAX);
            if(pl < 0.5){
                l = l1;
            }
            if(pl > 0.5){
                l = l2;
            }
            double a = 2*M_PI*(double(rand()) / double(RAND_MAX));
            x += l * cos(a);
            y += l * sin(a);
        }
        r2 += double(pow(x,2) + pow(y,2));
    }
    r2 = r2 / double(M);
    return r2;
}