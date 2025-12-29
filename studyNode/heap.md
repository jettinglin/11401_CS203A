# Heap（堆積）

## 1. Heap 是什麼

- Heap 是一種 **形狀固定、有順序限制的二元樹**
- 用來 **快速取得最大或最小的資料**
- 不追求完整排序，只保證「最重要的在最前面」

### 與 BST 的差別

| 結構 | 重點 | 主要用途 |
|---|---|---|
| BST | 左右子樹有大小關係 | 搜尋、排序 |
| Heap | 只有父子有大小關係 | 取最大 / 最小值 |

---

## 2. Heap 的兩個必要性質（必考）

### 2.1 Shape Property（形狀性質）

- Heap 一定是 **完全二元樹**
- 每一層填滿
- 最後一層由左到右填入

**意義**
- 樹高度最小
- 可以用 Array 儲存
- 操作效率穩定

---

### 2.2 Heap-Order Property（順序性質）

#### Max Heap
- 父節點 ≥ 子節點
- 最大值一定在 root

#### Min Heap
- 父節點 ≤ 子節點
- 最小值一定在 root

---

## 3. 為什麼 Heap 適合 Priority Queue

- Priority 使用「數值大小」表示重要程度
- Heap 的 root 永遠是目前最重要的資料
- 不需要對所有資料排序

### 對應方式

| Heap 類型 | 重要性 |
|---|---|
| Max Heap | 數值越大越重要 |
| Min Heap | 數值越小越重要 |

---

## 4. Heap 的 Array 實作（常考）

- 因為 Heap 是完全二元樹
- 可以直接用 Array 儲存，不需指標

### Index 關係（index 從 0 開始）

`parent(i) = (i - 1) / 2
left(i) = 2i + 1
right(i) = 2i + 2`

### 好處
- 記憶體連續
- Cache 友善
- 不需要額外指標

---

## 5. Heap 的核心操作

### Insert（sift-up / bubble-up）

- 新元素放在 Array 最後
- 與 parent 比較
- 若違反 Heap-Order 則交換並往上

**時間複雜度**
- O(log n)

---

### Extract Max / Min（sift-down / heapify-down）

- 移除 root
- 用最後一個元素補上
- 與子節點比較並向下調整

**時間複雜度**
- O(log n)

---

### Peek

- 只查看 root
- 不刪除資料

**時間複雜度**
- O(1)

---

## 6. Build Heap 為什麼是 O(n)

- 正確作法是 **bottom-up build-heap**
- 從最後一個非葉節點開始 heapify
- 越底層的節點調整成本越低
- 總成本被攤平為 O(n)

---

## 7. Heap vs BST

| 項目 | Heap | BST |
|---|---|---|
| 結構 | 完全二元樹 | 依插入而定 |
| 最大 / 最小 | O(1) | O(log n)* |
| 插入 / 刪除 | O(log n) | O(log n)* |
| 任意搜尋 | 不適合 | 適合 |

\* 平衡時

---

## 8. 常見應用

- Priority Queue
- CPU / 工作排程
- Heapsort
- Event-driven Simulation

---

## 9. 重點速記

- Heap = 完全二元樹 + 父子順序  
- root 永遠是最大或最小  
- 插入、刪除穩定 O(log n)  
- 非排序結構，只保證「最重要的在前面」
