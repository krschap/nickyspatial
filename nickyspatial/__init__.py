# nickyspatial/__init__.py

"""
NickySpatial: An open-source object-based image analysis library for remote sensing
=========================================================================

NickySpatial is a Python package for object-based image analysis,
providing functionality similar to commercial software like eCognition.

Key features:
- Multiresolution segmentation
- Object-based analysis
- Rule-based classification
- Statistics calculation
- Integration with geospatial data formats
"""

__version__ = "0.0.1"
__author__ = "Kshitij Raj Sharma"

# Import core components
from .core.layer import Layer, LayerManager
from .core.rules import Rule, RuleSet
from .core.segmentation import MultiResolutionSegmentation

# Import filters
from .filters.spatial import merge_small_segments, select_by_area, smooth_boundaries
from .filters.spectral import enhance_contrast, spectral_filter

# Import IO functions
from .io.raster import layer_to_raster, read_raster, write_raster
from .io.vector import layer_to_vector, read_vector, write_vector

# Import stats functions
from .stats.basic import attach_basic_stats, attach_class_distribution, attach_count
from .stats.spatial import (
    attach_area_stats,
    attach_neighbor_stats,
    attach_shape_metrics,
)
from .stats.spectral import attach_ndvi, attach_spectral_indices

# Import utility functions
from .utils.helpers import create_sample_data
from .viz.charts import plot_histogram, plot_statistics

# Import visualization functions
from .viz.maps import plot_classification, plot_comparison, plot_layer
