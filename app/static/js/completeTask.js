export function sendSubmition() {
    const content = []
    const checkboxes = document.querySelectorAll('.task-checkbox')
    checkboxes.forEach(checkbox => {
        let entry = {
            id: Number(checkbox.id.replace('task-completed-', '')),
            description: 'placeholder',
            completed: checkbox.checked
        }
        content.push(entry)
    })

    const request = {
        method: 'post',
        body: JSON.stringify(content),
        headers: { 'Content-Type': 'application/json' }
    }

    fetch('/complete_tasks', request)
}
