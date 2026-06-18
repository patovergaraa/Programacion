import java.util.Scanner;

public class Libros {
    public static void main(String[] args) {
        // Se recomienda usar minúscula para el nombre del objeto (scanner)
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el nombre del libro: ");
        String nombreLibro = scanner.nextLine();

        System.out.print("Escriba el nombre del autor del libro: ");
        String nombreAutor = scanner.nextLine();

        System.out.println("El libro " + nombreLibro + " fue escrito por " + nombreAutor);

        scanner.close();
    }
}
