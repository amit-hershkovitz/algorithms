from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        arr_sorted = arr
    else:
        arr1, arr2 = arr[len(arr) // 2:], arr[:len(arr) // 2]
        arr1_sorted, arr2_sorted = merge_sort(arr1), merge_sort(arr2)
        arr_sorted = merge(arr1_sorted, arr2_sorted)

    return arr_sorted


def merge(list1: List[int], list2: List[int]) -> List[int]:
    merged_list = []

    total_len = len(list1) + len(list2)
    index1 = 0
    index2 = 0

    while len(merged_list) < total_len:
        if index1 == len(list1):
            merged_list.extend(list2[index2:])
            break

        if index2 == len(list2):
            merged_list.extend(list1[index1:])
            break

        if list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1

        else:
            merged_list.append(list2[index2])
            index2 += 1

    return merged_list
