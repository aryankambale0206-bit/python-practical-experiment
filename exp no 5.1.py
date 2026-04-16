# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:46:58 2026

@author: User
"""
set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))
union_set = set1 | set2 # or set1.union(set2)
intersection_set = set1 & set2 # or set1.intersection(set2)
print("Union of the sets:", union_set)
print("Intersection of the sets:", intersection_set)