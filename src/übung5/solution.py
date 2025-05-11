#!/usr/bin/env python3
# coding: utf-8


# for 0-based indexing, children are at 2i + 1 and 2i + 2

def left(i: int) -> int:
    return 2*i + 1


def right(i: int) -> int:
    return 2*i + 2


def parent(i: int) -> int:
    return (i - 1) // 2


def max_heapify(l: list[int], i: int, heap_size: int) -> None:
    left_index = left(i)
    right_index = right(i)
    min = i
    if left_index < heap_size and l[left_index] > l[i]:
        min = left_index
    if right_index < heap_size and l[right_index] > l[min]:
        min = right_index
    if min!=i:
        l[min], l[i] = l[i], l[min]
        max_heapify(l, min, heap_size)
    """
    If l[left(i)] and l[right(i)] are roots of max heaps,
    construct a max heap rooted at l[i].

    heap_size should be used instead of len(l), as the heap
    may end before the list ends.
    """
    ...


def build_max_heap(l: list[int]) -> None:
    for i in range((len(l)-1)//2,-1,-1):
        max_heapify(l, i, len(l))
    """
    Rearrange the items of l to form a max heap
    """
    ...


class MaxHeap:
    def __init__(self, l):
        self.l = l
        build_max_heap(self.l)
        self.heap_size = len(self.l)

    def extract_max(self) -> int:
        if self.heap_size <= 0:
            raise "Heap is empty"
        min = self.l[0]
        self.l[0] = self.l[self.heap_size - 1]
        self.heap_size -= 1
        max_heapify(self.l, 0, self.heap_size)
        return min


def heapsort(l: list[int]) -> None:
    max_heap = MaxHeap(l)
    for i in range(len(l)-1,-1,-1):
        l[i] = max_heap.extract_max()
    """
    This function should sort l in-place,
    by constructing a heap and repeatedly
    extracting the maximum
    """
    ...

