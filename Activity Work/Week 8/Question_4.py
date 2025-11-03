def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged: list[list[int]] = []

    for s, e in intervals:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    return merged

if __name__ == "__main__":
    examples = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [],  # edge case
    ]
    
    for intervals in examples:
        print(intervals, "->", merge(intervals))