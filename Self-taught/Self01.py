def a():
    i = int(input("数字を入れろ:"))
    return i ** 2
    """
    2乗する
    """

print(a())

def b(s):
    print(s)
    """
    おはよう関数
    """

b("おはよう東京")

def c(aa, ab, ac, ba = 4, bb = 5):
    print(aa, ab, ac, ba, bb)
    """
    意味わからん関数
    """

c(1, 2, 3,)

def d(i):
    return i / 2


def e(i):
    return i * 4
"""
2で割って4で乗算する
"""
x = d(4)
y = e(x)
print(y)

def f(str):
    try:
        return float(str)
    except ValueError:
        print("数値を入れろ、数値だ")
        """
        文字列をfloat型の数値に変換する
        """

z = f("40")
print(z)
