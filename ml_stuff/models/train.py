from joblib import dump
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from scipy.stats import randint
import pandas as pd

import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("Starting workflow")


def ingest_data():
    """WIP: Read data from sklearn dataset"""
    X, y = fetch_california_housing(return_X_y=True)
    src_data = {"X": X, "y": y}
    return src_data


def eda(src_data):
    """WIP: Grab summary stats from features"""
    src_df = pd.DataFrame(src_data["X"])
    logging.info(src_df.describe())
    return src_df.head()


def feat_eng(src_data):
    """WIP: Prepare train test split"""
    X_train, X_test, y_train, y_test = train_test_split(
        src_data["X"], src_data["y"], random_state=0
    )
    train_data = {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
    }
    logging.info(train_data["X_train"][:3])
    return train_data


def train_model(train_data):
    """WIP: Set Hyperparams and train searchCV estimator"""
    # define the parameter space that will be searched over
    param_distributions = {"n_estimators": randint(1, 5), "max_depth": randint(5, 10)}

    # now create a searchCV object and fit it to the data
    logging.info("Starting model training")
    search = RandomizedSearchCV(
        estimator=RandomForestRegressor(random_state=0),
        n_iter=5,
        param_distributions=param_distributions,
        random_state=0,
    )
    search.fit(train_data["X_train"], train_data["y_train"])
    logging.info("Model training complete")
    return search


def model_metrics(search, train_data):
    """WIP: Track model metrics"""
    model_data = {
        "Max Depth": search.best_params_["max_depth"],
        "n_estimators": search.best_params_["n_estimators"],
        "score": search.score(train_data["X_test"], train_data["y_test"]),
    }
    logging.info(model_data)
    return model_data

def save_model(search):
    """WIP: Save model to registry"""
    sample_rec = [[34,
                  13,
                  7,
                  1,
                  1,
                  752,
                  2.79,
                  39.02]]
    logging.info(search.predict(sample_rec)[0])
    dump(search, "ml_stuff/models/model_store/clf_v1.joblib")
    

def run_full_pipeline():
    my_data = ingest_data()
    eda(my_data)
    clean_data = feat_eng(my_data)
    my_model = train_model(clean_data)
    model_results = model_metrics(my_model, clean_data)
    save_model(my_model)
    return model_results


if __name__ == "__main__":
    run_full_pipeline()
