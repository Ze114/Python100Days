# 建立字典
person = {"name": "小茗", "age": 26, "city": "台南"}
print("修改前:", person)
# 取出name的值
print(person["name"]) 

# 新增/修改
person["job"] = "軟體工程師"
person["age"] = 27

# 刪除鍵值對
del person["city"]

# 使用 .get() 方法避免錯誤
print(person.get("city", "找不到該資料")) # 輸出:找不到該資料

# 顯示整個字典
print("修改後:", person)
