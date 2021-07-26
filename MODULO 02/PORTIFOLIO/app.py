from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'antonio.testesdev@gmail.com',
    "MAIL_PASSWORD": 'mudar123'
}

app.config.update(mail_settings) #atualizar as configurações do app com o dicionário mail_settings
mail = Mail(app) # atribuir a class Mail o app atual.

# utiilizando classe para capturar as informações do form
class Contato:
   def __init__ (self, nome, email, mensagem):
      self.nome = nome
      self.email = email
      self.mensagem = mensagem

@app.route('/') # renderiza a pagina principal(rota)
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
      # Capiturando as informações do formulário com o request do Flask e criando o objeto formContato
      formContato = Contato(
         request.form['nome'],
         request.form['email'],
         request.form['mensagem']
      )

      # Criando o objeto msg, que é uma instancia da Class Message do Flask_Mail
      msg = Message(
         subject= 'Contato do seu Portfólio', #Assunto do email
         sender=app.config.get("MAIL_USERNAME"), # Quem vai enviar o email, pega o email configurado no app (mail_settings)
         recipients=[app.config.get("MAIL_USERNAME")], # Quem vai receber o email, mando pra mim mesmo, posso mandar pra mais de um email.
         # Corpo do email.
         body=f'''O {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
         
               {formContato.mensagem}''' 
         )
      mail.send(msg) #envio efetivo do objeto msg através do método send() que vem do Flask_Mail
    return render_template('send.html', formContato=formContato) # Renderiza a página de confirmação de envio.

if __name__ == '__main__':
   app.run(debug=True)
