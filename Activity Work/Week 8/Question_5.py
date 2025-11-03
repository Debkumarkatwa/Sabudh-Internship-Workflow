def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    i = 0
    n = len(intervals)
    new_start, new_end = newInterval

    while i < n and intervals[i][1] < new_start:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    res.append([new_start, new_end])

    while i < n:
        res.append(intervals[i])
        i += 1

    return res

if __name__ == "__main__":
    
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    print("Input:", intervals1, "New:", newInterval1)
    print("Output:", insert(intervals1, newInterval1)) 

    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    print("Input:", intervals2, "New:", newInterval2)
    print("Output:", insert(intervals2, newInterval2)) 