class UnitParser:
    """Parse the retreived strings into floats. (ditch the units)"""

    angle = "°"
    angular_rate = "°/s"
    position = "m"
    velocity = "m/s"

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
