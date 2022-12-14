import subprocess
from ml_stuff.models.train import run_full_pipeline

def run():
    run_full_pipeline()
    subprocess.Popen(["uvicorn",
                      "ml_stuff.models.inference:app", 
                      "--reload", 
                      "--host",
                      "0.0.0.0",
                      "--port",
                      "8001"])

if __name__ == "__main__":
    run()
