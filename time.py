import time
t = time.localtime()
start_sec = time.strftime("%S", t)
print(start_sec)
while True:
    s = time.localtime()
    new_sec = time.strftime("%S", s)
    diff=(abs(int(start_sec) - int(new_sec)))
    print("Start_sec " +start_sec)
    print("new_sec " +new_sec)
    new_sec
    print( diff )
    #old_
