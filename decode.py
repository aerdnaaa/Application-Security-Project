import base64
import zlib

print(zlib.decompress(base64.urlsafe_b64decode('enter cookie===')))
