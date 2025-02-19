from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import json

import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

app = Flask(__name__)
CORS(app)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    return "I do not understand..."

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json['message']
    response = get_response(message)
    return jsonify({'response': response})

@app.route('/generate-workout', methods=['POST'])
def generate_workout():
    with open('workout.json', 'r') as file:
        workouts = json.load(file)

    data = request.json
    target_area = data.get('target_area')
    level = data.get('level')

    response = workouts.get(level, {}).get(target_area, [])
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
