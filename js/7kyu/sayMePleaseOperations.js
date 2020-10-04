// You have a string of numbers; starting with the third number each number is the result of an operation performed using the previous two numbers.

// Complete the function which returns a string of the operations in order and separated by a comma and a space, e.g. "subtraction, subtraction, addition"

// The available operations are (in this order of preference):

// 1) addition
// 2) subtraction
// 3) multiplication
// 4) division
// Notes:

// All input data is valid
// The number of numbers in the input string >= 3
// For a case like "2 2 4" - when multiple variants are possible - choose the first possible operation from the list (in this case "addition")
// Integer division should be used
https://www.codewars.com/kata/5b5e0c0d83d64866bc00001d/train/javascript

function sayMeOperations(str) {
  let a = str.split(' ').map(item => parseInt(item));
  let message = [];
  for(let i = 2; i < a.length; i++) {
     let result = a[i] - a[i-1] ===  a[i-2] ? 'addition'
                : a[i] + a[i-1] ===  a[i-2] ? 'subtraction'
                : a[i-2] * a[i-1] ===  a[i] ? 'multiplication' : 'division';
    message.push(result);
  }
  let stringMessage = message.toString();
  return stringMessage.split(',').join(', ')
}
