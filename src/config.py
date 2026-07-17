from pathlib import Path


# ==========================
# PROJECT PATH
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent



# ==========================
# PROJECT INFO
# ==========================

PROJECT_NAME = "StoreScope"

PROJECT_TAGLINE = "Sales Intelligence Platform"



# ==========================
# DATA PATHS
# ==========================

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

CLEAN_DATA_DIR = DATA_DIR / "cleaned"

PROCESSED_DATA_DIR = DATA_DIR / "processed"



RAW_DATA_FILE = (
    RAW_DATA_DIR /
    "Global_Superstore.csv"
)


FEATURE_DATA_FILE = (
    CLEAN_DATA_DIR /
    "global_superstore_features.csv"
)



# ==========================
# MODEL PATHS
# ==========================

MODEL_DIR = BASE_DIR / "models"


MODEL_FILE = (
    MODEL_DIR /
    "best_model.pkl"
)



# ==========================
# OUTPUT PATHS
# ==========================

OUTPUT_DIR = BASE_DIR / "outputs"

FIGURE_DIR = OUTPUT_DIR / "figures"

REPORT_DIR = OUTPUT_DIR / "reports"

TABLE_DIR = OUTPUT_DIR / "tables"



# ==========================
# DASHBOARD
# ==========================

DASHBOARD_DIR = BASE_DIR / "dashboard"

ASSET_DIR = DASHBOARD_DIR / "assets"



LOGO_FILE = ASSET_DIR / "logo.png"

FAVICON_FILE = ASSET_DIR / "favicon.png"



# ==========================
# MODEL SETTINGS
# ==========================

RANDOM_STATE = 42


MODEL_NAME = "Gradient Boosting Regressor"


MODEL_R2_SCORE = 0.6722



# ==========================
# UI SETTINGS
# ==========================

PAGE_ICON = "📊"

PAGE_LAYOUT = "wide"


CURRENCY_SYMBOL = "$"


DATE_FORMAT = "%d-%m-%Y"


TOP_N = 10



# ==========================
# CREATE DIRECTORIES
# ==========================

for folder in [
    DATA_DIR,
    RAW_DATA_DIR,
    CLEAN_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODEL_DIR,
    OUTPUT_DIR,
    FIGURE_DIR,
    REPORT_DIR,
    TABLE_DIR,
    ASSET_DIR
]:
    folder.mkdir(
        parents=True,
        exist_ok=True
    )