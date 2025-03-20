import os
import base64
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image
from io import BytesIO

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__)
socketio = SocketIO(app)

convo = None
messages = []

@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@socketio.on("query_image")
def handle_query_image(data):
    global convo, messages

    image_data = data.get("image")
    question = data.get("question")

    if not question:
        emit("response", {"answer": "Please enter a question."})
        return

    if image_data:
        if image_data.startswith("data:image"):
            image_data = image_data.split(",")[1]

        img_binary = base64.b64decode(image_data)
        img = PIL.Image.open(BytesIO(img_binary))

        convo = model.start_chat()
        response = convo.send_message([img, question])

    elif convo:
        response = convo.send_message(question)
    else:
        emit("response", {"answer": "No image provided."})
        return


    messages.append({"type": "bot", "text": response.text})


    emit("response", {"answer": response.text})

if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)
