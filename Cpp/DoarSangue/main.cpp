#include<iostream>
#include<locale.h>

using namespace std;

int main(){
    setlocale(LC_ALL, "Portuguese");
    int idade;

    cout << "Quantos anos você tem? ";
    cin >> idade;

    if(idade>=18 && idade <= 67){
        cout << "Parabéns, você esta apto a doar sangue.\n";
    } else {
        cout << "Você não esta apto a doar sangue.\n";
    }
    return 0;
}
