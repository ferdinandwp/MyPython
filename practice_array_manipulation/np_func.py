import numpy as np

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n')

my_array = np.random.randint(1,100,20)

pretty_print('my_array',my_array)

#summarize array
pretty_print('mean',np.mean(my_array))
pretty_print('min',np.min(my_array))
pretty_print('max',np.max(my_array))
pretty_print('std',np.std(my_array))

pretty_print('mean', my_array.mean())
pretty_print('min', my_array.max())
pretty_print('max', my_array.min())
pretty_print('std', my_array.std())

reshaped_array = my_array.reshape(4,5)
pretty_print('my_matrix',reshaped_array)

pretty_print('mean',np.mean(reshaped_array))
pretty_print('min',np.min(reshaped_array))
pretty_print('max',np.max(reshaped_array))
pretty_print('std',np.std(reshaped_array))