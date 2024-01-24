from flask import Flask, request, jsonify
import joblib
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

def load_model(filename):
    with open(filename, 'rb') as f:
        model = joblib.load(f)
    return model

model = load_model('model/model.joblib')

@app.route("/health_check", methods=["GET"])
def health_check():
    app.logger.info("Received health check request")
    resp = jsonify({"success": True})
    resp.status_code = 200
    return resp

@app.route('/score', methods=['POST'])
def score():
    """Return a machine learning prediction."""

    app.logger.info("Received score request")
    app.logger.info("Additional Log")
    data = request.get_json()

    app.logger.info("Generating prediction")
    prediction = model.predict(data).tolist()

    app.logger.info("Returning prediction")
    return jsonify(prediction)


if __name__ == '__main__':
    app.logger.info("Loading model")
    load_model('model/model.joblib')

    app.logger.info("Starting application")
    app.run(host='0.0.0.0', port=8080, debug=True)
