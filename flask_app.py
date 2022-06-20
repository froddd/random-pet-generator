
# A very simple Flask Hello World app for you to get started with...
import random
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
def random_pet():
    name1 = random.choice(names1)
    name2 = random.choice(names2)
    animal = random.choice(animals)

    return {
        "image": f"images/{animal.lower().replace(' ','-')}.jpeg",
        "imageAlt": f"A picture of a {animal}",
        "info": f"{name1} {name2} the {animal}"
    }


