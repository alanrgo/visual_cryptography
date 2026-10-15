# Visual Cryptography

Python experiments for generating and combining black/white visual-cryptography image shares using OpenCV and NumPy.

## Overview

This repository implements a 2-share visual cryptography flow:

- convert an input image to binary (black/white),
- generate two randomized share images,
- recover the hidden content by stacking/summing both shares.

The project also includes helper scripts used for image amplification, intersections, overlap composition, and a batch "xmas card" workflow.

## Key Features

- Randomized 2-share cipher generation (`cipher.py`)
- Optional output resizing and pixel amplification
- Utilities for binary conversion and transparent-to-white preprocessing (`resources.py`)
- Batch workflow for generating per-person outputs and maps (`xmas.py`)

## Prerequisites

- Python 3
- `opencv-python`
- `numpy`

## Setup

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install opencv-python numpy
```

## Usage

### Generate visual-cryptography shares

```bash
python cipher.py -f path/to/input.png -p 1
```

Common options:

- `-s WIDTH HEIGHT` resize final output dimensions before ciphering
- `-t True` load input with alpha channel handling (transparent -> white)

Output is written under `ciphered/<input_name>/`:

- `<input_name>_cipher1.png`
- `<input_name>_cipher2.png`
- `<input_name>_summed.png` (reconstruction preview)

### Run the xmas batch workflow

`xmas.py` expects a `./people` directory with one folder per person containing images.

```bash
python xmas.py
```

It creates outputs in sibling `<person>_ciphered/` folders.

## Project Structure

- `cipher.py` - main share generation logic and CLI parser
- `resources.py` - image I/O, thresholding, resize, transparency helpers
- `amplify.py` - pixel amplification utility
- `intersection.py` - experimental intersection/share-combination logic
- `overlap.py` - image overlay helper logic
- `printfy.py` - binary-to-RGBA conversion helper
- `xmas.py` - batch script orchestrating multiple modules

## Testing

There is currently no automated test suite in this repository.

For a quick sanity check, run scripts directly with sample images (for example, `cipher.py` and `xmas.py`) and verify generated files in output folders.

## Contributing

No formal contributing guide is currently defined. Open an issue or pull request with a clear description of the change.

## License

No license file is currently present in this repository.
