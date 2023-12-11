# Sample Machine Learning model deployment

## Overview

- Step 1: Train the model on a dataset that is representative of your application's data.
- Step 2: Export the Model: Save the trained model in a format that can be easily loaded by your application (e.g., pickle, joblib, TensorFlow SavedModel, ONNX).
- Step 3: Load the Model into the Application. Optionally, deploy the model as an API using frameworks like Flask or FastAPI.

## Step 1 and 2: Train and export the model

```
py.exe .\train_model.py
```

## Step 3: Load the model by deploying it as an API

```
py.exe .\api.py
```

Sample invocations:

**curl**

```
curl --location --request POST 'http://127.0.0.1:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "features": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}'
```

**Powershell**

```
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Content-Type", "application/json")

$body = "{
`n    `"features`": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
`n}"

$response = Invoke-RestMethod 'http://127.0.0.1:5000/predict' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

