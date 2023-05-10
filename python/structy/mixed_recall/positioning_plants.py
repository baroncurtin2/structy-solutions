def positioning_plants(costs: list[list[int]], recur: bool = False) -> int:
    if recur:
        return positioning_plants_recur(costs)
    return positioning_plants_iter(costs)


def positioning_plants_recur(costs: list[list[int]]) -> int:
    # n = # of garden positions (rows)
    # m = # of plant types (columns)
    # Time: O(nm)
    # Space: O(nm)
    return _positioning_plants_recur(costs, 0, None, {})


def _positioning_plants_recur(costs: list[list[int]], pos: int, last_plant: int | None, memo: dict) -> int:
    key = (pos, last_plant)

    if key in memo:
        return memo[key]

    if pos == len(costs):
        return 0

    min_cost = float("inf")

    for plant_type, plant_cost in enumerate(costs[pos]):
        if plant_type == last_plant:
            continue

        candidate = plant_cost + _positioning_plants_recur(costs, pos + 1, plant_type, memo)
        min_cost = min(min_cost, candidate)

    memo[key] = min_cost
    return min_cost


def positioning_plants_iter(costs: list[list[int]]) -> int:
    pass
