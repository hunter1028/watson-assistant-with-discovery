#-*- coding: utf-8 -*-
'''
src.api.textFromSpeech -- watson assistant with discovery

@author: 
@copyright:  
@version: 1.0

Created on 2019/06/26
'''

from flask import Response
from flask import Blueprint, request
from src import speechToTextUser, speechToTextPassword, speechToTextIAMKey, speechToTextUrl
from ibm_watson import SpeechToTextV1
 
url = Blueprint('speechTotext', __name__)

@url.route('/api/speech-to-text', methods=['POST'])
def getTextFromSpeech():
    tts_kwargs = {
            'username': speechToTextUser,
            'password': speechToTextPassword,
            'iam_apikey': speechToTextIAMKey,
            'url': speechToTextUrl
    }

    sttService = SpeechToTextV1(**tts_kwargs)

    response = sttService.recognize(
            audio=request.get_data(cache=False),
            content_type='audio/wav',
            model = 'ja-JP_BroadbandModel',
            timestamps=True,
            word_confidence=True).get_result()

    if len(response['results']):
    
        text_output = response['results'][0]['alternatives'][0]['transcript']
    
    else:
        text_output = '';
        
    return Response(response=text_output, mimetype='plain/text')