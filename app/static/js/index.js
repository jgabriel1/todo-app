import { deleteTask } from './deleteTask.js'
import { createList } from './taskList.js'

const deleteButtons = document.querySelectorAll('.delete-button')
deleteButtons.forEach(button => {
    button.addEventListener('click', deleteTask)
})

// Display tasks in DOM:
createList()