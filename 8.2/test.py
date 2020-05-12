def seconds_to_time(s):
    minute, second = divmod(s, 60)
    hour, minute = divmod(minute, 60)
    overflow, hour = divmod(hour, 24)
    return (hour, minute, second)

def time_to_seconds(s, p, v):
    return s * 60 * 60 + p * 60 + v

def main():
    s = 12
    p = 17
    v = 47
    time = time_to_seconds(s, p, v)
    time = seconds_to_time(time)
    print(time)

if __name__ == '__main__':
    main()
