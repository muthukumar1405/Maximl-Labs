from collections import defaultdict
def smallest_sub_string(input_str):
    n = len(input_str)
    dist_count = len(set([x for x in input_str]))
    count, start, start_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0)
    for j in range(n):
        curr_count[input_str[j]] += 1
 
        if curr_count[input_str[j]] == 1:
            count += 1
 
        if count == dist_count:
            while curr_count[input_str[start]] > 1:
                if curr_count[input_str[start]] > 1:
                    curr_count[input_str[start]] -= 1
                start += 1
 
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start
 
    return len(input_str[start_index: start_index + min_len])
s = input()
out_ = smallest_sub_string(s)
print(out_)
