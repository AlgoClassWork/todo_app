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
    const title = todoTitleInputElement.value
    alert(title)
}


addTodoFormElement.addEventListener('submit', addTodoForm)
window.onload = fetchAndRenderTodos()
