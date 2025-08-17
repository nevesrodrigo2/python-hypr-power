#!/bin/bash
# Hyprland power menu replacement

# Kill previous instance
if pgrep -x "python_hypr_power" > /dev/null; then
    pkill -x "python_hypr_power"
    exit 0
fi

# Ensure library path is correct
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

# Launch python_hypr_power
/usr/local/bin/python_hypr_power &
