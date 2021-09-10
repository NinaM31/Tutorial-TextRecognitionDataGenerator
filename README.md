## Introduction

This repo will be a simple tutorial on how to use [trdg](https://github.com/Belval/TextRecognitionDataGenerator) which then was used for training EasyOCR recognition model 👍 (Future tutorial). One issue I was facing is that the generated Arabic text was reversed 🙃. So In this tutorial I'll show you how to avoid this when using `GeneratorFromStrings` without changing anything within the original repo.

## Getting started

Clone the repo and create a virtual environment + install the requirements

#### Windows

You need python 3.8 for this. 3.9 caused some issue with Pillow

```
py -m virtualenv -p="path/to/python38/python.exe" ./venv
```

```
venv\Scripts\activate
```

```
pip install -r requirement.txt
```

## Data

The data that I'll be using is this [Arabic Name](https://www.kaggle.com/lailamohammed/arabic-names)
