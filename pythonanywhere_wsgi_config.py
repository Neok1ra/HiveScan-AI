
# +++++++++++ PYTHONANYWHERE WSGI CONFIGURATION +++++++++++
# COPY EVERYTHING BELOW THIS LINE AND PASTE IT INTO THE 
# WSGI CONFIGURATION FILE ON PYTHONANYWHERE.COM
# (Found under the "Web" tab -> "Code" section)

import sys
import os

# 1. Update this path to match where you uploaded cloud_brain.py
# If you uploaded it to the default folder, it is likely:
path = '/home/yourusername/mysite'  # <-- CHANGE 'yourusername'

if path not in sys.path:
    sys.path.append(path)

# 2. Import the Flask app
# This assumes your file is named 'cloud_brain.py'
from cloud_brain import app as application
