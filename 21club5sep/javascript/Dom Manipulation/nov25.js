const btn2 = document.getElementById('btn2')
const btn3 = document.getElementById('')
const container3 = document.getElementById('container3')
const body = document.querySelector('body')

// const love = () => alert("You love Javascript!")

// btn2.addEventListener('click', love)

const changeBG = () => {
    container3.style.backgroundColor = "yellow";
}

btn2.addEventListener('click', () => alert("You love Javascript!"))

container3.addEventListener('mouseover', changeBG)

container3.addEventListener('mouseleave', ()=>container3.style.backgroundColor = 'skyblue')

// body.addEventListener('mouseleave', () => alert("You are about to leave this site!"))