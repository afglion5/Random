# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))