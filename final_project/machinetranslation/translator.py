"""This file creates an IBM Watson Translation Service and implements english<->french
translation methods."""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def englishToFrench(englishText):
    """Takes in English text, converts to French and returns"""
    if englishText is None:
        return ''
    translation = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    # print(json.dumps(translation,indent=2,ensure_ascii=False))
    frenchText = translation['translations'][0]['translation']
    # print(frenchText)
    return frenchText

def frenchToEnglish(frenchText):
    """Takes in French text, converts to English and returns"""
    if frenchText is None:
        return ''
    translation = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    # print(json.dumps(translation,indent=2,ensure_ascii=False))
    englishText = translation['translations'][0]['translation']
    # print(englishText)
    return englishText


# englishToFrench("Hello world")
frenchToEnglish(None)
