function countPositivesSumNegatives(input) {
  let pos = input.filter(item => item > 0);
  let neg = input.filter(item => item < 0);
  return [pos.length, neg.reduce((a, b) => a + b)];
}