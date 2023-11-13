setup(
    name='dsshw',
    version='0.1.0',
    packages=find_packages(include=['dsshw', 'dsshw.*']),
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0,,
        'jupyter'
    ]
)
