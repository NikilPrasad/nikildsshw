import setuptools

setuptools.setup(
    include_package_data=True,
    name='NikilPrasad',
    version='0.0.1',
    description='limeguru python module',
    url='https://github.com/limegurutech/examples/tree/main/python/pip%20installable%20package',
    author='NikilPrasad',
    author_email='contact@NikilPrasad.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='NikilPrasad python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)


