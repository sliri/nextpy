# 1.5
################
import functools

file_data_list = (open(r'/home/liron/PycharmProjects/nextpy/names.txt', 'r')).read().rsplit()

"THe longest name in the list"
longest = max(sorted(file_data_list, key=len))
print(longest)

"The sum of length of the names in the list"
sum_of_length = sum([len(word) for word in file_data_list])
print(sum_of_length)


"print length"
name_length_fid = open(r'/home/liron/PycharmProjects/nextpy/name_length.txt', 'w')
[name_length_fid.write(str(len(name))+'\n') for name in file_data_list]
name_length_fid.close()


"The 2 shortest names"
file_data_list.sort(key=len)
print('\n'.join(file_data_list[0:2]))

defined_length = int(input('Please enter a number'))
[print(name) for name in file_data_list if len(name) == defined_length]



if __name__ == "__main__":
    pass
