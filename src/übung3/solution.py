#!/usr/bin/env python3
# coding: utf-8

def list_reverse_recursion_wrapper(l:list, left=0, right=None):
    if right is None:
        right = len(l)-1
    if left >= right:
        return

    l[right], l[left] = l[left], l[right]
    list_reverse_recursion_wrapper(l, left+1, right-1)


def list_reverse(l: list[int]):
    l_copy = l.copy()
    list_reverse_recursion_wrapper(l_copy)

    return l_copy



