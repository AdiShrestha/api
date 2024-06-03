from flask import Flask, request, jsonify
import evaluate

app = Flask(__name__)

@app.route('/evaluate_text', methods=['POST'])
def evaluate_text():
    text = request.get_json()['text']
    is_offensive = evaluate.evaluate(text)
    return jsonify({'offensive': is_offensive})

if __name__ == '__main__':
    app.run(debug=True)