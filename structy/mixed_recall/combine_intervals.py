def combine_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # n = number of intervals
    # Time: O(nlogn)
    # Space: O(n)
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

    combined = [sorted_intervals[0]]

    for current_interval in sorted_intervals[1:]:
        current_start, current_end = current_interval
        last_start, last_end = combined[-1]

        # intervals overlap
        if last_end >= current_start:
            if current_end > last_end:
                combined[-1] = (last_start, current_end)

        # intervals do not overlap
        else:
            combined.append(current_interval)

    return combined
