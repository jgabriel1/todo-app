// In this file, the task list html will be created:

export function createList() {
    const request = {
        method: 'get',
        mode: 'same-origin'
    }

    fetch('/task_list', request)
        .then(response => response.json())
        .then(list => { createNodes(list) })
}

function createNodes(list) {
    const nodeList = document.querySelector('#task-list')
    for (let entry of list) {
        let node = document.createElement('li')
        node.className = 'form-check'

        let checkbox = document.createElement('input')
        checkbox.className = 'form-check-input task-checkbox'
        checkbox.name = `task${entry.id}`
        checkbox.id = `task-completed-${entry.id}`
        checkbox.type = 'checkbox'
        node.appendChild(checkbox)

        let taskLabel = document.createElement('label')
        taskLabel.innerHTML = entry.description
        taskLabel.setAttribute('for', `task-completed-${entry.id}`)
        node.appendChild(taskLabel)

        let deleteButton = document.createElement('button', {})
        deleteButton.className = 'btn btn-primary delete-button'
        deleteButton.type = 'button'
        deleteButton.id = `delete${entry.id}`
        deleteButton.innerHTML = 'Delete'
        node.appendChild(deleteButton)

        nodeList.appendChild(node)
    }
}