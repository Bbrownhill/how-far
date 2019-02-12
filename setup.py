from distutils.core import setup

setup(
    name='how_far',
    version='0.1.0',
    packages=['src'],
    install_requires=[
        'click==7.0',
        'astroquery==0.3.9',
        'astropy==3.1.1',
        'pyyaml==3.13',
    ],
    entry_points={
        'console_scripts': [
                    'how_far=src.how_far:how_far',
        ]
    }
)
