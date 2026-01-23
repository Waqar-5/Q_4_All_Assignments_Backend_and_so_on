'use client';
import { useState, useEffect } from 'react';
import styles from './page.module.css';

interface Todo {
  id: string | number;
  text: string;
}

export default function Home() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [input, setInput] = useState('');
  const [editingId, setEditingId] = useState<string | number | null>(null);
  const [editingText, setEditingText] = useState('');

  // Fetch todos
  const fetchTodos = async () => {
    const res = await fetch('/api/todos');
    const data = await res.json();
    setTodos(data);
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  // Add new todo
  const addTodo = async () => {
    if (!input.trim()) return;
    const res = await fetch('/api/todos', {
      method: 'POST',
      body: JSON.stringify({ todo: input }),
    });
    const newTodo = await res.json();
    setTodos([...todos, newTodo]);
    setInput('');
  };

  // Delete todo
  const deleteTodo = async (id: string | number) => {
    await fetch('/api/todos', {
      method: 'DELETE',
      body: JSON.stringify({ id }),
    });
    setTodos(todos.filter((t) => t.id !== id));
  };

  // Start editing
  const startEdit = (todo: Todo) => {
    setEditingId(todo.id);
    setEditingText(todo.text);
  };

  // Save edit
  const saveEdit = async () => {
    if (!editingText.trim() || editingId === null) return;
    const res = await fetch('/api/todos', {
      method: 'PUT',
      body: JSON.stringify({ id: editingId, text: editingText }),
    });
    const updated = await res.json();
    setTodos(todos.map((t) => (t.id === editingId ? updated : t)));
    setEditingId(null);
    setEditingText('');
  };

  // Cancel edit
  const cancelEdit = () => {
    setEditingId(null);
    setEditingText('');
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>📝 Next.js Todo App</h1>

      <div className={styles.inputGroup}>
        <input
          className={styles.input}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter a new task..."
        />
        <button className={styles.addButton} onClick={addTodo}>
          Add Task
        </button>
      </div>

      <ul className={styles.todoList}>
        {todos.map((todo) => (
          <li key={todo.id} className={styles.todoItem}>
            {editingId === todo.id ? (
              <div className={styles.editGroup}>
                <input
                  className={styles.editInput}
                  value={editingText}
                  onChange={(e) => setEditingText(e.target.value)}
                  autoFocus
                />
                <div className={styles.editButtons}>
                  <button className={styles.saveButton} onClick={saveEdit}>
                    Save
                  </button>
                  <button className={styles.cancelButton} onClick={cancelEdit}>
                    Cancel
                  </button>
                </div>
              </div>
            ) : (
              <div className={styles.todoContent}>
                <span className={styles.todoText}>{todo.text}</span>
                <div className={styles.todoButtons}>
                  <button className={styles.editButton} onClick={() => startEdit(todo)}>
                    Edit
                  </button>
                  <button className={styles.deleteButton} onClick={() => deleteTodo(todo.id)}>
                    Delete
                  </button>
                </div>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
