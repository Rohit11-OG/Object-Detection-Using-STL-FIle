# Object Detection Using STL File (ROS 2 Integration)

🎯 YOLOv8 Object Detection using STL files with synthetic + real training data.

A complete object detection system for robotic arm painting applications using YOLOv8 and Intel RealSense D435i camera. Designed for integration with Dobot Nova5 and ROS 2 Humble.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![ROS2](https://img.shields.io/badge/ROS2-Humble-green.svg)
![YOLO](https://img.shields.io/badge/YOLO-v8-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- 🎯 **Custom Object Detection** - Train YOLO models on synthetic + real images
- 📷 **RealSense D435i Integration** - RGB + Depth sensing with 3D positioning
- 🤖 **ROS 2 Ready** - Complete ROS 2 Humble package for robot integration
- 🔧 **Industrial Grade** - Auto-reconnect, graceful shutdown, centralized logging
- 🎨 **Designed for Painting** - Detect objects for robotic arm painting applications

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Rohit11-OG/Object-Detection-Using-STL-FIle.git
cd Object-Detection-Using-STL-FIle

# Install dependencies
pip install -r requirements.txt

# Run detection
python main.py detect --camera 0 --confidence 0.65
```

## Project Structure

```
Object-Detection-Using-STL-FIle/
├── main.py                 # CLI entry point
├── realtime_detector.py    # Real-time detection with RealSense
├── train_detector.py       # YOLO training pipeline
├── data_generator.py       # Synthetic data generation
├── real_image_labeler.py   # Tool to label real images
├── config.py               # Configuration settings
├── stl_detector_ros2/      # ROS 2 Humble package
│   ├── msg/                # Custom ROS messages
│   ├── launch/             # Launch files
│   └── config/             # ROS parameters
├── dataset/                # Training data
└── runs/                   # Trained models
```

## Usage

### Generate Synthetic Training Data
```bash
python main.py generate --stl your_object.stl --num-images 1000
```

### Train the Model
```bash
python main.py train --epochs 100
```

### Real-time Detection
```bash
python main.py detect --camera 0 --confidence 0.65
```

### Add Real Images for Better Detection
```bash
python real_image_labeler.py capture   # Capture images
python real_image_labeler.py label     # Label with bounding boxes
python real_image_labeler.py combine   # Add to training set
python train_detector.py --epochs 50   # Retrain
```

## Repo Notes

- Large files (datasets and model weights) are excluded by default via .gitignore.
- If you want to store weights in GitHub, use Git LFS and remove the ignore rule for `*.pt`.

## ROS 2 Integration

The project includes a complete ROS 2 Humble package for robot integration:

```bash
# Build the package
cd ~/ros2_ws/src
ln -s /path/to/stl_detector_ros2 .
cd ~/ros2_ws && colcon build --packages-select stl_detector_ros2

# Launch detection
ros2 launch stl_detector_ros2 detection.launch.py
```

### Published Topics
| Topic | Type | Description |
|-------|------|-------------|
| `/detections` | `DetectionArray` | All detected objects with 3D positions |
| `/best_detection` | `Detection` | Highest confidence detection |
| `/detection_image` | `Image` | Annotated visualization |

## Model Performance

| Metric | Value |
|--------|-------|
| mAP50 | 97.7% |
| mAP50-95 | 96.4% |
| Precision | 100% |
| Recall | 97.8% |

## Hardware Requirements

- **Camera**: Intel RealSense D435i (or compatible webcam)
- **GPU**: NVIDIA GPU with CUDA support (recommended)
- **Robot**: Dobot Nova5 (for painting integration)

## Dependencies

- Python 3.10+
- PyTorch 2.0+
- Ultralytics (YOLOv8)
- OpenCV
- pyrealsense2
- ROS 2 Humble (optional, for robot integration)

## License

MIT License - See [LICENSE](LICENSE) for details.

## Author

Created for robotic arm painting applications with Dobot Nova5.
