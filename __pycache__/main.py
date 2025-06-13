import time
start_time = time.time()

print("hello")
print("World")
print("hello World")

print("Halo")
# ini adalah comment
"""ini adalah comment juga
woiiiiiii""" # python akan dieksekusi sesuai urutan
a = 10 # ini adalah comment juga
print(a)
for i in range(1,1000):
    a = 10
print(time.time() - start_time, "detik")
#kita bisa mengcompile python ke bytecode
#cara mengcompile, buka terminal dan tuliskan python -m py_compile main.py
