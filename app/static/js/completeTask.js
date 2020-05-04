export function submitCompletion() {
    const checkboxes = document.querySelectorAll('.task-checkbox')
    const body = []
    checkboxes.forEach(checkbox => {
        let entry = {
            id: Number(checkbox.id.replace('task-completed-', '')),
            description: 'placeholder',
            completed: checkbox.checked
        }
        body.push(entry)
    })

    const request = {
        method: 'post',
        body: JSON.stringify(body),
        headers: { 'Content-Type': 'application/json' }
    }

    fetch('/complete_tasks', request)
}