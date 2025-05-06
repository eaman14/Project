from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Define the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'suit': s, 'value': v} for s in suits for v in values]

def draw_card():
return random.choice(deck)

def card_value(card):
order = {v: i for i, v in enumerate(values, start=2)}
return order[card['value']]

@app.route('/')
def index():
return render_template('index.html')

@app.route('/play')
def play():
player_card = draw_card()
computer_card = draw_card()

player_score = card_value(player_card)
computer_score = card_value(computer_card)

if player_score > computer_score:
result = "Player wins!"
elif player_score < computer_score:
result = "Computer wins!"
else:
result = "It's a tie!"

return jsonify({
'player_card': player_card,
'computer_card': computer_card,
'result': result
})

if __name__ == '__main__':
app.run(debug=True)
