# 讀取用戶輸入並定義為整數類型。
N: int = int(input("請輸入一個正整數 (1 ≤ N ≤ 100000): "))

# 將整數轉為字符串並反轉，然後轉回整數。
result: int = int(str(N)[::-1])

# 輸出結果。
print(result)