from flask import Flask, render_template, request, redirect

app = Flask(__name__)

next_id = 3

tasks = {
	1 : {
		"id": 1,
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"is_urgent": False
	},
	2 : {
		"id": 2,
		"name": "get milk",
		"description": "in a carton",
		"is_urgent": True
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
    		"is_urgent": "is_urgent" in request.form
        }
        
        tasks[next_id] = new_item
        next_id += 1
        return redirect("/")
    else:
        return render_template("todo_form.html")
    

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)