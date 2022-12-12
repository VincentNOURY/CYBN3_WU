from pwn import *
import time

target = remote("10.242.0.1", 10002)

for i in range(100):
  print(target.recvline())
  target.send(target.recvline())
