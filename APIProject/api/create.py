from http.client import responses
import requests
import json
import os
from rest_framework.response import Response
import openai
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from dotenv import load_dotenv
from django.conf import settings

import os
# import environ

# env = environ.Env()
# environ.Env.read_env()


def configure():
    load_dotenv()


@api_view(('GET','POST'))
@renderer_classes(( JSONRenderer,))
def createImage(request): 
    if request.data['size']=="small":
        Size="256x256"
    elif request.data['size']=="medium":
        Size="512x512"
    else :
        Size="1024x1024"
    if request.method == 'POST':

      openai.api_key=settings.API_KEY
      resp = openai.Image.create(
      prompt=request.data['prompt'],
      n=request.data['number'],
      size=Size,
      response_format="b64_json"
      )
      users=resp["data"]
      print(request.data)
      data=users
      return  Response(data,status=status.HTTP_201_CREATED)
    
    pass