#!/bin/bash
# N30K1RA Deployment Script
# Deploys the full suite on a VPS

echo "[*] HiveScan-AI AUTO-DEPLOY PROTOCOL INITIATED"

# Check for root
if [ "$EUID" -ne 0 ]
  then echo "[-] Please run as root"
  exit
fi

echo "[*] Updating system packages..."
apt-get update -y && apt-get upgrade -y

echo "[*] Installing dependencies..."
apt-get install -y python3 python3-pip git screen

echo "[*] Installing Docker..."
curl -sSL https://get.docker.com | sh

echo "[*] Setting up Cloud Brain..."
# In a real scenario, this would clone the repo or copy files
# For now, we assume files are present or created

chmod +x n30k1ra_v9.py
chmod +x cloud_brain.py

echo "[*] Launching Cloud Brain in background..."
screen -dmS n30k1ra_brain python3 cloud_brain.py

echo "[+] Deployment Complete."
echo "    - Cloud Brain is active on port 9999"
echo "    - Scanner node ready for distribution"
