from app import app,socketio, emit,configItem 
from flask import render_template, request, jsonify

video_url = configItem['video_url']
delay = str(configItem['delay'])

@app.route("/")
def cinema():
    global video_url
    global delay
    return render_template("cinema.html", video_url=video_url, delay=delay)


@app.route("/change-video", methods=["POST"])
def changeVideo():
    try:
        global video_url
        video_url = request.form["video_url"]
        response = {"status": "success", "video_url": video_url}
        return jsonify(response)
    except:
        response = {"status": "error"}
        return jsonify(response)


@socketio.on("video_data")
def handle_video_data(data):
    global last_data
    last_data = data
    emit("update_video_data", data, broadcast=True, include_self=False)
