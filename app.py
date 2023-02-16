from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 6,
        "category": "Servants of Vampire",
        "word": "Zombie"
    },
    {
        "inputs": 7,
        "category": "Scariest Monster",
        "word": "Vampire"
    },
    {
        "inputs": 11,
        "category": "Monster of Dr. Victor Franky",
        "word": "Frankestein"
    },
    {
        "inputs": 3,
        "category": "Jojo God Villain",
        "word": "Dio"
    }
]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()