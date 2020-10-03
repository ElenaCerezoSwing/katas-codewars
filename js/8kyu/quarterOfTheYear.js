const quarterOf = (month) => {
  return month / 3 > 3 ? 4 
    : month / 3 > 2 ? 3 
    : month / 3 > 1 ? 2 : 1; 
  
}