# AliExpress Platform Integration Library
A standard set of libraries for integrating with the AliExpress platform.

Currently a work in progress.

## Features:
- Synchronize an item's information, including:
  - title,
  - images,
  - price,
  - description,
  - SKUs, (WIP)
    - Combinations (WIP)
    - Pricing (WIP)
    - Weight (WIP)
    - Quantity (WIP)
    - Thumbnails (WIP)
    - Thumbnails Linkage (WIP)
  - shipping estimations, (WIP)
  - etc.
- Make a purchase automatically.

## Setting up (Ubuntu 20.04):
```
# Setup Python 3.9
sudo apt install python3.9 python3-venv

# Setup Virtual Environment
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# Setup Chrome Driver
wget https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mkdir -p bin
mv chromedriver bin
rm chromedriver_linux64.zip
```

## Testing:
```
python3 -m unittest
```

## Terms:
- `item` - A single product, containing one or more SKUs
- `sku` - A single variant of a product
