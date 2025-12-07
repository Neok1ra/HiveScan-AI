# HiveScan-AI v12 - The "God Mode" Scanner + Global Brain

**"The AI-Powered Nmap Killer"**

This tool is designed to be a distributed, self-learning network scanner. Every time anyone runs this tool, it sends scan data to a **Global Cloud Brain**. The AI learns which ports are most likely to be open, which vulnerabilities are successful, and shares that intelligence with **all** users instantly.

The more people use it, the smarter it gets.

## 🚀 Features
*   **God Mode Speed**: Uses `asyncio` to scan 10,000+ packets per second (Python-based).
*   **Hive Mind**: Automatically syncs results to the central AI server.
*   **Auto-Recon**: Brute-forces subdomains before scanning.
*   **Nuclei Integration**: Auto-triggers vulnerability scans on found services.

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/HiveScan-AI.git
cd HiveScan-AI
pip install -r requirements.txt
```

## ⚔️ Usage

**Standard Scan (Contributions to the Hive Mind):**
```bash
python3 n30k1ra_v9.py <TARGET_IP>
```

**Interactive Mode:**
```bash
python3 n30k1ra_v9.py
```

## 🧠 How the Brain Works
1.  **Scanner Node**: You run the script on your laptop/Termux.
2.  **Discovery**: It finds open ports (e.g., 80, 443, 8080).
3.  **Sync**: It sends this data to the `CLOUD_SYNC_URL`.
4.  **Learning**: The server aggregates stats. "Port 8080 is open on 45% of targets."
5.  **Optimization**: Next time *anyone* scans, the AI suggests checking Port 8080 *first*.

## ⚠️ Disclaimer
This tool is for educational purposes and authorized security testing only. You are responsible for your own actions.
