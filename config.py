from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA = DATA_DIR / "raw" / "Global_Superstore2.csv"

CLEAN_DATA = DATA_DIR / "cleaned" / "global_superstore_clean.csv"

FEATURE_DATA = DATA_DIR / "cleaned" / "global_superstore_features.csv"

MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

PLOT_DIR = BASE_DIR / "outputs" / "plots"

REPORT_DIR = BASE_DIR / "outputs" / "reports"

PLOT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)