var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre + ' ' + apellido; // Primera concatenación
console.log(nombreCompleto);
var nombreCompleto2 = 'Patricio' + ' ' + 'Vergara'; // Segunda concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izquierda a derecha
console.log(juntos);
juntos = nombre + 78 + 17; // Aquí se puede diferenciar por los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercera concatenación usando el operador simplificado
console.log(nombre);
