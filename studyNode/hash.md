# Data Structures 基本整理

本文件整理常見資料結構的 **核心概念、用途與差異**，適合快速複習與 README 使用。

---

## 1. Array（陣列）

### 核心概念
- 使用 **連續記憶體** 儲存資料
- 每個元素都有固定 index
- 可直接使用 `array[i]` 存取

### 特性
- Random Access，存取速度快
- 插入、刪除成本高（需搬移資料）

### 適合情境
- 資料量固定
- 讀取遠多於修改

### 時間複雜度
| 操作 | 複雜度 |
|---|---|
| Access | O(1) |
| Insert / Delete | O(n) |

---

## 2. Linked List（連結串列）

### 核心概念
- 由節點（node）組成
- 節點透過指標連接
- 記憶體不需連續

### 特性
- 無法用 index 直接存取
- 需從 head 逐一走訪
- 插入、刪除只需改指標

### 常見種類
- Singly Linked List
- Doubly Linked List
- Circular Linked List

### 時間複雜度
| 操作 | 複雜度 |
|---|---|
| Access / Search | O(n) |
| Insert / Delete（已知位置） | O(1) |

---

## 3. Stack（堆疊）

### 核心概念
- 遵守 **LIFO（Last In, First Out）**
- 只有一個出入口（top）

### 常見操作
- Push：加入資料
- Pop：移除最上層資料
- Peek：查看最上層資料

### 常見用途
- 函式呼叫（Call Stack）
- Undo / Redo
- 遞迴

---

## 4. Queue（佇列）

### 核心概念
- 遵守 **FIFO（First In, First Out）**
- 由 front（出）與 rear（進）組成

### 常見操作
- Enqueue：從 rear 加入
- Dequeue：從 front 移除

### 常見用途
- 排隊機制
- 工作排程
- I/O Buffer

---

## 5. Stack vs Queue

| 項目 | Stack | Queue |
|---|---|---|
| 規則 | LIFO | FIFO |
| 出入口 | 同一端 | 兩端 |
| 常見用途 | Undo、遞迴 | 排程、排隊 |

---

## 6. Hashing（雜湊）

### 核心概念
- 使用 **key 經 hash function**
- 將資料直接映射到 index
- 用空間換取查找速度

`index = h(key) % table_size`

### Hash Table
- 底層為 Array
- 每個位置稱為 bucket
- 不保證資料順序

### Collision（一定會發生）
- 不同 key 對應到相同 index

#### 解法
- Chaining：bucket 內用 Linked List
- Open Addressing：尋找其他空位

### Load Factor
`α = 元素數量 / table_size`
- α 越大，效能越差
- 常見控制在約 0.7

### 時間複雜度
| 情況 | 複雜度 |
|---|---|
| Average | O(1) |
| Worst | O(n) |

---

## 7. 結構選擇快速比較

| 結構 | 存取 | 插入 / 刪除 | 適合情境 |
|---|---|---|---|
| Array | O(1) | O(n) | 快速讀取 |
| Linked List | O(n) | O(1) | 常修改 |
| Stack | O(1) | O(1) | 回復狀態 |
| Queue | O(1) | O(1) | 排隊處理 |
| Hash Table | O(1)* | O(1)* | 快速查找 |

\* Average case

---

## 8. 重點速記

- Array：快取用，改資料慢  
- Linked List：改資料快，找資料慢  
- Stack / Queue：限制存取順序  
- Hashing：key 直接找資料，效能取決於設計
