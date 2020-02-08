#-*- coding: utf-8 -*-
'''
welcome -- watson assistant with discovery

@author: 
@copyright:  
@version: 1.0

Created on 2019/06/26
'''
# ======= APP ======= 
from src import app
from flask_cors import CORS
CORS(app)

# ======= login ======= 
from src import login_manager
login_manager.init_app(app=app)
from src.view import login
app.register_blueprint(login.url)

# ======= API ======= 
from src.api import conversation, speechFromText, textFromSpeech, discoveryChart, downloadFile
app.register_blueprint(conversation.url)
app.register_blueprint(speechFromText.url)
app.register_blueprint(textFromSpeech.url)
app.register_blueprint(discoveryChart.url)
app.register_blueprint(downloadFile.url)

# ======= run ======= 
import os
from flask_socketio import SocketIO
socketio = SocketIO(app)
app.secret_key = os.urandom(24)
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=int(port), debug=True)
