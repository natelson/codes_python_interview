# Calculate the angle between hour hand and minute hand.
#
# Note: There can be two angles between hands, we need to
# print minimum of two. Also, we need to print floor of final
# result angle. For example, if the final angle is 10.61, we need to print 10.

# Input:
# H = 9 , M = 0
# Output:
# 90

def getAngle(hour, minute):
    if hour == 12:
        hour = 0

    if minute == 60:
        minute = 0

    angle_hour = 0.5*(hour*60+minute)
    minAngle = 6*minute
    angle = abs(angle_hour-minAngle)
    if(angle > 180):
        angle = int(360-angle)
    else:
        angle = int(angle)

    print(angle)
    return angle


assert 90 == getAngle(9,0)
assert 180 == getAngle(6,0)
assert 15 == getAngle(6,30)