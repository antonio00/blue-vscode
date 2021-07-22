from flask import Flask, render_template, request, redirect
app = Flask(__name__)
tarefas = list()

@app.route('/')
def index():
    return render_template('index.html', titulo='Lista', tarefas=tarefas)

@app.route('/new', methods=['GET', 'POST'])
def new():
    item = request.form['item']
    tarefas.append(item)
    return redirect('/')

@app.route('/clear')
def clear():
    tarefas.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)