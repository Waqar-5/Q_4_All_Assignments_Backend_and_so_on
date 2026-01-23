import fs from 'fs';
import path from 'path';
import { NextRequest, NextResponse } from 'next/server';

const filePath = path.join(process.cwd(), 'data', 'todos.json');

// Define the type for a Todo
type Todo = {
  id: number;
  text: string;
};

// Ensure the todos.json file exists
function ensureFileExists() {
  if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, JSON.stringify([]));
  }
}

// Read todos from file
function readTodos(): Todo[] {
  ensureFileExists();
  const content = fs.readFileSync(filePath, 'utf-8');
  try {
    return JSON.parse(content) as Todo[];
  } catch {
    return [];
  }
}

// Write todos to file
function writeTodos(todos: Todo[]): void {
  fs.writeFileSync(filePath, JSON.stringify(todos, null, 2));
}

// GET all todos
export async function GET(req: NextRequest) {
  const todos = readTodos();
  return NextResponse.json(todos);
}

// POST create new todo
export async function POST(req: NextRequest) {
  const body = await req.json();
  const { todo } = body as { todo: string };

  const todos = readTodos();
  const newTodo: Todo = { id: Date.now() + Math.floor(Math.random() * 1000), text: todo };

  todos.push(newTodo);
  writeTodos(todos);

  return NextResponse.json(newTodo, { status: 201 });
}

// PUT update a todo
export async function PUT(req: NextRequest) {
  const body = await req.json();
  const { id, text } = body as { id: number; text: string };

  const todos = readTodos();
  const index = todos.findIndex((t) => t.id === id);

  if (index === -1) {
    return NextResponse.json({ error: 'Todo not found' }, { status: 404 });
  }

  todos[index].text = text;
  writeTodos(todos);

  return NextResponse.json(todos[index]);
}

// DELETE a todo
export async function DELETE(req: NextRequest) {
  const body = await req.json();
  const { id } = body as { id: number };

  let todos = readTodos();
  todos = todos.filter((t) => t.id !== id);
  writeTodos(todos);

  return NextResponse.json({ id });
}
