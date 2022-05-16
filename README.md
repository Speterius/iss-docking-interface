# iss-docking-interface

There are two parts to this repository:
1. The website to run it locally in folder: `iss-sim.spacex.com`
2. The python interface to the website is the python package `website_interface`

The latter requires a webdriver.

**A usage example is provided: `iss_docking_env.py` sets up an RL environment using the interface.**
**Currently, `main.py` uses the example RL environment.** 

## Dependency justification

- Requires a chromedriver executable. Download the appropriate one from: https://chromedriver.chromium.org/downloads
- `selenium`: python interaction with the website

## website-interface
- `docking_interface.py`: This is the main interface to the package. 
  1. Defines the DockingInterface class to interact with states, actions and the website. 
  2. Defines a function to fetch the `browser` object and the `DockingInterface` object.
  3. Defines a context manager so that the interface can be used with the `with (...) as x: ` syntax. 
- `web_elements.py`: Defines the ID of each website element
- `unit_parser.py`: Parses the information received from strings to some floats or ints.
- `states.py`: Finds the state web elements and adds methods to fetch the states
- `actions.py`: Finds the action web elements and adds methods to click the buttons
- `website_buttons.py`: Finds other website buttons and adds methods to interact with them.

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
