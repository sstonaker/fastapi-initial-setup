from setuptools import find_packages, setup

setup(
    name='fastapi-web-app',
    version='0.0.0',
    description="Initial setup for a FastAPI web application.",
    packages=find_packages(),
    install_requires=[
        'sqlalchemy==2.0.*',
        'fastapi==0.103.*',
        'uvicorn==0.23.*',
        'jinja2==3.1.*'
    ]
)