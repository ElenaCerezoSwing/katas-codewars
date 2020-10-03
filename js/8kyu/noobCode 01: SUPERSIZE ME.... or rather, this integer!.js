function superSize(num){
  // Pasamos a string
  let string = num.toString();
  // Hacemos un array de los elementos
  let splittedString = string.split('');
  // Los ordenamos de mayor a menor
  let sortedElement = splittedString.sort((a, b) =>b - a);
  // Realizamos un reduce para acumular los valores
  const reducer = (accumulator, currentValue) => accumulator + currentValue;
  // Aplicamos el reduce sobre el array de los elementos ordenados
  let reducedString = sortedElement.reduce(reducer);
  // Pasamos el resultado a entero
  let result = parseInt(reducedString);
  return result
}