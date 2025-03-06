from flask import Flask, render_template, jsonify, request
from models.queue_mang import queue

app = Flask(__name__)
my_queue = queue() #instanciamos la clase

@app.route("/")
def home():
    queue_data = my_queue.showQueue()
    waitlist_length = my_queue.waitlistLength()
    waitlist_data = my_queue.getWaitlist()
    return render_template("index.html", queue=queue_data, waitlistLength=waitlist_length, waitlist=waitlist_data)

@app.route("/queue", methods=["GET"])
def get_queue():
    return jsonify({
        "queue": my_queue.showQueue(),
        "waitlist": my_queue.waitlistLength()
    })

@app.route("/join", methods=["POST"])
def join_queue():
    user = request.json.get("user")
    message = my_queue.enqueue(user)
    return jsonify({"message": message})

@app.route("/remove", methods=["POST"])
def remove_from_queue():
    removed = my_queue.dequeue()
    return jsonify({"removed": removed})

@app.route("/peek", methods=["GET"])
def peek_queue():
    next_in_queue = my_queue.peek()
    return jsonify({"next": next_in_queue})

if __name__ == "__main__":        
    app.run(debug=True)