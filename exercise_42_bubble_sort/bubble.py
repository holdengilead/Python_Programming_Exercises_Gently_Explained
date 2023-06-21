def bubble_sort(numbers: list[int]) -> list[int]:
    while True:
        changes = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                changes = True
        if not changes:
            return numbers
