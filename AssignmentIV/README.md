# Homework Assignment IV: Hash Function Design & Observation (C/C++ Version)

This assignment focuses on the design and observation of hash functions using C/C++. 
Students are expected to implement and analyze the behavior of hash functions, 
evaluate their efficiency, and understand their applications in computer science.

Developer: jettinglin  
Email: s1121443@mail.yzu.edu.tw

## My Hash Function
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

## Results
| Table Size (m) | Index Sequence         | Observation              |
|----------------|------------------------|--------------------------|
| 10             | 1, 2, 3, 4, ...        | Pattern repeats every 10 |
| 11             | 10, 0, 1, 2, ...       | More uniform             |
| 37             | 20, 21, 22, 23, ...    | Near-uniform             |

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

### Result Snapshot
- (1)的寫法結果:

 ![int_1](https://github.com/user-attachments/assets/b285cc60-cd83-4992-90b5-6001f0417a00)
 
 ![int_2](https://github.com/user-attachments/assets/98c41648-c125-43ef-aee8-141c645faab8)
 
 ![int_3](https://github.com/user-attachments/assets/702eb0ee-7c9c-49bc-bf5c-346f08019586)


- (2)的寫法結果:

 ![str_1](https://github.com/user-attachments/assets/a033b369-0872-4f73-9c35-74f7a894d6c8)
 
 ![str_2](https://github.com/user-attachments/assets/70a8302a-cdfa-45e4-a636-4c90d36a5681)
 
 ![str_3](https://github.com/user-attachments/assets/059a6c88-1ce0-4489-b228-7c947e293971)


- Observations: Outputs align with the analysis, showing better distribution with prime table sizes.
- Example output for integers:
  ```
  Hash table (m=10): [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  Hash table (m=11): [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Hash table (m=37): [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, ...]
  ```
- Example output for strings:
  ```
  Hash table (m=10): ["cat", "dog", "bat", "cow", "ant", ...]
  Hash table (m=11): ["fox", "cat", "dog", "bat", "cow", ...]
  Hash table (m=37): ["bee", "hen", "pig", "fox", "cat", ...]
  ```
- Observations: Outputs align with the analysis, showing better distribution with prime table sizes.

## Analysis
- integer
  - 乘法法
    - 對 m 的選擇較不敏感，對連續整數（21~60）能產生比較亂的分布。
    - 特別是在 m=10 時，分布比單純 key % 10 均勻很多。
    - 缺點是需要浮點數運算，比純 % 慢一點，但在作業規模下可以忽略。
  - 除法法
    - 實作簡單、執行快速。
    - 當 m 是質數時（如 11, 37），分布可以接受。
    - 但如果 m 選不好（例如 10），pattern 非常明顯，容易集中在周期性的 bucket。
- string
  - 類 DJB2
     - 對字串長度與每個字元的位置都敏感，小變化會造成 hash 大變化。
     - 對一般英文單字（如 cat,dog,bat,cow,...）能提供較均勻的分布。
  - 加總字元
     - 實作最簡單
     - 很多不同字串（特別是同樣字母總和或字母重排）會得到相同 hash，
     - 導致碰撞嚴重，hash table 退化成一堆鏈結串列。 
## Reflection
1. Designing hash functions requires balancing simplicity and effectiveness to minimize collisions.
2. Table size significantly impacts the uniformity of the hash distribution, with prime sizes performing better.
3. The design using a prime table size and a linear transformation formula produced the most uniform index sequence.
