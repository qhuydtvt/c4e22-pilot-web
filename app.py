from flask import Flask, render_template, request
import mlab
from random import choice
from poll import Poll

app = Flask(__name__)
mlab.connect()

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/poll/<poll_code>")
def poll(poll_code):
  # 1. Get Poll
  # objects(yob__lte=1990)

  poll_list = Poll.objects(code=poll_code)
  poll = poll_list[0]

  # 2. Render
  return render_template("poll.html", p=poll_list[0])

@app.route("/polls")
def polls():
  #1 Read ALL polls
  poll_list = Poll.objects()

  #2. Render ALL polls
  return render_template("polls.html", polls=poll_list)

@app.route("/new_poll", methods=["GET", "POST"])
def new_poll():
  if request.method == "GET":
    return render_template("new_poll.html")
  elif request.method == "POST":
    # 1. Unpack data (form)
    form = request.form
    question = form['question']
    options = []
    for k,v in form.items():
      if k != "question":
        options.append(v)
    print(question)
    print(options)
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    code = ""
    for _ in range(6):
      code += choice(alphabet)
    
    p = Poll(question=question, options=options, code=code)
    p.save()
    return "Gotcha"

if __name__ == '__main__':
  app.run(debug=True)