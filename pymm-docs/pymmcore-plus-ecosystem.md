# The pymmcore-plus Ecosystem: A Comprehensive Guide

## Overview

The **pymmcore-plus ecosystem** is a collection of four tightly integrated
Python packages that together provide a complete, pure-Python solution for
controlling Micro-Manager hardware and building microscopy applications. This
ecosystem eliminates the need for Java while providing enhanced functionality,
modern Python APIs, and flexible GUI components.

The four core packages work together to create a layered architecture:

```text
┌──────────────────────────────────────────────────────────┐
│                    pymmcore-gui                          │
│         Complete GUI Application                         │
├──────────────────────────────────────────────────────────┤
│                  pymmcore-widgets                        │
│            Qt GUI Components & Widgets                   │
├──────────────────────────────────────────────────────────┤
│                   pymmcore-plus                          │
│         Enhanced Micro-Manager Core Interface            │
├──────────────────────────────────────────────────────────┤
│                   useq-schema                            │
│        Implementation-Agnostic Experiment Schema         │
└──────────────────────────────────────────────────────────┘
```

## Package Breakdown

### 1. useq-schema: The Foundation

**Purpose**: Implementation-agnostic schema for describing multi-dimensional
microscopy experiments.

**Key Components**:

- `MDAEvent`: Represents a single acquisition event with position, channel,
  exposure, etc.
- `MDASequence`: Declarative representation of a complete multi-dimensional
  experiment
- Serialization/deserialization support (JSON, YAML)
- Time/duration estimation utilities

**Core Features**:

```python
from useq import MDAEvent, MDASequence

# Single event
event = MDAEvent(
    channel="DAPI",
    exposure=100,
    x_pos=100.0,
    y_pos=100.0,
    z_pos=30.0
)

# Complete experiment sequence
sequence = MDASequence(
    time_plan={"interval": 2, "loops": 6},
    channels=[
        {"config": "DAPI", "exposure": 50},
        {"config": "FITC", "exposure": 80}
    ],
    z_plan={"range": 4.0, "step": 0.5}
)
```

**Design Philosophy**: Language-agnostic schema that can be adopted by any
microscopy control software, promoting interoperability between different
acquisition engines.

### 2. pymmcore-plus: The Enhanced Core

**Purpose**: Drop-in replacement for `pymmcore.CMMCore` with extensive
additional functionality.

**Key Features**:

#### Singleton Pattern

```python
from pymmcore_plus import CMMCorePlus

# Global singleton instance
mmc = CMMCorePlus.instance()
# All widgets automatically connect to this same instance,
# (if a different core is not explicitly provided).
```

#### Enhanced Event System

- Modern signal/slot architecture replacing traditional callbacks
- Type-safe event handling
- Rich event metadata

#### Multi-Dimensional Acquisition Engine

```python
# Execute useq-schema sequences directly
mmc.run_mda(sequence)

# Or run individual events
events = [MDAEvent(...), MDAEvent(...)]
mmc.mda.run(events)
```

##### Customizable MDA Engines

The acquisition engine in `pymmcore-plus` is fully customizable, allowing you to
extend or replace the default behavior for specialized needs:

```python
from pymmcore_plus.mda import MDAEngine

class CustomEngine(MDAEngine):
    def setup_sequence(self, sequence: MDASequence) -> SummaryMetaV1 | None:
        # Custom setup logic for the MDA sequence
        return super().setup_sequence(sequence)
        
    def setup_event(self, event: MDAEvent) -> None:
        # Custom hardware control logic
        super().setup_event(event)
    
    def exec_event(self, event: MDAEvent) -> Iterable[tuple[NDArray, MDAEvent, FrameMetaV1]]:
        # Custom acquisition logic
        return super().exec_event(event)

mmc.mda.set_engine(CustomEngine(mmc))
```

Use cases include driving hardware without Micro-Manager adapters,
implementing conditional acquisition logic, integrating high-performance
cameras, or handling custom MDAEvent metadata for specialized experiments.

#### Extended APIs

- Hardware discovery and characterization
- State management and configuration
- Convenience methods for common operations
- Better error handling and logging

**Core Architecture**:

```python
class CMMCorePlus(pymmcore.CMMCore):
    @classmethod
    def instance(cls) -> CMMCorePlus:
        """Global singleton access"""
        
    @property
    def events(self) -> PCoreSignaler:
        """Modern event system"""
        
    @property
    def mda(self) -> MDARunner:
        """Multi-dimensional acquisition engine"""
```

#### Comprehensive Metadata Schemas

Within `pymmcore-plus`, two key metadata schemas are defined.
These aren't intended to replace OME-XML (for example), but rather to
declare a clear schema for metadata that defines the system state
at any point during acquisition.

**Summary Metadata (SummaryMetaV1)**: Complete system snapshot emitted at MDA sequence start

