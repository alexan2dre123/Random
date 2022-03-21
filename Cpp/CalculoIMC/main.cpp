#include<iostream>
#include<cmath>
#include <locale.h>

using namespace std;
int main(){
    setlocale(LC_ALL, "Portuguese");
    float altura,peso,imc;
    cout << "Digite sua altura(m): ";
    cin >> altura;
    cout << "Digite seu peso(kg): ";
    cin >> peso;

    imc = peso/(pow(altura,2));
    if(imc < 17){
        cout << "Seu IMC é de " << imc << " e você esta muito abaixo do peso.";
    } else if(imc >= 17 && imc <= 18.49){
        cout << "Seu IMC é de " << imc << " e você esta abaixo do peso.";
    } else if(imc >= 18.5 && imc <= 24.99){
        cout << "Seu IMC é de " << imc << " e você esta com o peso ideal.";
    } else if(imc >= 25 && imc <= 29.99){
        cout << "Seu IMC é de " << imc << " e você esta acima do peso.";
    } else if(imc >= 30 && imc <= 34.99){
        cout << "Seu IMC é de " << imc << " e você esta com obesidade grau 1.";
    } else if(imc >= 35 && imc <= 39.99){
        cout << "Seu IMC é de " << imc << " e você esta com obesidade grau 2.";
    } else{
        cout << "Seu IMC é de " << imc << " e você esta com obesidade grau 3.";
    }
    cout << "\n";
    return 0;
}
