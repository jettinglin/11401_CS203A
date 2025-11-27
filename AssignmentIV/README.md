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
### 方法 (2)：基本除法法（key % m）— 實際結果
- m = 10
- 觀察
21–30 呈現 1 → 2 → 3 → … → 9 → 0 的完整循環。
51–60 完整重複相同 pattern。
明顯為線性週期行為。
- 幾乎沒有打散效果，是最規律的一組。
- m = 11
- 觀察
仍明顯呈現線性映射。
51~60 是前一段的「平移版」。
比 m=10 分布好，但規律依然可預測。
- m = 37
觀察
21–30 直接等於 key 本身（key < m → key % m = key）。
幾乎沒有「散佈」的效果。
也呈現單調線性。
### 整體結論：Integer Hash
| 方法            | 均勻度 | 規律性    | 碰撞 | 整體表現     |
| ------------- | --- | ------ | -- | -------- |
| **(1) 乘法法**   | 高   | 低      | 低  |  **最佳** |
| **(2) 基本除法法** | 低   | **極高** | 中  |  最弱     |

乘法法完全壓過基本除法法。
無論 m=10/11/37，乘法法都能有效打散連續整數，而除法法會出現明顯週期或線性關係。

## Reflection
在這次作業中，我分別比較了兩種整數的雜湊方法（方法一與方法二），以及兩種字串的雜湊方法，從中觀察它們在不同表格大小下的分布情況與碰撞特性。

在 (1) 的 integer 實作 中，我採用的是最基本的 線性（linear）方式：
就是直接以 key % m 取餘數。這種方式雖然簡單，但當測試資料本身較單純、尤其是本次的整數輸入是連續的（21,22,23…）時，分布會呈現非常明顯的規律與重複，常常可以看到週期性的循環，整體「打得不夠散」。因此，只要 table size m 不夠佳，例如 m=10，就會出現可預期的 pattern，而不是理想的均勻打散。

在 (1) 的 string 實作 中，我採用「加總字元 ASCII 值」後再對 m 取餘數的方式。雖然這種方法也算是簡單版本，但相比整數的線性方法，它確實能把結果打得更散一些，分布也更難直接目視出規律。不過它仍然有先天限制，因為字串不同但總和相同時，依然可能收到相同 hash 值（例如不同字母組合但和相同），因此碰撞問題仍然存在。

到了 (2) 的方法，不論是 integer 或 string，我採用的都是從網路查詢後參考較常見的雜湊演算法，例如 integer 的乘法法（multiplication method）、string 的類 DJB2 法等。這些方法的共同特性就是：
    能夠把輸入打散得更徹底
    規律不明顯、分布較均勻

從輸出結果來看，不管是整數或字串，方法 (2) 都明顯比方法 (1) 更能「完全打散」「看不出規律」。
但在 string 的部分，我仍然觀察到一些碰撞（或潛在碰撞）的情況。查過資料後得出的結論是：
這類較複雜的 hash 方法雖然強大，但在以下情況下仍可能碰撞偏高：

table size m 不夠大

輸入資料本身太過 simple（例如短字串或字母範圍小）

資料量不大但彼此類似

因此在實務中，這類方法比較適合用在較複雜的 hash 場景，例如資料量大、字串較長、m 是設計成質數或較大的容量。

整體來說，這次實作讓我清楚看見：「好的 hash function 不只是算式不同，而是要同時考慮資料特性、表格大小、算法特性」。簡單方法在某些情況下雖然有效，但面對敏感資料時容易失效；而複雜方法雖然打散能力強，但也需要良好的參數與場景搭配。可以說 hash function 的選擇本身，就是一種需要兼顧數學性質與資料特性的取捨。
