from itertools import permutations

ex_lst = list('012')
task_lst = list(range(10))

ex = list(permutations(ex_lst))
# print(ex)

# print(task_lst)
task = list(permutations(task_lst))
ind = 999999
result = ''
for w in (task[ind]):
    result += str(w)
print(result)
# print(task[ind])