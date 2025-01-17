'''
Translator
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# create an instance of IBM Watson language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function returns translating text from english to french
    """
    # write the code here
    french_text = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()

    # Print results
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    french_text=french_text["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """
    This function returns translating text from french to english
    """
    # write the code here
    english_text = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()

    # Print results
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    english_text=english_text["translations"][0]["translation"]
    return english_text
    