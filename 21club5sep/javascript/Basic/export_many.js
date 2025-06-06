function capitalizeString(str){
    return str[0].toUpperCase() + str.slice(1)
}
function capitalizeFirstAndLast(str){
    return str[0].toUpperCase() + str.slice(1, str.length-1) + str[str.length - 1].toUpperCase()
}
const SECRET = 3.14

// module.export = {capitalizeFirstAndLast, capitalizeString}

export {capitalizeString, capitalizeFirstAndLast}