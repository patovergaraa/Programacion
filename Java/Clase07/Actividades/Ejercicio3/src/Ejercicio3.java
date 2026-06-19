import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite la base del rectángulo:");
        double base = Double.parseDouble(entrada.nextLine());

        System.out.println("Digite la altura del rectángulo:");
        double altura = Double.parseDouble(entrada.nextLine());

        double area = base * altura;
        double perimetro = (base + altura) * 2;

        System.out.println("Área = " + area);
        System.out.println("Perímetro = " + perimetro);
    }
}