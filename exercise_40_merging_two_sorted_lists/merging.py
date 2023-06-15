def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    merged: list[int] = []
    i, j = 0, 0
    while True:
        if i == len(list1):
            return merged + list2[j:]
        if j == len(list2):
            return merged + list1[j:]
        merged.append(min(list1[i], list2[j]))
        if list1[i] <= list2[j]:
            i += 1
        else:
            j += 1
