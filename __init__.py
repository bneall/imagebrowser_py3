#
# IBView Init
#
# ------------------------------------------------------------------------------
# Subject to Licensing provided with this software

import os

from . import config
from . import utils

# Main Config Object
cfg = config.Config()

# Setup Constants
IB_CONVERTERMAP = utils.getConverterPlugins(cfg.converterPath)
IB_STYLESHEET = utils.getStyleSheet(cfg.resourcePath)
IB_FORMATS = ['png', 'jpg', 'jpeg', 'exr', 'tiff', 'tif']

# Force update configs converters
# to keep in step with converters available on disk.
cfg.set_converters(list(IB_CONVERTERMAP.keys()))