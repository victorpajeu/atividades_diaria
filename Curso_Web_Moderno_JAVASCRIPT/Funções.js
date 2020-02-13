function falar(){
    console.log("Estou Falando!!!")
}
// uma função pode ser um  bloco de código Que é Nomeado 
falar()

function andar(questao){
    nome = questao
    console.log(nome)
}

andar("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

var nome = "Ola mundo"

function editaNome(nome){
    this.nome = nome
    return this.nome
}


console.log(nome)
console.log(editaNome(nome))

function limpaNome(nome){
    this.nome = ''
    return this.nome 
}

console.log(limpaNome(nome))
console.log(nome)


// pode armazenar uma função em um  variável 


var nome = function andar(a, b ){
    console.log(a, 2* b)
}

nome('Ola Munbdo', 100)