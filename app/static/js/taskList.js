export async function createList() {
    await fetch('/task_list')
        .then(response => response.json())
        .then(list => { createNodes(list) })
}

function createNodes(list) {
    const nodeList = document.querySelector('#task-list')

    for (let entry of list) {
        let node = createWithAttributes('li', { className: 'form-check' })

        let checkbox = createWithAttributes('input', {
            id: `task-completed-${entry.id}`,
            type: 'checkbox',
            checked: entry.completed,
            className: 'form-check-input task-checkbox'
        })

        let taskLabel = createWithAttributes('label', { innerHTML: entry.description })
        taskLabel.setAttribute('for', `task-completed-${entry.id}`)

        let deleteButton = createWithAttributes('button', {
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

/**
 * @param {String} tag 
 * @param {Object} attrs 
 * @returns {Element}
 */
function createWithAttributes(tag, attrs) {
    const element = document.createElement(tag)
    Object.assign(element, attrs)

    return element
}
