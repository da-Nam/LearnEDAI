from flask import Flask, render_template, request
from gptutils import get_response

app = Flask(__name__, static_folder='static')

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template('home.html', name="you", interviews=[12,1], unfinished_interviews=1)

@app.route("/callmeskibidi", methods=["GET", "POST"])
def better_call_gpt():
    userText = request.args.get('msg')
    return str(get_response(userText))

if __name__ == '__main__':
    app.run(debug=True, threaded=True) 
