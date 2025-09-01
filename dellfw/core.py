import json, os, logging, pathlib, time

LOG_DIR = os.path.join(pathlib.Path.home(), ".dellfw")
LOG_FILE = os.path.join(LOG_DIR, "dellfw.log")

def ensure_logs_dir():
    os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("dellfw")
