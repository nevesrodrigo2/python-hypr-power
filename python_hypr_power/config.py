import os

APP_NAME="python_hypr_power"
# DIRECTORIES
ABS_PATH=os.path.abspath(__file__)
SRC_DIR = os.path.dirname(os.path.abspath(__file__)) 
BASE_DIR = os.path.dirname(SRC_DIR)                   
RESOURCES_DIR = os.path.join(SRC_DIR, "resources")   
ICONS_DIR = os.path.join(RESOURCES_DIR, "icons")     
STYLES_DIR = os.path.join(SRC_DIR, "styles")         

# FONT
FONT_NAME = "Monospace" 
FONT_WEIGHT = "SemiBold"
FONT_SIZE = 18
FONT_TOTAL = f"{FONT_NAME} {FONT_WEIGHT} {FONT_SIZE}"