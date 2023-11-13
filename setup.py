import setuptools

setuptools.setup(
    include_package_data=True,
    name='math_quiz',
    version='0.0.1',
    description='Nikil99 python module',
    url='https://github.com/NikilPrasad/nikildsshw.git',
    author='NikilPrasad',
    author_email='contact@nikil99.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='nikil99 python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)


