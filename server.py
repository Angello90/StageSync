from src import create_app
from src.config import PORT
import os

app, socketio = create_app()

if __name__ == "__main__":
    # app.run(port=PORT, debug=True)
    socketio.run(app, port=PORT, debug=True)