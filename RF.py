# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))