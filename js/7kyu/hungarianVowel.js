/* Vowel harmony is a phenomenon in some languages. It means that "A vowel or vowels in a word are changed to sound the same (thus "in harmony.")" (wikipedia). This kata is based on vowel harmony in Hungarian.

Task:
Your goal is to create a function dative() (Dative() in C#) which returns the valid form of a valid Hungarian word w in dative case i. e. append the correct suffix nek or nak to the word w based on vowel harmony rules.

Vowel Harmony Rules (simplified)
When the last vowel in the word is

a front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek
a back vowel (a, á, o, ó, u, ú) the suffix is -nak*/
https://www.codewars.com/kata/57fd696e26b06857eb0011e7/train/javascript

function dative(word) {
  const backVowels = 'aáoóuú';
  const vowels = 'aáeéiíoóöőuúüű'
  let index = word[word.length-2];
  let secIndex = word[word.length-3];
  let thirdIndex = word[word.length-4];
  
  return vowels.indexOf(index) != -1 ? (backVowels.indexOf(index)  != -1  ? word + 'nak' : word + 'nek') 
  : (vowels.indexOf(secIndex) != -1 ? (backVowels.indexOf(secIndex)  != -1  ? word + 'nak' : word + 'nek')
  : vowels.indexOf(thirdIndex) != -1 ? (backVowels.indexOf(thirdIndex)  != -1  ? word + 'nak' : word + 'nek'): 0)

}

