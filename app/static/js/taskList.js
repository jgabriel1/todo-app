export async function createList() {
    const request = {
        method: 'get',
        mode: 'same-origin'
    }

    await fetch('/task_list', request)
        .then(response => response.json())
        .then(list => { createNodes(list) })
}

function createNodes(list) {
    const nodeList = document.querySelector('#task-list')
    const setAttributes = (elem, attrs) => Object.assign(elem, attrs)

    for (let entry of list) {
        let node = document.createElement('li')
        node.className = 'form-check'

        let checkbox = document.createElement('input')
        setAttributes(checkbox, {
            id: `task-completed-${entry.id}`,
            type: 'checkbox',
            checked: entry.completed,
            className: 'form-check-input task-checkbox'
        })

        let taskLabel = document.createElement('label')
        taskLabel.innerHTML = entry.description
        taskLabel.setAttribute('for', `task-completed-${entry.id}`)

        let deleteButton = document.createElement('button')
        setAttributes(deleteButton, {
            id: `delete${entry.id}`,
            type: 'button',
            innerHTML: 'Delete',
            className: 'btn btn-primary delete-button'
        })

        let elements = [checkbox, taskLabel, deleteButton]
        elements.forEach(element => node.appendChild(element))

        nodeList.appendChild(node)
    }
}

