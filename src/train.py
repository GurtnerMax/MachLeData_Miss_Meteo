from sklearn.dummy import DummyRegressor
from sklearn.metrics import root_mean_squared_error
from pathlib import Path
from utils.seed import set_seed
import yaml
import pickle 
import sys
import pandas as pd

def main() -> None:
    if len(sys.argv) != 3:
        print("Arguments error. Usage:\n")
        print("\tpython3 train.py <train_dataframe_file> <val_dataframe_file>\n")
        exit(1)

    # Load parameters
    train_params = yaml.safe_load(open("params.yaml"))["train"]
    seed = train_params["seed"]

    # Set seed for reproducibility
    set_seed(seed)

    # Load train and validation datasets
    train_df = pd.read_parquet(Path(sys.argv[1]))
    val_df = pd.read_parquet(Path(sys.argv[2]))

    train_features = train_df.drop(["reference_timestamp", "air_temperature"], axis=1)
    train_target = train_df['air_temperature']

    # Train model
    regressor = DummyRegressor(strategy="mean").fit(train_features, train_target)

    # Save the model using pickle
    model_folder = "model"
    Path(model_folder).mkdir(parents=True, exist_ok=True)
    
    model_path = f"{model_folder}/model.pkl"

    with open(model_path, "wb") as f:
        pickle.dump(regressor, f)

    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()