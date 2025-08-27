# FogMLaaS
## Fog Machine Learning as a Service

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

FogMLaaS is a cloud-native extension of **FogML**, providing TinyML model generation and deployment as a scalable, accessible service.

FogML enables TinyML applications on highly resource-constrained devices like ARM M0 microcontrollers through classic ML algorithms—such as density-based anomaly detection, Bayesian classifiers, decision forests, and multilayer perceptrons (MLPs). FogML provides **off-device learning for classification** and **on-device active learning for anomaly detection**, combined with time-series feature extraction and efficient code generation for embedded inferencing.

FogMLaaS builds upon these capabilities by offering:

- A REST API to generate device-optimized inferencing code, and manage deployments.
- Integrations with deployment targets such as Arduino, Zephyr, and ISPU microcontroller ecosystems.
- Streamlined workflows for IoT device management using standard API.

---

## 🐳 Running with Docker

FogMLaaS provides a Dockerized environment for easier setup and deployment.

### 1. Build the Docker Image

Clone the repository and build the image:

```bash
git clone https://github.com/tszydlo/FogMLaaS.git
cd FogMLaaS

# Build the image (tag as fogmlaas:latest)
docker build -t fogmlaas:latest .
```

### 2. Run the Container

Start the service locally:

```bash
docker run -d --name fogmlaas -p 8000:8000 fogmlaas:latest
```

By default, the API will be available at:

```
http://localhost:8000
```

### 3. Verify the Service

Check logs to confirm it’s running:

```bash
docker logs -f fogmlaas
```

### 4. Test the API vie web browser

```
http://127.0.0.1:8000/docs#
```

### 4. Interactive Mode (Optional)

If you want to open a shell inside the container:

```bash
docker exec -it --entrypoint bash fogmlaas
```

---
# ✅ Testing


Script `fogmlaas_test.py` provides a basic end-to-end test of the **FogMLaaS** service.


## Purpose
- Validates that the FogMLaaS server is running.
- Ensures version compatibility between client and server.
- Confirms that trained scikit-learn models can be serialized and converted by the service.

## Key Steps

1. **Model Training**
   - Loads the Iris dataset (`sklearn.datasets`).
   - Trains a `RandomForestClassifier` with 10 estimators.
   - Prints the training accuracy.

2. **Model Serialization**
   - Serializes the trained model using `pickle.dumps()`.

3. **Environment Check**
   - Sends a `GET /environment` request to the FogMLaaS service (`http://127.0.0.1:8000/environment`).
   - Compares the server’s `scikit-learn` version with the local one.

4. **Model Conversion**
   - Sends a `POST /convert/pickle` request with the serialized model.
   - Prints the JSON response returned by the service.

5. **Additional Notes**
   - Contains commented examples for testing with `curl`.
   - Provides hints for running and testing via Docker (`docker run`).


