from pwn import *

host = "shell2017.picoctf.com"
port = 57641

conn = remote(host, port)

print conn.recvline()
print conn.recvline()
print conn.recvline()
print conn.recvline()
# conn.send(asm(shellcraft.sh()))
# r.interactive()

conn.close()