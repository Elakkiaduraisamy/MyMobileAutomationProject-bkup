import yaml
import logging
from browserstack_sdk import run_on_browserstack
import os
import json
import threading

logging.basicConfig(level=logging.DEBUG)

# Load the YAML configuration file
with open("browserstack1.yml", "r") as file:
    CONFIG = yaml.safe_load(file)

logging.debug(f"Loaded CONFIG: {CONFIG}")

# Ensure the CONFIG is correctly structured before passing it to run_on_browserstack
if "capabilities" in CONFIG and isinstance(CONFIG["capabilities"], list):
    os.environ["BROWSERSTACK_CAPABILITIES"] = json.dumps(CONFIG["capabilities"][int(threading.current_thread()._name) % len(CONFIG["capabilities"])])

    # Pass the loaded CONFIG to run_on_browserstack
    run_on_browserstack(CONFIG)
else:
    logging.error("The configuration file is missing the 'capabilities' key or it is not a list.")
