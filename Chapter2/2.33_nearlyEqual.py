import mutate
    
def nearlyEqual(s1, s2):
    mutated_list = mutate.mutate(s2)
    return s1 in mutated_list

print(nearlyEqual('python', 'perl'))
print(nearlyEqual('perl', 'pearl'))
print(nearlyEqual('python', 'jython'))
print(nearlyEqual('man', 'woman'))
