from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
BRAIN = "n30k1ra_global_brain.json"

@app.route('/')
def home():
    return "<h1>HiveScan-AI CLOUD BRAIN v12 — ACTIVE</h1>"

def deep_merge(dict1, dict2):
    """Recursive merge of two dictionaries."""
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            deep_merge(dict1[key], value)
        elif key in dict1 and isinstance(dict1[key], int) and isinstance(value, int):
            dict1[key] += value  # Add counts together
        elif key in dict1 and isinstance(dict1[key], list) and isinstance(value, list):
             # unique list items
             dict1[key] = list(set(dict1[key] + value))
        else:
            dict1[key] = value

@app.route('/sync', methods=['POST'])
def sync():
    new_data = request.json
    
    # Load existing brain
    existing_brain = {}
    if os.path.exists(BRAIN):
        try:
            with open(BRAIN, "r") as f:
                existing_brain = json.load(f)
        except:
            existing_brain = {}

    # Merge new intelligence
    deep_merge(existing_brain, new_data)
    
    # Save updated collective mind
    with open(BRAIN, "w") as f:
        json.dump(existing_brain, f)
        
    return jsonify({"status": "integrated", "total_knowledge": len(existing_brain.get("history", []))})

@app.route('/status')
def status():
    if os.path.exists(BRAIN):
        with open(BRAIN) as f:
            return jsonify(json.load(f))
    return jsonify({"status": "waiting for first sync"})

print("HiveScan-AI CLOUD BRAIN v12 RUNNING → http://0.0.0.0:9999")
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9999))
    app.run(host="0.0.0.0", port=port)
