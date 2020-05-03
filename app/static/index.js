function deleteTask(e) {
    const index = this.id.replace('delete', '')
    const request = {
        method: 'POST',
        mode: 'same-origin',
        body: null
    }

    fetch(`/delete_task/${index}`, request).then(response => {
        if (response.ok) {
            this.parentNode.remove()
        } else {
            console.log('Something went wrong!')
        }
    })
}

const deleteButtons = document.querySelectorAll('.delete-button')
deleteButtons.forEach(button => {
    button.addEventListener('click', deleteTask)
})
