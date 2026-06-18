// Clase 3 Tipos de Datos Parte 1

// Tipos de Datos de JavaScript
/*
La sintaxis en lo que es comentrios
es muy similar a la de Java
realmente diriamos que es identica
*/

//Tipo String
var nombre = 'Patricio'; //Tipo String
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre)
nombre = 12.3;
console.log(typeof nombre)

//Tipo Numérico
var numero = 3000; //Tipo Numérico
console.log(numero);

//Tipo Object
var objeto = {
    nombre : 'Patricio',
    apellido : 'Vergara',
    telefono : '2948323232'
}
console.log(typeof objeto);

/*
Clase 4 Tipos de Datos Parte 2
*/

//Tipo de dato Boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato Funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato Symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo)

//Tipo de dato Clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

