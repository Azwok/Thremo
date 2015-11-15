import numpy as np
import unittest
import pycuda.driver as drv
import pycuda.compiler
import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import pycuda.cumath as cumath
from pycuda.compiler import SourceModule

__author__ = 'AlistairMcDougall'