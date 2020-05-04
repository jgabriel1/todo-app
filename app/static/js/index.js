import { createList } from './taskList.js'
import { deleteTask } from './deleteTask.js'

document.addEventListener('DOMContentLoaded', () => {
    // Display tasks in DOM:
    createList().then(() => {
        // Adding deletion functionality:
        const deleteButtons = document.querySelectorAll('.delete-button')
        deleteButtons.forEach(button => {
            button.addEventListener('click', deleteTask)
        })
    })
})
