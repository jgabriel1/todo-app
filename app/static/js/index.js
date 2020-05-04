import { createList } from './taskList.js'
import { deleteTask } from './deleteTask.js'
import { submitCompletion } from './completeTask.js'

document.addEventListener('DOMContentLoaded', () => {
    // Display tasks in DOM:
    createList().then(() => {
        // Adding deletion functionality:
        const deleteButtons = document.querySelectorAll('.delete-button')
        /*
        If this is outside the "then haduken", the list has no elements because
        they haven't been created when this line gets executed. Need to find a 
        way to refactor. For now, this will do.
        */
        deleteButtons.forEach(button => {
            button.addEventListener('click', deleteTask)
        })

        const checkboxes = document.querySelectorAll('.task-checkbox')
        checkboxes.forEach(checkbox => {
            console.log(checkbox.checked)
            checkbox.addEventListener('change', submitCompletion(checkboxes))
        })
    })
})
