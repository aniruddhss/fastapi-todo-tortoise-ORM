# fastapi-todo-tortoise-ORM
## Introduction
This is a simple Todo application built with FastAPI and Tortoise ORM. It allows users to create, read, update, and delete tasks.

## Features
- Create a new task
- Retrieve a list of tasks
- Update an existing task
- Delete a task

## Requirements
- Python 3.7+
- FastAPI
- Tortoise ORM
- SQLite3
- Uvicorn

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-todo-tortoise-ORM.git
    ```
2. Change to the project directory:
    ```bash
    cd fastapi-todo-tortoise-ORM
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the FastAPI server:
    ```bash
    python rootmain.py
    ```
2. The application will be running at `http://127.0.0.1:8080`. 

3. FastAPI automatically generates an interactive API documentation using Swagger UI. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.


## Project Structure
```
api/
    __init__.py
    models/
        __init__.py
        modeltodo.py
    routes/
        __init__.py
        todo.py
    schemas/
        __init__.py
        schematodo.py
app/
    main.py
requirements.txt
rootmain.py
todo.db
```

## License
This project is licensed under the MIT License.