import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(f"A = \n{A}")
print(f"\n B = \n{B}")



suma = A + B
print( "\n-- SUMA (A+B) --")
print(f"A + B = \n{suma}")

prod_elem = A*B
print("\n-- MUILTIPLICACIÓN (AxB) --")
print(f"A x B = \n{prod_elem}")

prod_mat = A@B
print("\n-- PRODUCTO MATRICIAL (A@B) --")
print(f"A @ B = \n{prod_mat}")


transpuesta = A.T
print("\n-- TRANSPUESTA DE A (A.T)")
print(transpuesta)

det = np.linalg.det(A)
inv = np.linalg.inv(B)
print("\n-- Determinante de A --")
print(f"|A| = \n{det}")

print("\n-- Inversa de B --")
print(f"B! = \n{inv}")