from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('minesweeper.html')

@app.route('/AI_play', methods=["GET", "POST"])
def AI_play():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    board_reveal = data.get('board_reveal')
    board_unreveal = data.get('board_unreveal')
    is_first_move = data.get('is_first_move')
    

    if board_reveal is None or board_unreveal is None or is_first_move is None:
        return jsonify({"error": "Missing data"}), 400

    print(board_reveal)
    print('\n')
    print(board_unreveal)
    print('\n')
    print(is_first_move)
    if is_first_move:
        move = {
            'row': random.randint(0,9), 
            'col': random.randint(0,9)
            }
    return jsonify(move)
        

if __name__ == '__main__':
    app.run(debug=True)