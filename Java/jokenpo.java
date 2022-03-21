import java.util.Scanner;
import java.util.Random;

class Jokenpo {
    private static int randomNumberInRange(int min, int max) {
        Random random = new Random();
        return random.nextInt((max - min) + 1) + min;
    }

    public static void main(String[] args) {
        boolean menuLoop = true;
        boolean asking = true;
        int pjogador = 0, pcomputador = 0;
        System.out.println("Jogo termina quando um fizer 5 pontos(Mude a quantidade na aba opções)! Boa Sorte :D\nRegras:\n-Pedra ganha de Tesoura e perde pro Papel.\n-Papel ganha da Pedra e perde pra Tesoura.\n-Tesoura ganha do Papel e perde para Pedra.");
        Scanner input = new Scanner(System.in);
        int pontoFinal = 5;
        
        

        while(menuLoop){
            System.out.print("1 - Jogar\n2 - Opções\n0 - Sair\nDigite uma opção: ");
            int menuOp = input.nextInt();
            switch (menuOp) {
                case 1:
                    while(asking){
                        if(pjogador == pontoFinal){
                            System.out.println("Placar Final:\nComputador: " + pcomputador + " Ponto(s)\nJogador: " + pjogador + " Ponto(s)\n" + "Parabéns, você venceu ! Gostaria de jogar de novo ? 1 - Sim / 2 - Não");
                            int reboot = input.nextInt();
                            if (reboot == 1){
                                pjogador = 0;
                                pcomputador = 0;
                                continue;
                            } else {break;}
                        }
                        if (pcomputador == pontoFinal){
                            System.out.println("Placar Final:\nComputador: " + pcomputador + " Ponto(s)\nJogador: " + pjogador + " Ponto(s)\n" + "Infelizmente você perdeu ! Gostaria de jogar de novo ? 1 - Sim / 2 - Não");
                            int reboot = input.nextInt();
                            if (reboot == 1){
                                pjogador = 0;
                                pcomputador = 0;
                                continue;
                            } else {break;}
                        }
        
                        int computador = randomNumberInRange(1, 3);
                        System.out.print("Escolha entre pedra, papel ou tesoura.\n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Checar pontuação\n0 - Sair\nDigite um dos números indicados: ");
                        int jogador = input.nextInt();
        
                        if(jogador == 0){
                            asking = false;
                            break;
                        }
                        if (jogador > 4 || jogador < 0){
                            System.out.println("\nNúmero incorreto, digite novamente.\n");
                            continue;
                        }
                        if(jogador == 4) {
                            System.out.println("\nSua pontuação: " + pjogador + " Ponto(s)" + "\nComputador: " + pcomputador + " Ponto(s)\n");
                        }
                        if (jogador == computador) {
                            String resultado = (jogador == 1)? "Pedra":((jogador == 2)? "Papel":"Tesoura");
                            System.out.printf("\nJogador: %s \nComputador: %s\n", resultado, resultado);
                            System.out.println("\nEmpate! Nenhum ponto foi creditado.\n");
                        }
        
                        else if (jogador == 1 & computador == 2) {
                            System.out.println("\nJogador: Pedra\nComputador: Papel");
                            System.out.println("\nVocê Perdeu. +1 Ponto pro computador.\n");
                            pcomputador++;
                        }
                        else if (jogador == 1 & computador == 3) {
                            System.out.println("\nJogador: Pedra \nComputador: Tesoura ");
                            System.out.println("\nVocê Ganhou. +1 Ponto adicionado.\n");
                            pjogador++;
                        }
                        else if (jogador == 2 & computador == 1) {
                            System.out.println("\nJogador: Papel \nComputador: Pedra");
                            System.out.println("\nVocê Ganhou. +1 Ponto adicionado.\n");
                            pjogador++;
                        }
                        else if (jogador == 2 & computador == 3) {
                            System.out.println("\nJogador: Papel \nComputador: Tesoura");
                            System.out.println("\nVocê Perdeu. +1 Ponto pro computador.\n");
                            pcomputador++;
                        }
                        else if (jogador == 3 & computador == 1) {
                            System.out.println("\nJogador: Tesoura \nComputador: Pedra");
                            System.out.println("\nVocê Perdeu. +1 Ponto pro computador.\n");
                            pcomputador++;
                        }
                        else if (jogador == 3 & computador == 2) {
                            System.out.println("\nJogador: Tesoura \nComputador: Papel");
                            System.out.println("\nVocê Ganhou. +1 Ponto adicionado.\n");
                            pjogador++;
                        }
                    }
                    break;
                case 2:
                    System.out.print("1 - Mudar pontuação necessaria para ganhar\n0 - Sair\nDigite uma opção: ");
                    int optionNumber = input.nextInt();
                    switch (optionNumber) {
                        case 1:
                            System.out.print("\nDigite quantidade de pontos necessario para terminar a partida: ");
                            pontoFinal = input.nextInt();
                            break;
                        case 0:
                            break;
                    
                        default:
                            System.out.println("\nNúmero incorreto, retornando para o menu...\n");
                            break;
                    }
                    break;
                case 0:
                    menuLoop = false;
                    break;
                default:
                    break;
            }
        }
    }
}