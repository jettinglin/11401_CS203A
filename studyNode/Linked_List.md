# Linked List（連結串列）

## 1. Linked List 是什麼

- 由一個個節點（node）串起來的資料結構
- 節點之間用指標（next）連接
- 節點在記憶體中不需要連續存放

## 2. 用途與特性

### 用途

- 適合資料數量不固定、會動態變化的情況
- 常用在需要頻繁插入、刪除資料的情境

### 特性

- 不靠 index 存取
- 只能從 head 開始，沿著 next 逐步走訪
- 記憶體配置較有彈性（不需連續）

## 3. Node（節點）

- Linked List 的基本單位
- 常見結構包含：
  - `data`：資料本體
  - `next`：指向下一個節點的指標

## 4. Head（表頭指標）

- 指向第一個節點的指標
- 是整條 Linked List 的入口
- 所有走訪、插入、刪除等操作通常都從 head 開始

## 5. 存取（Access）特性

- Linked List 無法像 Array 用 `list[i]` 直接存取
- 若要存取第 i 個元素，必須從 head 開始逐節點走訪
- 時間複雜度：`O(n)`
- 屬於 Sequential Access，不支援 Random Access

## 6. 插入（Insert）

- 插入的本質是「改指標」，不需要搬移其他資料

### 插入在開頭

- 直接讓新節點的 next 指向原本 head
- 再把 head 改成新節點
- 時間複雜度：`O(1)`

### 插入在中間

- 需先走訪到插入點前一個節點：`O(n)`
- 接上新節點的指標調整：`O(1)`

## 7. 刪除（Delete）

- 刪除的本質是「跳過目標節點」
- 將 `prev.next` 改成 `target.next`

### 特殊情況

- 刪除 head：head 改成 head.next
- 刪除尾端：需先找到尾端前一個節點

## 8. 常見變形

### Singly Linked List（單向）

- 只有 `next`
- 只能往後走訪
- 結構簡單、記憶體用量較少

### Doubly Linked List（雙向）

- 有 `prev` 與 `next`
- 可前後走訪
- 記憶體用量較大（多一個指標）

### Circular Linked List（環狀）

- 最後一個節點的 next 指向第一個節點
- 走訪可以循環
- 常用在排程、輪播機制

## 9. Linked List vs Array

- Array 依靠 index 存取，Random Access 快（`O(1)`）
- Linked List 依靠指標走訪，存取慢（`O(n)`）
- Array 插入/刪除常需搬移資料（`O(n)`）
- Linked List 插入/刪除在已知位置下只改指標（`O(1)`）

## 10. 時間複雜度整理

| 操作 | Linked List |
|---|---|
| 存取第 i 個 | O(n) |
| 搜尋 | O(n) |
| 插入（已知位置） | O(1) |
| 刪除（已知節點） | O(1) |

## 11. 三行速記

- 節點用指標串起來，不需要連續記憶體  
- 存取要從 head 走訪，`O(n)`  
- 插入刪除主要改指標，已知位置時可到 `O(1)`
