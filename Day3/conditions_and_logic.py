# # 輸入年齡，判斷是否可以參加活動
# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are too young to participate")
# elif 18 <= age <= 35:
#     print("You are eligible to participate")
# else:
#     print("Sorry, this activity is only for people under 35")

# # 運算邏輯範例
# is_member = input("Are you a member? (yes/no): ").lower() == "yes"

# if age >= 18 and is_member:
#     print("Welcome to the members-only event!")
# elif age >= 18 and not is_member:
#     print("You need to register as a member to join.")
# else:
#     print("Sorry, you are not eligible")

pay = int(input("請輸入您的消費金額: "))
if pay >= 1000:
    discount = 0.10
elif pay >= 500:
    discount = 0.05
else:
    discount = 0

final_pay = int(pay * (1 - discount))
print(f"您所需支付的金額為: {final_pay}")
