
# Quickstart for GUI Users

Get a complete microscopy application with zero code required.

## Installation

The easiest way to get started is with the pre-built GUI application:

```bash
# Install using pip
pip install pymmcore-gui

# Or using conda
conda install -c conda-forge pymmcore-gui
```

## Launch the Application

```bash
# Start the GUI
pymm
```

The application will open with a modern, dockable interface including:

- **Device Property Browser** - Control all hardware settings
- **Live View** - Real-time camera display
- **MDA Designer** - Multi-dimensional acquisition planning
- **Image Viewer** - Built-in viewer with analysis tools
- **Stage Control** - XY and Z positioning
- **Snap & Live Controls** - Quick image capture

## Hardware Configuration

1. **Load Your Configuration**
   - Go to `File → Load Configuration`
   - Select your Micro-Manager `.cfg` file
   - Or use `Tools → Hardware Configuration Wizard` to create one

2. **Test Your Setup**
   - Click "Live" to start camera streaming
   - Use the stage controls to move around
   - Adjust camera settings in the Device Property Browser

3. **Run Your First Acquisition**
   - Open the MDA Designer dock
   - Set up channels, positions, time points, and Z-stacks
   - Click "Run MDA" to start acquisition

## Next Steps

- **Hardware Configuration Guide** - Detailed device setup
- **MDA Planning Tutorial** - Design complex experiments
- **Image Analysis Workflows** - Built-in analysis tools
