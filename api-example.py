import json

import requests

todos = requests.get("http://jsonplaceholder.typicode.com/todos").json()
users = requests.get("http://jsonplaceholder.typicode.com/users").json()

user_map = {user["id"]: user["name"] for user in users}

report = {}
for todo in todos:
    user_id = todo["userId"]
    if user_id not in report:
        report[user_id] = {"total": 0, "completed": 0}
    report[user_id]["total"] += 1
    if todo["completed"]:
        report[user_id]["completed"] += 1

for user_id, data in report.items():
    total_todos = data["total"]
    completed_todos = data["completed"]
    completion_percentage = (completed_todos / total_todos) * 100
    user_name = user_map[user_id]
    print(
        f"{user_name} has {total_todos} todos, {completed_todos} of which are completed giving them a completion percentage of {round(completion_percentage)}%"
    )
