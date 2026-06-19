import java.util.Scanner;

public class Ejercicio2 {

    public static void main(String[] args) {

        try (Scanner teclado = new Scanner(System.in)) {
            System.out.print("Ingrese el valor de a: ");
            double a = teclado.nextDouble();
            
            System.out.print("Ingrese el valor de b: ");
            double b = teclado.nextDouble();
            
            double resultado = Math.pow(a, 2) + Math.pow(b, 2) + (2 * a * b);
            
            System.out.println("El cuadrado de la suma es: " + resultado);
        }
    }
}