package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese un primer numero: ");
        int numero1 = teclado.nextInt();

        System.out.print("Ingrese un segundo numero: ");
        int numero2 = teclado.nextInt();

        if (numero1 == numero2) {
            System.out.println(numero1 * numero2);
        } else if (numero1 > numero2) {
            System.out.println(numero1 - numero2);
        } else if (numero1 < numero2) {
            System.out.println(numero1 + numero2);
        }

        teclado.close();
    }
}
