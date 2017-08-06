from distutils.core import setup

setup(name='StressCalc',
      version='1.0',
      install_requires=[
          'numpy==1.13.1',
          'pandas==0.20.3',
          'scipy==0.19.1',
      ],
      packages=['stress_calc_package'],
)
