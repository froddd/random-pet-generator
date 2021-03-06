
# A very simple Flask Hello World app for you to get started with...
import random
from flask import Flask, json, render_template

app = Flask(__name__)
names1 = [
    "Maxime",
    "Vincent",
    "Lincka",
    "Marie-Annick",
    "Eléonore",
    "Christian",
    "Frédéric",
    "Julien",
    "Carole",
    "Sylvia"
]
names2 = [
    "Henri",
    "Joseph",
    "Anne",
    "Léone",
    "Yvette",
    "Gérard"

]
animals = [
    "Baby Goat",
    "Border Collie",
    "Boxer",
    "Golden Retriever",
    "Lion",
    "Maine Coon",
    "Savana",
    "Snake",
    "Sphynx",
    "Tiger"
]


@app.route('/')
def root():
    return render_template('index.html')


def get_data():
    name1 = random.choice(names1)
    name2 = random.choice(names2)
    animal = random.choice(animals)

    data = {
        "image": f"static/images/{animal.lower().replace(' ','-')}.jpeg",
        "imageAlt": f"A picture of a {animal}",
        "info": f"{name1} {name2} the {animal}"
    }

    return data


@app.route('/api')
def api():
    data = get_data()

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/one')
def one():
    return render_template('one.html')


@app.route('/two')
def two():
    return render_template('two.html')


@app.route('/three')
def three():
    data = get_data()

    return render_template('three.html', image=data['image'], imageAlt=data['imageAlt'], info=data['info'])
