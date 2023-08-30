#!/bin/bash

# Install dependencies
echo "Installing PyTorch..."
pip3 install torch torchvision torchaudio

echo "Installing EasyOCR..."
pip install easyocr

echo "Installing Pillow 9.5.0..."
pip uninstall Pillow
pip install Pillow==9.5.0

# Run Python script
echo "Running DEAValidator.py..."
python "$(dirname "$0")/DEAValidator.py"
