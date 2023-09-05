from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path="/static")

todos = []


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


# Create a new todo
@app.route("/todos/create", methods=["POST"])
def create_todo():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        new_todo = {"id": len(todos) + 1, "title": title, "description": description}
        todos.append(new_todo)
        return redirect(url_for("index"))


# Update an existing todo
@app.route("/todos/update/<int:todo_id>", methods=["GET", "POST"])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return "Todo not found", 404

    if request.method == "POST":
        todo["title"] = request.form["title"]
        todo["description"] = request.form["description"]
        return redirect(url_for("index"))

    return render_template("update_todo.html", todo=todo)


# Delete an existing todo
@app.route("/todos/delete/<int:todo_id>", methods=["GET"])
def delete_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return "Todo not found", 404

    todos.remove(todo)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
