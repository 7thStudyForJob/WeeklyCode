def solution(gems):
    answer = []
    setlen = len(set(gems))
    gemdict = dict()

    start = 0
    end = 0
    sect = len(gems) + 1

    while end < len(gems):
        # 없으면 1, 있으면 += 1 씩 k, v 추가
        gemdict[gems[end]] = gemdict.get(gems[end], 0) + 1
        end += 1
        if len(gemdict) == setlen:
            while start < end:
                if gemdict[gems[start]] > 1:
                    gemdict[gems[start]] -= 1
                    start += 1

                elif end - start < sect:
                    sect = end - start
                    answer = [start + 1, end]
                    break

                else:
                    break

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
