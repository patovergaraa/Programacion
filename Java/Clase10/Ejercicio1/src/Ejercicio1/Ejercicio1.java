import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {

        try (Scanner teclado = new Scanner(System.in)) {
            System.out.print("Ingrese el total de horas: ");
            int horasTotales = teclado.nextInt();
            
            int semanas = horasTotales / 168; // 1 semana = 168 horas
            int resto = horasTotales % 168;
            
            int dias = resto / 24;
            int horas = resto % 24;
            
            System.out.println("Semanas: " + semanas);
            System.out.println("Días: " + dias);
            System.out.println("Horas: " + horas);
        }
    }
}