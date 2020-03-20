//Head.
#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

//Variable declaration.
int N; //Number of steps.
int M; //Number of repetitions.
int l = 1; //Step lenght.

//Method declaration.
void Random_2D_Grid_Walk(int N, int M);

//Main.
int main(){
    N = 50;
    M = 1;
    Random_2D_Grid_Walk(N,M);
    return 0; 
}

//Methods.
void Random_2D_Grid_Walk(int N, int M){
    for(int i=0; i<M; i++){
        int x = 0;
        int y = 0;
        for(int j=0; j<N; j++){
            double p = double(rand()) / double(RAND_MAX);
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
        }
        
    }
}