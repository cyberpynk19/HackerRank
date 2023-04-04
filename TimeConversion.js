function timeConversion(s) {
    // Write your code here
    let texto = s.split(':');
    let hora = parseInt(texto[0]) 
    let min = parseInt(texto[1])
    let seg = parseInt(texto[2])

    if (texto[2].includes('PM')) {
        if (hora !== 12) {
            hora+=12
        }
    } else 
        if (hora === 12) {
            hora = 0
        }
     
    
//Aqui estamos retornando uma string que contém as variáveis hora, min e seg, 
//formatadas para ter dois dígitos em cada uma, e separadas por dois-pontos. 
//Para fazer isso, usamos o método toString() para converter os valores numéricos em strings
//e o método padStart() para adicionar um zero à esquerda, caso o valor tenha apenas um dígito.

    return `${hora.toString().padStart(2, '0')}:${min.toString().padStart(2, '0')}:${seg.toString().padStart(2, '0')}`;
}

s = '12:05:45PM';

console.log(timeConversion(s));