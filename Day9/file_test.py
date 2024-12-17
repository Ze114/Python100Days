# with open("example.txt", "r") as file:
#     # 讀取整個檔案
#     content = file.read()
#     print(content) # 讀取並印出檔案

#     # 一行一行讀取
#     file.seek(0) # 將檔案指標移回起點
#     for line in file:
#         print("讀取一行: ", line.strip())

# # 寫入檔案
# with open("example.txt", "w") as file:
#     file.write("This is new content.\n")

# # 追加內容到檔案
# with open("example.txt", "a") as file:
#     file.write("This is append content.\n")

def display_file(file_name):
    """顯示檔案內容"""
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if content:
                print("檔案內容:\n", content)
            else:
                print("檔案是空的!")
    except FileNotFoundError:
        with open(file_name, "w") as file:
            file.write("")

def write_to_file(file_name):
    """新增內容到檔案(覆蓋模式)"""
    content = input("輸入要寫入的內容:")
    with open(file_name, "w") as file:
        file.write(content + "\n")
    print("內容已寫入檔案")

def append_to_file(file_name):
    """追加內容到檔案"""
    content = input("請輸入要追加的內容: ")
    with open(file_name, "a") as file:
        file.write(content + "\n")
    print("內容已追加到檔案")

def clear_file(file_name):
    """清空檔案內容"""
    confirm = input("確定要清空檔案內容嗎?(y/n): ").lower()
    if confirm == "y":
        with open(file_name, "w") as file:
            file.write("")
        print("檔案已清空")
    else:
        print("操作取消")

def main():
    file_name = "my_file.txt"
    while True:
        print("\n---文字檔案管理系統---")
        print("1.顯示檔案內容")
        print("2.新增內容(覆蓋模式)")
        print("3.追加內容")
        print("4.清空檔案內容")
        print("5.離開系統")
    
        choice = input("請選擇操作(1-5): ")
        if choice == "1":
            display_file(file_name)
        elif choice == "2":
            write_to_file(file_name)
        elif choice == "3":
            append_to_file(file_name)
        elif choice == "4":
            clear_file(file_name)
        elif choice == "5":
            print("quit")
            break
        else:
            print("無效輸入，請輸入正確編號")

if __name__ == "__main__":
    main()