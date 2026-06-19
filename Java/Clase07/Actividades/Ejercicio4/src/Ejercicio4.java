import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite el primer número:");
        int num1 = Integer.parseInt(entrada.nextLine());

        System.out.println("Digite el segundo número:");
        int num2 = Integer.parseInt(entrada.nextLine());

        var mayor = (num1 > num2) ? num1 : num2;

        System.out.println("El número mayor es: " + mayor);
    }
}