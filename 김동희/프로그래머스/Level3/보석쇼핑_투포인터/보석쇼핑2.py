def solution(gems):
    bucket = {}
    for gem in gems:
        bucket[gem] = 0
    gem_total = len(bucket)

    answer = [0, 0]
    left = 0
    right = 0
    length = float('inf')

    lo = 0
    hi = 0
    now_len = 0
    now_left = 0
    now_right = 0
    count = 0

    while True:
        if count >= gem_total:
            now_gem = bucket[gems[lo]]
            bucket[gems[lo]] = now_gem - 1
            if now_gem == 0:
                count -= 1
            lo += 1
        elif hi == len(gems):
            break
        else:
            now_gem = bucket[gems[hi]]
            bucket[gems[hi]] = now_gem + 1
            if now_gem == 0:
                count += 1
            hi += 1

        if count == gem_total:
            now_left = lo
            now_right = hi
            now_len = now_right - now_left
            if now_len < length:
                length = now_len
                left = now_left + 1
                right = now_right

    answer[0] = left
    answer[1] = right

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
