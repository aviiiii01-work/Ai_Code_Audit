import { debounce } from './utils/debounce.js';
import { throttle } from './utils/throttle.js';
import { groupBy } from './utils/groupBy.js';

const input = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

let todos = JSON.parse(localStorage.getItem('todos')) || [];

function saveTodos() {
  localStorage.setItem('todos', JSON.stringify(todos));
}

function renderTodos() {
  todoList.innerHTML = '';
  todos.forEach((todo, index) => {
    const li = document.createElement('li');
    li.className = 'todo-item';
    li.innerHTML = `
      <span class="todo-text" contenteditable="false">${todo}</span>
      <div>
        <button class="edit-btn">Edit</button>
        <button class="delete-btn">Delete</button>
      </div>
    `;
    todoList.appendChild(li);

    const text = li.querySelector('.todo-text');
    const editBtn = li.querySelector('.edit-btn');
    const deleteBtn = li.querySelector('.delete-btn');

    editBtn.addEventListener('click', () => {
      if (text.isContentEditable) {
        text.contentEditable = 'false';
        todos[index] = text.textContent.trim();
        saveTodos();
        renderTodos();
      } else {
        text.contentEditable = 'true';
        text.focus();
      }
    });

    deleteBtn.addEventListener('click', () => {
      todos.splice(index, 1);
      saveTodos();
      renderTodos();
    });
  });
}

function addTodo() {
  const value = input.value.trim();
  if (!value) return;
  todos.push(value);
  saveTodos();
  renderTodos();
  input.value = '';
}

addBtn.addEventListener('click', addTodo);

// Optional: Throttled console log (example usage)
window.addEventListener('scroll', throttle(() => {
  console.log('Scroll event throttled');
}, 1000));

// Optional: Debounced log when typing
input.addEventListener('input', debounce(() => {
  console.log('User stopped typing');
}, 800));

// Example usage of groupBy (not required in main app)
const sampleData = [
  { name: 'Task A', category: 'Work' },
  { name: 'Task B', category: 'Home' },
  { name: 'Task C', category: 'Work' }
];
console.log('Grouped:', groupBy(sampleData, 'category'));

renderTodos();
