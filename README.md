# N30K1RA Final 2025

This repository contains the complete N30K1RA suite for network analysis and distributed scanning.

## Structure

*   `n30k1ra_v9.py`: **Desktop Scanner**. A python-based network scanner compatible with Windows, Linux, macOS, and Termux.
*   `n30k1ra_android.apk`: **Android Application**. A compiled APK for mobile deployment (Placeholder).
*   `cloud_brain.py`: **AI Brain Server**. The central command and control server that aggregates data from all nodes.
*   `deploy_full.sh`: **VPS Deployment**. Shell script to auto-deploy the environment on a Linux VPS.

## Usage

### 1. Cloud Brain (Server)
Deploy the brain on your VPS:
```bash
sudo ./deploy_full.sh
```
Or run manually:
```bash
python3 cloud_brain.py
```

### 2. Desktop/Termux Node
Run the scanner on any client machine:
```bash
python3 n30k1ra_v9.py --target <TARGET_IP> --ports 21,80,443
```

### 3. Android
Install the `.apk` on your Android device to join the swarm from mobile.

## Disclaimer
For educational and authorized testing purposes only.
