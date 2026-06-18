
import java.util.Scanner;




public class Clase05 {

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
        /*var miVariableEntera2 = 10;
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
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/  
        
        //Clase 4 Tipos Primitivo en Java Parte 1
        /*
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: "+ Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: "+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int: "+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long: "+ Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: "+ Long.MAX_VALUE);
        
        float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del Float: "+ Float.MIN_VALUE);
        System.out.println("Valor maximo del Float: "+ Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo del Double: "+ Double.MIN_VALUE);
        System.out.println("Valor maximo del Double: "+ Double.MAX_VALUE);*/
        
        //Clase 5 Tipos Primitivos en Java Parte 2
        
        //Interferencia de tipos var y tipos primitivos
        var numEntero = 20; //Las literales sin punto automáticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; // Automáticamente con la F se transforma en tipo float 
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0; // Automáticamente es de tipo double
        System.out.println("numDouble = " + numDouble);
    }
}
