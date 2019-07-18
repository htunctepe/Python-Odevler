# _______________________________5.Hafta, Bonus Odev_______________________________

numList = [num+1 for num in range(10)]
charList = list("abcdefghij")
numToChar = [(str(row)+col+',') for row in numList for col in charList]
charToNum = [(col+str(row)+',') for col in charList for row in numList]
print('1.List : ', '\n', numToChar, '\n', '2.List : ', '\n', charToNum, sep='')