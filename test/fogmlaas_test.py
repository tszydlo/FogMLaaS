import pickle
import requests
import sklearn

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target

clf = RandomForestClassifier(n_estimators=10)

clf.fit(X, y)
print( 'accuracy: ',clf.score(X,y))

# Serialize the model
model_bytes = pickle.dumps(clf)

# Check scikit version
url = "http://127.0.0.1:8000/environment"
headers = {}
response = requests.get(url, headers=headers)
print("Server response:", response.json())

# Comparing scikit versions

if (response.json()["scikit-learn"] != sklearn.__version__):
    print("SCIKIT-LEARN VERSION IS DIFFERENT!")
else:
    print("SCIKIT-LEARN VERSION IS THE SAME!")

# Send model to server
url = "http://127.0.0.1:8000/convert/pickle"
headers = {"Content-Type": "application/octet-stream"}
response = requests.post(url, data=model_bytes, headers=headers)
print("Server response:", response.json())

# curl --data-binary "@fogmlaas_test.py" -H "Content-Type: application/octet-stream" -X POST http://127.0.0.1:8000/convert/pickle
# curl -X GET http://127.0.0.1:8000/environment -H "accept: application/json"

# Docker test
# docker run -it --entrypoint bash fogml

# Docker run
# docker run -p 8000:8000 fogml

