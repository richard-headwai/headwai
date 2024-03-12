from setuptools import setup, find_packages

# Ensure 'README.md' is in the same directory as 'setup.py'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='headwai',
    version='0.1.1',
    author='Richard',
    author_email='richard.deetlefs@headwai.org',
    description='A package for evaluating text correctness.',
    long_description=long_description,  
    long_description_content_type='text/markdown',
    url='https://github.com/richard-headwai/headwai',  
    packages=find_packages(),
    install_requires=[
        'websockets',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.10',
)
