# iss-docking-interface

There are two parts to this repository:
1. The website so that you can run it locally.
2. The python interface to the website

The latter requires a webdriver.

## Dependency justification

- Requires a chromedriver executable. Download the appropriate one from: https://chromedriver.chromium.org/downloads
- `selenium`: interact with the website

## Install 

### Clone the repository
```bash
git clone https://github.com/Speterius/iss-docking-interface.git
cd iss-docking-interface
```

### Set up the virtual environment (optional)
`python -m venv venv`

Activate with 
`venv\scripts\activate` or the Unix eqquivalent

### Install dependencies

`pip install -r requirements.txt`

## Run the simulator locally

Start the local server
```bash
cd spacex-iss-sim
python3 -m http.server 5555
```
Navigate to: [http://localhost:5555/iss-sim.spacex.com](http://localhost:5555/iss-sim.spacex.com)
