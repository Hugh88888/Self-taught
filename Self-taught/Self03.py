az = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for a in az:
    print(a)

for i in range(25, 51):
    print(i)

for index, a in enumerate(az):
    print(index)
    print(a)

z = [1,2,3,4,5]
"""なるべく簡潔に、分かりやすく"""

while True:
    answer = input("数字を当てろ！:")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字を入力するか、ｑで終了します。")
    if answer in z:
        print("正解！")
        break
    else:
        print("不正解！")


iz0 = [8,19,148,4]
iz1 = [9,1,33,83]
iz10 = []
for i in iz0:
    for j in iz1:
        iz10.append(i * j)

print(iz10)
