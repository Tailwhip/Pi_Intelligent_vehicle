from distutils.core import setup, Extension
from Cython.Build import cythonize

extension = Extension(
    name="ultrasonic",
    libraries=['wiringPi'],
    sources=["ultrasonic.pyx", "../clib/ultrasonic.c", "../clib/clamp.c"]
)

setup(ext_modules=cythonize([extension])
)

extension = Extension(
    name="intensity",
    libraries=['wiringPi', 'pigpio'],
    sources=["intensity.pyx", "../clib/intensity.c"]
)

setup(ext_modules=cythonize([extension])
)

extension = Extension(
    name="acceleration",
    libraries=['wiringPi'],
    sources=["acceleration.pyx", "../clib/acceleration.c"]
)

setup(ext_modules=cythonize([extension])
)

extension = Extension(
    name="servo",
    libraries=['pigpio'],
    sources=["servo.pyx", "../clib/servo.c", "../clib/clamp.c"]
)

setup(ext_modules=cythonize([extension])
)

extension = Extension(
    name="led",
    libraries=['wiringPi'],
    sources=["led.pyx", "../clib/led.c"]
)

setup(ext_modules=cythonize([extension])
)