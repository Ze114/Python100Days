# # 建立集合
# fruits = {"apple", "banana", "cherry"}
# print(fruits) # 輸出集合內容

# # 用set()建立集合
# numbers = set([1, 2, 3, 3, 4, 5]) # 自動去重複
# print(numbers) # 輸出{1,2,3,4,5}

# A = {1, 2, 3, 4}
# B = {2, 4, 6, 8}
# print("聯集: ", A | B) # {1, 2, 3, 4, 6, 8}
# print("交集: ", A & B) # {2, 4}
# print("差集: ", A - B) # {1, 3}
# print("對稱差集: ", A ^ B) # {1, 3, 6, 8}
def display_set(s):
    """顯示集合"""
    if not s:
        print("集合是空的")
    else:
        print("集合內容: ", s)

def add_item(s):
    """新增元素"""
    item = input("請輸入要加入的元素: ")
    s.add(item)
    print("已新增元素: ", item)

def remove_item(s):
    """刪除元素"""
    if not s:
        print("集合是空的")
    else:
        item = input("請輸入要刪除的元素: ")
        if item in s:
            s.remove(item)
            print("已刪除元素: ", item)
        else:
            print(f"{item}不存在")

def union_sets(s1, s2):
    """聯集"""
    print("\n聯集結果: ", s1 | s2)

def intersection_sets(s1, s2):
    """交集"""
    print("\n交集結果: ", s1 & s2)

def difference_sets(s1, s2):
    """差集"""
    print("\n差集結果: ", s1 - s2)

def check_item(s):
    item = input("請輸入要查詢的元素: ")
    if item in s:
        print("烏拉")
    else:
        print("哞")

def main():
    set1 = set() # 可操作集合1
    set2 = set([1, 2, 3]) # 初始集合2
    while True:
        print("\n---操作選單---")
        print("1.顯示集合內容")
        print("2.新增元素")
        print("3.刪除元素")
        print("4.聯集")
        print("5.交集")
        print("6.差集")
        print("7.檢查元素")
        print("8.離開")

        try:
            choice = input("請輸入操作項目編號: ")
            if choice == "1":
                display_set(set1)
            elif choice == "2":
                add_item(set1)
            elif choice == "3":
                remove_item(set1)
            elif choice == "4":
                union_sets(set1, set2)
            elif choice == "5":
                intersection_sets(set1, set2)
            elif choice == "6":
                difference_sets(set1, set2)
            elif choice == "7":
                check_item(set1)
            elif choice == "8":
                print("離開")
                break
            else:
                print("無效輸入，請輸入正確編號")
        except ValueError:
            print("無效輸入，請輸入數字編號")

if __name__ == "__main__":
    main()