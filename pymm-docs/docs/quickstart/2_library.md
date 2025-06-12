
# Quickstart for Python Users

Supercharge your microscopy workflows with powerful Python APIs.

## Installation

Install the core library for programmatic control:

```bash
# Install the enhanced core
pip install pymmcore-plus

# Optional: Add useq for experiment design
pip install useq-schema
```

## Your First Script

```python
from pymmcore_plus import CMMCorePlus

# Get the enhanced core instance
mmc = CMMCorePlus.instance()

# Load your hardware configuration
mmc.loadSystemConfiguration('path/to/your/config.cfg')

# Take a snapshot
mmc.snapImage()
image = mmc.getImage()

print(f"Captured image: {image.shape}")
```

## Key Productivity Features

### 1. **Modern Event System**

React to hardware changes and acquisition events:

```python
# Connect to events
@mmc.events.imageSnapped.connect
def on_image_captured(image, metadata):
    print(f"New image: {image.shape}")
    # Process image immediately

@mmc.events.propertyChanged.connect  
def on_property_changed(device, prop, value):
    print(f"{device}.{prop} = {value}")
```

### 2. **Multi-Dimensional Acquisitions**

Use declarative experiment design:

```python
from useq import MDASequence

# Define a complex experiment
sequence = MDASequence(
    channels=["DAPI", "FITC", "TRITC"],
    time_plan={"interval": 300, "loops": 24},  # Every 5 min for 2 hours
    z_plan={"range": 10, "step": 0.5},         # 10μm Z-stack
    stage_positions=[(100, 200), (300, 400)]   # Multiple positions
)

# Run it
mmc.run_mda(sequence)
```

### 3. **Context Management**

Automatic state saving and restoration:

```python
# Safely change settings temporarily
with mmc:
    mmc.setExposure(100)  # Change exposure
    mmc.setProperty("Camera", "Gain", "High")
    # Take images with these settings
    images = [mmc.snapImage() for _ in range(10)]
# Settings automatically restored here
```

## Building Simple GUIs

Create custom interfaces with minimal code:

```python
import sys
from qtpy.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from pymmcore_plus import CMMCorePlus
from pymmcore_widgets import LiveButton, SnapButton, ExposureWidget

app = QApplication(sys.argv)
mmc = CMMCorePlus.instance()

# Create a simple control panel
widget = QWidget()
layout = QVBoxLayout(widget)

# Add pre-built widgets
layout.addWidget(ExposureWidget())
layout.addWidget(SnapButton())
layout.addWidget(LiveButton())

widget.show()
mmc.loadSystemConfiguration('demo_config.cfg')
app.exec()
```

## Integration Patterns

### With NumPy and SciPy

```python
import numpy as np
from scipy import ndimage

@mmc.events.imageSnapped.connect
def process_image(image, metadata):
    # Real-time analysis
    filtered = ndimage.gaussian_filter(image, sigma=1.0)
    mean_intensity = np.mean(filtered)
    print(f"Mean intensity: {mean_intensity}")
```

### With Napari

```python
import napari

viewer = napari.Viewer()

@mmc.events.frameReady.connect  
def display_frame(image, event, metadata):
    # Live display in napari
    viewer.layers["live"].data = image
```

## Next Steps

- **API Reference** - Complete pymmcore-plus documentation
- **Widget Gallery** - Pre-built GUI components
- **Integration Examples** - Real-world workflows
