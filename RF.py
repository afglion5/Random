# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))