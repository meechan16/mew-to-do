# Flask To-Do List

A lightweight and simple to-do list web application built using Flask, with tasks stored in a CSV file. This project is great for beginners learning Flask and working with file-based storage.

---

## Features

- ✅ Add tasks with a description  
- ✅ Mark tasks as complete  
- ✅ Delete tasks  
- ✅ Store tasks persistently in a CSV file  
- ✅ Minimal and clean UI  

---

## Getting Started

### Prerequisites
Make sure you have Python installed (version 3.x recommended). You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-todo.git
   cd flask-todo
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Flask application**
   ```bash
   python app.py
   ```
2. Open your browser and go to:  
   **http://127.0.0.1:5000/**

---

## Project Structure

```
flask-todo/
│── static/
│   ├── styles.css
│── templates/
│   ├── index.html
│── app.py
│── tasks.csv
│── requirements.txt
│── README.md
```

- `app.py` - Main Flask application logic
- `tasks.csv` - CSV file storing tasks
- `templates/` - HTML templates
- `static/` - CSS files for styling

---

## API Endpoints

| Method | Endpoint       | Description          |
|--------|--------------|----------------------|
| GET    | `/`          | View tasks          |
| POST   | `/add`       | Add a new task      |
| POST   | `/complete`  | Mark task complete  |
| POST   | `/delete`    | Delete a task       |

---

## Example CSV Format

```csv
id,task,completed
1,Buy groceries,False
2,Finish project,True
```

- `id` - Unique identifier for each task
- `task` - Task description
- `completed` - `True` if task is done, `False` otherwise

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing
Pull requests are welcome! If you find any issues or have suggestions, feel free to create an issue or contribute.

---

## Author
**Your Name**  
GitHub: [yourusername](https://github.com/yourusername)
