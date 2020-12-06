def driver_speed(speed):
    point=12
    if speed<70:
        print("ok")
    elif speed>70:
        a=speed-70
        point=a//5
        print("point",point)
    if point>12:
        print("License suspended")
driver_speed(135)