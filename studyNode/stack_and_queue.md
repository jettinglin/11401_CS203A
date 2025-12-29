# Stack / Queue（堆疊與佇列）

## 1. 為什麼會有 Stack / Queue

### 問題背景

- 在某些情況下，資料不能被隨意存取
- 資料的進出必須遵守特定順序

### 核心目的

- 限制資料的進出方向
- 強制使用固定規則來存取資料

### Array / Linked List 的限制

- 結構過於自由
- 可以隨意用 index 或指標存取任意位置的資料

### Stack / Queue 的解法

- 明確規定「誰可以先進、誰必須先出」
- 防止資料被亂拿

---

## 2. Stack（堆疊）

## 2.1 Stack 是什麼

- Stack 是一種受限制的資料結構
- 遵守 **LIFO（Last In, First Out）** 規則
- 後放進去的資料，會先被取出

### 結構特性

- 只有一個出入口
- 所有操作都在同一端（top）

---

## 2.2 Stack 的用途

- 函式呼叫（Call Stack）
- Undo / Redo 機制
- 表達式計算
- 遞迴（Recursion）

### 使用原因

- 最後進來的狀態，通常最先需要被處理
- 非常適合用於「回復上一個狀態」

---

## 2.3 Stack 的基本操作

### Push

- 將資料放到 stack 的最上方（top）

### Pop

- 將最上方的資料移除

### Peek / Top

- 查看最上方的資料
- 不移除資料

---

## 2.4 Stack 的實作方式

## 2.4.1 Array-based Stack

### 實作方式

- 使用 array 存放資料
- 使用變數 `top` 記錄目前最上方的位置

### 優點

- 結構簡單
- 存取速度快

### 缺點

- 大小固定
- 容易發生 overflow
- 需要自行檢查 top 是否超出範圍

---

## 2.4.2 Linked List-based Stack

### 實作方式

- top 指向 linked list 的 head
- push / pop 都在 head 進行

### 優點

- 不需預先決定大小
- 記憶體夠就能一直加入

### 缺點

- 每次操作需要 malloc / free
- 記憶體管理較複雜

---

## 3. Queue（佇列）

## 3.1 Queue 是什麼

- Queue 是一種受限制的資料結構
- 遵守 **FIFO（First In, First Out）** 規則
- 先進來的資料，會先被取出

### 結構特性

- 有兩個端點
  - `rear`：資料加入的位置
  - `front`：資料移除的位置

---

## 3.2 Queue 的用途

- 工作排程
- 印表機佇列
- I/O Buffer
- 作業系統的排隊機制

### 使用原因

- 公平處理資料
- 不允許插隊

---

## 3.3 Queue 的基本操作

### Enqueue

- 從 rear 將資料加入 queue

### Dequeue

- 從 front 將資料移除

---

## 3.4 Queue 的實作方式

## 3.4.1 Array-based Queue

### 問題

- dequeue 之後
- front 前方會留下無法再使用的空間

### 解法：Circular Queue

- 將 array 視為環狀結構
- 指標走到尾端後可回到開頭

### 核心技巧

- `(rear + 1) % MAX_SIZE`

### 缺點

- 邏輯較複雜
- 必須同時正確維護 front 與 rear
- 容易實作錯誤

---

## 3.4.2 Linked List-based Queue

### 實作方式

- front 指向第一個節點
- rear 指向最後一個節點

### 優點

- enqueue / dequeue 都是 `O(1)`
- 不需要環狀設計

### 缺點

- 每次操作都需處理記憶體配置與釋放
- 指標錯誤會導致嚴重 bug

---

## 4. Stack vs Queue

| 項目 | Stack | Queue |
|---|---|---|
| 規則 | LIFO | FIFO |
| 出入口 | 同一端（top） | 不同端（front / rear） |
| 常見用途 | Undo、函式呼叫 | 排隊、排程 |

---

## 5. Array 與 Linked List 實作差異

## 5.1 Array 實作

### 特性

- 存取速度快
- 結構直觀

### 缺點

- 大小固定
- 需要處理 overflow / underflow
- Queue 必須額外設計為 Circular Queue

---

## 5.2 Linked List 實作

### 特性

- 動態大小
- 不需預先決定容量

### 缺點

- 每次操作都需 malloc / free
- 指標錯誤難以除錯

### 重點提醒

- 在考試與實作中，邏輯正確性比效能更重要
