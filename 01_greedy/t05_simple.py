def soulution(untilOne):
    count = 0
    number = untilOne[0]
    share = untilOne[1]
    while number >= share:
        if(number % share != 0):
            k = (number // share) * share
            count += (number - k)
            number = k
        elif(number % share == 0):
            number = number // share
            number += 1
    if(number > 1):
        return count+number-1
    if (number == 1):
        return count
untilOne = [34 ,7 ]
print(soulution(untilOne))