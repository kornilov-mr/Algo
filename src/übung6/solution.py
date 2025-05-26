#!/usr/bin/env python3
# coding: utf-8


class HashMap:
    """
    This is a HashMap that maps integer keys to arbitrary python objects as values.

    Internally, the key-value pairs are stored in the self.values and self.keys arrays.
    """
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def _hash_key(self, x: int):
        """
        Simple division hash function.
        Maps all integers into the range [0, self.capacity).
        """
        return (11 + 137 * x) % self.capacity

    def _probe_index(self, hsh: int, i: int) -> int:
        """
        Given the initial hash of a key, and the
        index in the probe sequence, determine
        the index at which to check

        This should implement quadratic probing
        with constants c1 = 1 and c2 = 2.
        """
        return (hsh + i + 2 * i * i) % self.capacity

    def insert(self, key: int, value) -> int:
        """
        Use hash_key with quadratic probing to find an empty slot
        in the self.keys array. Store the key there, and the
        value in the self.values array at the same index.

        If the key is already in the table, it should uptate
        the associated value.

        If no empty slot is found, this function should throw
        an exception.
        """
        hash_key = self._hash_key(key)
        for i in range(self.capacity):
            index = self._probe_index(hash_key, i)
            if self.keys[index] is None:
                self.keys[index] = key
                self.values[index] = value
                return index
            elif self.keys[index] == key:
                self.values[index] = value
                return index

        raise Exception("HashMap is full, could not insert key")


    def search(self, key: int):
        """
        This function should check whether there is
        a key-value pair with this key stored in
        this hash table. If there is one, it should
        return the value, otherwise it should return
        None.
        """
        hash_key = self._hash_key(key)

        for i in range(self.capacity):
            index = self._probe_index(hash_key, i)
            if self.keys[index] is None:
                return None
            elif self.keys[index] == key:
                return self.values[index]
        return None


