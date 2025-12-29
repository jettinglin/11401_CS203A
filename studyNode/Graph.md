# Graph（圖）

## 1. Graph 是什麼

- Graph 是由 **節點（vertices）** 與 **邊（edges）** 組成的資料結構
- 用來表示物件之間的關係
- 不一定有階層，也不一定只有一條路

### 與 Tree 的差別

| 結構 | 特性 |
|---|---|
| Tree | 一定連通、無環 |
| Graph | 可有環、可不連通 |

---

## 2. Graph 的基本組成

### Vertex（節點）
- 圖中的基本單位
- 代表物件本身（人、城市、網頁）

### Edge（邊）
- 連接兩個節點的關係
- 可能具有方向或權重

---

## 3. Graph 的分類

### Directed / Undirected

| 類型 | 說明 |
|---|---|
| Undirected Graph | 邊無方向，雙向連結 |
| Directed Graph | 邊有方向，只能單向移動 |

### Weighted / Unweighted

| 類型 | 說明 |
|---|---|
| Weighted Graph | 邊有權重（距離、成本） |
| Unweighted Graph | 邊無權重，只表示連結 |

---

## 4. Degree（度數）

### 無向圖
- Degree：節點連接的邊數

### 有向圖
- In-degree：指向該節點的邊數
- Out-degree：由該節點指出的邊數

---

## 5. Graph 的種類（常考）

- Connected Graph：所有節點皆可到達
- Disconnected Graph：存在不相連的部分
- Cyclic Graph：存在環（cycle）
- Acyclic Graph：沒有環（Tree 屬於此類）
- Multigraph：節點間可有多條邊
- Self-loop：邊連回自己

---

## 6. Graph 的儲存方式（重點）

### Adjacency Matrix（鄰接矩陣）

- 使用 `V × V` 矩陣表示
- `matrix[i][j]` 表示是否存在邊

**特性**
- 查邊快：O(1)
- 空間成本高：O(V²)
- 適合 Dense Graph

---

### Adjacency List（鄰接串列）

- 每個節點只記錄相鄰節點
- 使用 List / Vector 儲存

**特性**
- 空間效率高：O(V + E)
- BFS / DFS 效率佳
- 適合 Sparse Graph

---

## 7. Graph Traversal（走訪）

- Graph 可能有環或不連通
- 必須使用 `visited[]` 避免重複走訪

---

### BFS（Breadth-First Search）

- 一層一層往外擴散
- 使用 Queue

**常見用途**
- 最短路徑（邊數）
- 層級關係分析

---

### DFS（Depth-First Search）

- 一條路走到底再回頭
- 使用 Stack 或 Recursion

**常見用途**
- 探索所有路徑
- 偵測 cycle
- 拓樸相關問題

---

## 8. Graph vs Tree

| 項目 | Tree | Graph |
|---|---|---|
| 是否有環 | 否 | 可有 |
| 是否一定連通 | 是 | 不一定 |
| 階層結構 | 有 root | 無 |
| Traversal | 不需 visited | 需 visited |

---

## 9. 常見應用

- 最短路徑（地圖、導航）
- 社群網路分析
- 網頁連結結構
- 網路拓樸
- 排程與相依關係

---

## 10. 重點速記

- Graph 用來表示「關係」
- 可有環、可不連通
- Traversal 一定要 visited
- BFS 找距離，DFS 找結構
