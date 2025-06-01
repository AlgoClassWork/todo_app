const activeTodoListULElement = document.getElementById('active-todo-list')
const completedTodoListULElement = document.getElementById('completed-todo-list')

async function fetchAndRenderTodos() {
    const response = await fetch('/api/todos/')
    const todos = await response.json()
   
    todos.forEach(todo => {
        const listItem = document.createElement('li') 
        listItem.textContent = todo.title 
        if (todo.done) {
            completedTodoListULElement.appendChild(listItem)
        } else {
            activeTodoListULElement.appendChild(listItem)
        }
    })
}

window.onload = fetchAndRenderTodos
