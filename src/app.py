from flask import Flask, render_template, jsonify, request
from models.queue_mang import QueueManager

app = Flask(__name__)
queue_manager = QueueManager() #instanciamos la clase
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/queue", methods=["GET"])
def get_queue():
    return jsonify({
        "queue": queue_manager.get_queue(),
        "waitlist": queue_manager.get_waitlist()
    })

@app.route("/join", methods=["POST"])
def join_queue():
    user = request.json.get("user")
    message = queue_manager.add_user(user)
    return jsonify({"message": message})

@app.route("/remove", methods=["POST"])
def remove_from_queue():
    message = queue_manager.remove_user()
    return jsonify({"message": message})
if __name__ == "__main__":        
    app.run(debug=False)