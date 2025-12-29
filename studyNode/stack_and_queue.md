# Stack / Queue（堆疊與佇列）

---

## 一、為什麼會有 Stack / Queue

- 白話解釋
  - 有些情況下，資料不能隨便拿
  - 一定要照特定順序進出

- 用來幹嘛
  - 解決資料「進出順序必須受限制」的問題
  - 避免資料被隨意存取

- 核心概念
  - 限制資料進出方向
  - 強制使用固定規則

- Array / Linked List 的問題
  - 太自由
  - 想拿哪個就拿哪個

- Stack / Queue 的解法
  - 直接規定誰先進、誰先出

- 生活比喻
  - 有規則的排隊或堆放
  - 不能插隊、不能亂拿

---

## 二、Stack（堆疊）

### Stack 是什麼

- 白話解釋
  - 後進來的，先出去

- 正式規則
  - LIFO（Last In, First Out）

- 結構特性
  - 只有一個出入口
  - 所有操作都在 top

- 生活比喻
  - 疊盤子
  - 疊書本
  - 河內塔

---

### Stack 用來幹嘛

- 常見用途
  - 函式呼叫（Call Stack）
  - Undo / Redo
  - 表達式計算
  - 遞迴（Recursion）

- 重要特性
  - 最後一個進來的狀態，最先被處理
  - 非常適合「回復上一個狀態」

---

### Stack 的基本操作

- Push
  - 把資料放到最上面（top）

- Pop
  - 把最上面的資料拿走

- Peek / Top
  - 只看最上面是誰
  - 不移除資料

---

### Stack（Array-based）

- 怎麼做
  - 使用一個 array 存資料
  - 用 top 記住最上面的位置

- 優點
  - 實作簡單
  - 存取速度快

- 缺點
  - 容易 overflow（滿了）
  - 需要自行檢查 top 範圍

- 生活比喻
  - 固定高度的盤子架

---

### Stack（Linked List-based）

- 怎麼做
  - top 指向 head
  - push / pop 都在 head 操作

- 優點
  - 不怕滿
  - 記憶體夠就能一直加

- 缺點
  - 每次操作都要 malloc / free
  - 記憶體管理較麻煩

- 生活比喻
  - 一直往上疊盤子
  - 不限高度

---

## 三、Queue（佇列）

### Queue 是什麼

- 白話解釋
  - 先來的，先走

- 正式規則
  - FIFO（First In, First Out）

- 結構特性
  - 兩個端點
    - rear：進
    - front：出

- 生活比喻
  - 排隊結帳

---

### Queue 用來幹嘛

- 常見用途
  - 工作排程
  - 印表機佇列
  - I/O buffer
  - 作業系統排隊機制

- 重要特性
  - 公平處理
  - 不會插隊

---

### Queue 的基本操作

- Enqueue
  - 從 rear 加入資料

- Dequeue
  - 從 front 移除資料

---

### Queue（Array-based）

- 問題點
  - dequeue 之後
  - front 前面會留下很多空位

- 解法
  - 使用 Circular Queue（環狀佇列）

- 核心技巧
  - `(rear + 1) % MAX_SIZE`
  - 指標繞回前面使用

- 缺點
  - 邏輯較複雜
  - 容易寫錯
  - 要同時顧 front / rear

- 生活比喻
  - 轉盤式排隊機

---

### Queue（Linked List-based）

- 怎麼做
  - front 指向第一個節點
  - rear 指向最後一個節點

- 優點
  - enqueue / dequeue 都是 O(1)
  - 不需要環狀設計

- 缺點
  - 每次操作都要處理記憶體
  - 指標錯誤很致命

- 生活比喻
  - 用繩子串起來的排隊人龍

---

## 四、Stack vs Queue（一定會考）

| 項目 | Stack | Queue |
|----|----|----|
| 規則 | LIFO | FIFO |
| 出入口 | 同一端（top） | 不同端（front / rear） |
| 常見用途 | Undo、函式呼叫 | 排隊、排程 |

---

## 五、Array vs Linked List 實作差異

### Array 實作

- 特性
  - 存取快
  - 結構簡單

- 缺點
  - 固定大小
  - 要處理 overflow / underflow
  - Queue 必須做成環狀

---

### Linked List 實作

- 特性
  - 動態大小
  - 不怕滿

- 缺點
  - 每次操作都要 malloc / free
  - 指標錯誤很難除錯

- 重點提醒
  - 邏輯正確比速度更重要
