import json
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

X, y = make_blobs(random_state=RANDOM_STATE)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_STATE)

model = LogisticRegression(random_state=RANDOM_STATE)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f'Model Accuracy on test set: {acc}')

model_file = "model/model.joblib"  

with open(model_file, 'wb') as f:  
    joblib.dump(model, f)

X_sample = X_train[np.random.randint(X_train.shape[0], size=5), :]

sample_file = "data/sample_input.json"

with open(sample_file, 'w') as f:
    json.dump(X_sample.tolist(), f)

print(y_pred)