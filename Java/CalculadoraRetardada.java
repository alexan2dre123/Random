import java.util.Scanner;


class Calculadora{
    public static boolean asking = true;    
    

    private static int operations(int op){
        Scanner input = new Scanner(System.in);
        int result = 0;
        switch (op) {
            case 1:
                System.out.print("Digite o primeiro número: ");
                int n1Sum = input.nextInt();
                System.out.print("Digite o segundo número: ");
                int n2Sum = input.nextInt();
                result = n1Sum + n2Sum;
                break;
            case 2:
                System.out.print("Digite o primeiro número: ");
                int n1Sub = input.nextInt();
                System.out.print("Digite o segundo número: ");
                int n2Sub = input.nextInt();
                result = n1Sub - n2Sub;
                break;
            case 3:
                System.out.print("Digite o primeiro número: ");
                int n1Multi = input.nextInt();
                System.out.print("Digite o segundo número: ");
                int n2Multi = input.nextInt();
                result = n1Multi * n2Multi;
                break;
            case 4:
                System.out.print("Digite o primeiro número: ");
                int n1Div = input.nextInt();
                System.out.print("Digite o segundo número: ");
                int n2Div = input.nextInt();
                if (n2Div == 0){
                    System.out.print("Divisão por 0 é indefinida, tente novamente.");
                } else result = n1Div * n2Div;
                break;
            case 0:
                break;
            
        }
        return result;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (asking) {
            System.out.print("Escolha um tipo de operação.\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n\nDigite uma opção: ");
            int option = input.nextInt();
            if (option == 0){
                asking = false;
            } else System.out.println("\nResultado: " + operations(option) + "\n"); 
        }
    }
}