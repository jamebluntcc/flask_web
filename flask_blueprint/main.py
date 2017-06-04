#coding=utf-8
'''
flask中的blueprint可以根据不同的开发需求进行模块化的设计让应用层次化更加清晰
'''
from flask import Flask
import user

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(user.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)
