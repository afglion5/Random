# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))