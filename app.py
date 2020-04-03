from flask import Flask, Response
import tweepy
import os, sys
from random import randint
from threading import Thread
import time


app = Flask(__name__)

isActive = True

def xingar():
    global isActive

    while isActive:
        consumer_key = ""
        consumer_secret = ""             # colocar os tokens etc
        access_token = ""
        access_token_secret = ""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)   # login


        pessoa_file = open("pessoas.txt", 'r')            
        xingamento_file = open("xingamentos.txt", 'r')     # abre o arquivo

        pessoa = pessoa_file.readlines()
        xingamento = xingamento_file.readlines()      # converte em lista

        pessoa_max = len(pessoa)
        xingamento_max = len(xingamento)              # define o número de itens das listas

        random_pessoa = randint(0, pessoa_max) - 1
        random_xingamento = randint(0, xingamento_max) - 1

        texto = ""
        texto2 = ""

        if random_pessoa == 0:
            texto = "babu lindo s2"
            texto2 = ""
        else:
            texto = f'vsf {pessoa[random_pessoa]}'
            texto2 = f' sua {xingamento[random_xingamento]}'

        # print(random_pessoa)
        # print(random_xingamento)
        # print(texto.strip('\n') + texto2)           # texto do post

        api.update_status(texto.strip('\n') + texto2)   # post final

        time.sleep(3600)

def manual_run():
    t = Thread(target=xingar)
    t.start()
    return "Xingando..."

@app.route('/start', methods=['GET'])
def start():
    global isActive
    isActive = True
    return Response(manual_run(), mimetype="text/html")

@app.route('/stop')
def stop():
    global isActive
    isActive = False
    return 'Stopped'