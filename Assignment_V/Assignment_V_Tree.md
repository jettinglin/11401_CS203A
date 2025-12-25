# Assignment V – Tree

Course： Data Structures（11401_CS203A)

---

## Section A　a. Understand and clearly define:

> 本節說明各種樹狀結構的基本定義與特性。

![53803](https://github.com/user-attachments/assets/ecd695c1-a11b-49bd-b268-aeb78cd43b9e)

## Section B　ｂ. Build a hierarchy and transforma on path from the general tree to these variants, and 

> 下圖展示從 General Tree 發展至各種樹狀結構的階層關係，以及每一階段所加入的限制條件。

![53802](https://github.com/user-attachments/assets/1a5fa933-35cb-49e8-9a42-30d5685edf8a)

### Transformation Explanation

| From | To | Added Constraint |
|---|---|---|
| General Tree | Binary Tree | 每個節點最多兩個子節點 |
| Binary Tree | Complete Binary Tree | 節點以 level-order 填滿 |
| Binary Tree | BST | 左小右大的排序規則 |
| BST | AVL Tree | 嚴格高度平衡 |
| BST | Red-Black Tree | 顏色規則維持近似平衡 |
| Complete Binary Tree | Max Heap | 父節點值 ≥ 子節點值 |
| Complete Binary Tree | Min Heap | 父節點值 ≤ 子節點值 |
