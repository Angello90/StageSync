from src import create_app
import os

PORT = os.getenv("PORT", 5000)

app = create_app()

if __name__ == "__main__":
    app.run(port=PORT, debug=True)