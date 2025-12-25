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
| Complete Binary Tree | Min Heap | 父節點值 ≤ 子節點值 |\

## Section C. Tree Constructions Using Given Integers

**Given integers（所有樹皆使用同一組）：**
37, 142, 5, 89, 63, 117, 24, 176, 58, 133,
92, 11, 151, 72, 39, 184, 7, 101, 54, 160
> 本節使用樹狀結構視覺化工具建構不同類型的樹，並透過截圖與簡要說明呈現其建構方式
# 使用的網站有用以下幾個
> https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
> https://sercankulcu.github.io/files/data_structures/slides/Bolum_08_Heap.html

---
### Binary Tree（二元樹）

**建構說明：**  
將所有給定整數插入二元樹中，每個節點最多具有兩個子節點，不加入任何排序或平衡規則，僅展示一般二元樹的基本結構。
(上面的網站跟我找了許久都沒找到對應的視覺化，固用BST作替代)

**Screenshot：**  

<img width="901" height="476" alt="螢幕擷取畫面 2025-12-24 164043" src="https://github.com/user-attachments/assets/f5ff0edb-688f-4b90-a9f9-b06110dad06e" />

---

### Complete Binary Tree（完全二元樹）

**建構說明：**  
依照給定順序以 level-order（由左至右）方式插入節點，使樹的結構符合完全二元樹的定義，即除最後一層外皆填滿，最後一層由左至右排列。
(用min heap作替代)

**Screenshot：**

<img width="1247" height="717" alt="螢幕擷取畫面 2025-12-24 165513" src="https://github.com/user-attachments/assets/2f2ac4db-0b9c-4968-b5e8-3802dc02a44d" />

---

### Binary Search Tree（BST）

**建構說明：**  
依給定整數順序逐一插入節點，插入過程中遵守二元搜尋樹性質：左子樹中所有節點值小於節點，右子樹中所有節點值大於節點。

**Screenshot：**  

<img width="901" height="476" alt="螢幕擷取畫面 2025-12-24 164043" src="https://github.com/user-attachments/assets/624cd646-4bd1-4c87-9bf3-f59d74185dc8" />

---

### AVL Tree

**建構說明：**  
依序插入所有節點，當插入後造成樹的高度失衡時，透過旋轉操作調整結構，以維持任一節點左右子樹高度差不超過 1。

**Screenshot：**  

<img width="855" height="436" alt="螢幕擷取畫面 2025-12-24 164310" src="https://github.com/user-attachments/assets/f16d4967-242b-4381-9687-d5d9c7c2e77e" />

---

### Red-Black Tree（紅黑樹）

**建構說明：**  
依序插入節點，並透過紅黑節點的顏色規則與必要的旋轉操作，使樹保持近似平衡，確保操作效率。

**Screenshot：**  

<img width="1271" height="402" alt="螢幕擷取畫面 2025-12-24 164750" src="https://github.com/user-attachments/assets/200317a0-18fc-4aef-9c7d-2be3159fee19" />

---

### Max Heap（最大堆積）

**建構說明：**  
使用 heapify（BuildHeap）或逐一插入的方式建立最大堆積，使樹結構維持完全二元樹，並確保父節點的值大於或等於其子節點。

**Screenshot：**  

<img width="797" height="710" alt="螢幕擷取畫面 2025-12-24 172154" src="https://github.com/user-attachments/assets/6bce95ff-44c1-43b1-9be5-17c8949bad90" />

---

### Min Heap（最小堆積）

**建構說明：**  
使用 heapify（BuildHeap）或逐一插入的方式建立最小堆積，使樹結構維持完全二元樹，並確保父節點的值小於或等於其子節點。

**Screenshot：** 

<img width="1247" height="717" alt="螢幕擷取畫面 2025-12-24 165513" src="https://github.com/user-attachments/assets/6d411f6e-d808-44d8-8ed1-c14334d28ae9" />

---

## Section D. Application Examples

