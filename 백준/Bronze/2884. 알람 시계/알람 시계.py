def clock45(hour, minute):
    if minute - 45 >= 0:
        return hour, minute - 45
    elif hour == 0:
        return 23, 60 - abs(minute - 45)
    else:
        return hour - 1, 60 - abs(minute - 45)


hour, minute = map(int, input().split())
result_hour, result_minute = clock45(hour, minute)
print(f"{result_hour} {result_minute}")