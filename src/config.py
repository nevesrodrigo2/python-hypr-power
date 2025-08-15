import os

SRC_DIR = os.path.dirname(os.path.abspath(__file__))  # src directory
BASE_DIR = os.path.dirname(SRC_DIR)  # project root
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")


STYLES_DIR = os.path.join(SRC_DIR, "styles/styles.css")  # styles directory