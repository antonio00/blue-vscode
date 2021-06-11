from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    nome = 'Rango'
    idade = 21
    sextou =True
    imagem = "https://media4.giphy.com/media/l0i9g3tAFRx8Dad8bG/giphy.gif?cid=790b7611508d4c435c0c2e46b405c39412eb6a202b2bd01b&rid=giphy.gif&ct=g"
    img = "https://www.artecines.com.br/wp-content/uploads/2016/06/20160610_103344.gif"

    return render_template(
        "index.html",
        nome = nome,
        idade = idade,
        sextou = sextou,
        imagem = imagem,
        img = img
    )

if __name__ =="__main__":
    app.run(debug=True)