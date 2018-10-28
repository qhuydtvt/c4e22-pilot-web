from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/new_poll")
def new_poll():
  return render_template("new_poll.html")

if __name__ == '__main__':
  app.run(debug=True)