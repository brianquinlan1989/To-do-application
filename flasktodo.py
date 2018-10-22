from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

next_id = 3

tasks = {
	1 : {
		"id": 1,
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"is_urgent": False,
		"is_done": True,
	},
	2 : {
		"id": 2,
		"name": "get milk",
		"description": "in a carton",
		"is_urgent": True,
		"is_done": False,
	},
}



@app.route("/")
def show_index():
    return render_template("index.html", tasks=tasks.values())
    
@app.route("/add", methods=["GET", "POST"])
def show_form():
    global next_id
    if request.method =="POST":
        new_item = {
            "id": next_id,
    		"name": request.form["add_todo"],
    		"description": request.form["add_description"],
    		"is_urgent": "is_urgent" in request.form,
    		"done": "is_done" in request.form
        }
        
        tasks[next_id] = new_item
        next_id += 1
        return redirect("/")
    else:
        return render_template("todo_form.html")
        
        
@app.route("/edit/<int:id>", methods =["GET", "POST"])
def show_edit_form(id):
    if request.method == "POST":
        edited_item = {
            "id": id,
    		"name": request.form["add_todo"],
    		"description": request.form["add_description"],
    		"is_urgent": "is_urgent" in request.form,
    		"is_done": "is_done" in request.form
        }
        
        tasks[id] = edited_item
        return redirect("/")
    else:
        return render_template("edit_task_form.html", task=tasks[id])
    

    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)