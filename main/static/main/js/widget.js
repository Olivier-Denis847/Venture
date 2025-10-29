 export async function slides () {
    for (let i = 0; i < 3; i++){
        fetch('/slides')
        .then(response => response.json())
        .then(data => {
            const element = document.createElement('img');
            element.src = data['url']
            element.alt = `slide ${i}`
            document.getElementById(`slide${i}`).appendChild(element)
        })
    }
 }
document.addEventListener('DOMContentLoaded', () => {
   slides()
})