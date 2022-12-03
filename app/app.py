from flask import Flask, render_template, request, redirect, url_for
from bd_connection import Database
from werkzeug.utils import secure_filename

from Send_Mail import SendMail

app = Flask(__name__)
app.secret_key = "MySecretKey"
db = Database()

@app.route("/")
def home():
    correos = db.ver_correos()
    return render_template("index.html", data = correos)


@app.route("/registrar_correo", methods = ["POST"])
def registro():
    if request.method == "POST":
        email = request.form["email-registrar"]
        nombre = request.form["nombre-registrar"]
        curso = request.form["curso-registrar"]
        db.registrar_correo(email, nombre, curso)
        return redirect(url_for("home"))


@app.route("/editar_correo/<string:id>", methods = ["POST"])
def editar_correo(id):
    if request.method == "POST":
        email = request.form["email-update"]
        nombre = request.form["nombre-update"]
        curso = request.form["curso-update"]
        db.actualizar_correo(id, email, nombre, curso)
        return redirect(url_for("home"))


@app.route("/eliminar/<string:id>")
def eliminar_correo(id):
    db.eliminar_correo(id)
    return redirect(url_for("home"))


mensaje = SendMail()

@app.route("/enviar_mensaje", methods = ["POST"])
def enviar_correo():
    if request.method == "POST":
        correo_remitente = request.form["correo_remitente"]
        password = request.form["password"]

        correo_destinatario = request.form["correo_destinatario"]
        asunto_mensaje = request.form["asunto"]
        contenido_mensaje = request.form["contenido_mensaje"]

        mensaje.definiendo_remitente(asunto_mensaje, correo_remitente, correo_destinatario)
        mensaje.contenido_correo(contenido_mensaje)
        mensaje.enviando_correo(correo_remitente, password)

        uploaded_files = request.files.getlist("arhivos_mail")

        for file in uploaded_files:
            print(file)

        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True)