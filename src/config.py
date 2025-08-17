import os

# DIRECTORIES
SRC_DIR = os.path.dirname(os.path.abspath(__file__))  # src directory
BASE_DIR = os.path.dirname(SRC_DIR)  # project root
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
ICONS_DIR  = os.path.join(RESOURCES_DIR, "icons")  # icons directory
# STYLES_DIR = os.path.join(SRC_DIR, "styles/")  # styles css directory
STYLES_DIR = os.path.join(BASE_DIR, "src", "styles")

# FONT
FONT_NAME = "Inter"
FONT_WEIGHT = "SemiBold"
FONT_SIZE = 20
FONT_TOTAL = f"{FONT_NAME} {FONT_WEIGHT} {FONT_SIZE}"