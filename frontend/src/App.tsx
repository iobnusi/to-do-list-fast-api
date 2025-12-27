import { useState, useEffect } from 'react';
import './App.css';
import type { Todo, TodoCreate } from './types/todo';
import { getTodos, createTodo, updateTodo, deleteTodo } from './services/api';

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      setLoading(true);
      const data = await getTodos();
      setTodos(data);
      setError('');
    } catch (err) {
      setError('Failed to load todos');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    try {
      const newTodo: TodoCreate = {
        title: title.trim(),
        description: description.trim() || undefined,
        completed: false,
      };
      await createTodo(newTodo);
      setTitle('');
      setDescription('');
      setError('');
      await fetchTodos();
    } catch (err) {
      setError('Failed to create todo');
    }
  };

  const handleToggleComplete = async (todo: Todo) => {
    try {
      await updateTodo(todo.id, { completed: !todo.completed });
      await fetchTodos();
    } catch (err) {
      setError('Failed to update todo');
    }
  };

  const handleDelete = async (id: string) => {
    try {
      await deleteTodo(id);
      await fetchTodos();
    } catch (err) {
      setError('Failed to delete todo');
    }
  };

  return (
    <div className="container">
      <h1>To-Do List</h1>

      {error && <div className="error">{error}</div>}

      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <input
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="input"
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            placeholder="Description (optional)"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="input"
          />
        </div>
        <button type="submit" className="btn">Add Todo</button>
      </form>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul className="todo-list">
          {todos.map((todo) => (
            <li key={todo.id} className="todo-item">
              <div className="todo-content">
                <input
                  type="checkbox"
                  checked={todo.completed}
                  onChange={() => handleToggleComplete(todo)}
                  className="checkbox"
                />
                <div className="todo-text">
                  <h3 className={todo.completed ? 'completed' : ''}>
                    {todo.title}
                  </h3>
                  {todo.description && <p>{todo.description}</p>}
                </div>
              </div>
              <button
                onClick={() => handleDelete(todo.id)}
                className="btn-delete"
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}

      {!loading && todos.length === 0 && (
        <p className="empty">No todos yet. Add one above!</p>
      )}
    </div>
  );
}

export default App;
