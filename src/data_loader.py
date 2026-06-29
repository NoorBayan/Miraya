# ==============================================================================
# File: data_loader.py
# Description: Handles downloading, extracting, and loading JSON data.
# ==============================================================================

import urllib.request
import zipfile
import json
import glob
import os

def load_data_from_github(zip_url, extract_to="maraya_temp_data"):
    """
    يقوم بتحميل الملف المضغوط من الرابط، فك ضغطه، واستخراج الداتا من ملف JSON
    """
    zip_path = "temp_dataset.zip"
    
    print("📥 Downloading data...")
    urllib.request.urlretrieve(zip_url, zip_path)
    
    print("📦 Extracting data...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        
    json_files = glob.glob(f"{extract_to}/**/*.json", recursive=True)
    
    if not json_files:
        raise FileNotFoundError("❌ لم يتم العثور على ملف JSON في المجلد المضغوط.")
        
    data_file = json_files[0]
    print(f"⏳ Loading JSON from {data_file}...")
    
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    print(f"✅ Successfully loaded {len(data):,} records.")
    return data
