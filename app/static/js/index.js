import { createList } from './taskList.js'
import { deleteTask } from './deleteTask.js'
import { sendSubmition } from './completeTask.js'

document.addEventListener('DOMContentLoaded', () => {
    // Display tasks in DOM:
    createList().then(() => {
        // Adding deletion functionality:
        const deleteButtons = document.querySelectorAll('.delete-button')
        deleteButtons.forEach(button => {
            button.addEventListener('click', deleteTask)
        })

        // Adding submition on change:
        let timer
        const checkboxes = document.querySelectorAll('.task-checkbox')
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                clearTimeout(timer)
                // To avoid spamming, the submition is sent only after 2 seconds
                // of the last modification on any task:
                timer = setTimeout(sendSubmition, 2000)
            })
        })
    })
})
