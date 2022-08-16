def time_past_0(h, m, s):
    hours = h * 60 * 60 * 1000
    minutes = m * 60 * 1000
    seconds = s * 1000

    return hours + minutes + seconds



print(time_past_0(3, 19, 30))
answer = time_past_0(4, 40, 32)

print(answer)


