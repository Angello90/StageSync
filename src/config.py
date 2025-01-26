import os


nodes = {}
PORT = os.getenv("PORT", 5000)

planning = [
    {
        "id": 1,
        "nom": "Nirvana",
        "duree": 3600  
    },
    {
        "id": 2,
        "nom": "Metallica",
        "duree": 3600
    },
    {
        "id": 3,
        "nom": "ACDC",
        "duree": 3600
    },
    {
        "id": 4,
        "nom": "Iron Maiden",
        "duree": 3600
    },
    {
        "id": 5,
        "nom": "Led Zeppelin",
        "duree": 3600
    },
    {
        "id": 6,
        "nom": "Queen",
        "duree": 3600
    },
    {
        "id": 7,
        "nom": "Pink Floyd",
        "duree": 3600
    },
    {
        "id": 8,
        "nom": "The Rolling Stones",
        "duree": 3600
    },
    {
        "id": 9,
        "nom": "The Beatles",
        "duree": 3600
    },
    {
        "id": 10,
        "nom": "The Doors",
        "duree": 3600
    },
    {
        "id": 11,
        "nom": "The Who",
        "duree": 3600
    },
    {
        "id": 12,
        "nom": "The Eagles",
        "duree": 3600
    }
];


template_return_noeud = [
    {
        "nom du groupe": "",
        "temps_restant":{
            "hours": 0,
            "minutes": 0,
            "seconds": 0
        },
        "duree": 3600
    }
]
