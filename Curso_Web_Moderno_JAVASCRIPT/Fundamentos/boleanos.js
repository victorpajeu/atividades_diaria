isActive = true
console.log(isActive)

isActive = 1 
console.log(!!isActive)

isActive= 0 

console.log(!!isActive)

isActive = ''
console.log(!!isActive)
console.log(!!NaN)
console.log(!!undefined)
console.log(!!null)

console.log(isActive || 'Não é conhecido ')
console.log(!!null || 'Foi colocado um  valor  invalido')