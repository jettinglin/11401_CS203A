# Hashing（雜湊）

## 1. Hashing 是什麼

- Hashing 是一種 **利用 key 快速定位資料位置** 的技術
- 透過 hash function 將 key 轉換成 array 的 index
- 目的是讓查找、插入、刪除都能非常快

---

## 2. Hash Table 結構

- Hash Table 底層通常是 **Array**
- 每個位置稱為 **bucket**
- 不保證資料的儲存順序

---

## 3. Key / Value

- 使用 **key 查找 value**
- key 用來計算位置
- value 是實際儲存的資料

| 項目 | 說明 |
|---|---|
| Key | 必須唯一 |
| Value | 可重複 |

---

## 4. Hash Function（重點）

- 將 key 轉換成 index
- 相同 key 一定會得到相同 index

`index = h(key) % table_size`


### 好的 Hash Function 應具備

- 計算速度快  
- 分布平均  
- collision 少  

---

## 5. Collision（碰撞）

- 不同 key 經過 hash function
- 得到相同的 index
- 在 Hashing 中 **一定會發生**

---

## 6. Collision 解法

### Chaining

- bucket 內使用 Linked List 存放資料
- 實作簡單，穩定

### Open Addressing

- bucket 被佔用時，尋找其他空位
- load factor 高時效能下降

---

## 7. Load Factor（α）

`α = 元素數量 / table_size`

- α 越大，collision 越多
- 效能越差
- 一般建議控制在 **0.7 左右**

---

## 8. Static vs Dynamic Hashing

| 項目 | Static | Dynamic |
|---|---|---|
| table size | 固定 | 可成長 |
| 效能 | 逐漸下降 | 較穩定 |
| rehash | 無 | 需要 |

---

## 9. 時間複雜度

| 情況 | Search / Insert / Delete |
|---|---|
| Average | O(1) |
| Worst | O(n) |

---

## 10. 重點速記

- Hashing：**key → index**
- 核心在 hash function
- collision 一定會發生
- load factor 決定效能
