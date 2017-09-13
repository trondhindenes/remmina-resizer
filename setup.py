from setuptools import setup

setup(
    name='remmina-resizer',
    version='0.0.4',
    packages=['remmina_resizer'],
    description='A simple package for auto-adjusting screen resolutionsin Remmina connection files',
    author='Trond Hindenes',
    author_email='trond@hindenes.com',
    url='https://github.com/trondhindenes/remmina-resizer',
    download_url='https://github.com/trondhindenes/remmina-resizer/archive/0.0.4.tar.gz',
    install_requires=[
        'screeninfo',
        'ruamel.yaml',
    ],
    entry_points={
        'console_scripts': ['remmina-resizer=remmina_resizer.cmd_line:entrypoint'],
    },
    zip_safe=True
)
