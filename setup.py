"""
Setup file for EduMentor package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="edumentor",
    version="0.1.0",
    author="Tethi Biswas",
    author_email="your-email@example.com",
    description="AI-powered educational assistant system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tethi04/EduMentor-Capstone-Project",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "black>=21.12b0",
            "flake8>=3.9.0",
        ],
        "full": [
            "matplotlib>=3.4.0",
            "seaborn>=0.11.0",
            "scikit-learn>=0.24.0",
            "requests>=2.26.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "edumentor=main:main",
        ],
    },
)
