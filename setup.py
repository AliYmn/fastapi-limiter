from setuptools import setup, find_packages

setup(
    name="fastapi-throttle",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
    ],
    description="A rate limiter for FastAPI without using Redis.",
    author="Ali Yaman",
    author_email="aliymn.db@gmail.com",
    url="https://github.com/AliYmn/fastapi-throttle",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8, <3.13",
)
