function noBoringZeros(n) {
  return n === 0 ? 0 : n % 10 != 0 ? n : noBoringZeros(n/10);
}