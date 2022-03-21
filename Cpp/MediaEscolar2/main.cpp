#include<iostream>
#include<cmath>

using namespace std;

int main(void){
	float nota1,nota2,nota3,nota4,media;

	cout << "Digite a primeira nota: ";
	cin >> nota1;

	cout << "Digite a segunda nota: ";
	cin >> nota2;

	cout << "Digite a terceira nota: ";
	cin >> nota3;

	cout << "Digite a quarta nota: ";
	cin >> nota4;

	media = (nota1+nota2+nota3+nota4)/4;
	if(media >= 6){
        cout << "Parabens, voce foi aprovado com um total de " << media << " Pontos";
	} else{
        cout << "Infelizmente, voce foi reprovado com um total de " << media << " Pontos";
	}


	return 0;

}
