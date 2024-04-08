from app import app,configItem,socketio
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=configItem['port'])