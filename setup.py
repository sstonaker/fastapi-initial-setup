from setuptools import find_packages, setup

setup(
    name='wizard-bro-prompt-api',
    version='0.0.0',
    description="Generates a prompt for creating wizard bro AI images.",
    packages=find_packages(),
    install_requires=[
        'fastapi==0.103.*',
        'uvicorn==0.23.*'
    ]
)
