# """ Ro'yhatlar (Ko'p o'lchovli ro'yhatlar) """
# numbers = [1, 2, 3, 4, 5, 'ha', True]
#
# # Ro'yhatni o'zi ham ro'yhat elementi bo'la oladimi?
# # Javob: ha
#
# """ chop etish """
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list1 = [[[1, 2, 3], 2, 3], [4, 5, 6]]
#
# for element in matrix:
# print(element)
#
# for element in matrix:
# for raqam in element:
# print(raqam)
#
# # satrlar ham massiv bo'la oladi:
#
# satr = "O'zbekiston"
#
# for harf in satr:
# print(harf)
#
# gap = ["Men", "Pythonda", "ishlayapman"]
# for suz in gap:
# print(suz)
#
# for suz in gap:
# for harf in suz:
# print(harf)

""" indekslar bilan ishlash """

numbersList = [[1, 2, 3], [4, 5, 6], [7, 8, [1, 2, 3, 4, [5, 6]]]]
print(numbersList[2][0])
print(numbersList[2][2][4][1])

""" ko'p o'lchovli ro'yhatni yaratishni maxsus usullari """
numbersList = [[[1, 2, 3] * 1] * 3] * 2
print(numbersList)

numbersList = [[0] * 4 for i in range(4)]
print(numbersList)