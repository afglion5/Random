# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))