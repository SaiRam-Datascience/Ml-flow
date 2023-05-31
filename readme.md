# mle-training-mlflow

## To run the file

We have to create an environment from conda.yaml file which is attached in this repository .

First we have to download that file and save it in working directory.

"conda env create -f mlflow_env.yaml" Type this command in the terminal .

Now we can see newly created environment by typing the command "conda env list" .

Activate the environment -- "conda activate mlflow-env"

Use below code to launch the ML-Flow server:- mlflow server --backend-store-uri mlruns/ --default-artifact-root mlruns/ --host 0.0.0.0 --port 5000

## To execute the script

$ conda env create -f mlflow_env.yml"

$ conda activate mlflow-env"

$ mlflow server --backend-store-uri mlruns/ --default-artifact-root mlruns/ --host 0.0.0.0 --port 5000
