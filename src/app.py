from flask import Flask, render_template, jsonify, request
from models.queue_mang import queue

app = Flask(__name__)
my_queue = queue() #instanciamos la clase

@app.route("/")
def home(): #endpoint para mostrar la cola y la lista de espera
    queue_data = my_queue.showQueue()
    waitlist_length = my_queue.waitlistLength()
    return render_template("index.html", queue=queue_data, waitlistLength=waitlist_length)

@app.route("/queue", methods=["GET"])
def get_queue(): #endpoint para obtener la cola y la lista de espera
    return jsonify({
        "queue": my_queue.showQueue(),
        "waitlist": my_queue.waitlistLength()
    })

@app.route("/join", methods=["POST"])
def join_queue(): #endooint para agregar un usuario a la cola
    user = request.form.get("user") 
    message = my_queue.enqueue(user)
    return render_template("index.html", 
        queue=my_queue.showQueue(),
        waitlistLength=my_queue.waitlistLength())

@app.route("/remove", methods=["POST"])
def remove_from_queue(): #removemos el primer usuario de la cola
    removed = my_queue.dequeue()
    return render_template("index.html",
        queue=my_queue.showQueue(),
        waitlistLength=my_queue.waitlistLength())

@app.route("/peek", methods=["GET"])
def peek_queue(): #obtenemos el siguiente usuario en la cola
    next_in_queue = my_queue.peek()
    return jsonify({"next": next_in_queue})

if __name__ == "__main__":        
    app.run(debug=True)