# Bibliotecas de pré-processamento de dados de texto
import nltk

import json
import pickle
import numpy as np
import random

ignore_words = ['?', '!',',','.', "'s", "'m"]

# Biblioteca load_model
import tensorflow
from data_preprocessing import get_stem_words

model = tensorflow.keras.models.load_model('./chatbot_model.h5')

# Carregue os arquivos de dados
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))


def preprocess_user_input(user_input):
    return

def bot_class_prediction(user_input):
    return
#resposta para o usuario
def bot_response(user_input):

    return 

print("Oi, eu sou a Estela, como posso ajudar?")

while True:
    user_input = input("Digite sua mensagem aqui:")
    print("Entrada do Usuário: ", user_input)

    response = bot_response(user_input)
    print("Resposta do Robô: ", response)

