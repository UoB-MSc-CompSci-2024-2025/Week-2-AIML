import sdp
import math

mylist = [1, -3, 2, 6]

partitioned_list = sdp.listparts(mylist)


def maketuple(partitioned_list):
    tuple_list = []
    for partition in partitioned_list:
        product = 1
        for part in partition:
            s = sum(part)
            product = product * s
        new_tuple = (partition, product)
        tuple_list.append(new_tuple)
    return tuple_list


new_list = maketuple(partitioned_list)


def max_sum_tuple(list):
    maxsum = -math.inf
    for partition, partition_sum in list:
        if partition_sum > maxsum:
            maxpart, maxsum = partition, partition_sum
    return (maxpart, maxsum)


print(f"Partition with the maximum sum: {max_sum_tuple(new_list)}")
