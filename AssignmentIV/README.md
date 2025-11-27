# Homework Assignment IV: Hash Function Design & Observation (C/C++ Version)

This assignment focuses on the design and observation of hash functions using C/C++. 
Students are expected to implement and analyze the behavior of hash functions, 
evaluate their efficiency, and understand their applications in computer science.

Developer: jettinglin  
Email: s1121443@mail.yzu.edu.tw

## My Hash Function
## 須注意事項:
  目前在code是(1)方法，(2)的方法是事先註解掉的，如要測試須把她解開
### Integer Keys 
- 以下皆以c++當範例
- Formula / pseudocode:
  ```text
    /**/(1)  
    double A = 0.6180339887;          
    double frac = key * A - (int)(key * A);  
    return (int)(m * frac);         
    (2)
    return (key % m + m) % m;  // basic division method
  ```
- Rationale: [(2)是我以自己的見解所做的Func，其本身設計就很簡單，就只是在一開始的m的餘數再加一次m和餘數一次，(1)是我網上所查到的function方法叫我Knuth 乘法法，簡單來講就是key * A 會將輸入產生均勻的小數分布再乘以 m，讓數值能分部到0~m-1]

### Non-integer Keys
- 以下皆以c++當範例
- Formula / pseudocode:
  ```text
    (1)
     unsigned long hash = 5381;
    for (unsigned char c : str) {
         hash = ((hash * 33) + hash) + c;
    }
    (2)
    unsigned long hash = 0;
    for (unsigned char c : str) {
         hash += c;
    }
    return static_cast<int>(hash % m);  // basic division method
  ```
- Rationale: [(2)就是把所有單字給加起來餘數取int，而(1)設定一個變數為一個初始值通常是5381，將當前雜湊值左移5位(大概是乘以33或32)，將當前字元的ASCII碼值加到這個計算結果上，將上述計算結果作為新的雜湊值]

## Experimental Setup
- Table sizes tested (m): 10, 11, 37
- Test dataset:
  - Integers: 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60
  - Strings: "cat", "dog", "bat", "cow", "ant", "owl", "bee", "hen", "pig", "fox"
- Compiler: visual studio 2022
- Standard: C23 and C++23

## Compilation, Build, Execution, and Output

