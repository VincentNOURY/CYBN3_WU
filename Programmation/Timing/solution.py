from pwn import *
import random

conn = remote("10.242.0.1", 10003)
random.seed(int(time.time()))

print(conn.recvline().decode("utf-8"))

true_num_1 = str(random.randint(0, 50))
true_num_2 = str(random.randint(0, 50000000000))
true_num_3 = str(random.random())

print(true_num_1)
conn.sendline(true_num_1.encode())
print(conn.recvline().decode("utf-8"))

print(true_num_2)
conn.sendline(true_num_2.encode())
print(conn.recvline().decode("utf-8"))

print(true_num_3)
conn.sendline(true_num_3.encode())
print(conn.recvline().decode("utf-8"))
print(conn.recvline().decode("utf-8"))
