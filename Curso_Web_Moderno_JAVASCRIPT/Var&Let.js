// A diferença entre o Var e o Let é só a questão de escopo.

var nome = "Nome"

{
    var nome = 'Ola mundo'
    console.log(nome)
}

console.log(nome)
