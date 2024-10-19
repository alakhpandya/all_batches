/*
“Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” – Martin Fowler
“First, solve the problem. Then, write the code.” – John Johnson
“Experience is the name everyone gives to their mistakes.” – Oscar Wilde
“ In order to be irreplaceable, one must always be different” – Coco Chanel
“Java is to Javascript what car is to Carpet.” – Chris Heilmann
“Knowledge is power” – Francis Bacon
“Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday’s code.” – Dan Salomon
“Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away.” – Antoine de Saint – Exupery
“Ruby is rubbish! PHP is phpantastic!.” – Nikita Popov
“ Code is like humor. When you have to explain it, it’s bad.” – Cory House
“Fix the cause, not the symptom.” – Steve Maguire
“Optimism is an occupational hazard of programming: feedback is the treament. “ Kent Beck
“When to use iterative development? You should use iterative development only on projects that you want to succeed.” – Martin Fowler
“Simplicity is the soul of efficiency.” – Austin Freeman
“Before software can be reusable it first has to be usable.” – Ralph Johnson
“Make it work, make it right, make it fast.” – Kent Beck
*/

const all_quotes = [
    {
        "author" : "Martin Fowler",
        "quote" : "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."
    },
    {
        "author" : "John Johnson",
        "quote" : "First, solve the problem. Then, write the code."
    },
    {
        "Oscar Wilde" : "Experience is the name everyone gives to their mistakes."
    },
    {
        "Coco Chanel" : "In order to be irreplaceable, one must always be different."
    },
    {
        "Chris Heilmann" : "Java is to Javascript what car is to Carpet."
    },
    {
        "Francis Bacon" : "Knowledge is power."
    },
    {
        "Dan Salomon" : "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Mondays code."
    },
    {
        "Antoine de Saint" : "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away."
    },
    {
        "Nikita Popov" : "Ruby is rubbish! PHP is phpantastic!."
    },
    {
        "Cory House" : "Code is like humor. When you have to explain it, its bad."
    },
    {
        "Steve Maguire" : "Fix the cause, not the symptom."
    },
    {
        "Kent Beck" : "Optimism is an occupational hazard of programming: feedback is the treament."
    },
    {
        "Martin Fowler" : "“When to use iterative development? You should use iterative development only on projects that you want to succeed."
    },
    {
        "Austin Freeman" : "Simplicity is the soul of efficiency."
    },
    {
        "Ralph Johnson" : "Before software can be reusable it first has to be usable."
    },
    {
        "Kent Beck" : "Make it work, make it right, make it fast."
    }
]

const btn = document.querySelector('.btn');
const quote_text = document.querySelector('.quote')
const author_name = document.querySelector('.author-name')
let quote_index

btn.addEventListener('click', ()=>{
    quote_index = Math.floor(Math.random()*16);     // 1
    // quote_index = 1;
    author_name.innerText = all_quotes[quote_index]["author"];
    quote_text.innerText = all_quotes[quote_index]["quote"];
})