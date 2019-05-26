import numpy as np

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

#create random array
my_array = np.random.randint(1,100,30)

#get array info
pretty_print('array_shape', my_array.shape)
pretty_print('array_datatype', my_array.dtype)

#array slicing
pretty_print('random_array',my_array)
pretty_print('slice1',my_array[1:10]) #get entry 1 to 9
pretty_print('slice2',my_array[1:10:2]) #get entry 1 to 9 but skip by 2  
pretty_print('slice3',my_array[:]) #same as print all
pretty_print('slice4',my_array[5:-5]) #print all but exclude last 5

#reshape array
reshaped_array = my_array.reshape(5,6)
pretty_print('matrix_shape',reshaped_array.shape)
pretty_print('matrix_shape',reshaped_array.dtype)

#slice matrix
pretty_print('reshaped_matrix',reshaped_array)
pretty_print('slice1',reshaped_array[1:4, 3:6]) #arg (rows,columns)
pretty_print('slice2',reshaped_array[0:3, :]) #only print row index 0 to 2
pretty_print('slice3',reshaped_array[:, 3:6]) #only print column index 3 to 5

#filter matrix with condition
pretty_print('filtered_matrix', reshaped_array[reshaped_array > 10])

#multiply matrix with constant
pretty_print('multiplied_matrix', reshaped_array * 2)






