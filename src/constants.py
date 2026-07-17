from pathlib import Path

PROJECT_NAME = "StoreScope"
PROJECT_TAGLINE = "Sales Intelligence Platform"

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CLEAN_DATA_DIR = DATA_DIR / "cleaned"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"

OUTPUT_DIR = BASE_DIR / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"
REPORT_DIR = OUTPUT_DIR / "reports"
TABLE_DIR = OUTPUT_DIR / "tables"

DASHBOARD_DIR = BASE_DIR / "dashboard"
ASSET_DIR = DASHBOARD_DIR / "assets"

RAW_DATA_FILE = RAW_DATA_DIR / "Global_Superstore.csv"
FEATURE_DATA_FILE = CLEAN_DATA_DIR / "global_superstore_features.csv"

MODEL_FILE = MODEL_DIR / "best_model.pkl"

LOGO_FILE = ASSET_DIR / "logo.png"
FAVICON_FILE = ASSET_DIR / "favicon.png"

RANDOM_STATE = 42

MODEL_NAME = "Gradient Boosting Regressor"

MODEL_R2_SCORE = 0.6722

PRIMARY_COLOR = "#2563EB"
SUCCESS_COLOR = "#16A34A"
WARNING_COLOR = "#F59E0B"
DANGER_COLOR = "#DC2626"

CHART_HEIGHT = 450

PAGE_ICON = "📊"

PAGE_LAYOUT = "wide"

CURRENCY_SYMBOL = "$"

DATE_FORMAT = "%d-%m-%Y"

TOP_N = 10