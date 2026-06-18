class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degrees = 360

        # angle_per_minute_partition = degrees/partitions
        apmp = degrees/60
        # angle_per_hour_partition = degrees/12
        aphp = degrees/12

        # Eg. When it is 5, hour hand is at 5 + x% towards 6, where x% is the minute hand passing
        hour_angle = aphp * hour
        minute_angle = apmp * minutes
        hour_angle += aphp * (minute_angle/degrees)  # Unit partition for the timespan of an hour * minute percentage

        between_angle = abs(hour_angle - minute_angle)
        return min(between_angle, 360-between_angle)
