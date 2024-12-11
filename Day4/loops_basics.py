# # 使用for遍歷清單
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"I like {fruit}")

# # 使用range函數
# for i in range(5):
#     print(f"Number{i}")

# # 使用while迴圈
# count = 0
# while count < 5:
#     print(f"Count is {count}")
#     count += 1 # 每次迴圈後將 count 增加 1

# # for 迴圈範例
# print("Using for loop")
# for i in range(1, 11):
#     print(f"{i} squared is {i ** 2}") # 求 i 的平方

# # while 迴圈範例
# print("\nUsing while loop")
# num = 0
# while num < 11:
#     print(f"{num} cubed is {num ** 3}") # 求 num 的立方
#     num += 1

# 計算偶數總和
total = 0
for num in range(2, 101, 2):
    total += num

print(f"Sum of even numbers 1 to 100 is {total}")

# 猜數字遊戲
import random

ans = random.randint(1, 100)
guess = 0
while guess != ans:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess > ans:
        print("Too high!")
    elif guess < ans:
        print("Too low!")
print("Congratulations! You guessed it!")