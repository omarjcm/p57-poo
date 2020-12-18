from setuptools import setup

setup(
    name='upsv',
    version='0.1',
    py_modules=['upsv'],
    install_requires=[
        'Click',        
    ],
    entry_points='''
        [console_scripts]
        upsv=upsv:cli
    ''',
)