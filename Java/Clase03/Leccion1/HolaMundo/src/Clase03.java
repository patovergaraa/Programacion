
import java.util.Scanner;




public class Clase03 {

    public static void main(String[] args) {
        //Clase 2: Variables en Java Parte 1
        /*System.out.println("Hola mundo desde Java");
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
         */
        
        //Clase 3 Variables en Java Parte 2
        
        //Var - inferencia de tipos en Java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 - " + miVariableEntera2);
        System.out.println("miVariableCadena2 - " + miVariableCadena2);
        //soutv + tab
        //Para ejecutar Shift + F6 es ka tecka oara mayuscula
        //Reglas para definir una variable en Java
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union); 
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        
        //Ejercicio: Caracteres Especiales con Java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre);//Diagonal inversa y letra n
        System.out.println("Tabulador: \t" + nombre);//Tabulador
        System.out.println("\t\t.:MENÚ:.");
        System.out.println("Retroceso: \b\b" + nombre);//Caracter de retroceso
        System.out.println("Comillas simples: \'" + nombre + "\'");
        System.out.println("Comillas dobles: \"" + nombre + "\"");
        
        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);        
    }
}
