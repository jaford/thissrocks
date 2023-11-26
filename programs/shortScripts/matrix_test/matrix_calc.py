import numpy as np

matrix_a = np.array([[1,2],[3,4]])
matrix_b = np.array([[5,6],[7,8]])
result = matrix_a + matrix_b

print(f'Matrix A:\n{matrix_a}\n\nMatrix B:\n{matrix_b}\n\nThe result of both A and B:\n{result}\n')

random_matrix_a = np.random.randint(1,10, size=(10, 10)) 
random_matrix_b = np.random.randint(1,10, size=(10, 10)) 

random_result_addition = random_matrix_a + random_matrix_b
random_result_subtraction = random_matrix_a - random_matrix_b
random_result_multiplication = random_matrix_a @ random_matrix_b # You can also use np.dot(A, B)


random_scalar_val = np.random.randint(2,10)
random_scalar_result_a = random_matrix_a * random_scalar_val
random_scalar_result_b = random_matrix_b * random_scalar_val

random_power_val = np.random.randint(2,10)
random_power_result_a = np.linalg.matrix_power(random_scalar_result_a, random_power_val)
random_power_result_b = np.linalg.matrix_power(random_scalar_result_b, random_power_val)

random_result_transpose_a = np.transpose(random_matrix_a)
random_result_transpose_b = np.transpose(random_matrix_b)

random_max_matrix = np.maximum(random_matrix_a, random_matrix_b)
random_min_matrix = np.minimum(random_matrix_a, random_matrix_b)
random_equality_matrix = random_matrix_a == random_matrix_b

num_true_values = np.count_nonzero(random_equality_matrix)


print(f'Random Matrix A:\n{random_matrix_a}\n\nRandom Matrix B:\n{random_matrix_b}\n\nThe result of both A + B:\n{random_result_addition}\n\nThe result of both A - B:\n{random_result_subtraction}\n\nThe result of both A * B:\n{random_result_multiplication}\n\nThe result Transposed Matrix A:\n{random_result_transpose_a}\n\nThe result Transposed Matrix A:\n{random_power_val}\n\n')
print(f'Random scalar value: {random_scalar_val}\n\nRandom scalar result Matrix A:\n{random_scalar_result_a}\n\nRandom scalar result Matrix B:\n{random_scalar_result_b}\n\n')
print(f'Random power value: {random_scalar_val}\n\nRandom power result Matrix A:\n{random_power_result_a}\n\nRandom power result Matrix B:\n{random_power_result_b}\n\n')
print(f'Maximum of A and B:\n{random_max_matrix}\nMinimum of A and B:\n{random_min_matrix}\n\nElement-wise equality check between matrices A and B:\n{random_equality_matrix}\nThe amount of True statements in this matrix: {num_true_values}')

