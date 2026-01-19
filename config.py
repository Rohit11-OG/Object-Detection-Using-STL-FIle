"""
Configuration file for STL Object Detection System
All adjustable parameters are defined here.
"""

import os
from pathlib import Path

# =====================================================
# PATH CONFIGURATIONS
# =====================================================

# Base directory
BASE_DIR = Path(__file__).parent.absolute()

# STL file path - UPDATE THIS TO YOUR STL FILE
STL_FILE = BASE_DIR / "your_object.stl"

# Dataset directories
DATASET_DIR = BASE_DIR / "dataset"
IMAGES_DIR = DATASET_DIR / "images"
LABELS_DIR = DATASET_DIR / "labels"
TRAIN_IMAGES_DIR = DATASET_DIR / "train" / "images"
TRAIN_LABELS_DIR = DATASET_DIR / "train" / "labels"
VAL_IMAGES_DIR = DATASET_DIR / "val" / "images"
VAL_LABELS_DIR = DATASET_DIR / "val" / "labels"

# Model output directory
MODEL_DIR = BASE_DIR / "runs" / "detect"
BEST_MODEL_PATH = MODEL_DIR / "stl_object" / "weights" / "best.pt"

# =====================================================
# RENDERING CONFIGURATIONS
# =====================================================

# Image size for rendering
RENDER_WIDTH = 640
RENDER_HEIGHT = 480

# Number of synthetic images to generate
NUM_SYNTHETIC_IMAGES = 1000

# Train/Val split ratio
TRAIN_VAL_SPLIT = 0.8  # 80% train, 20% val

# Camera distance range (from object center)
CAMERA_DISTANCE_MIN = 1.5
CAMERA_DISTANCE_MAX = 4.0

# Object scale variations
OBJECT_SCALE_MIN = 0.7
OBJECT_SCALE_MAX = 1.3

# Lighting configurations
AMBIENT_LIGHT_INTENSITY = 0.3
DIRECT_LIGHT_INTENSITY_MIN = 2.0
DIRECT_LIGHT_INTENSITY_MAX = 5.0

# Background types: 'solid', 'gradient', 'noise', 'texture'
BACKGROUND_TYPES = ['solid', 'gradient', 'noise']

# =====================================================
# AUGMENTATION CONFIGURATIONS
# =====================================================

# Enable/disable augmentations
ENABLE_BLUR = True
ENABLE_NOISE = True
ENABLE_BRIGHTNESS = True
ENABLE_CONTRAST = True

# Augmentation probabilities
BLUR_PROBABILITY = 0.3
NOISE_PROBABILITY = 0.3
BRIGHTNESS_PROBABILITY = 0.4
CONTRAST_PROBABILITY = 0.4

# Augmentation ranges
BLUR_KERNEL_SIZE = (3, 7)
NOISE_INTENSITY = (0, 25)
BRIGHTNESS_RANGE = (-30, 30)
CONTRAST_RANGE = (0.8, 1.2)

# =====================================================
# TRAINING CONFIGURATIONS
# =====================================================

# YOLO model to use: 'yolov8n', 'yolov8s', 'yolov8m', 'yolov8l', 'yolov8x'
YOLO_MODEL = "yolov8n.pt"  # nano for faster training, use 'yolov8s.pt' or 'yolov8m.pt' for better accuracy

# Training parameters
EPOCHS = 100
BATCH_SIZE = 16
IMAGE_SIZE = 640
PATIENCE = 20  # Early stopping patience

# Device: 'cpu', 'cuda', '0', '1', etc.
DEVICE = "0"  # Use GPU 0 if available, change to 'cpu' for CPU training

# Learning rate
LEARNING_RATE = 0.01

# Workers for data loading
NUM_WORKERS = 4

# =====================================================
# DETECTION CONFIGURATIONS
# =====================================================

# Detection confidence threshold
CONFIDENCE_THRESHOLD = 0.65

# IOU threshold for NMS
IOU_THRESHOLD = 0.45

# Maximum detections per image
MAX_DETECTIONS = 10

# =====================================================
# REALSENSE CAMERA CONFIGURATIONS
# =====================================================

# Camera ID (0 for default webcam, or specific RealSense serial)
CAMERA_ID = 0

# RealSense configurations
REALSENSE_WIDTH = 640
REALSENSE_HEIGHT = 480
REALSENSE_FPS = 30

# Enable depth stream
ENABLE_DEPTH = True

# Depth range (in meters)
DEPTH_MIN = 0.3
DEPTH_MAX = 10.0

# =====================================================
# OUTPUT CONFIGURATIONS
# =====================================================

# Save detection results
SAVE_DETECTIONS = True
DETECTION_OUTPUT_DIR = BASE_DIR / "detections"

# Show FPS on detection window
SHOW_FPS = True

# Show depth information
SHOW_DEPTH = True

# Proximity warning threshold (in meters) - object turns red when closer
PROXIMITY_THRESHOLD = 0.4  # 400mm

# =====================================================
# CLASS CONFIGURATIONS
# =====================================================

# Class name for the object (will be used in training)
CLASS_NAME = "custom_object"

# Number of classes
NUM_CLASSES = 1


def create_directories():
    """Create all necessary directories"""
    dirs = [
        DATASET_DIR, IMAGES_DIR, LABELS_DIR,
        TRAIN_IMAGES_DIR, TRAIN_LABELS_DIR,
        VAL_IMAGES_DIR, VAL_LABELS_DIR,
        MODEL_DIR, DETECTION_OUTPUT_DIR
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)


def get_dataset_yaml_content():
    """Generate dataset.yaml content for YOLO training"""
    return f"""
path: {DATASET_DIR}
train: train/images
val: val/images

nc: {NUM_CLASSES}
names: ['{CLASS_NAME}']
"""


if __name__ == "__main__":
    create_directories()
    print("Configuration loaded successfully!")
    print(f"Base directory: {BASE_DIR}")
    print(f"STL file path: {STL_FILE}")
    print(f"Dataset directory: {DATASET_DIR}")
