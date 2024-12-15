def display_dict(data):
    """顯示當前字典"""
    if not data:
        print("字典是空的")
    else:
        print("目前字典內容:")
        for key, value in data.items():
            print(f"{key}: {value}")

def add_item(data):
    """新增資料到字典"""
    key = input("請輸入鍵: ")
    value = input("請輸入值: ")
    data[key] = value
    print(f"{key}: {value}已加入字典")

def modify_item(data):
    """修改字典中的資料"""
    key = input("請輸入要修改的鍵: ")
    if not key in data:
        print(f"{key}不存在")
    else:
        value = input("請輸入要修改的值: ")
        data[key] = value

def delete_item(data):
    """刪除字典中的資料"""
    key = input("請輸入要刪除的鍵: ")
    if not key in data:
        print(f"{key}不存在")
    else:
        del data[key]
        print(f"{key}已刪除")

def search_item(data):
    """查詢字典中的資料"""
    key = input("請輸入要查詢的鍵：")
    value = data.get(key, "找不到該鍵的資料")
    print(f"{key}: {value}")

def main():
    data = {}
    while True:
        print("\n---顯示清單選項---")
        print("1.顯示當前字典")
        print("2.新增資料")
        print("3.修改資料")
        print("4.刪除資料")
        print("5.查詢資料")
        print("6.離開")

        choice = input("請輸入要進行的操作項目編號(1-5): ")
        if choice == "1":
            display_dict(data)
        elif choice == "2":
            add_item(data)
        elif choice == "3":
            modify_item(data)
        elif choice == "4":
            delete_item(data)
        elif choice == "5":
            search_item(data)
        elif choice == "6":
            print("感謝使用本系統")
            break
        else:
            print("無效輸入")

if __name__ == "__main__":
    main()