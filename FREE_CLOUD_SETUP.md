# ☁️ FREE CLOUD BRAIN SETUP (FOREVER)

You can host the **N30K1R4 Brain** for **FREE** using **Render.com** or **Glitch**.

---

## 🚀 OPTION 1: The "Hacker" Way (Instant Local Cloud)
1. Install **Ngrok**: [https://ngrok.com/download](https://ngrok.com/download)
2. Run your local brain:
   ```bash
   python cloud_brain.py
   ```
3. In a new terminal, expose it:
   ```bash
   ngrok http 9999
   ```
4. Copy the `https://xxxx.ngrok-free.app` URL.
5. Paste it into `n30k1ra_v9.py` as `CLOUD_BRAIN`.

---

## 🌍 OPTION 2: The "Pro" Way (Render.com - 24/7)
1. Create a [GitHub Account](https://github.com/).
2. Drag and drop the `n30k1ra_final_2025` folder into a new Repository.
3. Sign up for [Render.com](https://render.com/) (It's free).
4. Click **New +** -> **Web Service**.
5. Connect your GitHub Repo.
6. Use these settings:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn cloud_brain:app`
7. Click **Deploy Web Service**.
8. Render will give you a URL like `https://n30k1ra-brain.onrender.com`.
9. Paste that URL into `n30k1ra_v9.py`.

---

## ⚡ OPTION 3: PythonAnywhere (Easiest)
1. Sign up at [PythonAnywhere.com](https://www.pythonanywhere.com/).
2. Go to **Files** -> Upload `cloud_brain.py`.
3. Go to **Web** -> **Add a new web app**.
4. Select **Flask** -> **Python 3.10**.
5. Edit the WSGI configuration file to import your app:
   ```python
   from cloud_brain import app as application
   ```
6. Hit **Reload**. Your brain is live!
