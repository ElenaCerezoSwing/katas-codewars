function generateRange(min, max, step){
  let a = [min], b = min;
  while (b < max) {
      a.push(b += step);
  }
  return a;
}