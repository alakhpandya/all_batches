const li = document.getElementsByTagName('li')
const btn = document.getElementsByClassName('plus-btn')
var btn_icon;

for (let i = 0; i < btn.length; i++) {
    btn[i].addEventListener('click', () => {
        li[i].classList.toggle('show-hide');
        btn_icon = btn[i].children[0]
        if (btn_icon.classList.contains('fa-plus')){
            btn_icon.classList.remove('fa-plus');
            btn_icon.classList.add('fa-minus');
        }
        else{
            btn_icon.classList.add('fa-plus');
            btn_icon.classList.remove('fa-minus');
        }
    })
}