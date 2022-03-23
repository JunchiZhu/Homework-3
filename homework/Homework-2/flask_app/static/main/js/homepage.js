/*homepage.js*/
const toggleBottom = document.querySelector('.toggle');
const collapsedElm = document.querySelector('.menu_list');
toggleBottom.addEventListener('click', function() {
    collapsedElm.classList.toggle('collapse');
})