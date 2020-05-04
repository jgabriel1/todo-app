export function deleteTask(e) {
    e.preventDefault()

    const index = this.id.replace('delete', '')
    const csrfToken = document.querySelector('#csrf_token').getAttribute('value')

    const headers = new Headers({ 'X-CSRFToken': csrfToken })
    const request = {
        headers,
        method: 'POST',
        mode: 'same-origin',
        body: {},
    }

    fetch(`/delete_task/${index}`, request).then(response => {
        if (response.ok) {
            this.parentNode.remove()
        } else {
            console.log('Something went wrong!')
        }
    })
}
