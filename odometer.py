
def odometer():
    for i in range(1000000):
        if str(i).zfill(6)[2:] == str(i).zfill(6)[5:1:-1]:
            if str(i).zfill(6)[1:] == str(i).zfill(6)[5:0:-1]:
                if str(i).zfill(6)[1:6] == str(i).zfill(6)[5:1:-1]:
                    if str(i).zfill(6) == str(i).zfill(6)[::-1]:
                        print(i)
#odometer()

test = ''