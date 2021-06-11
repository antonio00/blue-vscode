from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    nome = 'Rango'
    hp = 1200
    exibir_imagem =True
    imagem = "https://images.gr-assets.com/hostedimages/1465981934ra/19423258.gif"

    return render_template(
        "index.html",
        nome = nome,
        hp = hp,
        exibir_imagem = exibir_imagem,
        imagem = imagem
    )

if __name__ =="__main__":
    app.run(debug=True)