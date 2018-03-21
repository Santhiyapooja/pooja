
time = float(input("Input time in minutes: "))

hour=time/60 
hour1=time%60
time %= 3600
minutes = time // 60

print("h:m->%d:%d" % (hour,hour1))
