import os


nodes = {}
PORT = os.getenv("PORT", 5000)

planning = [
    {
        "id": 1,
        "nom du groupe": "",
        "durée": 3600   
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
        "durée": 3600
    }
]
