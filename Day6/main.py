from list_operations import display_list, add_item, modify_item, delete_item

def main():
    items = []
    while True:
        print("\n---動態清單管理---")
        print("1.顯示清單")
        print("2.新增元素")
        print("3.修改元素")
        print("4.刪除元素")
        print("5.離開")

        choice = int(input("請輸入想進行的操作(1-5): "))
        if choice == 1:
            display_list(items)
        elif choice == 2:
            add_item(items)
        elif choice == 3:
            modify_item(items)
        elif choice == 4:
            delete_item(items)
        elif choice == 5:
            print("感謝使用本系統")
            break
        else:
            print("請輸入正確編號")

if __name__ == "__main__":
    main()