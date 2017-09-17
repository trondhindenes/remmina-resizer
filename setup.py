from setuptools import setup

setup(
    name='remmina-resizer',
    version='0.0.5',
    packages=['remmina_resizer'],
    description='A simple package for auto-adjusting rdp session resolution in Remmina connection files',
    long_description="Remmina (http://www.remmina.org) is a great RDP tool, but it has some limitations regarding screen resolution, which this project attempts to solve. See the readme at https://github.com/trondhindenes/remmina-resizer/blob/master/README.md for full info",
    author='Trond Hindenes',
    author_email='trond@hindenes.com',
    url='https://github.com/trondhindenes/remmina-resizer',
    download_url='https://github.com/trondhindenes/remmina-resizer/archive/0.0.5.tar.gz',
    install_requires=[
        'screeninfo',
        'ruamel.yaml',
    ],
    entry_points={
        'console_scripts': ['remmina-resizer=remmina_resizer.cmd_line:entrypoint'],
    },
    zip_safe=True
)
