/* Return the inputted numerical year in century format. 
The input will always be a 4 digit string. 
So there is no need for year string validation.*/
https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/javascript

function whatCentury(year) {
  const s = year.slice(0, 2);
  const cent = year.slice(2, 4);
  const lastDigit = s[s.length - 1];
  return lastDigit != 0 && lastDigit != 1 && lastDigit != 2 ? (parseInt(s)+1) + 'th'
  : (s[s.length - 1] == 0 ? (s == 10 ? '11th' 
  : (cent == 00 ? s + 'th' :(parseInt(s)+1) + 'st'))
  : (s[s.length - 1] == 1 ? (s == 11 ? '12th' :(parseInt(s)+1) + 'nd')
  : s[s.length - 2] ? (s == 12 ? '13th' :(parseInt(s)+1) + 'rd') : 0))
}


  
