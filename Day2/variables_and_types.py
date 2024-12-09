# # 數字型變數
# age = 26    # 年紀
# height = 174    # 身高
# print(f"age: {age}, height: {height}")

# name = "Jason"  # 名字
# greeting = f"My name is {name}" # 格式化字串
# print(greeting)

# # 布林值
# is_student = True
# print(f"is student: {is_student}")

# # 數學運算
# num1 = 10
# num2 = 3
# print("加法: ", num1 + num2)
# print("減法: ", num1 - num2)
# print("乘法: ", num1 * num2)
# print("除法: ", num1 / num2)
# print("整除: ", num1 // num2)
# print("取餘數: ", num1 % num2)

print("請幫我輸入兩個數，讓其進行加減乘除和比大小")
num1 = int(input("這裡是第一個數: "))
num2 = int(input("這裡是第二個數: "))

print(f"加法: {num1 + num2}")
print(f"減法: {num1 - num2}")
print(f"乘法: {num1 * num2}")
print(f"除法: {num1 / num2}")
print(f"兩者一樣大嗎?: {num1 == num2}")
print(f"誰比較大呢?: {max(num1, num2)}")