- **System State**: Full device information, config groups, pixel size presets
- **Timestamp**: ISO 8601 formatted datetime with UTC offset
- **Device Registry**: All loaded devices with their properties and capabilities
- **Configuration**: Current config groups and pixel size configurations
- **Position**: Current 3D stage position
- **Sequence Info**: Optional MDA sequence definition and custom metadata

**Frame Metadata (FrameMetaV1)**: Lightweight per-frame acquisition metadata

- **Acquisition Details**: Exposure time, camera device, pixel size
- **Property Values**: Changed device properties for this frame
- **Timing**: Runner elapsed time since sequence start
- **Optional Data**: Stage position, MDA event, hardware trigger status
- **Camera Metadata**: Unstructured device-specific information
- **Buffer Info**: Remaining images in hardware-triggered sequences

Both schemas use TypedDict definitions for type safety and support optional fields with `NotRequired` for flexible metadata collection.

### 3. pymmcore-widgets: The GUI Components

**Purpose**: Collection of Qt widgets that connect to `CMMCorePlus` instances
for building microscopy UIs.

**Widget Categories**:

#### Device & Property Control

- `PropertyBrowser`: Comprehensive device property viewer/editor
- `PropertiesWidget`: Simple property control for specific devices
- `PropertyWidget`: Individual property control

#### Configuration Management

- `ConfigurationWidget`: System configuration management
- `GroupPresetTableWidget`: Configuration group presets
- `PixelConfigurationWidget`: Pixel size configuration

#### Multi-Dimensional Acquisition

- `MDAWidget`: Complete MDA experiment designer
- `ChannelTable`: Channel configuration
- `PositionTable`: Stage position management
- `TimePlanWidget`: Time series planning
- `ZPlanWidget`: Z-stack configuration
- `GridPlanWidget`: Multi-position grid setup

#### Camera & Live View

- `CameraRoiWidget`: Camera ROI control
- `ExposureWidget`: Exposure time control
- `ImagePreview`: Live image display
- `LiveButton`: Start/stop live mode

**Integration Pattern**:

```python
from pymmcore_widgets import PropertyBrowser, MDAWidget
from pymmcore_plus import CMMCorePlus

# Widgets automatically connect to singleton
mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

# All widgets share the same core instance
prop_browser = PropertyBrowser()  # Uses CMMCorePlus.instance()
mda_widget = MDAWidget()          # Uses CMMCorePlus.instance()
```

#### Core-Connected Variants

Many widgets have "core-connected" variants that integrate directly with
hardware:

- `CoreConnectedChannelTable`: Auto-populates from hardware configuration
- `CoreConnectedZPlanWidget`: Integrates with focus devices
- `CoreConnectedGridPlanWidget`: Works with stage coordinates
- `CoreConnectedPositionTable`: Hardware-aware position management

### 4. pymmcore-gui: The Complete Application

**Purpose**: Complete, ready-to-use GUI application combining all ecosystem
components.

**Architecture**:

```python
class MicroManagerGUI(QMainWindow):
    """Main application window with dockable interface"""
    
    def __init__(self, *, mmcore: CMMCorePlus | None = None):
        self._mmc = mmcore or CMMCorePlus.instance()
        self._viewers_manager = NDVViewersManager(self, self._mmc)
```

**Key Features**:

#### Dockable Interface

- Qt Advanced Docking System integration
- Flexible workspace organization
- Persistent layout saving/restoration

#### Integrated Viewer

