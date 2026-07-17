import pandas as pd

from config import RAW_DATA
from logger import logger


def load_data():

    logger.info("Loading dataset")

    df = pd.read_csv(RAW_DATA, encoding="latin1")

    logger.info(f"Dataset Loaded : {df.shape}")

    return df