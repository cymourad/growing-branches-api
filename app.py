import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# import the blue print routes
from routes.lesson_routes import lesson_routes

app = Flask(__name__)
CORS(app)

# import the routes using blueprints
app.register_blueprint(lesson_routes)

# for imports to work correctly
if __name__ == "__main__":
    load_dotenv()
    if os.getenv("ENV") == "DEV":
        # running on localhost, use debug to recompile everytime you save
        app.run(debug=True)
    else:
        app.run(
            host=os.getenv("LISTEN", "0.0.0.0"),
            # port 8080 is for http, TODO in the future use https for the app store
            port=int(os.getenv("PORT", "8080"))
        )
