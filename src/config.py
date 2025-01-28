import os


nodes = {}
PORT = os.getenv("PORT", 5000)

planning = [
    {
        "id": 1,
        "nom": "Nirvana",
        "debut": "15:30",
        "fin": "16:30"  
    },
    {
        "id": 2,
        "nom": "Metallica",
        "debut": "16:30",
        "fin": "17:30"  
    },
    {
        "id": 3,
        "nom": "AC/DC",
        "debut": "17:30",
        "fin": "18:30"  
    },
    {
        "id": 4,
        "nom": "Iron Maiden",
        "debut": "18:30",
        "fin": "19:30"  
    },
    {
        "id": 5,
        "nom": "Led Zeppelin",
        "debut": "19:30",
        "fin": "20:30"  
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
