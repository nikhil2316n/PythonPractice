lst=[3,5,454,73,82,3,90,234,566,892,342,111,1000]
def second_largest(lst):

    if len(lst)<2:
        return "Second largest is not possible"

    largest=lst[0]
    second_largest=lst[0]


    for i in range(len(lst)):
        if lst[i]>largest:
            second_largest=largest
            largest=lst[i]

    return second_largest

print(second_largest(lst))
