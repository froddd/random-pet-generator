
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

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
def hello_world():
    return {
        "image": "images/border-collie.jpeg",
        "imageAlt": "A picture of a Border Collie",
        "info": "Christian Gérard, the Border Coluilie"
    }


