/*
let myArray = ["Zero", "One", "Two", "Three", "Four", "Five"];

// Getting random integer between 5 to 25
// console.log(Math.floor(Math.random()*20 + 5));

// Getting random integer between 0 to 9
let random_index = Math.floor(Math.random()*5);
console.log(myArray[random_index]);
*/

const quotes_Array = [
    {
        author : "Denis Waitley",
        quote : "Time and health are two precious assets that we don’t recognize and appreciate until they have been depleted."
    },
    {
        author : "Robert Urich",
        quote : "A healthy outside starts from the inside."
    },
    {
        author : "Naval Ravikant",
        quote : "A fit body, a calm mind, a house full of love. These things cannot be bought – they must be earned."
    },
    {
        author : "Lucius Annaeus Seneca",
        quote : "The wish for healing has always been half of health."
    },
    {
        author : "Irish proverb",
        quote : "A good laugh and a long sleep are the best cures in the doctor’s book."
    },
    {
        author : "Maxime Lagacé",
        quote : "The more you understand yourself, the more silence there is, the healthier you are."
    },
    {
        author : "Hippocrates",
        quote : "Let food be thy medicine and not the medicine be thy food."
    },
    {
        author : "William Londen",
        quote : "To ensure good health: eat lightly, breathe deeply, live moderately, cultivate cheerfulness, and maintain an interest in life."
    },
    {
        author : "Joseph Pilates",
        quote : "Physical fitness is the first requisite of happiness."
    },
    {
        author : "Voltaire",
        quote : "I have chosen to be happy because it is good for my health."
    }
];

let new_quote_btn = document.getElementById('new_q');
var quote_index;
var quote_object;
const quote_text = document.getElementById('para');
const author_name = document.getElementById('auth_name');

new_quote_btn.addEventListener('click', () => {
    quote_index = Math.floor(Math.random()*10);
    quote_object = quotes_Array[quote_index];
    quote_text.innerText = quote_object["quote"];
    author_name.innerText = quote_object["author"];
})