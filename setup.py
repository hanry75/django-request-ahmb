from setuptools import setup, find_packages

setup(
    name='django-request-ahmb',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2',  # Specify Django version requirements if necessary
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
    ],
)
