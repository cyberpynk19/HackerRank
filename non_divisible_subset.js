const k = 7
let s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]

//const k = 3
//let s = [1, 7, 2, 4]

function nonDivisibleSubset(k, s) {
//    // Write your code here
//
//}
//    let soma = []
//
//    for (let i = 0; i < s.length; i++) {
//        for (let j = i+1; j < s.length; j++) {
//            if((s[i] + s[j]) % k != 0){
//                if (!soma.includes(s[i])) 
//                {
//                    soma.push(s[i])}
//                if (!soma.includes(s[j])) {
//                    soma.push(s[j])
//                }
//            }
//        }
//    }
//
//    const tamanho_soma = soma.length
//
//    return tamanho_soma

  // Contagem de módulos de k para os elementos de s
  const count = Array(k).fill(0);
  console.log(count)
  for (let i = 0; i < s.length; i++) {
    count[s[i] % k]++;
  }

  // Seleciona um elemento de módulo 0, se houver
  let result = Math.min(count[0], 1);
  //console.log(result)

  // Seleciona um elemento para cada par de módulos opostos
  for (let i = 1; i <= k / 2; i++) {
    if (i != k - i) {
      result += Math.max(count[i], count[k - i]);
      //console.log(result)
    } else {
      result += Math.min(count[i], 1);
      //console.log(result)
    }
  }

  return result;

    }

console.log(nonDivisibleSubset(k, s))    