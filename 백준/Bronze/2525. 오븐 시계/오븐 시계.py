a_hour, b_minute = map(int, input().split())
o_minute = int(input())

total_minutes = a_hour * 60 + b_minute + o_minute

result_hour = total_minutes // 60
result_minute = total_minutes % 60

if result_hour >= 24:
    result_hour %= 24

print(result_hour, result_minute)