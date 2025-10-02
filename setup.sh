#!/bin/bash

# Exit script on error
set -e

echo "🚀 Setting up LinkedIn Video Downloader Project..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "⚠️ Python3 is not installed. Installing..."
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
else
    echo "✅ Python3 is already installed."
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists."
fi

# Activate virtual environment
echo "🔑 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install flask yt-dlp requests

# Create necessary folders
echo "📂 Creating project folders..."
mkdir -p downloads static templates

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔧 Creating .env file..."
    cat <<EOT >> .env
FLASK_APP=app.py
FLASK_ENV=development
DOWNLOAD_DIR=downloads
EOT
else
    echo "✅ .env file already exists."
fi

echo "✅ Setup complete! Run the app with: "
echo "-----------------------------------"
echo "source venv/bin/activate"
echo "python app.py"
echo "-----------------------------------"
