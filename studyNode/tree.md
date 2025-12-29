# Tree（樹狀結構）

## 1. Tree 是什麼

- Tree 是一種 **非線性資料結構**
- 用來表示具有 **階層關係** 的資料
- 一個節點可以連接多個子節點

### 常見用途
- 檔案系統
- 組織架構
- 族譜、分類結構

---

## 2. Tree 的基本名詞

### Node
- 樹中的基本單位
- 用來儲存資料

### Root
- 樹的最上層節點
- 沒有 parent
- 每棵樹只有一個 root

### Parent / Child
- 上層節點為 parent
- 下層節點為 child
- 每個 child 只有一個 parent

### Leaf
- 沒有任何 child 的節點
- 位於樹的最底層

### Level
- 節點距離 root 的層數
- root 的 level 為 0

### Depth / Height
- Depth：節點距離 root 的距離
- Height：節點到最深 leaf 的距離

### Degree
- 節點擁有的 child 數量

---

## 3. Tree 與 Linked List 的關係

- Linked List：每個節點只有一個 next
- Tree：每個節點可以有多個 child
- Tree 可視為 Linked List 的延伸

---

## 4. Binary Tree（二元樹）

- 每個節點 **最多兩個 child**
- 分為 left child 與 right child
- 不包含任何排序規則

---

## 5. Binary Search Tree（BST）

### 規則（必考）
- 左子樹 < 節點
- 右子樹 > 節點
- 每一層都遵守此規則

### 特性
- 適合搜尋與排序
- Inorder traversal 會得到排序結果

### 時間複雜度
- Average：`O(log n)`
- Worst（退化成線）：`O(n)`

---

## 6. Balanced Tree

### 為什麼需要平衡
- 不平衡的 BST 會退化成 Linked List
- 搜尋效率大幅下降

### AVL Tree
- 一種自我平衡的 BST
- 任一節點左右子樹高度差 ≤ 1
- 保證操作時間為 `O(log n)`
- 插入與刪除需要 rotation

---

## 7. Tree Traversal（走訪）

### DFS（Depth-First）

#### Preorder（Root → Left → Right）
- 用於複製或儲存樹結構

#### Inorder（Left → Root → Right）
- 在 BST 中可得到排序結果
- 考試重點

#### Postorder（Left → Right → Root）
- 適合刪除整棵樹
- 釋放記憶體

### BFS（Breadth-First）

#### Level-order
- 一層一層走訪
- 使用 Queue 實作

---

## 8. Tree 與其他結構比較

| 結構 | 特性 | 搜尋效率 |
|---|---|---|
| Array | 線性、index 存取 | O(1) |
| Linked List | 動態、指標連接 | O(n) |
| Tree | 階層結構 | O(log n)（平衡時） |

---

## 9. 重點速記

- Tree 是非線性、階層式結構  
- BST 有排序規則，搜尋快  
- 不平衡會退化成 Linked List  
- Traversal 決定資料被「看見的順序」
