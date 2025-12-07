# 🐍 PYTHONANYWHERE DEPLOYMENT GUIDE

**Follow these 4 steps to get your Cloud Brain running:**

### 1. Upload Files
1. Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
2. Go to the **Files** tab.
3. Upload `cloud_brain.py` to your main directory (usually `/home/yourusername/`).

### 2. Create Web App
1. Go to the **Web** tab.
2. Click **Add a new web app**.
3. Choose **Flask** -> **Python 3.10** (or latest).
4. For "Path", just keep the default (`/home/yourusername/mysite/flask_app.py` is fine, we will change it).

### 3. Configure WSGI
1. On the **Web** tab, scroll down to the **Code** section.
2. Click the link next to **WSGI configuration file** (it looks like `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
3. **DELETE EVERYTHING** in that file.
4. **COPY & PASTE** the contents of the local file `pythonanywhere_wsgi_config.py` (which I just created for you) into that box.
5. **IMPORTANT**: loops for the line `path = '/home/yourusername/mysite'` and change `yourusername` to your actual PythonAnywhere username.
6. Click **Save**.

### 4. Activate
1. Go back to the **Web** tab.
2. Click the big green **Reload** button at the top.
3. Click the link to your site (e.g., `https://yourusername.pythonanywhere.com`).
4. You should see: **"N30K1R4 CLOUD BRAIN v9 — ACTIVE"**.

### 5. Connect the Scanner
1. Copy your new URL (e.g., `https://darklord.pythonanywhere.com`).
2. Open `n30k1ra_v9.py` on your computer.
3. Find the line:
   ```python
   CLOUD_SYNC_URL = "https://your-domain.com/brain"
   ```
4. Replace it with your new URL:
   ```python
   CLOUD_SYNC_URL = "https://darklord.pythonanywhere.com/sync"
   ```
   *(Note: add `/sync` to the end if using the content from v11 pro, or just the base URL if using v9. Check the code!)*
