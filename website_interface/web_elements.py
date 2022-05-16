from selenium.webdriver.common.by import By

""" This file contains the html and css id tag of each web elemenent to interact with. """


class StateElements:
    # Angle identifiers:
    roll = (By.ID, "roll")
    pitch = (By.ID, "pitch")
    yaw = (By.ID, "yaw")

    # Velocity norm
    velocity_rate = (By.ID, "rate")

    # Position elements
    pos_x = (By.ID, "x-range")
    pos_y = (By.ID, "y-range")
    pos_z = (By.ID, "z-range")

    # Type identifiers
    error = (By.CSS_SELECTOR, ".error")
    rate = (By.CSS_SELECTOR, ".rate")
    pos = (By.CSS_SELECTOR, "div")

    # Action strength state
    rotation_status = (By.ID, "precision-rotation-status")
    translation_status = (By.ID, "precision-translation-status")


class ActionElements:
    # Angle controls
    pitch_up = (By.ID, "pitch-up-button")
    pitch_down = (By.ID, "pitch-down-button")
    roll_left = (By.ID, "roll-left-button")
    roll_right = (By.ID, "roll-right-button")
    yaw_left = (By.ID, "yaw-left-button")
    yaw_right = (By.ID, "yaw-right-button")

    # Translation controls
    translate_left = (By.ID, "translate-left-button")
    translate_right = (By.ID, "translate-right-button")
    translate_up = (By.ID, "translate-up-button")
    translate_down = (By.ID, "translate-down-button")
    translate_forward = (By.ID, "translate-forward-button")
    translate_backward = (By.ID, "translate-backward-button")

    # Toggle strength:
    toggle_rotation_strength = (By.ID, "toggle-rotation")
    toggle_translation_strength = (By.ID, "toggle-translation")


class WebsiteElements:
    begin_button = (By.ID, "begin-button")
    fail_button = (By.ID, "fail-button")
    fail_message = (By.ID, "fail")
    success_message = (By.ID, "success")
