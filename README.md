## Introduction

This repo will be a simple tutorial on how to use [trdg](https://github.com/Belval/TextRecognitionDataGenerator) which can be used for training EasyOCR recognition model 👍 (Future tutorial). One issue I was facing is that the generated Arabic text was reversed 🙃. So In this tutorial I'll show you how to avoid this when using `GeneratorFromStrings` without changing anything within the original repo.

## Getting started

Clone the repo and create a virtual environment + install the requirements

#### Windows

```
py -m virtualenv -p="path/to/python39/python.exe" ./venv
```

```
venv\Scripts\activate
```

```
pip install -r requirements.txt
```

## Data

The data that I'll be using is this [Arabic Name](https://www.kaggle.com/lailamohammed/arabic-names)
