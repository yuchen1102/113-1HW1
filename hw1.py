from typing import List 
# 導入 List，讓我們可以指定函數參數的類型。 
 
def countLetters(sentence: str) -> List[int]: 
    # 定義一個函數來計算字母出現的次數，接收一個字串作為輸入。 
 
    letterCount: List[int] = [0] * 26 
    # 創建一個⻑度為 26 的列表，初始值都是 0，代表字母 a-z 的計數。 
 
    for char in sentence: 
        # 檢索字串中的每個字符。 
 
        if char.isalpha(): 
            # 如果這個字符是字母，進行下一步。 
 
            index = ord(char) - ord('a') 
            # 計算字母在字母表中的位置（例如，'a' 是 0，'b' 是 1）。 
 
            letterCount[index] += 1 
            # 增加對應字母的計數。 
 
    return letterCount 
    # 返回包含每個字母出現次數的列表。 
 
def printLetterCount(letterCount: List[int]) -> None: 
    # 定義一個函數來打印字母的計數，接收字母計數的列表作為參數。 
 
    for i in range(26): 
        # 每個字母（從 a 到 z）。 
 
        if letterCount[i] > 0: 
            # 如果這個字母出現過（計數大於 0），進行下一步。 
            
            print(f"{chr(i + ord('a'))}: {letterCount[i]}") 
            # 打印字母及其出現的次數。 
 
inputSentence: str = "this is an apple"
# 定義要計算的字串。 
 
letterCount: List[int] = countLetters(inputSentence) 
# 計算字串中每個字母的出現次數。 
 
printLetterCount(letterCount) 
# 輸出每個字母的出現次數。