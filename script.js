const button = document.createElement('button')
button.innerText = 'Redirect to TinyDesk'
button.addEventListener('click', () => {
    alert('Clicked!')
})
document.body.appendChild(button)