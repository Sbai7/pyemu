"""pyEMU: python modules for Environmental Model Uncertainty analyses.  These
modules are designed to work directly and seamlessly with PEST and PEST++ model
independent interface.  pyEMU can also be used to setup this interface.

Several forms of uncertainty analyses are support including FOSM-based
analyses (pyemu.Schur and pyemu.ErrVar), Monte Carlo (including
GLUE and null-space Monte Carlo) and a prototype iterative Ensemble Smoother

"""

from .ensemble_method import *
from .smoother import *
from .moouu import *

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
