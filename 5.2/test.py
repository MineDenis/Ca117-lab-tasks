line = "Rachel 8:12 8:32 7:12 8:00 08:09"
tokens = line.strip().split()
name, time = tokens[0], tokens[1:]
for i in range(time):
    seconds = time[i].split(":")
    total = int(seconds[0]) * 60 + int(seconds[1])
    

