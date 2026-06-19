package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {

        try (Scanner teclado = new Scanner(System.in)) {
            double nota1, nota2, nota3;
            double promedio;
            System.out.println("Digite las 3 calificaciones:");
            nota1 = teclado.nextDouble();
            nota2 = teclado.nextDouble();
            nota3 = teclado.nextDouble();
            promedio = (nota1 + nota2 + nota3) / 3;
            if (promedio >= 70) {
                System.out.println("El alumno esta aprobado con: " + promedio);
            } else {
                System.out.println("El alumno esta desaprobado con: " + promedio);
            }
        }
    }
}