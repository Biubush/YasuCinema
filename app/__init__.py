from flask import Flask
import configparser
from flask_socketio import SocketIO, emit

# 创建 Flask 应用实例
app = Flask(__name__,static_url_path='/static')
socketio = SocketIO(app)

# 从配置文件加载配置
config = configparser.ConfigParser()
config_path = './config.ini'  # 配置文件路径，根据实际情况进行调整
config.read(config_path, encoding='utf-8')
configItem = dict(config['app'])

# 设置 Flask 应用的调试模式
app.config['DEBUG'] = configItem['debug']
app.config['JSON_AS_ASCII'] = configItem['json_as_ascii']
app.config['SECRET_KEY'] = configItem['secret_key']
from app import views

# 如果是作为主应用运行，启动应用
if __name__ == '__main__':
    app.run(debug=True)
