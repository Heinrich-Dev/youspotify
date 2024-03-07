const button = document.createElement('button')
button.innerText = 'Get TinyDesk Playlist'
button.addEventListener('click', () => {
    alert('Clicked!')
})
document.body.appendChild(button)

function darken_img(x){
    x.style.filter = "brightness(50%)";
}
function brighten_img(x){
    x.style.filter = "brightness(100%)";
}