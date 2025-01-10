let bar_icon = document.querySelector(".bar-icon");
let nav_expand;

bar_icon.addEventListener("click", () => {
  nav_expand = document.querySelector(".nav-expand");
  nav_expand.classList.toggle("show-nav");
});
