import numpy as np



def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

#create 1 by 2 array
pretty_print('simple_array', np.array([1,2]))

#create 2 by 2 matrix
pretty_print('matrix', np.array([[1,1],[2,2]]))

#create arrange array - 1 dimensional
pretty_print('arranged_array', np.arange(1,10))

#zeros 1D array
pretty_print('zeros_array', np.zeros(10))

#zeros array
pretty_print('zeros_array', np.zeros((4, 4)))

#ones matrix
pretty_print('ones_matrix',np.ones((3,3),int))

#multiplication matrix
pretty_print('multiply', np.ones((3,3),int)*7)

#random array 1D
pretty_print('random_array', np.random.rand(5))

#random matrix
pretty_print('random_matrix', np.random.rand(3,3))

#random array with steps
my_array = np.random.randint(1,100,20)
pretty_print('random_matrix', my_array)

#reshape the matrix
pretty_print('reshape_array', my_array.reshape(4,5))

#identity matrix
pretty_print('identity_matrix', np.eye(3))

#linear space
pretty_print('linear_space', np.linspace(0,10,20))







