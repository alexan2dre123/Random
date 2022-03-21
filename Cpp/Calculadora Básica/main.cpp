#include <iostream>

using namespace std;

int main(void){
    int option, n1, n2, total;

    do{
        cout << "1 - Soma\n";
        cout << "2 - Subtracao\n";
        cout << "3 - Divisao\n";
        cout << "4 - Multiplicacao\n";
        cout << "0 - Sair\n";
        cout << "Escolha uma opcao: ";
        cin >> option;

        switch (option)
        {
            case 1:
                cout << "Digite dois numeros: \n";
                cin >> n1;
                cin >> n2;
                total = n1 + n2;
                cout << n1 << " + " << n2 << " = " << total << endl;
                system("pause");
                break;

            case 2:
                cout << "Digite dois numeros: \n";
                cin >> n1;
                cin >> n2;
                total = n1 - n2;
                cout << n1 << " - " << n2 << " = " << total << endl;
                system("pause");
                break;

            case 3:
                cout << "Digite dois numeros: \n";
                cin >> n1;
                cin >> n2;
                total = n1 / n2;
                cout << n1 << " / " << n2 << " = " << total << endl;
                system("pause");
                break;

            case 4:
                cout << "Digite dois numeros: \n";
                cin >> n1;
                cin >> n2;
                total = n1 * n2;
                cout << n1 << " x " << n2 << " = " << total << endl;
                system("pause");
                break;

            case 0:
                break;
        
            default:
                cout << "Opcao incorreta.\n";
                system("pause");
                break;
        }
    } while(option != 0);

    return 0;
}