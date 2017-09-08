# def solution(A):
#     current = 0
#     num_strokes = 0
#     for i, rect in enumerate(A):
#         if i > 0 and A[i - 1] > rect:
#             num_strokes += A[i - 1] - rect
#             if num_strokes > 1000000000:
#                 return -1
#
#     num_strokes += A[-1]
#     if num_strokes > 1000000000:
#         return -1
#     else:
#         return num_strokes
#
#
# # print "this is a debug message"
#
# from extratypes import Tree  # library with types used in the task
# import copy
#
#
# def solution(T):
#     most_distinct = 0
#     value_dict = {}
#     return dfs_distinct(T, value_dict, most_distinct)
#
#
# def dfs_distinct(T, value_dict, num_distinct):
#     most_distinct = num_distinct
#     v_dict = copy.deepcopy(value_dict)
#
#     if T is None:
#         return 0
#
#     if T.x not in value_dict:
#         v_dict[T.x] = 1
#         most_distinct += 1
#
#     left_distinct = dfs_distinct(T.l, v_dict, most_distinct) if T.l is not None else most_distinct
#     right_distinct = dfs_distinct(T.r, v_dict, most_distinct) if T.r is not None else most_distinct
#
#     return max(left_distinct, right_distinct)


# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, T):
    expanded_s = expand_string_array(S)
    expanded_t = expand_string_array(T)
    print("expanded S = ", expanded_s)
    print("expanded T = ", expanded_t)
    if len(expanded_s) != len(expanded_t):
        return False
    for i in range(len(expanded_s)):
        if expanded_s[i] != expanded_t[i] and expanded_s[i] != 0 and expanded_t[i] != 0:
            return False
    return True


def expand_string_array(A):
    s_arr = []
    in_num_str = False
    for c in A:
        if c == '?':
            s_arr.append(0)
        elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if in_num_str is False:
                in_num_str = c
            else:
                in_num_str += c
            if c == A[-1]:
                for n in range(int(in_num_str)):
                    s_arr.append(0)
        else:
            if in_num_str is not False:
                for n in range(int(in_num_str)):
                    s_arr.append(0)
                in_num_str = False
            s_arr.append(c)
    return s_arr

if __name__ == '__main__':
    print("('A2Le', '2pL1') is", solution('A2Le', '2pL1'))
    print("('?pLe4','Ap6') is ", solution('?pLe4','Ap6'))