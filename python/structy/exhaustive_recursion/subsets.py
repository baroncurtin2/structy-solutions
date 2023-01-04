def subsets(elements):
    # n = length of elements array
    # Time: ~O(2^n)
    # Space: ~O(2^n)
    if not elements:
        return [[]]

    first = elements[0]
    remaining_elements = elements[1:]
    subsets_without_first = subsets(remaining_elements)

    subsets_with_first = [[first, *sub] for sub in subsets_without_first]
    return subsets_without_first + subsets_with_first


def subsets_with_tail_call_optimization(elements: list[str], subsets_without_first=None) -> list[list[str]]:
    # n = length of elements array
    # Time: ~O(2^n)
    # Space: ~O(2^n)

    if subsets_without_first is None:
        subsets_without_first = [[]]

    if not elements:
        return subsets_without_first

    first = elements[0]
    remaining_elements = elements[1:]
    subsets_with_first = [[first, *sub] for sub in subsets_without_first]
    return subsets_with_tail_call_optimization(remaining_elements, subsets_without_first + subsets_with_first)