- `ndv` ([n-dimensional viewer](https://github.com/pyapp-kit/ndv)) integration
- Real-time image display during acquisition
- Multi-dimensional data visualization, including 2D & 3D rendering

#### Comprehensive Widget Integration

All `pymmcore-widgets` components are available as dockable panels:

- Property Browser
- MDA Widget
- Camera ROI control
- Stage control
- Device installation wizard

#### Action System

Unified action management for:

- Core operations (snap, live, load config)
- Widget visibility toggling
- Application lifecycle management

## Integration Patterns & Data Flow

### 1. Singleton Core Pattern

All packages use the `CMMCorePlus.instance()` singleton pattern:

```python
# In pymmcore-widgets
class MDAWidget(MDASequenceWidget):
    def __init__(self, *, mmcore: CMMCorePlus | None = None):
        self._mmc = mmcore or CMMCorePlus.instance()

# In pymmcore-gui  
class MicroManagerGUI(QMainWindow):
    def __init__(self, *, mmcore: CMMCorePlus | None = None):
        self._mmc = mmcore or CMMCorePlus.instance()
```

### 2. Event-Driven Architecture

```python
# pymmcore-plus emits events
mmc = CMMCorePlus.instance()
mmc.events.systemConfigurationLoaded.connect(widget._on_config_loaded)
mmc.events.propertyChanged.connect(widget._on_property_changed)

# MDA events
mmc.mda.events.sequenceStarted.connect(viewer._on_sequence_started)
mmc.mda.events.frameReady.connect(viewer._on_frame_ready)
```

### 3. useq-schema Integration

```python
# Widgets produce useq-schema objects
mda_widget = MDAWidget()
sequence = mda_widget.value()  # Returns MDASequence

# Core executes useq-schema objects
mmc.run_mda(sequence)

# Events are useq.MDAEvent objects
def on_frame_ready(image: np.ndarray, event: MDAEvent, metadata: dict):
    print(f"Acquired {event.index} at position {event.x_pos}, {event.y_pos}")
```

### 4. Widget Composition Hierarchy

```text
MicroManagerGUI
├── PropertyBrowser (pymmcore-widgets)
├── MDAWidget (pymmcore-widgets)
│   ├── CoreConnectedChannelTable
│   ├── CoreConnectedZPlanWidget  
│   ├── CoreConnectedPositionTable
│   └── TimePlanWidget
├── ImagePreview (ndv integration)
└── Various Control Widgets
```

## Key Workflows

### 1. Basic Hardware Control

```python
from pymmcore_plus import CMMCorePlus
from pymmcore_widgets import PropertyBrowser
from qtpy.QtWidgets import QApplication

app = QApplication([])

# Create core and load configuration
mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

# Create and show property browser
browser = PropertyBrowser()  # Automatically connects to core
browser.show()

app.exec_()
```

### 2. Multi-Dimensional Acquisition

```python
from pymmcore_widgets import MDAWidget
from useq import MDASequence

# Create MDA widget
mda_widget = MDAWidget(include_run_button=True)

# Set up experiment
sequence = MDASequence(
    time_plan={"interval": 1, "loops": 10},
    channels=["DAPI", "FITC"],
    z_plan={"range": 5, "step": 0.5}
)
mda_widget.setValue(sequence)

# Run button automatically executes via CMMCorePlus.run_mda()
mda_widget.show()
```

### 3. Complete GUI Application

```python
from pymmcore_gui import create_mmgui

# Creates complete application with all features
app = create_mmgui()
app.run()
```

## Advanced Features

### Hardware Sequencing

```python
# pymmcore-plus supports hardware-timed sequences
mmc.startSequenceAcquisition(100, 10, True)  # 100 images, 10ms interval
```

### Custom MDA Engines

```python
from pymmcore_plus.mda import PMDAEngine

class CustomEngine:
    def setup_sequence(self, sequence: MDASequence) -> None:
        # Custom setup logic
        pass
        
    def exec_event(self, event: MDAEvent) -> Iterator[tuple]:
        # Custom acquisition logic
        yield (image_array, event, metadata)

mmc.mda.set_engine(CustomEngine())
```

### Plugin Architecture

```python
# Widgets can be easily extended
class CustomMDAWidget(MDAWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add custom controls
        self.custom_controls = MyCustomWidget()
        self.layout().addWidget(self.custom_controls)
```

## Benefits of the Integrated Ecosystem

### 1. **Consistency**

- Shared `CMMCorePlus` instance across all components
- Unified event system
- Common configuration and state management

### 2. **Modularity**

- Use individual widgets in custom applications
- Mix and match components as needed
- Clear separation of concerns

### 3. **Extensibility**

- Plugin-friendly architecture
- Custom widget development
- Configurable acquisition engines

### 4. **Performance**

- Direct C++ core access (no Java overhead)
- Efficient memory management
- Hardware-timed acquisitions

### 5. **Developer Experience**

- Type hints throughout
- Rich documentation
- Familiar Qt/Python patterns

## Getting Started

### Installation

```bash
pip install pymmcore-plus pymmcore-widgets pymmcore-gui useq-schema
```

### Basic Usage

```python
# Quick start with complete GUI
from pymmcore_gui import create_mmgui
app = create_mmgui()
app.run()
```

```python
# Or build custom applications
from pymmcore_plus import CMMCorePlus
from pymmcore_widgets import PropertyBrowser, MDAWidget

mmc = CMMCorePlus.instance()
mmc.loadSystemConfiguration()

# Use any combination of widgets
prop_browser = PropertyBrowser()
mda_widget = MDAWidget()
# ...
```

## Ecosystem Evolution

The pymmcore-plus ecosystem represents a significant evolution in microscopy
software architecture:

- **From Java to Python**: Pure Python implementation eliminates Java
  dependencies
- **From Callbacks to Signals**: Modern event-driven architecture
- **From Monolithic to Modular**: Composable widgets and clear separation of
  concerns  
- **From Vendor-Specific to Universal**: useq-schema promotes interoperability

This ecosystem provides a solid foundation for modern microscopy applications
while maintaining compatibility with the extensive Micro-Manager hardware
ecosystem.
