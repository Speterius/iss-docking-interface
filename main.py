import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from website_interface import DockingInterface


def main():
    # Set up the webdriver
    service = Service("./chromedriver.exe")
    options = ChromeOptions()

    # Headless option might be useful later:
    # options.headless = True

    with Chrome(service=service, options=options) as browser:

        # Go to the website
        browser.get("http://localhost:5555/iss-sim.spacex.com")

        # Web Element interface
        w = DockingInterface(browser)

        # Wait for the website to lead and for the user to click the begin button.
        print(f"waiting for 15 seconds:")
        time.sleep(15)

        print(f"Pringing states for 20 seconds as a test ... ")
        for i in range(20):
            print(f"\n_____________________")
            print(f"Angles: {w.states.get_angles()}")
            print(f"Agnular rates: {w.states.get_angular_rates()}")
            print(f"Positions: {w.states.get_positions()}")
            print(f"Velocity: {w.states.get_velocity()}")

            time.sleep(1)

    print("Closing session")


if __name__ == "__main__":
    main()
