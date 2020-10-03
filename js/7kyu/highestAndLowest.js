function highAndLow(numbers){
  let a = numbers.split(' ').map(item => parseInt(item));
  let max = Math.max(...a);
  let min = Math.min(...a);
  return `${max} ${min}`
}