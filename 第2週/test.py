# =========================
# : N 以下の奇数をすべて表示せよ (NO function)
# =========================
N = int(input("Q1) N を入力してください (N 以下の奇数を表示): "))

print("N 以下の奇数:")
for i in range(1, N + 1):
    if i % 2 == 1:
        print(i)


# =========================
# Q2: for文とwhile文の両方を使って階乗を計算せよ (NO function)
# =========================
num = int(input("\nQ2) 階乗を計算する非負整数を入力してください: "))

if num < 0:
    print("負の数の階乗は定義されていません。")
else:
    # factorial using for loop
    fact_for = 1
    for i in range(1, num + 1):
        fact_for *= i

    # factorial using while loop
    fact_while = 1
    j = 1
    while j <= num:
        fact_while *= j
        j += 1

    print(f"{num}! (for文)   = {fact_for}")
    print(f"{num}! (while文) = {fact_while}")


# =========================
# Q3: str 変数に文字数を数える関数を作成せよ (FUNCTION)
# =========================
def count_chars(s):
    """文字列 s の文字数を返す"""
    count = 0
    for _ in s:
        count += 1
    return count


text = input("\nQ3) 文字数を数えたい文字列を入力してください: ")
print("文字数 =", count_chars(text))


# =========================
# Q4: 円の面積を求める関数を作成せよ (FUNCTION)
# area = π r^2, and do not use math module
# =========================
def circle_area(r):
    """半径 r の円の面積を返す: area = π r^2"""
    pi = r=3.143  # math を使わないため定数で指定
    return pi * r * r


r = float(input("\nQ4) 半径 r を入力してください: "))

if r < 0:
    print("半径は負にできません。")
else:
    print("円の面積 =", circle_area(r))