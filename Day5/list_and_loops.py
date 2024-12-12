# # 建立清單
# fruits = ["apple", "banana", "cherry"]

# # 取得清單元素
# print(fruits[0])    # 第一個元素
# print(fruits[-1])   # 最後一個元素

# # 新增元素
# fruits.append("orange")     # 在末尾新增
# fruits.insert(1, "peach")   # 在索引1 插入
# print(fruits)

# # 修改元素
# fruits[0] = "grape"
# print(fruits)

# # 刪除元素
# fruits.remove("banana")     # 刪除指定元素
# del fruits[2]   # 刪除索引2 的元素
# print(fruits)

# # 使用 for 迴圈遍歷清單
# fruits = ["apple", "banana", "cherry", "orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")

# # 使用 while 迴圈
# index = 0
# while index < len(fruits):
#     print(f"Fruit {index + 1}: {fruits[index]}")
#     index += 1

# # 建立並操作清單
# names = ["Alice", "Bob", "Charlie"]
# print("Orignal list:", names)

# # 新增元素
# names.append("Jason")
# print("After appending:", names)

# # 修改元素
# names[1] = "Bill"
# print("After modifying:", names)

# # 刪除元素
# names.remove("Charlie")
# print("After deleting:", names)

# # 使用 for 迴圈列印清單
# print("Using for loop")
# for name in names:
#     print(f"My name is {name}")

# # 使用 while 迴圈列印清單
# index = 0
# while index < len(names):
#     print(f"Name {index + 1} is {names[index]}")
#     index += 1

# # 建立有10個數字的清單
# numbers = [10, 0, 20, 40, 50, 30, 60, 70, 90, 80]

# # 計算總和及平均值
# total = sum(numbers)
# average = total / len(numbers)
# print(f"Total: {total}, Average: {average}")

# # 排序清單
# numbers.sort()
# print("Sorted list:", numbers)

# 動態清單
fruits = []
fruit = ""
while fruit != "quit":
    print("Fruits:", fruits)
    mod = input("Choose mod(append, modify, remove, quit):")
    if mod == "append":
        fruit = input("Append fruit: ")
        fruits.append(fruit)
    elif mod == "remove":
        fruit = input("Remove fruit: ")
        fruits.remove(fruit)
    elif mod == "quit":
        fruit = "quit"
    elif mod == "modify":
        index = int(input("which number fruit you want to modify?: "))
        fruit = input("what's fruit: ")
        fruits[index - 1] = fruit