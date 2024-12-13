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

# # 動態清單
# fruits = []
# fruit = ""
# while fruit != "quit":
#     print("Fruits:", fruits)
#     mod = input("Choose mod(append, modify, remove, quit):")
#     if mod == "append":
#         fruit = input("Append fruit: ")
#         fruits.append(fruit)
#     elif mod == "remove":
#         fruit = input("Remove fruit: ")
#         fruits.remove(fruit)
#     elif mod == "quit":
#         fruit = "quit"
#     elif mod == "modify":
#         index = int(input("which number fruit you want to modify?: "))
#         fruit = input("what's fruit: ")
#         fruits[index - 1] = fruit

# 動態清單管理
def display_menu():
    print("\n---顯示清單選項---")
    print("1.顯示當前清單")
    print("2.新增元素")
    print("3.修改元素")
    print("4.刪除元素")
    print("5.離開")

def display_list(items):
    '''顯示目前清單'''
    if not items: # 檢查清單是否為空
        print("\n清單是空的")
    else:
        print(f"目前清單內容: {items}")
        for index, item in enumerate(items, start=1):
            print(f"{index}: {item}")

def add_item(items):
    '''清單中新增元素'''
    item = input("請輸入要加入的水果: ")
    items.append(item)
    print(f"{item}已新增成功")

def modify_item(items):
    '''修改清單中元素'''
    if not items:
        print("清單是空的!")
        return
    
    # 顯示清單中的內容
    print("\n顯示目前清單中的內容:")
    for index, item in enumerate(items, start=1):
        print(f"{index}: {item}")
    try:
        # 提示使用者輸入要修改的項目編號
        index = int(input("\n請輸入要修改的項目編號：")) - 1
        if 0 <= index < len(items):  # 檢查編號是否有效
            old_item = items[index]
            new_item = input(f"請輸入新的內容來替換「{old_item}」：")  # 提示輸入新資料
            items[index] = new_item  # 更新清單內容
            print(f"已成功將「{old_item}」修改為「{new_item}」！")
        else:
            print("無效的編號，請重新輸入！")
    except ValueError:
        print("無效輸入，請輸入數字編號！")    

def delete_item(items):
    '''刪除清單中元素'''
    if not items:
        print("清單是空的!")
        return
    display_list(items)
    try:
        index = int(input("請輸入要刪除的項目編號: ")) - 1
        if 0 <= index < len(items):
            removed_item = items.pop(index)
            print(f"已成功刪除: {removed_item}")
        else:
            print("無效編號，請重新輸入!")
    except ValueError:
        print("無效輸入!，請輸入數字編號!")

def main():
    '''主程式'''
    fruits = ["apple", "banana"] # 初始化清單
    while True:
        display_menu()  # 顯示選單
        choice = input("請輸入操作選項(1-5): ")
        if choice == '1': # 顯示清單
            display_list(fruits)
        elif choice == '2': # 新增元素
            add_item(fruits)
        elif choice == '3': # 修改元素
            modify_item(fruits)
        elif choice == '4':# 刪除元素
            delete_item(fruits)
        elif choice == '5': # 離開
            print("再見!期待您下次使用本管理")
            break
        else: # 無效輸入
            print("無效輸入!請重新輸入")

if __name__ == "__main__":
    main()
