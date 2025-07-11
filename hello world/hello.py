from fastapi import FastAPI
api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Go shopping'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'Study for exam'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': 'Meditate 20 minutes'},
]

# GET,PUT,POST,DELETE
@api.get('/')
def index():
    return {"message":"Hello World"}

@api.get('/todos/{todo_id}')
def get_todo(todo_id):
    for todo in all_todos:
        if todo['6']
