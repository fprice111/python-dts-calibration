# coding=utf-8
import ast
import inspect
from os.path import dirname
from os.path import join


# from . import plot as dtspltfuncs
# from . import datastore as dsfuncs

from .datastore import DataStore
from .datastore import open_datastore
from .datastore import open_mf_datastore
from .datastore import read_apsensing_files
from .datastore import read_sensornet_files
from .datastore import read_sensortran_files
from .datastore import read_silixa_files

from .datastore_utils import check_dims
from .datastore_utils import check_timestep_allclose
from .datastore_utils import get_netcdf_encoding
from .datastore_utils import merge_double_ended
from .datastore_utils import shift_double_ended
from .datastore_utils import suggest_cable_shift_double_ended

from .plot import plot_accuracy
from .plot import plot_location_residuals_double_ended
from .plot import plot_residuals_reference_sections
from .plot import plot_residuals_reference_sections_single
from .plot import plot_sigma_report

__version__ = '1.0.0'
__all__ = []

# datastore
__all__.extend(["DataStore", "open_datastore", "open_mf_datastore",
                "read_apsensing_files", "read_sensornet_files",
                "read_sensortran_files", "read_silixa_files"])

# datastore_utils
__all__.extend(['check_dims', 'check_timestep_allclose', 'get_netcdf_encoding',
                'merge_double_ended', 'shift_double_ended',
                'suggest_cable_shift_double_ended'])

# plot
__all__.extend(['plot_accuracy', 'plot_location_residuals_double_ended',
                'plot_residuals_reference_sections',
                'plot_residuals_reference_sections_single',
                'plot_sigma_report'])

# filenames = ['datastore.py', 'datastore_utils.py', 'calibrate_utils.py',
#              'plot.py', 'io.py']
# filenames = ['plot.py']
#
# for filename in filenames:
#     with open(join(dirname(__file__), filename)) as file:
#         node = ast.parse(file.read())
#
#     functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
#     classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
#     __all__.extend([i.name for i in functions])
#
# __all__.sort()
# print(__all__)
