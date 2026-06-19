import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {

        try (Scanner teclado = new Scanner(System.in)) {
            double participacion, parcial1, parcial2, examenFinal;
            double notaFinal;
            System.out.print("Ingrese la nota de participación: ");
            participacion = teclado.nextDouble();
            System.out.print("Ingrese la nota del primer parcial: ");
            parcial1 = teclado.nextDouble();
            System.out.print("Ingrese la nota del segundo parcial: ");
            parcial2 = teclado.nextDouble();
            System.out.print("Ingrese la nota del examen final: ");
            examenFinal = teclado.nextDouble();
            notaFinal = (participacion * 0.10)
                    + (parcial1 * 0.25)
                    + (parcial2 * 0.25)
                    + (examenFinal * 0.40);
            System.out.println("La calificación final es: " + notaFinal);
        }
    }
}