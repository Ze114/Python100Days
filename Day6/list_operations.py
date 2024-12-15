# def example_function(a, b=2, *args, **kwargs):
#     print(f"位置參數 a: {a}")
#     print(f"預設參數 b: {b}")
#     print(f"動態參數 *args: {args}")
#     print(f"動態參數 **kwargs: {kwargs}")

# example_function(1) # 只有位置參數 a
# example_function(1, 3) # 覆寫預設參數 b
# example_function(1, 3, 4, 5, 6) # 添加 *args
# example_function(1, key1="value1", key2="value2") # 添加 **kwargs

def display_list(items):
    '''顯示目前清單'''
    if not items: # 檢查清單是否為空
        print("\n清單是空的")
    else:
        print(f"目前清單內容: {items}")
        for index, item in enumerate(items, start=1):
            print(f"{index}: {item}")

def confirm_action(action):
    '''
    確定是否進行操作
    action:為要進行的操作
    回傳 True 表示確認，False 表示取消
    '''
    while True:
        check = input(f"確定要進行{action}嗎?(Y/N): ").strip().upper()
        if check == "Y":
            return True
        elif check == "N":
            print(f"已取消{action}")
            return False
        else:
            print("輸入無效，請輸入(Y/N)")        

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
            print(f"你選擇的項目為{old_item}")

            # 確認是否進行修改
            if not confirm_action("修改此項目"):
                return # 使用者取消操作

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