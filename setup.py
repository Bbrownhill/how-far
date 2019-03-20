from distutils.core import setup
from m2r import parse_from_file
import os


readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
readme = parse_from_file(readme_file)


def get_requirements():
    with open('requirements.txt', 'r') as file:
        requirements = file.read().split('\n')
    requirements.remove('')
    return requirements


setup(
    name='how_far',
    version='1.0.2',
    URL='https://github.com/sorcerermjolnir/how_far/',
    author='Robert Brownhill',
    author_email='rbrownhill@live.co.uk',
    license='gpl-3.0',
    license_file='LICENSE',
    description='Display realtime distances between planets',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    packages=['src'],
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
                    'how_far=src.how_far:how_far',
        ]
    }
)
