from setuptools import setup, find_packages

setup(
    name='headwai',
    version='0.1.0',
    author='richard',
    author_email='richard.deetlefs@headwai.org',
    description='A package for evaluating text correctness.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/headwai',
    packages=find_packages(),
    install_requires=[
        'asyncio',
        'websockets',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
