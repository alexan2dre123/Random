import java.util.ArrayList;
import java.util.Scanner;


class App{
    
    private static ArrayList<Double> addNota(){
        System.out.print("\nLembrando que são quatro notas!");
        ArrayList<Double> notas = new ArrayList<Double>();
        for(int i = 1; i < 5; i++){
            try {
                Scanner input = new Scanner(System.in);
                System.out.print("\nDigite a nota " + i + ": ");
                double nota = input.nextDouble();
                if(nota > 10 || nota < 0){
                    System.out.println("Nota incorreta, Digite novamente!");
                    i--;
                } else {notas.add(nota);}

            }
            catch(Exception e) {
                System.out.println("Ocorreu um erro, tente novamente!");
                i--;
            }
        }
        System.out.print("\nNotas cadastradas com sucesso!\n");
        
        return notas;
    }
    public static void main(String[] args) {
        boolean asking = true;
        Scanner input = new Scanner(System.in);
        ArrayList<Double> notaAluno = new ArrayList<Double>();
        double mediaFinal = 0;

        while(asking){  
            System.out.print("1 - Adicionar notas\n2 - Mostrar notas\n3 - Calcular Média\n4 - Remover Notas\n5 - Checar aprovação\n0 - Sair\nDigite uma opção: ");
            int menuop = input.nextInt();

            switch (menuop) {
                case 1:
                    notaAluno = addNota();
                    break;
                case 2:
                    System.out.println("\nNotas bimestrais: " + notaAluno + "\n");
                    break;
                case 3:
                    if (notaAluno.size() <= 3) {
                        System.out.println("\nA quantidade de notas não é o suficiente(4) ou você não adicionou nenhuma nota.\n");
                        continue;
                    } else {
                        mediaFinal = (notaAluno.get(0) + notaAluno.get(1) + notaAluno.get(2) + notaAluno.get(3)) / 4;
                        System.out.println("\nMédia: " + mediaFinal + " Ponto(s)\n");
                    }
                    break;
                case 4:
                    notaAluno.clear();
                    mediaFinal = 0;
                    System.out.println("\nTodas as notas foram removidas !\n");
                    break;
                case 5:
                    if(mediaFinal == 0){
                        System.out.println("\nVocê não calculou a média ainda.\n");
                        break;
                    }
                    System.out.print("Digite a média bimestral de sua escola: ");
                    int mediabi = input.nextInt();
                    if(mediaFinal < mediabi){
                        System.out.println("\nAluno reprovado ! Pontuação: " + mediaFinal + "\n");
                    } else if(mediaFinal >= mediabi) {System.out.println("\nAluno aprovado ! Pontuação: " + mediaFinal + "\n");}
                    break;
                case 0:
                    asking = false;
                    break;
                default:
                    System.out.println("\nOpção inexistente, Por favor digite uma opção correta!\n");
                    break;
            }
            
        }
        input.close();
    }
}
