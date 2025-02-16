from flask import Flask, request, jsonify, render_template
import csv
import os

app = Flask(__name__)

CSV_FILE = "tasks.csv"

def load_tasks():
    tasks = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                tasks.append({"name": row[0], "completed": row[1] == "True"})
    return tasks

def save_tasks(tasks):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task["name"], task["completed"]])

@app.route("/")
def index():
    return render_template("index.html")  # This serves your HTML file

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks()
    data = request.json
    tasks.append({"name": data["name"], "completed": data["completed"]})
    save_tasks(tasks)
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks", methods=["PUT"])
def update_task():
    tasks = load_tasks()
    data = request.json
    tasks = [task for task in tasks if not (task["name"] == data["name"] and data["completed"])]
    save_tasks(tasks)
    return jsonify({"message": "Task updated and removed if completed"})

if __name__ == "__main__":
    app.run(debug=True)
