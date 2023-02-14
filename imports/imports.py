import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import time
import pyperclip
import whisper


def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        temperature=0.75,)
    return response["choices"][0]["text"]


def copy_to_clipboard(txt):
    pyperclip.copy(txt)
