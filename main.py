print("Ini Adalah Code dari Tugas Pertemuan 1")

"""
Algoritma & Analisis – 3 Mini-Case (FIXED, Windows-safe)
1. Pencarian Buku (Linear vs Binary Search)
2. Rute Tercepat Gedung (BFS pada graf kecil)
3. Validasi NIM (10 digit numerik)
-------------------------------------------------
Run: python mini_case_algoritma_fixed.py
"""

import time
import random
from collections import deque

# ------------------------------------------------------------------
# 1. Pencarian Buku – Linear vs Binary Search
# ------------------------------------------------------------------
def linear_search(catalog, target):
    """O(n)"""
    for idx, book in enumerate(catalog):
        if book == target:
            return idx
    return -1

def binary_search(catalog, target):
    """O(log n) – prerequisite: catalog TERSORTIR"""
    left, right = 0, len(catalog) - 1
    while left <= right:
        mid = (left + right) // 2
        if catalog[mid] == target:
            return mid
        elif catalog[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def demo_search():
    print("\n=== 1. PENCARIAN BUKU ===")
    n = 1_000_000
    catalog = sorted([f"buku-{i:07d}" for i in range(n)])  # terurut
    target = catalog[random.randint(0, n-1)]  # pasti ada

    # Linear
    t0 = time.perf_counter()
    linear_search(catalog, target)
    t1 = time.perf_counter()

    # Binary
    t2 = time.perf_counter()
    binary_search(catalog, target)
    t3 = time.perf_counter()

    print(f"Jumlah data: {n:,}")
    print(f"Linear Search : {(t1-t0)*1000:.2f} ms")
    print(f"Binary Search : {(t3-t2)*1000:.2f} ms")
    print(f"Binary ~ {(t1-t0)/(t3-t2):.0f}x lebih cepat")

# ------------------------------------------------------------------
# 2. Rute Tercepat – BFS pada graf sederhana
# ------------------------------------------------------------------
def bfs_shortest_path(graph, start, goal):
    """
    graph: dict {node: [tetangga1, tetangga2, ...]}
    return: list jalur terpendek atau None
    """
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

def demo_bfs():
    print("\n=== 2. RUTE TERCEPAT GEDUNG ===")
    # Contoh mini-kampus
    g = {
        "Gerbang": ["GA", "GB"],
        "GA": ["Gerbang", "Gedung_A"],
        "GB": ["Gerbang", "Gedung_B"],
        "Gedung_A": ["GA", "Kantin"],
        "Gedung_B": ["GB", "Kantin"],
        "Kantin": ["Gedung_A", "Gedung_B", "Perpus"],
        "Perpus": ["Kantin"]
    }
    start, goal = "Gedung_A", "Perpus"
    jalur = bfs_shortest_path(g, start, goal)
    print("Graf kampus (simplified):")
    for k, v in g.items():
        print(f"  {k} -> {v}")
    # FIXED: pakai "->" alih-alih "→"
    print(f"Jalur tercepat {start} -> {goal}: {' -> '.join(jalur)}")

# ------------------------------------------------------------------
# 3. Validasi NIM – cek 10 digit numerik
# ------------------------------------------------------------------
def valid_nim(nim: str) -> bool:
    # Algoritma sederhana: panjang 10 & karakter digit semua
    return len(nim) == 10 and nim.isdigit()

def demo_valid():
    print("\n=== 3. VALIDASI NIM ===")
    uji = ["1030320001", "103032AB01", "123", "10303200012"]
    for n in uji:
        print(f"{n} -> {'VALID' if valid_nim(n) else 'TIDAK VALID'}")

# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
if __name__ == "__main__":
    demo_search()
    demo_bfs()
    demo_valid()