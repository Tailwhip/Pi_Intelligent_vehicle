from distutils.core import setup, Extension
from Cython.Build import cythonize

extension = Extension(
    name="ultrasonicWrp",
    libraries=['wiringPi'],
    sources=["ultrasonicWrp.pyx", "clib/ultrasonic.c", "clib/clamp.c"]
)

setup(ext_modules=cythonize([extension])
)