### Compilation
- The project uses a comprehensive Makefile that builds both C and C++ versions with proper flags:
  ```bash
 
![螢幕截圖](https://github.com/user-attachments/assets/fff495bc-cc03-4e36-b4f6-6aeb0a5de868)

  
  放在visual studio 2022裡


### Manual Compilation (if needed)
- Command for C:
- Command for C++:

![C++ and C Command](https://github.com/user-attachments/assets/0a4dbd27-c81b-4998-8a7a-7360947b7836)

C++和C都可以直接按建置或按ctrl+B
### Execution
- Run:

![Execution Button](https://github.com/user-attachments/assets/1f090b24-86d0-42a2-b539-2e82ca183505)

按綠色箭頭或按F5
## Result
### Result Snapshot
- (2)的寫法結果:

 ![int_1](https://github.com/user-attachments/assets/b285cc60-cd83-4992-90b5-6001f0417a00)
 
 ![int_2](https://github.com/user-attachments/assets/98c41648-c125-43ef-aee8-141c645faab8)
 
 ![int_3](https://github.com/user-attachments/assets/702eb0ee-7c9c-49bc-bf5c-346f08019586)


- (1)的寫法結果:

 ![str_1](https://github.com/user-attachments/assets/a033b369-0872-4f73-9c35-74f7a894d6c8)
 
 ![str_2](https://github.com/user-attachments/assets/70a8302a-cdfa-45e4-a636-4c90d36a5681)
 
 ![str_3](https://github.com/user-attachments/assets/059a6c88-1ce0-4489-b228-7c947e293971)

# Hash Function Analysis
## Analysis
本次作業比較了兩組雜湊方法，使用相同資料與三種表格大小
m=10,11,37 觀察其分布情況。
| 類型               | 方法 (1)                     | 方法 (2)         |
| ---------------- | -------------------------- | -------------- |
| **Integer Hash** | 乘法法（Multiplication method） | 基本除法法（key % m） |
| **String Hash**  | DJB2（hash = hash * 33 + c） | ASCII 加總法      |

## 4.1 Integer Hash 分析
### 方法 (2)：基本除法法（key % m)
- m = 10
- 觀察
21–30 呈現 1,2,3,…,9,0 的完整循環。
51–60 完整重複相同 pattern。
明顯為線性週期行為。
- 幾乎沒有打散效果，是最規律的一組。
- m = 11
- 觀察
仍明顯呈現線性映射。
51~60 是前一段的「平移版」。
比 m=10 分布好，但規律依然可預測。
- m = 37
- 觀察
21–30 直接等於 key 本身（key < m -> key % m = key）。
幾乎沒有「散佈」的效果。
也呈現單調線性。
### 方法 (1) — 乘法法
- m = 10
- 觀察：
完全無週期性，index 亂度高。
21–60 的映射呈現不規則跳動。
打散效果良好。
- m = 11
- 觀察：
分布更均勻，仍無規律。
不會形成線性 pattern。
乘法法不依賴 m 是否為質數。
- m = 37
- 觀察：
分布最均勻的一組。
幾乎沒有 cluster。
完全看不出規律打散效果最佳。
### 整體結論：Integer Hash
| 方法            | 均勻度 | 規律性    | 碰撞 | 整體表現     |
| ------------- | --- | ------ | -- | -------- |
| **(1) 乘法法**   | 高   | 低      | 低  |  **最佳** |
| **(2) 基本除法法** | 低   | **極高** | 中  |  最弱     |

乘法法完全壓過基本除法法。
無論 m=10/11/37，乘法法都能有效打散連續整數，而除法法會出現明顯週期或線性關係。

## 4.2 String Hash 分析
### 方法 (2)：ASCII 加總法
- m = 10
- 觀察：
bee / pig -> 同為 0（碰撞）
fox / ant -> 同為 3
集中現象明顯
- m = 11
- 觀察：
bat / bee / fox -> 都是 3（碰撞）
cat / ant -> 同為 4
仍呈現部分規律與集中
- m = 37
- 觀察：
分布較散，但仍因字串太短 → 容易集中於相近區間
### 方法 (1) — DJB2
- m = 10
- 觀察：
分布較不規律，無固定週期。
部分碰撞（如 hen / ant / cat = 2），但整體跳動大。
相較 ASCII 加總法更打散。
- m = 11
- 觀察：
分布仍無規則可循。
少量碰撞（bat / bee / fox = 5），但不具明顯模式。
平均性明顯比 ASCII 加總法好。
- m = 37
- 觀察：
此組 m 下分布最漂亮，呈現完整打散效果。
無明顯集群；大部分字串落在不同 bucket。
這符合 DJB2 對短字串仍能保持良好亂度的特性。
### 整體結論：String Hash
| 方法               | 均勻度 | 對字串內容敏感度 | 碰撞率    | 整體表現     |
| ---------------- | --- | -------- | ------ | -------- |
| **(1) DJB2**     | 高   | 高        | 低      |  **最佳** |
| **(2) ASCII 加總** | 中   | 低        | **較高** |  較弱     |

## 4.3 Final Discussion
- Integer：
乘法法對連續鍵（21–60）分布最均勻，不會形成週期。
基本除法法在所有 m（尤其 m=10）都呈現強烈線性規律。
- String：
DJB2 能根據字元順序與權重打散字串，分布最佳。
ASCII 加總法只看字母總和 → 碰撞與集中情況明顯。
- 因此，本次所有測試結果顯示：
- 方法 (1)（乘法法 + DJB2）全面優於方法 (2)（基本除法 + ASCII 加總）。
## Reflection
透過本次作業，我對「雜湊函式的設計」與「實際輸出分布」之間的關係有了更具體的理解。雖然在課堂上知道哪些方法理論上表現較佳，但真正把同一組輸入餵到不同方法後，從輸出結果觀察分布差異，讓我更明確感受到每種方法的特性與侷限。

首先，在 integer hash 的部分，最明顯的觀察是：
當輸入鍵本身具有強烈規律性（如連續整數 21–60）時，雜湊方法的好壞會被放大到非常清楚的程度。
方法 (2) 的基本除法法（key % m）對於這組輸入完全失效，尤其在 m=10 時直接呈現完整循環，而在 m=37 時更是直接映射到原本的 key 值，幾乎沒有任何打散能力。
反觀方法 (1) 的乘法法，即使面對高度規律的輸入，也能讓輸出完全看不出規律，呈現明顯的「去線性化」效果。這讓我更明白：
好的 integer hash 函式，核心在於能否有效破壞輸入模式，而非單純依賴 m 的特性。
在 string hash 的部分，也讓我真正體會到「字串長度短」時雜湊方法設計的重要性。ASCII 加總法（方法 (2)）雖然簡單，但從結果可以看到：
只要兩個字串的 ASCII 總和接近，就容易落到同一個 bucket
也因為測試字串都很短，大部分字串的 ASCII 總和範圍其實不大
因此生成的雜湊值集中在少數幾個位置，碰撞機率偏高
相較之下，方法 (1) 的 DJB2 能把字串的「順序」與「權重」納入考量，即使字串短也能讓輸出呈現更大的跳動幅度。這讓我體會到：
對字串來說，一個好的 hash function 必須同時利用字元內容與順序來產生差異，否則很容易被字串本身的特性限制。

另一個觀察是：
即使採用較好的方法，如果 m 太小，結果仍可能出現碰撞或集中。
這意味著：
選擇 hash function 並不是唯一變數，m 的設計與輸入資料的性質同樣重要。
透過這次比較，我更能理解為什麼在實務中常說「hash 不是一個公式，而是一整套策略」：
包含演算法、表格大小、輸入特性、資料規模等多個因素共同影響最終效果。
最後，實際跑完這些測試後，我最大的感想是：
雖然方法 (1)（乘法法 + DJB2）在所有測試中明顯優於方法 (2)，但這並不表示它「永遠」是最好的，而是對於這次的輸入資料特性與 m 的選擇，它呈現出較佳的分布。未來若面對不同型態的資料，最佳方法仍可能不同。

這次實作讓我更深入理解了雜湊函式背後的原理，也讓我意識到：
真正的雜湊設計不是照著公式做，而是要根據資料特性去選擇最合適的策略。
