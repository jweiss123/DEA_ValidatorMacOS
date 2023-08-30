#!/bin/bash

# Uninstall dependencies
echo "Uninstalling PyTorch..."
pip3 uninstall torch torchvision torchaudio

echo "Uninstalling EasyOCR..."
pip uninstall easyocr

echo "Uninstalling Pillow..."
pip uninstall Pillow

echo "Dependencies uninstalled successfully!"
