#!/bin/bash

echo "🚀 Setting up LinkedIn Video Downloader..."

# Step 1: Create virtual environment
if [ ! -d "venv" ]; then
  echo "📦 Creating virtual environment..."
  python -m venv venv
fi

# Step 2: Activate virtual environment
echo "🔑 Activating virtual environment..."
source venv/Scripts/activate  # For Windows Git Bash
# For Linux/Mac use: source venv/bin/activate

# Step 3: Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Step 4: Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Step 5: Create necessary folders
echo "📂 Creating folders..."
mkdir -p downloads
mkdir -p static
mkdir -p templates

# Step 6: Reminder for environment variables
echo "⚙️ Creating .env file (if missing)..."
if [ ! -f ".env" ]; then
  cat <<EOT >> .env
# Flask settings
FLASK_ENV=development
PORT=5000

# App settings
DOWNLOAD_DIR=downloads
EOT
  echo "✅ .env file created with default values"
fi

echo "✅ Setup complete!"
echo "👉 To run your app: source venv/Scripts/activate && python app.py"
