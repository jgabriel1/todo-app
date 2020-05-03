$(document).ready(() => {
    $('.task-checkbox').each((i, checkbox) => {
        $(checkbox).change(() => {
            console.log(`${checkbox.id}: ${checkbox.checked}`)
            // Able to access element through ~checkbox~
        })
    })

    $('.delete-button').each((i, del_btn) => {
        $(del_btn).click((e) => {
            // Prevent default for now...
            e.preventDefault() 
            const id = del_btn.id.replace('delete', '')
            $.ajax({
                url: `/delete_task/${id}`,
                type: 'POST'
            })
            // it is posting \o/
        })
    })
})