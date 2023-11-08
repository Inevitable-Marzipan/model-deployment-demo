from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

def load_model(filename):
    with open(filename, 'rb') as f:
        model = joblib.load(f)
    return model

model = load_model('model/model.joblib')

@app.route("/health_check", methods=["GET"])
def health_check():
    resp = jsonify({"success": True})
    resp.status_code = 200
    return resp

@app.route('/score', methods=['POST'])
def score():
    """Return a machine learning prediction."""
    data = request.get_json()
    prediction = model.predict(data).tolist()
    return jsonify(prediction)


if __name__ == '__main__':
    load_model('model/model.joblib')
    app.run(host='0.0.0.0', port=8080, debug=True)
