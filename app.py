from flask import Flask, render_template, request, redirect

# Create Flask app instance
app = Flask(__name__)

# In-memory list to hold tasks (for now, no DB)
tasks = []

# Route for home page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a task
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'done': False})
    return redirect('/')

# Route to mark task as complete
@app.route('/complete/<int:index>')
def complete(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
    return redirect('/')

# Run the app (IMPORTANT PART to run with python app.py)
if __name__ == "__main__":
    app.run(debug=True)
