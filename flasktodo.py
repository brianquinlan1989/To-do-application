from flask import Flask, render_template

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

next_id += 1

@app.route("/")
def show_hi():
    return render_template("index.html", tasks=tasks.values())
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)