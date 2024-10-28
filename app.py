from flask import Flask, render_template, request, session
# from gptutils import get_response
import os
from dotenv import load_dotenv
from flask_session import Session
from gptutils import get_response

load_dotenv()

app = Flask(__name__, static_folder='static')
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/home')
def home():
    chat_history = session.get('chat_history', [])
    return render_template('home.html', name="you", chat_history=chat_history)

@app.route("/callmeskibidi", methods=["GET", "POST"])
def better_call_gpt():
    userText = request.args.get('msg')
    return str(get_response(userText))

if __name__ == '__main__':
    app.run(debug=True, threaded=True) 
