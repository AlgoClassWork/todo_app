const activeTodoListULElement = document.getElementById('active-todo-list')
const completedTodoListULElement = document.getElementById('completed-todo-list')
const addTodoFormElement = document.getElementById('add-todo-form')
const todoTitleInputElement = document.getElementById('todo-title-input')
const todoDescriptionInputElement = document.getElementById('todo-description-input')


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

async function addTodoForm(event) {
    const title = todoTitleInputElement.value.trim()
    const description = todoDescriptionInputElement.value.trim()

    const response = await fetch('/api/todos/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title, description})
    })

    fetchAndRenderTodos()
}

addTodoFormElement.addEventListener('submit', addTodoForm)
window.onload = fetchAndRenderTodos()