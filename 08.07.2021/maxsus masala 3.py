EnUz = {
  "i": "men",
  "you": "siz",
  "he": "u",
  "she": "u",
  "it": "u",
  "we": "biz",
  "they": "ular",
  "teacher": "o'qituvchi",
  "pupil": "o'quvchi",
  "hello": "salom",
  "bye": "xayir",
  "world": "dunyo",
  "uzbekistan": "O'zbekiston"
}
suz = input("ingilizcha so'z kiriting -> ")
suz =suz.lower()

if suz in EnUz.keys():
    print(EnUz[suz])
else:
    print("Bunday so'z lug'atda yo'q")

# gapni tarjima qilish uyga vazifa