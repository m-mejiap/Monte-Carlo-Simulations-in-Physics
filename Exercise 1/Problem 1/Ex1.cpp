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
double Random_2D_Grid_Walk(int N, int M);

//Main.
int main(){
    ofstream outfile;
    outfile.open("data.dat");
    M = 10;
    for(int i=0; i<5; i++){
        N = 50;
        for(int j=0; j<10; j++){
            outfile<<N<<", "<<Random_2D_Grid_Walk(N,M)<<endl;
            N += 50;
        }
        M *= 10;
    }
    outfile.close();
    return 0; 
}

//Methods.
double Random_2D_Grid_Walk(int N, int M){
    double r2 = 0;
    double arr [M];
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
        arr[i] = double(pow(x,2) + pow(y,2));
        r2 += double(pow(x,2) + pow(y,2));
    }
    r2 = r2 / double(M);
    double sum = 0;
    for(int k=0; k<M; k++){
        sum += pow(arr[k]-r2,2);
    }
    double sigma = sqrt(sum/double(M));
    double uncert = sigma/sqrt(M);
    return r2;
}