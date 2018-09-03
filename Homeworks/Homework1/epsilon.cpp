#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>


using namespace std;

double higher;

void handler(int sign){
  cout << "\n" << "Mayor número de la máquina: " << setprecision(20) << higher << "\n";
  exit(1);
}

int main(int argc, char** argv){
  double temp = 0.5;
  double smaller;
  double power = 1;
  double tmp = pow(power,10);

  ofstream result;
  result.open("result.txt");

  // Excepción para cuando se demora demasiado hallando el número mayor Ctl+c  
  struct sigaction sigIntHandler;
  sigIntHandler.sa_handler = handler;
  sigemptyset(&sigIntHandler.sa_mask);
  sigIntHandler.sa_flags = 0;

  sigaction(SIGINT, &sigIntHandler, NULL);

  // Halla el menor número
  while(1+temp != 1){
    smaller = temp;
    temp = temp/2;
  }

  result << "Menor número de la máquina: " << setprecision(20) << temp << "\n";

// Halla el mayor número con potencias de 2
  while(!(isinf(tmp))){
    higher =  pow(10, power);
    ++power;
    tmp = pow(10, power);
  }

  result <<  "Mayor número de la máquina: " << setprecision(20) << higher << "\n";

  result.close();
  return 0;
}
