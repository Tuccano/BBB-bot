import tweepy
import os, sys
from random import randint
import time

def xingar():
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

    pessoa_file.close()
    xingamento_file.close()

    pessoa_max = len(pessoa)
    xingamento_max = len(xingamento)              # define o número de itens das listas

    random_pessoa = randint(0, pessoa_max) - 1
    random_xingamento = randint(0, xingamento_max) - 1

    if random_pessoa == 0:
        texto = "Babu lindo s2"
        texto2 = ""
    else:
        texto = f'vsf {pessoa[random_pessoa]}'.strip('\n')
        texto2 = f' sua {xingamento[random_xingamento]}'.strip('\n')

    tweet = texto + texto2 + " #BBB20"

    print(tweet)           # texto do post
    api.update_status(tweet)   # post final

while True:
    xingar()
    
    sleep_time = 3    # cooldown (em horas)
    time.sleep(sleep_time * 3600)   # cooldown entre posts (em segundos)