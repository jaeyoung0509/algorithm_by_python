def soulution(untilOne):
    count = 0
    number = untilOne[0]
    share = untilOne[1]
    while (number >= share):
        if(number % share == 0):
            number =  number // share
            count += 1
        elif(number %  share != 0):
            while (number % share != 0):
                number -= 1
                count += 1
    if(number > 1):
        return count+number-1
    if (number == 1):
        return count
untilOne = [34 ,7 ]
print(soulution(untilOne))