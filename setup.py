from setuptools import setup, find_packages

setup(
    name='django_request_ahmb',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.8',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
    ],
)
