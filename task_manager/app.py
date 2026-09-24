from flask import Flask, render_template, request, redirect, url_for

from linked_list import TaskList

app = Flask(__name__)

task_list = TaskList()


@app.route("/", methods=["GET"])
def index():
    tasks = task_list.display_tasks()
    return render_template(
        "index.html",
        tasks=tasks,
        search_query="",
        search_active=False,
    )


@app.route("/add_task", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name", "").strip()

    if task_name:
        try:
            task_list.add_task(task_name)
        except ValueError:
            pass

    return redirect(url_for("index"))


@app.route("/complete_task", methods=["POST"])
def complete_task():
    task_name = request.form.get("task_name", "").strip()

    if task_name:
        task_list.complete_task(task_name)

    return redirect(url_for("index"))


@app.route("/delete_task", methods=["POST"])
def delete_task():
    task_name = request.form.get("task_name", "").strip()

    if task_name:
        task_list.delete_task(task_name)

    return redirect(url_for("index"))


@app.route("/search_task", methods=["POST"])
def search_task():
    search_query = request.form.get("search_task", "").strip()
    tasks = task_list.display_tasks()

    if search_query:
        filtered_tasks = []
        for task in tasks:
            if search_query.lower() in task["task_name"].lower():
                filtered_tasks.append(task)
        return render_template(
            "index.html",
            tasks=filtered_tasks,
            search_query=search_query,
            search_active=True,
        )

    return render_template(
        "index.html",
        tasks=tasks,
        search_query="",
        search_active=False,
    )


if __name__ == "__main__":
    app.run(debug=True)
