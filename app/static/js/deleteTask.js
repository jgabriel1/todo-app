export async function deleteTask(e) {
    e.preventDefault()

    const index = this.id.replace('delete', '')
    const url = `/delete_task/${index}`
    const request = {
        method: 'POST',
        mode: 'same-origin',
    }

    await fetch(url, request).then(response => {
        if (response.ok) {
            this.parentNode.remove()
        } else {
            console.log('Something went wrong!')
        }
    })
}
