#include<iostream>
#include<locale.h>

using namespace std;

int main(){
    setlocale(LC_ALL, "Portuguese");
    int idade;

    cout << "Quantos anos voc� tem? ";
    cin >> idade;

    if(idade>=18 && idade <= 67){
        cout << "Parab�ns, voc� esta apto a doar sangue.\n";
    } else {
        cout << "Voc� n�o esta apto a doar sangue.\n";
    }
    return 0;
}
