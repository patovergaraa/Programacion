//Ejercicio para encontrar números pares e impares

let parImpar = 1;
if(parImpar % 2 ==0){
    console.log("Es uin número PAR")
}
else{
    console.log("Es un número IMPAR")
}

//Ejercicio: es mayor de edad
let edad = 20; adulto = 18;
if( edad >= adulto ){
    console.log("Es una persona adulta");
}
else{
    console.log("Es una persona menor de edad");
}

//Ejercicio: dentro de un rango
let dentroRango = 5; //Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}

// Clase 8 Algunos Operadores y Algunas Funciones

// Ejercicio: Si el padre puede asistir al juego de su hijo

let vacaciones = true, diaDescanso = false;
if (vacaciones || diaDescanso) {
    console.log("El padre puede asistir al juego de su hijo");
} 
else {
    console.log("El padre no puede asistir al juego de su hijo");
}