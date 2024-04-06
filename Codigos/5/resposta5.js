let inverterString = (str) => {
    let novaString = ''

    for(let i = str.length - 1; i >= 0; i--)
       novaString += str[i]
    
    return novaString
}

const stringAtual = "Codar eh muito legal!"
const stringInvertida = inverterString(stringAtual)

console.log(stringInvertida)