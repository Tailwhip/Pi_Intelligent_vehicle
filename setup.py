from distutils.core import setup, Extension
from Cython.Build import cythonize

extension = Extension(
    name="ultrasonicWrp",
    sources=["ultrasonicWrp.pyx", "clib/ultrasonic.c"]
)
setup(
    name="ultrasonic",
    ext_modules=cythonize([extension])
)