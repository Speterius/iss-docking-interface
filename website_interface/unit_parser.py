class UnitParser:
    """Parse the retreived strings into floats. (ditch the units)"""

    angle = "°"
    angular_rate = "°/s"
    position = "m"
    velocity = "m/s"

    small_strength = "noselect"
    large_strength = "noselect large"

    @classmethod
    def parse_angle(cls, s: str) -> float:
        return float(s.replace(cls.angle, ""))

    @classmethod
    def parse_rate(cls, s: str) -> float:
        return float(s.replace(cls.angular_rate, ""))

    @classmethod
    def parse_position(cls, s: str) -> float:
        return float(s.replace(cls.position, ""))

    @classmethod
    def parse_velocity(cls, s: str) -> float:
        return float(s.replace(cls.velocity, ""))

    @classmethod
    def parse_status(cls, s: str) -> int:
        if s == cls.small_strength:
            return 0
        elif s == cls.large_strength:
            return 1
        else:
            raise ValueError(
                f"Error while parsing precision status.\n \
                             Expected either noselect or noselect large. Got: {s}"
            )
