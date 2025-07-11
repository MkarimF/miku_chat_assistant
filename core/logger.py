import logging
from core.config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("miku.log"),
        logging.StreamHandler()
    ]
)


