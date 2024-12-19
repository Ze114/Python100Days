# with open("log.txt", "w", encoding="utf-8") as file:
#     file.write("堅持練習\n")

# with open("log.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# with open("log.txt", "a", encoding="utf-8") as file:
#     file.write("加油，可以的\n")

# with open("log.txt", "r", encoding="utf-8") as file:
#     print(file.read())

def replace_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        replace = input("請輸入想覆寫的內容: ")
        file.write(f"{replace}\n")
    
def add_file(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        add = input("請輸入想覆寫的內容: ")
        file.write(f"{add}\n")

def main():
    print("操作選單\n")
    print("1.覆寫檔案")
    print("2.附加內容")

    choice = input("請輸入操作項目編號: ")
    if choice == "1":
        replace_file("log.txt")
    elif choice == "2":
        add_file("log.txt")

if __name__ == "__main__":
    main()