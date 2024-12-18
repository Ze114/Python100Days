with open("test.txt", "w", encoding="utf-8") as file:
    file.write("今天學習簡單的文字檔案建立與操作\n")
    file.write("今天時間比較晚，而且有點累了，仍然想努力堅持一下\n")
    file.write("明天也要繼續維持，加油^^\n")

def display_file_content(file_name):
    """顯示檔案內容"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print("\n檔案內容：")
            print(file.read())
    except FileNotFoundError:
        print(f"檔案 {file_name} 不存在！")

display_file_content("test.txt")

