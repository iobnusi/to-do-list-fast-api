import type { Todo, TodoCreate, TodoUpdate } from '../types/todo';

const API_BASE_URL = 'http://localhost:8000';

export async function getTodos(): Promise<Todo[]> {
  const response = await fetch(`${API_BASE_URL}/todos/`);
  if (!response.ok) {
    throw new Error('Failed to fetch todos');
  }
  return response.json();
}

export async function createTodo(data: TodoCreate): Promise<Todo> {
  const response = await fetch(`${API_BASE_URL}/todos/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error('Failed to create todo');
  }
  return response.json();
}

export async function updateTodo(id: string, data: TodoUpdate): Promise<Todo> {
  const response = await fetch(`${API_BASE_URL}/todos/update/${id}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error('Failed to update todo');
  }
  return response.json();
}

export async function deleteTodo(id: string): Promise<boolean> {
  const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error('Failed to delete todo');
  }
  return response.json();
}

