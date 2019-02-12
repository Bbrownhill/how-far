from distutils.core import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def get_requirements():
    with open('requirements.txt', 'r') as file:
        requirements = file.read().split('\n')
    requirements.remove('')
    return requirements


setup(
    name='how_far',
    version='1.0.0',
    URL='https://github.com/sorcerermjolnir/how_far/',
    author='Robert Brownhill',
    author_email='rbrownhill@live.co.uk',
    license='gpl-3.0',
    license_file='LICENSE',
    description='Display realtime distances between planets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['src'],
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
                    'how_far=src.how_far:how_far',
        ]
    }
)
