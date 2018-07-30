try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='coinflip',
    version=0.1,
    description='A coin flipping masterpiece',
    author='Xc1d30us Mercy',
    author_email='',
    url='https://github.com/Xc1d30us-Mercy/CoinFlip',
    packages=[
        'coinflip'
    ],
    package_dir={'CoinFlip': 'CoinFlip'},
    include_package_data=True,
    zip_safe=False,
    keywords='coin randomizer'
)
