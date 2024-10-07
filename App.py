from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample chess board representation
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/board')
def get_board():
    return jsonify(board)

@app.route('/api/move', methods=['POST'])
def make_move():
    data = request.json
    # Here you would implement the logic to update the board based on the move
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
