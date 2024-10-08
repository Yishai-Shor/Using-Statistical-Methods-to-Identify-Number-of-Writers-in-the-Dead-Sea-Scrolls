from setuptools import setup, find_packages

setup(
    name="IdentifyWriters", 
    version="0.1.0", 
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "chardet",
        "scipy",
        "matplotlib",
        "seaborn",
        "python-docx",
        "altair",
    ],
    author="Yishai Shor & Dr. Barak Sober",  
    author_email="yishai.shor@gmail.com",  
    description="A versatile package for handling text documents and performing various statistical tests to identify the number of writers who contributed to the document",
    long_description=open('README.md', encoding='utf-8').read(),  # Added encoding
    long_description_content_type="text/markdown",
    url="https://github.com/Yishai-Shor/Using-Statistical-Methods-to-Identify-Number-of-Writers-in-the-Dead-Sea-Scrolls",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
