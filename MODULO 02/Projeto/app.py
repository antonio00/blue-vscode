from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    nome_jogador = 'Antonio'
    premio = False
    return render_template(
        "index.html",
        nome_jogador = nome_jogador,
        premio = premio
    )

if __name__ =="__main__":
    app.run(debug=True)