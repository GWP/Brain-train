def longest__string_k_distinct(char_list, most_distinct):

    def too_many_distinct(cur_range):
        print("testing distinctness of: ", cur_range)
        distinct = 0
        elements = {}
        temp_index = 0

        while distinct <= most_distinct:
            if temp_index == len(cur_range):
                print("Number of distinct is: ", distinct)
                return False
            if type(cur_range[temp_index]) != str:
                raise Exception("Wrong type of element in char array!")
            if cur_range[temp_index] not in elements:
                elements[cur_range[temp_index]] = temp_index
                distinct = distinct + 1

            temp_index = temp_index + 1

        return True

    try:

        def find_static_limit(char_list, current_range, index):
            c = index + 1
            while too_many_distinct(current_range) is False:
                current_range.append(char_list[c])
                c = c + 1
            return current_range, c

        current_range = []
        current_range, index = find_static_limit(char_list, current_range, 0)
        new_start_index = 0

        while index < len(char_list) - 1:
            if too_many_distinct(current_range) is True:
                current_range = current_range[1:] + [char_list[index+1]]
                new_start_index = new_start_index + 1
            else:
                current_range, index = find_static_limit(char_list, current_range, index)

            index = index + 1

        return len(current_range)
    except Exception:
        raise Exception("Something went wrong")

if __name__ == '__main__':
    print("longest string is: ", longest__string_k_distinct(['a', 'b', 'a', 'g', 'h', 'r', 'y', 'e', 'h', 'j'], 2))



