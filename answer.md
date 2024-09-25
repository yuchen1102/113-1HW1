# 第1次作業-作業-HW1
>
>學號：112111205
><br />
>姓名：鄭宇辰
><br />
>作業撰寫時間：300 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2023/09/22
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容
- [x] 個人認為完成作業須具備觀念

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)

請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。

1. 請解釋何謂git中下列指令代表什麼？並舉個例子，同時必須說明該例子的結果。其指令有add、commit、push、fetch、pull、branch、checkout與merge。

Ans:
```git
1.  
    解釋:add
    git add 檔名(或 . #全部檔案) #添加至暫存區
    例子:
    git add file.txt #把file.txt添加至暫存區
2.  
    解釋:commit
    git commit #從暫存區提交到本地倉庫 可以進行備註
    例子:
    git commit #提交到本地倉庫，並進行備註
3.  
    解釋:push
    git push #從本地倉庫推送到遠端倉庫
    例子:
    git push #推送到遠端倉庫，讓其他人可以看到最新的變更。
4.
    解釋:fetch
    git fetch #從遠端倉庫下載所有新的資料，但不會合併到本地分支。
    例子:
    git fetch #本地倉庫的資料將更新，但不會影響當前分支。需要使用 git merge 或 git pull 來整合變更。
5.
    解釋:pull
    git pull #從遠端倉庫下載新資料並自動合併到當前分支(fetch 和 merge的結合體)
    例子:
    git pull #新資料會被下載並合併到當前分支。如果有衝突，需要手動解決。
6.
    解釋:branch
    git branch (新的分支名稱) #用於創建新分支(用於做新東西而不影響之前版本)
    例子:
    git branch newfile #創建名為newfile的分支
7.
    解釋:checkout
    git checkout (分之名稱) #切換分支
    例子:
    git checkout newfile #切換到newfile分支
8.
    解釋:merge
    git merge #將另一個分支的變更合併到當前分支
    例子:
    git merge newfile #若處於main下，使用此指令可以把newfile併入到main中
```


2. 於專案下的檔案—**hw1.py**，撰寫註解，以說明該程式每列中之背後意義。

    該hw1.py題目如下：

    ```
    統計字母數。假設今天輸入一句子，句子中有許多單字，單字皆為英文字母小寫，
    請統計句子中字母出現的字數，輸出實需要照字母排序輸出，且若該字母為0則不輸出

    如輸入
    this is an apple
    輸出
    a: 2
    e: 1
    h: 1
    i: 2
    l: 1
    n: 1
    p: 2
    s: 2
    t: 1
    ```

Ans:
```py
from typing import List
# 導入 List，讓我們可以指定函數參數的類型。

def countLetters(sentence: str) -> List[int]:
    # 定義一個函數來計算字母出現的次數，接收一個字串作為輸入。

    letterCount: List[int] = [0] * 26
    # 創建一個長度為 26 的列表，初始值都是 0，代表字母 a-z 的計數。

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
```




3. 請新增檔案**hw1_2.py，**輸入一個正整數(N)，其中$1\le N \le 100000$，請將該正整數輸出進行反轉

    ```
    如輸入
    1081

    輸出
    1801

    如輸入
    1000

    輸出
    1
    ```

Ans:
```py
# 讀取用戶輸入並定義為整數類型
N: int = int(input("請輸入一個正整數 (1 ≤ N ≤ 100000): "))

# 將整數轉為字符串並反轉，然後轉回整數
result: int = int(str(N)[::-1])

# 輸出結果
print(result)
```

4. **[課外題]**：請找尋資料，說明何謂**單元測試**，請新增檔案**hw1_3.py**，並利用溫度計攝氏轉華氏撰寫單元測試。

Ans:
1.單元測試（Unit Testing）是一種軟體測試方法，主要目的是對應用程式中的最小可測試單元進行檢查，以確保其按預期運行。這些最小可測試單元通常是指程式中的函數、方法或類別。單元測試的主要特點包括：

針對性：單元測試專注於檢查單一功能或邏輯，確保其在不同情況下的表現都符合預期。

自動化：通常使用專門的測試框架（如 JUnit、pytest 等）來自動執行測試，這樣可以提高測試效率並減少人為錯誤。

及早發現錯誤：通過在開發過程中隨時執行單元測試，開發者可以及早識別並修正錯誤，這樣可以降低後期維護的成本。

增強可維護性：良好的單元測試能夠使代碼更易於理解和修改，因為測試案例能夠清晰地描述函數的預期行為。

支援重構：在進行代碼重構時，單元測試可以確保新代碼仍然保持原有的功能。

2.單元測試的過程
編寫測試用例：開發者針對特定的功能編寫測試用例，這些用例通常包括正常情況、邊界情況和異常情況。

執行測試：使用測試框架執行測試用例，檢查實際輸出是否符合預期輸出。

分析結果：根據測試結果判斷是否需要修正代碼。如果測試失敗，開發者需要檢查並修正代碼，再重新執行測試。

持續測試：在整個開發過程中持續進行單元測試，確保每次修改不會影響到其他功能。

3.優點
提高代碼質量
降低維護成本
提升開發效率
促進良好的編碼習慣



## 個人認為完成作業須具備觀念

開始寫說明，需要說明本次練習需學會那些觀念 (需寫成文章，需最少50字，並且文內不得有你、我、他三種文字)且必須提供完整與練習相關過程的notion筆記連結