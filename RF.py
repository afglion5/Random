# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJzsvQl0HNd5LtgbdpIAd3ABWAQIEiCBRlV1Vy8ESamxg1iJbixsioQaXQWgid5Y3eDSAmTHcWLHkR3asWPalp8hRbJJh47pPGsiJ/KLvMiRE9vp1rRGOHXCczKe43mjM2fmQc/yexq8N/Pm/28tvWAhKMlxnAjo/uq7/92XunXv7fvX/d90WX+VyvWX7+zU6T6v43VeXYmO1/OGoN6rJ1eD10CuRq+RXE1eE7kWeAvItdBbSK5F3iJyLfYWk2uJt4RcS72lcDUGSzxyuGXeMriagltCW73b9CgrCJaFyr0VWbxcrwvbanXC9iM60azXGXTCDr7wq3qd7s/0asKJVH95p2rmix5gX5xvf14XNl3TXTee113Tl6Brw+VdmuuSXNeXd6vMuwdc7uVL+bKvGsCFQZUvqiWZ8yfsy481XAX52g/52u09QPK1ZXW6eIP3wIUD4WL5ek2vplKJeWtezAfXivmr8P0zzbRY9WA33n3TOm/1qpLYtl5JbCrMQ8Khdt3FvV5KqF48vJZ7gcrP/1OV4aJauX6Mcr4hXTWr0lX+ntJVK9SSdB0RatZJ15EHpwtSVHi5TnUxreMrntXn+vIehbQfA3f1/PZcG4j9k95afoe3YVUoO1eFcpzfBa5OCEdz5V/SfdngbeR3e5tIGGatbPbwe3PbiLeZr/TSea728fvzXDF5Lg7wB/NcsHyV1yI0fEnHVwvHAQ8JjYCU0PQlndAM7LBAE2QIssSdBdJZ4bUKx9Ypaeuqkv7UOiX2kpfjazZZYrXexlXujqxyZ8vLcR1/NC/HBzYRip0/9puuA8EG3wPwtW+qPnZ6HevWh2NVfXwXWrFz7Tq5qb+o956EFLdo6Tu1iRI7/cByP8PXY5uH7ym+gT+ea5t/H/AnyP1xOl9OpGfWlK5yyzdq8TXx5gfE16y5pXnmAW4Pa25ZvukBbi1ZabBuOg16ntt0Gh7s1gat45DgXKd1HMpvHTf1TxmhfTyyzj37v3sfzW0dvF1Li4N3PiAt1Q/h9qTmto5veIDblqxyPrXpcj79EHXdlH/frnJ75jefhi/vgCfhI+vUdO2qfuA/bvA0W69vfmSNvvnRf8V9s+ufu2/mW30uSFfp5VYtXW18+92OvFFi21rh8Z254S22r+mqi2/Ny2dHXozdv/YYO/Ni7Pm1x9jFn/V2k3Fndry97zrenjVd9eW64vX7NLtNp/RsuARHpny/92zO6DQ73QO/9vLqzYtx8NceY5/Q6e0XOrwDeTEPvc8x9/Hn8kLbbAoH+eG8tLl/3aWSQKkHMS/mkX+OmL1D/9x3jPcsr/eeE87CM6jISwvn+LrEVpCee6qYH/UOC8P82CyJV7z423Anxz+SsRfOYk58rvCnIBfjSi7m/9l7pLr3LR/HlbWPPd4D2Fet5UZb/diVv/qxno+1+j6hQ+gUuoRuoVeAPkIYEAaFIf7806VeN+/9qM7rgXHMCH/BO8o/5h3jL3rH+Uve8/yE18s/7r3A+7yP8ZPei7zfe4nnvRO84H2cn/L6+GnvJD/j9fMBL89f9gr8rHdKeBye2kGCIcEPGP5yoXeaj0AcM3wUMMDrfZendb5ZiDEI3xB8w/CNQB0GctckIA9XwEeUFwGv8DFAkY8Dxvg5wDh/FXCOvwZ4lb/uvcbfAHadTwDe4J8ATPDzJN4FwCcg/CfywwdZdFWcBreu4ckGU2KvPxIyT/n8wmQkMmv28bGQL+ybFsTE9hyLYCAu5Ikiot+3sjNHNOuLg+83MYqBBr2kPw6wwzMjCj5+KBIJdlwX/HPxiAjSra2Cby4emJoLuiNz0QRVSvWEY3FfMBgIT1OhQCxGrhF+LijEKLPZnGiOBqJUQHZDicKVOSEWj1GTMSs1NRefE4XY6dMsdYZq5oWrzeG5YDCxLXojPhMJU3OxUMAcvZE4MxOPR2Mnm5tF3zXzdCA+Mzc5FxNEfyQcF8JxM+Sj2TU+2O/knM2TN5qbQ75AuDkqRq4HhJg5fj2eKMsySPprcycgkwcuMC1ONnTh5x//4kVqqK/D5e6gxlw9Hqqtu6Ott2egixoZand5OiADkl5MPPrgJMTFeFNnQBSaeShKORGxuAiFISei5V2FMOdDz/ULcG+vFHV5mhia4RTC0gqxaES1sqoSqyrhFAmrWlk1AlbFSByMU2WsjV0pQeakbXSPLHTSDlZjFoVBwCrjVFvGqTILrQTo5Gg5ISytiJDQqihGiAUlGKuVsY4PDhGZzck4CLHTDK0QViUWlVhVouTSztAa4RSiemdVCcvIKbFDkQwrIqW47BbaohDVm4XViOqGtSlEjd5Kc4kKJBxHl3BAHLQSmQNTX4CEWSkkF9mLQ02fg1FS42BZ2i2LrIojUowygUQUEtJFHLtIRgmDEqZXSpENtA8P9rQTaStrV4Jt5SwWuXAJa83QvpVtKvX2unoGRhT3nOaTY1iF2VmF2TVbe0bmUGXQFlRmcTgIa7PQim2bRW1cbRYo3WFFaGEyQnZYoxaPas9q9iwbUIQcSytCYD2qUGl+yDiF2ZWm22azK/F0MKyDlQPvYDilFDug8DOMVRmnyThVZlOaKjCOHZOFFrVFdUBZOmVrZD0ZKkfYxVno7gSyaSdNT8kyqOVOwrqdanJ6oB05FAYtSGY2qxJLjwOLeZvMbPRgb59nyJUxe8f6PB6P4pLlHCQRPXhntycUoc2hMLw7ZY+QslaXq9Uzkm3ua+sezDFjwHJwkMIOEkjAYVdT7bArt2GPUyklJI4+2Z0T71ZF6KA7NMq2yVEg7RgjDVGzCigUWnuX4gpoXy8kzJOx6s/QoQz1aB64Ebg3WjUPrKMjQ3sydFSlnGMoQzWpLePWyWYo152hfXI5OLHhyELoT3o0yg1oVAsLaqArQ8c1ah9VwoIGl8AyDamddD9n4xRRICwX0AA0HOg8iglVewZknMoYTabcOQNQa9AbFCuUU4Sk3IoVymosY81lrB2a0CH3OgMOtZMfIB2gwhhNxirMqblzqi1wCGKm28Zc424XCZaY+zNUjhYoI6d/CLoQJf1IOY05VKZEO6QVyBCHN3mZzBh6vJ1RxUq6hmys0m4J69OEjMoYzSGjyhxq6FqXPGS3qMEga1WFjGbNqtZQb+0Z2p/Q6HCGjiaKFcqojJGZ2wJdi8ZYjVlUZldtOcahMpCVEAYNK6AIsUEpQs4yplC7ne7N0H6FQnbHFF9QnyrjlIiwKGWHyIY1Iasyi2Ztocc0avEQGkN6TXWaCZOTMwTWNk3myDBWDcdhaVWFTjVGqADFGlifJmQ0IdOaoRl7VhOyrZrQogm1iKBSVSFDt2ZoW4Z2ZGhXhvZkaF+G9mfogBaDlhaGzcTAZmJgtWSrrYGDylWtbZlk2TJR2WiP5tSiMbvGnCpzaAE56HZFCI1SZVo8wAIqtWtRAu3JUDWdnF1pjZxNC8lGq8mwaUUKrFcTMipjNS92zSHGuE2l3b2tXo9LdeTUHDm1BunQmiGw9gztytBAhvZlaH+GejJ0VKNMQIvBoQmditAGfZecSmStrfi01WyUSkamtC3IvSpkaLXmbaxTuVncNtLitqnUO+bq71FqyKY1GhuOpFQhp9wUNk69KZC1Z6hSQTa7WmjI+jJ0QKNqm8PuT0kDsO5e13inS7NRo3OoNYqsNUM7MrQvQ/vV8IC2wuRsOGM1pAXIakI2E6B6TyANaE4dmtChVJQdOp8OjVo0yqkt3A6DJZWpjQxZnyZkNaEaKVC1pIE6NKFDqWO7RS1UZF0Z2qfZs5pQLV7s/+XiQOaSm0y2GYY12WaPp28oY4bHKdqXqOa+DFVTqt3AyPo1IasJtewBDWSolj6bTWMOzdrRowq1goJxbIdGtYLiHOMqU3tsu11tLcjUeBxONXRgSugOrR/C0anCbGrT9sBsxEmGSR7GSisEnik4jRp1+JSr3ExG29RmMtoPvtzE9RhjYRQCDyAk4w5FMu7QJHZaIU45BedxEByoOKbTJar7I4lAMOhr5sw0Vd8XCM9db6FGWihXmBcjAb6hWNLbJL1d0jskvVMyMDR8Gfiy8IXOkBLCTXOxFiphdkWjQWFMmOwNxJs5i91ssVH1vd2e/r5GKhiYFaguwT8baaDaZsRISGh+E1cK3+QBJD0dmKnQ6QJHdoKkHsV/ApDY1R+ZDAQFyu2b8okBJcgVPZUwQGyGBmpFb07UrJV4JeWUzUybmZaEXUkhQ7dQMC6VAw3d8ETm/DOUpYtyBwO8QLXOBYJ8c9dwj5Vu6GGsjtGGhv2S3iXpWyV9m6Rvl/Qdkr5T0ndJ+m5J3yPpz0r6XknfJ+n7Jf2ApB+U9EOS/pykH5b0bknvkfQjkn5U0o9J+nFJf17Se9/E9c83/6MRsnbq4coKRsOQFavDaTMzrD2vxsYCYT5yLUYNeCCHZsjjmyUYTxkW4dYWCqxt1hbqus3akKhvoDYX8Zt+DOJzGIQRYg58djtUz8ewempRVqxV4jfRXQHKtuXWU6IuJ5H9Pn8gHI/EZlqonnBcCFIgoAbd1JtFGEA5aQUTCXqz6dPi/1vwGfgK+E/szI2fGhwabm4oEn8IDsRXEH6EgO7FVxF+jPB3mPITD9E+En1rNUqqg59WKgmGsBaANRONSXKyWJMcw5kZzinpEtS0EI+KkSglRsyTGIX5qiDGApGwWRSCgi8meBr0UkFsRggGEwVz8akmx4q+NFGZ5Quu/Jw/bg5FeCGY2LkqvAAvFQjhia7WxH7VbjoWMkeiguiLR0SzLxid8a3oG6UiD8QYjoiJQ2uF7gvPTfn8uBwqrhn9pOgL84nqNWz80TmzDwotEIuv6E8mdj3BC+FYIH7jNBRF44wQmJ6Jn04cy/I4c20uYI4L1+MTQZ84LUz4ff4ZYUJ2mShqvBbg4zOnE0cf6IM4bDBIekbSs6Iebj/RANBQKpX75C5iQilsqYCUnlRAikwyTU0G/YihKcRJIuGvIsYI+n1EEvJn/2ZRCF+4uXW/HNXhxte4PmMVN2b4Ze0nDdy8utFmigUdb5yXf3wzIbp1DQUD4k+xyd8ER4nKC52troHmQdHva1L6vBaQjDYn/hcztkXWbmYZK4haR5utLIws7E6LDYx9bc2kQQAdRhsHa7fZbOiwbbjZNTU94wtDXfnCFDYIfyQEFv2dzX1dHRhUe3NwWgAyNNC8askexO2jzX39vTAZAu4ebWYYuA4ONeOlzdXsE0MCNIWmq3bfSYWjn/5mrU0wZjun1LCd1ZoHY2XZhZaLDUbJGIuLUiG2tUhIKsIr9CtwixjFmVAMS46SjL5YRCqc8034ogFxJ8g+A+IYB/Bh3f2i0k/anjpzq/aWP1VWky6rSRXVpotqP7xzqeTIojtVUr+s0x1vNb2l05W2moAb2ky/xKpIFB244LS3MCFCGJWwKrGoxKoSTiU2JKYDF+hQovTABYujhWux2ogV0+JkQisysSsSC6sSi0qsKuFUAkGVKUGxtCM0NwWZLP355z7788/d/PnnPr+aUNTPP/dVArl2iOBvkYj+lJA/BVefVp1/moAs+LT2AR93QHDn55/7Itp/kfj+MiWLkMp2Kv8y4V8upR7ir/TCzz/87EXKNeLpHhxWZCcpV2cX1dczOKDYdgXi3XOTGdup6SDcypxi2wkNsxUapmLb7fPP4u8+3UIQOj41Ak8kEqSgqcfnYuhoyNXTrtiMyh2DGjhFMazZVlqaePz0Q/5p+VaqkBoTgnDjCBC3nKHAYFhOBzSRllBpgnnYGE7n9EJGtRc6sqoX4vX5W3146FPuGAZWOJI4e6jpof7uwJMpKsL9d0cn7sLedQeAVBAMhIXr4kHgL+KNt1e+8UwlydL2lKkjbepIqh/ia+3Ur+5DL2f9DJ6fj3hBVl9bmOFr5bfBMCAV+OHZKjaYJEMkJhXGbsTiQkjcj6k3BSPTEfEA5kbLklitwl9jhg7LGSoufark5rFU8f508f5k8f77xVs/yf9B2VNlHyf/q7NWrGbt56WYNdSJWNDNA8q/wt8sEI/nVJZhVSazbY0b2ppW2WY9gPJ/r80uPL4g7xGkjxdlbC+bNHerdCfm9XzRVd1Nk6iPl20QV3YqV+lPbDqVeboUC4YSXXxrxn7ewJfm7V7IysV6cSwWP9jNgjHsqtXFd2Tsj+hEa16+ylbla3fG9rJWOqv1NOKZbRGr8p+tW7LpEt66YSvZtqFt+buunYq82jFt6HODvEzrFgqgZg9kXOTEk7djNC/WQmUXx46FwswujnebkpyS2flQJZOlOzKfd9e06y6eWCiaL1gs163xl5PXXfNF/A4cBH5Jx+/+snGjnOt1TzW+L/nc8761gOL5Yn7vVZ14IE5lXK2da75ylX7T/k34WqUVFa/Nst1/90CuPadbKNmwHOoydvFjGT6/YckvlOaU38H5UjJ4r0qscplX0tUPU9LzRmg3v7NQNl+2uEu3xh+ft5/+MegFF7YsbJ0vWNg2b8JeWqyeL1ncvZbfeGNWXrfMb53f9lXo8/9M6/ehbZ2BMKgNwzA/MIzHIYzDEEbVumHQDwzjI/AEJf+5PT20l7JaHaOLma4Z5Hse+059fonXPFTbzva5ag97ju2R9VpOnM0Kf4M2RFpMHeK6IVk3H9K7voOPrvK59jjg2FpDLBgLYAv58033NPXvOp0N+VNmGFFhC6+I29cPgaRRR9JYEXc+0N1h4q7lge6OE3enH+juBHH3yMbuNhoLKGXcCOHsiLs2dqd+YdTSmnF5uUZjWj8JI5nDefXStKpeNojtPIlHHaM0mAcSxuPHjyfKLzAXqbZhV1sv1dnT10ElKi6wF6lh10D7YL8sT5RcoC9SHeM9Hiqxg2rrHhx0d1AuanDIA5O9k1Ri6Do/3RSJCmFK3aJ27dq1zMoD7kyLipGpQFAwR2eijwT40/hTPI070DiLlebsR0OBSeF6HCy8k2O91/oaDGQ1SDLQTMJMDY145JR1jLv6h+AK073mGO/3iXyzMm3EPW5mIe43mxN7M+6HXJ5uZeJ0khJx9JiokG0GBsHJ4MhAOyX+XyjehmXQ3wGz2XaqnmkAM5sxs2i2ZMyWhkSpWgqQ+xqqe3CM6ncNnIcI3e6xweF2N9U+SJ0fHKHGXAMe6hFK/BVG0qysH2TlYyogxuJU0BeLNwKNx1QWizOsJbGNZEUNlEoYILYjWtAdELQbo24bHOzt6XBTJx+h6s83DzScpBoKJP0N8f+ESCXjDSEmGc8LMXl97QgWqz4cWPx9vQ6mh2Uh3/WJaxFxFmbTiUrKM+hx9VGutjYoGg8kT0mwmMLk1yhFKbcJ3ODo9riGPR3tZrNZsVrRz0PVGeSqY3FlzwLEIi+hoP1+ytMN9TI82NbhdlPdLjckHosCQlnZBrPsuC9IDfY2tw2dpFb0zSu7wSk6hKx2DEPqqFZspSvq9k6PLzyH2zunKKy+1jkxJMQofzAShhZRSmEVtvrC00EfL8RmsuRQldmLaBkL60WqJ8wHfFkiGsPwz1IhITyXKKHaZiKRmAAFDFmzQtasSDggHOT7ZzqSbzpxsBQaGNWDiR7o8EAWBwY62vBewd2sDUfIRJbMv6WCQDg6FxcPoYBSJ7GSCe8lyYRbZ6XSWDQYiOOUPSZt74RbaCAS74zMhfkOUYyIkikeCAlSQSwoCFHJhKmUjDDhlwpEyLkgFfqiEBQvGaN+sI6LAi9uwxiMQYiggAQN0+u5yRBcjVNTk5LRFw1IJgBGMkZmoeX4owCToZhkmIRgfFPTGD4vFUyHfIGgZBKug89idU+uVCpc9wvReCASjknlbZFwWPCjgaS1oVzSX5cM13GxFvIhGaYikOL4DAQWxbVnqTgamwgGMCn6gGTwX5e2+EUo+wklfSVxbB4TAT4mmXDjKyQEaEHYB7UOfn2xGIYSw+Fn3mqVvEjwqAr4a0Ps3xXgIsGy4ZK+ZO/S7v039Us7d93a/ZlTnz51v7IqWd2cqqTTlXSykiZGOlXJpCuZZCUDxluzqcrj6crjycrjYPpC0dNFt4ruH6CSh7nUAVv6gO2W4X7l/qdLkjXxVOVcunIuWTm3dKBqcX/ywInUgRP3qbpnip4rWiz6BVWXPDqaosbS1FiSGtPk9481Jpt6UsfOpo+dXTQtGwoON99vYu4duRe7c+nupTeaHn2t6dFUU2u6qfWNpv7XmvpTTYPppsHbhtuGd+4fcyzrjIebM3C/vilpfjRV70rXu5L1rvv1jXdL7zF3tt7densrGO4U3i28Tf6Xi8D1O++886ti3eGjSkIwgbYUZU9T9iRlf6BR8VV3/PapVJ0jXedYNGWkKlmqP75YsGwwHrbet9hemEue9qXsk2n7ZMriT1v8t4tvF7+zbNAfti6xFjSA8Z13VodCIvemqAtp6kKSupCRN5hvX79z6O6hZZ3+8KhexkXXUn3TN7d8fcsLI8kW96uuV30/bgMif1KcJ815UvUj6fqRJPmsE1tfiupPU/1Jqj8jr62/fTBVa0vX2hYNS7V1yYbWZC1+7tef+Gbp10vvWe6U3y2/Df+/yBXcr2u4N5WsO52qO52uO72sKz8s6F8+CHV1p+hu0e2i+1b7d40vtn6n6KWib/V9u+92yS+wFntf7UmZR5Kj3pTZm6q/kK6/kKy/QOp3PFV/Pl1/Pll/XgtiyWpb1hU3CHoZb7cvnXr0b87+1dmXY98ZfGnwWyX3jPc6lloevVe8ZLG/eDJp6YDPkqP9DUfva47en7Ylh9xJz/mkdzLl8Kcd/iT5LHHOF71Jrgs+78ppe/KcJzniTV7wpxx82sEnHfw7y9tJIsuxBORykPEtgm/r8uXrIbSS9ax+RUGLXgymKEuasiQpS261tqaotjTVlqTa5Ab9Quy7lu/GvuN4yfGthW8vpI62v+xOHe3+6c6ful8/5/nx+E/Gf1z1k6rUmvct+j+dos6kqTNJ6sx9qua5kuTxkymqJU21JNXPUtWhxZPJqib4ZPtc1umOuQ1v6XSHPYa3CS4TzLipOXa7LFVjTddYF/VLtUduly4+svgINLQ7BXcLbpP/pbqjt48vTixO3K8/fsd013Sb/GdJ13a7tlRpR/j/i+x+Iif9R54pfK5wkfwvXzHodlE3Ty2HDbpqM9i+86tCXUVlurwmXc4u6wwlezNwv2J3cg+XqrClK2zJCtv9il2fLvxs4U3lf7kAnEB9xp6BfvojrUc9Tt33G6xt1bofVOmB/6C6pf2g8Yf7DMB/eECP/KDLCYYf7TnYadH9iEVHP7KYOp3GH9nbS8Hw9/q2wwPNxp/VbgHDz5pNA5ain1mMyG165PZWGxhSza4KuPzP+h2Iuwk2EDyNmN6+DfEw4U5mxGx8vUkPuPYScqMJl5CnYbqTPVxfNVHKmkRtvGaev9i8oC/JmfDluN14CcQQ3gFTjaylVJhWFMBUxLRgWG8Jc96walmsbcHIFyxmreRnxV/40ZwlrPzX9LTnlUP+YuT8OovB86sWzZ9qj2/Piqf4bsmqRaSCDct/Z8Yuewl4fsNp+0JhTr2Vzhc+aCK/xoLz3vVTNY/le3yhaF4/X4QhLxTPF80X81v4rfy26YKFkvmCxS1rlU98f1YOiudLvgop+DMtFVBaJx56QSY7D6uXmzfIQ47Pig3LZvt6tRDPesnRAxdkyNLruiFVbz6kh8pl9l23etH5cMb2stZO+V1r/ua1eyDRQSZJDMyvBtuz57onnJyT5RrxYnM00k4rbQe022kistvli0O+cCs71Gkazh0xKJg0OtSgM6Gi/lQjxREks/HSbH99Pf09OAF88+NQpOIKpNOfdR/pcHnJAt9fDgP0Qh4+D632Ys2Cfu3fA+OmLKlW97nlMKr7PLS7p2rJL576gTsmsRwnKoX+mUjADxMZWRNOKuQD04F47I5BMphp8R3wGMOGrIzxV0pOTQth4XpUPJPYA5MW86lgxO8Lxs6YNXkzOPslLoD+H/D/YV2ybgQ+L195fuq50Aud3+5PHW1NH22Vpdkf+cfG/wL+3sTGJNZjbAcunLioTFp9fj9MyuIxec7shKnuEbQcEiN+IRajZnwxalIQwvhbthgXeNUVzlvCYQbqVCqd9c2Fp2Hab+WA3/Bdm74RAI4vQ9OJmGqcIJP5uTJBFhm0YQESW5QJcb8HpsN3dsi/h5JZphPBhSVZOuoLzglkJia2klnm5UggLLahgw4EnBiKnerUVOwmbsQwHxL70NyPoE1U75SKk8SBP8IL+JMyztBM4dAkTMvCoahk9Ax7JEM8CDPP2HURG48oAMRKddmzM3liNqBCHbo4acCJ2dLuvTdNME74dNFni24WkQHD46kKX7rCl6zw3d97MFllTe3l0nu5mzBDMm6vu0/VPt+RPD6bOhJMH4GxXihNhW4V3Cp45/7ewzAL2F6XgSXqCNrcKlg2ggkGGr84eHix7gt9T/fB4GR7A4Gb7UvV1Femvzgt1/5PO5LD7h93/6QbeKpuJA1YPZKuHrllXKo8+JWyL5YttqUq69OV9Unyub973+JkcndDandDejcEWLr9zG23NlX8RRX1/M5FzzP7ntv3hUtPX8LZIswwz7wopqpdqcrWdGVrsrKVyLpSld3pyu5kZbfmean2GMzr9p0hcKtt6ejx25ZnZhaNS43NMKQ/++L8q33JE+cXi5eo2q+VPlv6DStIu1PU6TR1Okk+MM8D3+WQJJIuAm8hvK3Lka0FZJC9WvyrPbrte24GUxW16YraZEVtbrWxqQpLusKSrLAQ49HnY9+wfCN2x3HX8czCcwupPdZ77tQex3d3ftf9ys7vjL80/p2ql6pSezpTFV3piq5kRVduaE2pCnO6wpysMN+v2PHZklvmVEVDuqIhqX5iuKvi3kHXVt33tm5xHTR+74Ae8AeG1qKOPcZX9pg69he9UqUHzBm3Yask4zb2g3FbxvzBuO3hx21Na4/b+HK+gt8+XfweRm/m9zR62/GuR28b/pjO73pfRm+7f+Ojt9U/pa89etu75uitckBZHV89eqMZGK0xNvg6xGl8ip9Zbyxm2dSITJzR/wZGZCJ6FWcRIvrcMZd4BUcguyf5NQZbZMwg6tW9Wjh8EnETKBk+iZg0cQ59lwaoYOSqQN2IzEnFAaTAEiVToiDgTySCVIxUZpyTtjihxIChrgywzBBJvIGgjYtEC0IC4cn1Bh+DKuBAKNa+3uDjdKriTLriTLLizPqDjyupI2L6iJiiYmkq9m9v8NH38v5Xe5Pjk0l/KBm+njxx49/MKCS5/3iq4kS64kRS/aw7DCnt2Gd8ZZ+po6roFUoPmDMMwU6PDEO6PxiGZMwfDEMefhji2GgYwu/gd/K7+N34TkS+Et95iG81nN75HgYnzvc0OKl614OTDfdl8Yfel8EJ9RsfnBze5OBk1Z4pMjipHUgcX2dw4rTY7Y0ATgQrgjxISdgfPEj5bRqd7PFNTa8xPAlubngiFfrIdgGpTL7KazQlmkEqtNG0HUYkij3ZViCVKvYMy0qFUGDwkQphXEeGLji+wwKVCp007UTJrG9yLoiBlWYikUpUqRUcgBC/UtGsEm3prJoYmyy0O2zvaSw0pAIu7cQ+u95YqCNV0Zmu6ExWdK4/FrqcOjKbPjKbooJpKvhvbyzU/eLFV1uSYxPJx2EslFiGXlPfjr/odRj68TJgGMfLeYMPL5OGIF5Chht4SRg6jHDpNA7h5ZzRi5cLxmm8zBiv4KVRNH4wtlo9ttrdccT4yhFTR33RKyf0gGv/NHf8g7FVxvzB2Orhx1YNa42tpk3vYfR0/D2NnlZriWx29LShBglf8b6Mnrb/xkdPq5e+1h49rVroIqOnXQMJar3RE3P8+PFGIe4nYybxYwj/Qsc/gfBayzOf2Nz4R3wKB0ElMxDIHA5t3tMY45wKH0YXzvXGGC2pilPpilPJilMfrLes+2PPE8kTvR8MBFYPBAo7dhtf2W3q2Ff0ykE9YM5AALtoMhBoLXm3Gqyrupush+IaaqElG/jMfhjnDQ4WNvaZHedqddLNxrlanXSzca5SMN10nEX5w56NfOYqjuaEU7zhUMBIBlPbMu6VwVTJgjFnMLXZ/JauejyU8VumDQum7IFOvvoZOSxnCoY6WQ/Ay6Waa1P+8IUvmy+8Ch0uv3UxK6dZqdgGA7jsgVX5Qw3girKVVnApKE8JN6uks/KkW9y2ljw3pnn9Zlzhg1weOs0bMvt2lHdo7CRcT/iutR754T9ct1x255XLnn9L5ZKX+ryDTtZWyMxTra54sJuF4pv6p2Zy1DYr7+apdRK1zfVUMze+X0s33cPul9U2N1KA4w88TO80XwzD+p9toLCZN4TUFDa3rq0cmT+U5A9mKmhhW4lu0/6qsvyVk/4sS/1T6c+qF8qz+7P5bZtpbwsV8+Wbcrd9vmKeDOHnK5R2qJoOKVdKuR6Wr8BqFEmtcj2C1+mShR3zJYt7V0WoW6VMumPVBOkfHnqClN0W6h7qSZXtc0MlS/7Y+6JKWv9rUyXd7PO4YZXPtcdEx9ecIJ0YSGwTQ1STOEWZRYG8qV59WwklXPeFokHhJBWam/GFQj6+kfIFA41UzHf5MhqmfIGEL6y+X2c7NTQXV1TiUKvnJJVoWBUSrnNCKDNqYOpOukQF8Y0KdKrneqpD9fUoUVdCTUSqkXr0hm8mEiEGojJoTpRQfATflg+etsjB4H42ZTk7sYPqEuJxfDkNCSUGPsRGnMZY/0VO9irlvK6e7r0Itr9s1mlbH82X8DN07htX7y58d/Sli6nm3nRzryLO+pDZ4ZuYtESRUsWS3icexxhRM1D87781RfDX6OR5dcb7JsZL9EIz017Ugsze0ZnRgsw066xXO43EBMoVEKNBX1jAMysEaioiUrGoIPCKaxEzRLRMJVMvrt8bce2+QP4RwUR+HjCRFX4jLt/jC+/I/Dqxn/LMCFQ0awMpNFhozHGBF2l12p3YTQ2JaC+E44JIxSPUJGorkol4w4E8vcKM3mFmW6j4BALuByX7bUXyk8g8wkk96ideEwNx3N8ZuSaIYgvKT+lXbxjtQreFoqxPWNoT5oXr8kZT3EQq4tkTmT2kDTulAnKPSya8WaVC+dYTP6yX300Ui8fEceRFQWXvrwkrU/SizOR19QxIBUQTkGxAlbeW8mhXSkKdwJtfKsGgZWqYikmGYEzefrpTt0o5MLM0MazCV9DpbRN5i1D+1DN3jupOVXjSFZ5khScjx8k8k6pk05XszYJc512piu50RXeyojsjx+WN5tReOr2Xzl8EeTRV4UpXuJIVrox8X/WtJ1L7TqT3nbhZqEnlVZHqw8/X3d6WqrGna+ypake62rHpRZGcaDOZXdp38Jb7VglkY/+hxYIvND7duKwr3t6pf4vgzdb7NfXPNd0rSNXY0jW2W0VLB6oXj906c+vM0rGGr1179prcfbyOKl+PpUYupkcugjFlvpQGPHYpfewSKggeWTx/OyYrZ71BOV+jnC/W/c2JvzrxnaaXml41/UPp35X+eMtPtqROepIj51Mnzye9j6dOPp708amTfFK4nDp5OTkbTp0MJyOx1MlYMn49dfJ6irqRpm4kyeef/mWk5H7V4cWG2+5UFZOuYt6osr1WZUtVOdJVjjeq2l6raktVdaSrOm4ZvmDIX02q2P7IbQ+ud7XdNjzT9VzXM1ue23KrIKN2io2t5cWOVatJl1KVE+nKiWTlRGY16cjRZV3pvkcI3GpfaqS/efbrZ+/F7gzeHXymZNG42LHUxH7zsa8/9mJtqulMuunMi1fSTa7FUlTWbFmyOv+y7y/6Xt6ZsnakrR0v+9LW7tslt0veuX+MQS3LlgwsWU+ize0SaF2HW6B1/VNd8xt13Gt1XKrOnq6zLxqW6sxfm3h2IlVnS9eh5mSj+bZ4p+NezT33t46+uONbDS+2vjj3ne6Xh18t+p43OTScdJ9PDUF5P5a8OJF8fCp1cSo5HUhejqSmI8momIxdS0WvJU9cx5WwI18re7bsG+33dt4b1xTx4LO8G/O9FQqTlCiBtxDe1uXI1gKyErZa/Kuaf0krYWehX/vBjoNtzbofNG9pO2P8wWk94N81tG4fPGz8ScuB/r2mn+7RA//p3i39R4t+WmtAXqdHftRlBsM/HDYN1hX9Q70e0J/1M4AOR5FkvYzfJr8WLZ5lmXmGLxp0a/zx+uy3vX1Jz+es9cRLMzz3aQ8ujV8uWDUuXTvmNX/qWjXH06/901X+2hlfkDXnMpZs3l9hlj+T/GqreeOCKfNqq3lDu+5m4cXgQsF8wdqvMuOL5o2LJWvZ5K1e5M7v1w6reN64KXcl86b3Lc7SedOm3JXN6zflbguU/kOnbaGQ37pQtM4r3bbx5bmuv4Q/dK3tdjvM+/Pd7tx8uF8uWCjOXplZx+cufveG75gtyf75kN+T1cpKc2z2ZtmU5dhUZtlsybHZl2WzNftnvYVtOe72Z69D5NgcyLKpyLHJXvPYnmOTvaqxI8emOstmZ47NoSybXTy1sJs/vLCHr1nYy9cuVOaUrLbaxR/h66bzf5zft7bbaZjr5x8jvLB/XbfHVrk9wNdvoq63b3xINVkPqCDrAeuFpa3T8cf5Ew8Ka1Mpanxgipo2GZaZb35gWDT52fxgTgjaum3e2lNVzroms5j1UsfM33zV4s615PH6rBi02Hj2rmWjNObVanVOrpuyQtTWsTZcVz70Hv1T79H/YegJa963UqzUQrE+VCnW8tx8LTlk3rhwBO4e+7P6hbq17635vLW6haPrpZh3fFQXt2SZnQ+14n9s/uj8MdIW6wM6/iTf8sd6/hR/GvAM/wjgo7wLsJVvA2znOwA7+S7Abr4H8CzfC9jH9wMO8IOAQ/w5wGHeDejhRwBH+THAcf48oJe4pPgL/GP8xaeNz+sXGiDWS++tdiHECf5xQN97DmdyHtE/XwjI8xSgwDOAU/w04AyRBN5zLJd5P+AsHwQM8WHACB8FvELCFwnG+MOAcX6Ov8pfmy/irz9dAKV1gL+xcJxPLJyIc1nxaq8dnT8ed2Sl7WSG330idy15MWvDSeYvr99p5Ofn8dVtf5X9Cjh+Qfk15kmyqk02FvEfWmvdlf/wOi32dz6qm2/kP5Ipxge00absl7nxv8t/NG/MtOaIe17H/15WCuXUkh6c//01V4mz4/jYu4pj7XCzxvaLh9cOJd+PXhe+P38iu53NN+a6gVo5yX88nnUkMUiac+rpD1bXU3488yceIkWfvVnw1D/yn4Ca+8NMwvinMhxS8OFVaerJSdMnN9t2cmrjU+9fbUA+6F9j2IabhU+Fs2d6fCE5qNmovNiwO2NzRCeWLZjxVYQL5ifN8ssPkWUOfW74o4GV3Vu3qoutF9S3yl+kVrbMK9LB3pNNK8WUusRKVqG1dVbx22QpsROXA8UXyLJhH640mgZwPdCEq4IrTRaOtjk4zsLYWce8jZ1y+AXnlN06yQC1+hnW4vezFqvF7rP6LOybEQz2/wZYKSAnN4jLKHgL4TWAN/929iuFb/6PH3+xRTTiIqIJoQChEKEIoRihBKEUoQxhCwJ5Lx95d5yps9XqErEiyIkgI27x/wV+55BU1DbUzTjtToU4LCqxE8LSNKcSp0IYVcKpEhujEtXKplrZVSu7RSVqyE7Vyqn6ciq+GItdJarEqrhh1LgYhyKBBKlEyYVDkQCxqIRTieqGtSvEohJO9cVZGkySyRsJT0tFI+FAMBCelcr6fWJsJuQLBiPXVrbi6RizkRDVNhMI+1Yq5MM4sIjlQzje7Mfq+09YfQwCromvFMqncbz5t5+4o3vzyt8/a/pf/wQmoPle7Q7SChib2WaXPVhojnU6GFveaRl4gsrqwzJYB72gHfMx4pbP9ej3DFADXfJRHj3hqUA4cF0+ziNjyD/SQz5yWz7UQ3E1Mc6xjHy0h81MP/Bsj4vHGo/JmVPOJ3GTH8xc0aicUcZKcsoxZhsrpzjAT/S0K0eW0A4rZ6Pl5ENhQ1nHhKCcg5gvFJsLT8s5yBggoe7+prMWlu6UE8mZGfNDnD2Ch/tyNKOUqcXOqWXqYFgs0onOMchuJleZKrPSnHzmisVsZ5X0c3i0JcuxedFYtEpjaIdWayzD2ZRaC8QnejzK4Swcx9hQt0MuhU6X2zPW0SqXweDQ0KBcAArbqP6UO1M5lYXNrzmbtemqw3dyzazZ7XLOaLPNprZG2mK1Wa2ryk89usWayZeDs65ujB3xQMwX9MW1FunpaBtQMqPSjXJD3DSNWd5NS8xkjKFtcs7gPnOodeakrQxpdA+uMsbJ0mtVmRYE5HQoEosL8plRck59sbmYnFGFbZRPl3vEPeGlGVu72pxzc3rdYTuZldu1q09rmDannEnWyVhZJ21/19V31pdIyLk5p2UNMpQxbJQnxRUVsFH9Ankh60DHe6vHf8X3HvRHJGtW6MgY5VnA4sHanJVmNnl0kk2tQV6YaO+Q88Y6LDaGYUiLgLxF2CZe2LBn3Sh/0OW6rKytdb0jnzbKIGuxkAxabJkMMjYbQ1udXH7/svbTzmLVWmhsos8l54+x2Rkaz35XOm1WeQhGrqL2nChnNRSJR8RI0CfnNcu0UWbRGTVdb2ugokHfDTnL5CH2EE23X4jFhPC0IPYF4kLWIx+eVQ5oxbY1khAKyk7lbPaPK00BugZsozblIdnR19bRt4knZJfTTo8oz3GGzq+o8FwwuLn7hsYOcM1qtctdq9WKJxYqiWU5hnVaHPn9znr3pMW5ul7p1RntHnGNdfTI+dT4RjU4NOhp6hu3ZOV+7dZKtt68iSuid/SSfvZN3Lu3YrhQs2KouXjHKBlYB3ydkpFl6LV3p+C0RNudUrWZ3Slr7kmp1vak3DFm7aII69fXx5iamlxjd4rRgK+O1GkbdI70w+fFK8+PPnfxBVuq7mS67qQsy/7IO1nIpKHENxefiYhQZyvbQjnvX5cKfX58MfPKx/AQvuaZeCjY6ItGgwG/D9/P3HwdJSeu50tDwZYrp2mzszEQ8k0Lzb6rgSmFXhMmo6o0Gp5uPN58nDh15AQQC0yHBb5JuO6fwddRt1w9PWkhzuwr5XKCmoJgMQfBrOwXwk1drY2A8BSTYxXCcpgrW8l5gU3+SDgOPcBKSch3vQn8nKYlIx8VVwpYGJ7C3EEUpgQ8/jCtvoY+txCaw/HmmF8UhHDzI1GfCLfc6Tp7ax3LRmd8MQGudRYX4FwYi1EIxzEXAo9ytg0QxglRzVEAU6JZBWITQjAwHZgMChNTEXECshsMYgcSkz3ExTmhzt5+NOqDm6iO7QzHASBH/tloJEAMDhb+GdpCO1m7k7OBZEYIRidCEd4XPIoHoAkrB2KCv8k/0xQl2YxBaQQjYlMMggmRN7DBTblSoriZ863U1wxE4k0ucyuewVcDRV/jdNY0UjXkZM7AXIiIGNZaowU852uagp6lSTlzsYkcCGlfIxjSc9BrBQZym4W1myHUikyoITKgWDE8wqyUZ0t5IbhSWgPd3YDdTnfWrOzIWELfHYeSDK2U1Cgzk5qV/aut1bSuFNcw5DlVs7INXU0JcXDIC/hWcT7inwtBdWbbYNxScRga9DQWbZYN9HjCShn0x0IT3EnTgXC2Jb52fCWy0ZG2eEZp78OekioXHPxTax1eKhmdDrrBuLJvLjot+nihKRCGFM2JQpP62vWVUkwY3hGYy6sB4Vo0IsabSJ8tmXx8gJcKsbR8ccl0ORYJSyW8cDXgFybI0aPkRe7k/enXIiIv7cPeSIRSmYAOOXgD7oLYhD/oC4Ri0ha4iUJzYehf0KfRHw3iO+XnBKkoLt6YCM+FpIopXygQvDGRCb8Cbjgebybo6ibiN6L4KsfInOgnm8qgeKXtAu4UAx9xSIfsYtfkXDweCU9cC8RnJniYicB9xUvbhDDc/MGJEAjgBpUKpiBIQarU0huDpza0hQk/3O8BISbt1GxC0H0EwiQ9+6HkREgPJBLinxb4iUB4AosPyyIan2gdlgzw3ZLdB0jUgxaI7hRIhaQ7F6Sd/mAAPE6Q3YNQLOQFiZVTk3ja5QTU2MSUCPY8xE+2pxWheFa4ATH6caffRDwyK4RXjqld2GQTVHp0Jrcjw8Q1k+Jb6e3DCwW9rhi5CgVC+USBioTNVMf1qOCPU74w5e53UzF4LkCeKSxSykdhonC3IGScbFiEsKhA+I5BMvHwIJaKZgRoaGJMKlPLFFK4UqksyrFZi3JNg70XqRUjNU+Ju3H9RN+y9qP2TPajtnJBP6/ndVnLqXpZxYE3ZGSJzAN2H2906+6YxL8lMZyWCq7iqywHyCmAdwxiFJ+rlx7mQVuLD1pr5kFrj+JnZPRF/YtHXyp5ufY7W1/2vVr0w8spx5Bil/UhD1ypPK+1JQ6oR5JoRSOfy4HbZcWvYYrIhlncK7uyd5XbwV7iDo/nwHKmlINFM+XMdkI5V+SfqwK3LzkGoigEqcGnqFpHTHYdtQ2B39Vxtg1hnA11kjF2A09ZjPORubh4Ty+fshiJyns7+8hi6lRwLjYj7/OExyx0v35B/JZe3TVaoVe2g0qF8p0PoQVCcLuRkZBUgs8O5UCKYXIyLNliKhXJGzxjYoi4mhGuy293lUxzc3g7IlrlcRTZoeohSYvCjF08Z0CKzVSkDerWVtyyKr/QtF2v7DaVSjrUEykamjObRcluUMkwFZYMQfhGr0lG6ADle1BQ7kE8QdhHThOevLrWsi45Z1jceHEX3UxdQxRJSD4SahSihPChA4Xu+VpgKiAZ5nxSmXxoLnRjAi+aMVMMZrJQ7uyhByddq1Qm9xMeTKK8UbYMyxp7MGjkkJ+AZAwGWMlwmZGKLvsSEXhCiMMYknFODErG+LUpyHAE39w6G5D0QqxZt+ae2I3+5DusR4UlvPf8JfKBGn59ye5fVOz8bOkbFdRrFVSygnr9oi9JPq9PCq9PBVKTl9OTl5Py5/BsqiKYrggmK4Kvh6Lp0LU3QguvhRZSoQ+lQx9Khj60tHv/5y985sLiztTuuvTuukVfenf9TQPud6WWqmq+cuGLF27vTFU1pauabvvSVfQtwy0Dnh+BtofQAMZ33lnaX7OsG9dvZ94ieLMV9X0vf/Hy7b33dvxl5V9Ufmv/t/enqk+lq0+9Ud3+WnX7y2OvDqeqh9LVQ29Uj79WPZ48P5F8fPKNx2dee3wm9fjl9OOXU9Wz6erZN6pjr1XHkvFE8omFVPWT6eon/6tOd6jL8J8JLut03YYBvAwaPPhq/0Mj+Gp/QHR1kbi6iNaXDDxeBMNltBEMUbTCy1t4EdETXjCEGAkhZrhlXDo2emsL7r8139t5z52qcaZrnMlDV+DzSuEPt70qJoc9qUdH0o+OyMLXxy+lx6eS02ST6ngkPR6R5bdM9w/VPG977sy9hhd7UrWd6drO1KGu9KEusDhOJ5nW9PG2W+X3qaOL154rv1WQIYfqFqeefhK91xHQTJsnS4dqNKhDsIJlVe3TF2933etKnjiVqjqdrjp9y3C/+sjTISigJr4gG7E8hIK3Cd4yQqhPLySbLsqf1KFL6UOXIMxq+oWdL4x++9LLrS+LKe5smjubYnrTTG+quvfVrlS1+3XPGCmamWQAiiaUGg+nx8MpTyTtiaSqI69HY6/HExDFnL4Nq6jd0ImXLsNZrI05fa/hbfkCpiv6PjThBVPWJ7/nZZQYRg2/0unGDF68XDD40N0FQwBdXIaKXcYn1xPo8IJhXrabR9OYYQFNeMFAFtDhk4bRBhJiA5TL0cbnQs9EnovcKoNKXGS/Zn/WfrvljRNnXjtx5rtX048MJt0jyRNnUidG0ydGU7Vj6dqx1KHx9KFxKOYjx75hult6Z8vdLakjXPoId6vk/uEjz3ue8z7z2HOPpQ6z6cPsrcI1REtHRyC2g4cWDV8rerbodtkb9S2v1bd8t/Ol/leHk/UtqfqhdP1QijqXps6lDg6nDw7fMiwdZW6zi7P4f6tsqcqcJB+lWm+3pqqb09XN0KCrDn1l7Itj8qT2lY5XD3+v+4fdQFNH+tOAVf3pqn4IrKZucfKZo7eKlg17ag1LpvLk9sPLRqD/ZNoCxVM+blguANNyoa5gT3KvZbkIDcW6gl03LyyXIN+iKyj9uH15K/JtuoJt4KliyrhcjuYKXUHNon15O/IduoKK5PaW5Z1o2AUWydrHlnejYY+uYO8t0/Je5JUQzc355X3I9+sK9t06sXwA+UFdweHF48tVyKt1BbtvXl4+hJyS+WHkNchDy7XIjyDnl+uQH9XV1C0bdDvbDUt7DiyfQJFOBci3WUf5SxYLn499w3r35J1Td0+ljjnSeO4Pyl+sfPmozF498PrI+OvnL6bP+1PnhfR5ITUylR6Zki2T0+FkRFR4bAHIh/StBtkM2Ga4hIYJw2RG5jdcQYNoiGdkc4YEGp4wuIyarNXYi4Y+42BGNmScNELL9xun8DJtnDW+jZcrxrfwEpNNMTT5jXE04SUTi7ELT3rvNg2bNJnbdAENj5n8GRlvuoaG66aBAk02WDCBhscLpjOymYLWQsxkYWehJusqfAwNFwsfz8h8hQtoeLLQVaTJ+orcaJgtiuClt/h8MUZc3Il2oyWTJZpDDW+Z/qm6C1p3dQL6qKo66NwsL7S/sitZ1Zmq6kxXdb5R1ftaVa/WvA/U325NHjDDh5zs0/+qP2U+lxweS5nHkuMXUuYLycdmUuaZVH0gXR9I1geWmtlvXv/6dWVwilvkw2lvBHjKHk0DNkfTzdHbpl/UNyabzr5qSdUPpusH36gfea1+JDl6Pum9mBq9mLzkS436kv6Z1OhM8nI4NUp0GEZjqfp4uj6erI/fR9+dL4OgN13f+0b9udfqIU0YQGqYhDEMYUymhidT9f50vT9Z7887AGmpvul2wVIVpWox3Lp069LSCfMLtbdP3j55n+aSNhKYDQKbSNngYetP2fwpmk/TfJLml2jLX5b+RemLlm+Vf7v8XvkSzd0reKtI12iDG7uavsfem/52y4s30paeZBV+Hhhwko+mbNEUfSVNX0nSV+7T1iQ38GosRbvTtPsN+vxrNGYKS8XrS04KKa+QnLqc8l5O0bNpejZJz5IU/KpQx3DvxuNbhboG5n7Frpu+TxfdNOH/O/fLK5d1MG7KwBLYm9T/d1AHwQhSPBXnBAzXPuKyPbZf9z3ngdbduu/v0gP//m5T6wHj9/edfwQM/7i/9LFm4z8eLwBs+G8i7qAWcTuOiHs1RXwBhoga7SIqAIu4907ERVQR92GKuHVJxL2AIi6nirhLT9yDgLu8RNwCKOIcTcTNuSLuwBJx27CIhyiL5GSEQwgUAu6xEfEcSxF1xkV8W4eIeq7iUQTUchVxe6HYgHAcAfMm4gKoiPvLRDymQcThqYgKwiL+Si+iaq2IU0oR528i7gdLVHR5muwcR1McEAdNc6IN7fCAURE3hol4hKiI28JEPCRUPIWAx4CKOC0VcaeO+CgC7pAR8RROsQ0Bt/SIHQidCF0IuGYs9iCgzoXYi9CHQHYTDCAMIgwhnENAHUjRjeBBGEEYRRhDGEc4j+BFuIDwGMJFhEsIEwiPI/gQJhHwlSYijyAgTCFMI8wgBBAuI8wiBBFCCGEEspklinAFQUSIIcTVwuxxsDYHuXJQmHNodxXhGsJ1hBsIOEUXn0CYR1hAeBLhQwgfRvgdhI8g/C7CRxF+D+H3ET6G8HGEP0D4BMIfYiKKMXIn46Q1xopPoe0nET6F8EcZdxaaTpSorEejTI94E11+GuEzGeccTYt/jLLPInwO4U8QPo9wC+ELCF9E+BLC0whfRvh3aigDdgZC+QrKFhGeQXgW4U8RnkN4HgF3+IlfQ7iNcAfh6wi47U+8i/ANhD9H+CbCPYRvIfwFwr9XoxziGIYWv50xsmB8AZ38Twh/ifAiwncQ/grhrxFeQvguwn9A+BuElxG+h/B9hB/ocDbudvW7Rwa6JFNf/3mrVIhoH5UK+/tbWWevcu0H+fA4y7YpV3A90N/JSoWItvFEkXxtAcFwu5PuBwG5tiSK3UPdTX12lpYKe/r77NZevPbbbe1Swdn2cxanVHjW7Wa4s3D1DnJgbeod9EAyEJ3diTK8uvubPBYGQuj1jDisQxBmf5MLqrMzUaKyEU3YTVgXZ2E7ZeZEhzJjNWYBViQzThFxiiXZpkJCJmxAE3ZrrF+25hjN2k4zsu8BiMRNgvYwDCMT1kKrRJNwCnEoVhbVsYVRrDhWJaovTvXFcSqxKVZ2WpE4NMLSayt0ffsDha6N/G1WoeuzHyh0faDQ9YFCl2Lzr0aha1239avcHlzXbcMqt1Xruj2+ym31Q7g9tK7bE6vcUuu6bVzl9jDftCk1MvP7ptjWzNPvi2Ib88AUsZsMy8JbHxgWR5SJajal2Fabo5JlW0clq/ahFNvsdx0PoZJ15D0qltW9R/9H36P/Y/BEqH/fSjGj2OZ8qFJsQMWxacPCcf7UfAM8S05/2bhwAu6iM8/qFxrXUXDLU2hZaFov5fwjeQpujz6Ugpt5vmneTNpkc0DHu96z8paiCveew+kgqmadRNWsi6h8dfM2wB7+LGAvkfS951j6+c51VPMw/BGCo0TVbAxV9HjvfBF/gaia0VBaj/EXweYSPwH4OO9DBTmiusbzQpZSXICotM0CBvkQYJiPAEb5K0SZLSarsQFe5a8BXudvACb4JwDnicsFnuKf5D/Ef/hpE8TL8L+zwPIfWbCso+LGztPzzN3fzVNny3rCZ/7yehsr/9F561Wd6I+3ZNzwv6eoJP1+lnrPx9ZUSTqd5evj/B9sUm3oE1nh/uEDFcQOrR3KmgpilhwFMesaCmJPxR/NuCAKYtk5/+TqnK9SELM8RIo+e7PwKRP/qXkr/0dZOxpu5imI5aepJydNn35XtfGZ9682iILYry9sVBD7kw0UxLKU54iCGEcUxLgnOUVBDFiWgtgfD4jfw9+ev4/wA4Q1FMDEHyKg+pf4CsKPEHAHifgqwo8RUKNL/Dtkufpc4t+j7CcI70GfS/wpMiw28WfIiDKXM1HcT7VG4hRnVZmNlgz9DHwtkrHfEksU9XMUbjwGYqMGIvj+rX7fdMCfKOn3BUK+8DTFJXb3++ICxdDEIdU+5wtS7p7+xHYiZmlqnKonak8NiUIickAYrRxrgzgFPuCLUeMJU38PxSYKAC1jIA5QVqrP00EE1gCx5YiBG4dLgHIxK4Vw6fddXymWrxQrswAwqaQ/EBRi8UhYkIr6A6LPHxQS5f0R3HhH1bujYiAcb4A0RMIJX6KsP4IbMqih4FwM0ocbttsSFeTawVL11i5MSENiqyyxUEP49jEoDWK0JrYoRPaviDlVzGUH25XYJl8pNsxTXUKYxI3moaDvhuK3ywLFKRPKMydOQiB8ABOo2qtRdilhFyummJJEYNlp6bIpsY8r4Y6rsVP1Ls9RT4Ni7U0c6J8LxgNRH0+x1EgwLvqgJiOUw0xTlq7ETmI5NANFSlksHI12OUIrbbWuEnIcDcKRQUUYJUK7jSbeoX2Ns1AL4xYHjZy787VEIWPBY4oTZa1BfHWce8Ynzia2ZhmgkeQYLYltOUZ3rrU1sT3HSALPccHluuCIi4psUbcQjEimtsDVQKIQEdpXYXckPB0KJErkK8W4E8UKZRNlKsNyyxisXZpzoOUKxTuKYjztpM23Rq5DiqHxUm2+sB/SUYS0jXJCQ5EJSV2xYhAShYQ5E3vg2ueLCSLaXxb88YhIMRwt3sWNO98w4CKtcpdYSJj9rnFWJr7rFhIK3Dfin6PDEvUmcifU+8lCoieM4ro0sVUTd0aCfKK0X80NDfeaxuXOY1uWALOQccyQGAlnM9SSoQ4SDaHYI2gGDEZ1BFEWK5Qj2RkMC8QSrlQbQzwhVW7GADXk44mPIWztGrNozAo3k8LUu0w24p2tMJKC8mwTlk6RLLCqhJMJ3uDYcY33QVMPEKFnlLK6MGmEkNAUaZtKelTiVsm4QoYYhZxjsDCBuOMB/ywmW+WUtRet5OqBXJb3e2x2GwfdjVsQcZNgmVwDrFyUmAsboVuGIv6IfK92QjTnAmGKiZ1IFCCBOiIXuSEOCzy2fkZj7EqRzDRiUYlVJZxKbAmF2FXiUIlTDdGlhe1iNQatQ2a9Flqj1gzlMtRGJ0plGobMJrbIXM54Yn+2ic42MImt2UY2sS3H6Mm1tiS2ZxvllpEdFbuSbbLkmKw5Jm6lItu0KiRbjsmeyHZtl/uuLIlD7u+yJZ6cAJyJ8mwTNuCKHAH635kvQWe7VgmhL8mJyunONXpyg/bkRzYkBkI5NQR39dZskydRljHasw2ObG+OHHdOtSngLa9SMbKitCU3qza5cVV0nlnZqjLSe2kWWgs8bxG/g13rX5GuVWnobvGvs4xwa6tsXHwJLNRqlh/bapicS/wu+irNpFj8Dxj036A0u/wgmJfR4nv5Fpwrp4Y4l1yS4vfR9Q8QfojwCqahcFi4DkM8+QqP3YLhmRshAYz9TRyM/EzDc5M37ljFn5AkjUJnrYwRthHuaZJVAmA0RMyj0I8kImEYSo0yUPuScZSF2w1A9baFcGXABYGweYGw2YEYRi3w5SAULgYEOoVROykryTTqoB0gckrFo76gEPYHfInCUV6IQHdUMSpM+6geMYKd0ligMwDeApMCdAIQu0xIuSR2qyYMMjNILSTiceXqleCKO6kT2+UrPPI0p6WjkWCc6nPbrZjLYXngzMFoYHScwwP1jOdZRjIB9CF1JErOW6h6lmYcDYni8xaLrWmEZhM7znNaiMTW3pAoAFlPT2LPeU6uOgo9aa4gMA7D5SBcQK4PArapAe8AmhMcyMrP25RwZAEEYOMQbAhOADsD4CBgSWw5H4n7KHnAxiYKzw81dfUwdxoT5UPnLK1mxkk7aMZMY9KHzjEuM+NgWFShpVmzi5G2kl8ox8dHrO3uVpdmdHPt7s6MrdvR7mmzodHpGHGfG2FcnrYRNDo49Gtv95xlpa0DToetFYxMq+esVdrq4lhia3GNdFmlLR6nnUZT60iPXdra6WRUt72d6NUux9Ph6bViwHYO47F2eLogFS47o4Tk6XFASFBZckguR2LH4FC/zczYGZpxmmkLbe5liIwlMtYGGbWZYQixw4OZZy00QzLPmOEpVO4mMkYpEAjM3U4EtIOxQ2B2KKHEjuEhlIE/4siKsvLckrRJhQPOTtbeBxZDw6jXSdsY2kwzDBGwKHDKLhPl5zA4xsnI6bBA+O1y+IoAEqv8PD4CwbZ32CzdcLV2sraz8g/j9nbFPC7+KdnTfXZs2Gbrk39jd3QpV3Dc395KO/phsNvXa+e6lWunVNA93OOwKMY2qbBjqIOztmZagqVtuKs7U/W2do+LufNoonQwGg+E4NYbnUsUD3qaUOG6HcYa6rQRBneSYQi62CFWGTRWDFnIaJGq7wpGJn1B6GeGLFaaThQNcRx53BQO2cm1aMihTFKHnDLZMuTzB6YCfujk6ECidEjwiUHKweDeDGjpQphMEwtIo4dL4LoQBL94wUGgTGCoZgIGo/wh0cf7KIsZOsghUbCgIBCCqVW3PbH93ByMmzpGB6mOsCBO34ABYgmIwvG5EAwii4fBo4jj/TKZtUEtCfhg8AXxNiePCGo44BcyzxPyFCFPDPFHCH+LgM+IzHNBfhBk+nfs2sVXEX6M8HcIf4/wE1K/bitHs/3ylSNXO5pNbg6eACa3jbEhQvdf4hbCMaIsmSh2d3U3dbAwkiKsh7Pa5Q0JVgc2AXcUJ2Zl7jjkCXvISCxR6oZZR4hychYaooiLgi+U2OuO3whGcLSIfW5W11+MFiCCp6+nv8lqsdsTWz0R0T8DZUU5oZ7Ef9DrUMvmPxG9BdQxFt/CZYv/jPBLhLcR8IUp4q+Q/ReE/4rwDsL/g7BCAJ38N2T/HeH/A1gxdnmaVoyQHfF/oEyHZaU3rPfe+PddM1csxAjXOx02GlhDSSiKPooQyOloxciIWkYzAq0qaIgsggXBisAh2BDsCA4EPOZMPInQgnAK4TTCGYRHEB5FcCG0IrQh4Gn0YgdCJ0IXQjdCCUIpQhnCFoStCNsQyhEqELYj7EDYiUORw+voxSIJQeuKNYu70PFuhD0IexEqEfYh7Ec4gHAQoQqhGuEQAoVwGKEGAZWsxCMIdQhHEY4h1GNafvREzWzNyRpRuNoIzwEba8c3lrTIOnSN8qss/BFUWmtsHTrZ3tHpGunztEyKMEmfaYyLc+HZFj4qNjItU4IvPicKscaWuUY8VRceknarw2K10HRLTWOND+Jg7CyMtDiHxQaCeM1JC8NZbHiOcU0YbOOzI5cFerwP7K6CkbUxFqDRmpPWxhqx5mQmcY01EbCfYcH2BpBrk8F4zYLYgDk6bsA7J3E4Joio/dR0LSLOCmKTol+KurRRUQhGfLx4Ap03IjQhDCAMIgwhuBE8CCOkHrDdXUKWqz9G1MTECbR4HMGHMIngR+ABGmpFAfkUAqp0idOkHSEjr+KfIS0KWQDZGrpc4mW0mEUg+uxBZCEEcj5AmBiRRZCRu+UKQq6+lihqd8t6OlpiHBNsy9POEufQz1WEawjXEW4gJBCeQFhrcXae3LYbrtAuoJMnET6E8GGE38F+u1h9x4RkDIWiCCHJNAl/UkEoRAyI4kfQbVFYiGM9ix9F77+n9Q6kT/h9hI8hfByBqGkZYiHxD9D0CYQ/RHgK4ZMIqM9GtLTETyH8EcJNhM8AxGy6h1bRytHUOqsC9jexNxVNrel/oZpajxFNrcc+0NT67dPUwvMgoICY6JZshPKovbLlbYK3ijV1rtHabMRCG6t9m+Ato+bofGk2oiNv6dsEFZ0vsDCPlmUjOKLGyt4mCOmkjj63FSyar27JRnB0+BqmCZAUkhzS3JZsxJCuoiNACGlTemhYBEn6ovxJ1VxK11y6VbRU1fyC8YXObw+8zL48mbL2pK09Kfpsmj6bqjr7qj1VNfy6e/T1sYvpsenkTCB5OZgaC6XHQil3OO0Op6rCr0fE12M3IIq4rKbTZujAS6ehB9taXH/W8LZ8AVNU1kqLylpp1b3osN8wQgwjqIA2ajiPF6/hcXTnNcygi4Cq3pNAh17DE7Id0UoblbXSRmWttOp5dLhgGGkgIf4W6aEdPLzI3Trz61NI+0Ax67dLMWvZsDejQrg3R4Vwb7YK4d4sFcK9WSqEexUVwmQ5u1y+N0t/cG+2/uDebP3B/7+9b49tKkvzvC/73jgvSEIcAontEIIDJMR2nryKPAkkBEjIg0BIOb7OA5I4+BFCyqZNdWY6VZPRpHZqNZnVdotp9WgoiZYYaUZitKMVNdPToqTq1b3WZezyLBKabf5Y7T9mVastjbTSnu9cP64dOyRFVXXXbtlX33e+e96P+zq/75xPq1g/qFWsH9Qq1g9qFesHtYr1g1rF+kGtYv2gVrF+UIvXDx520iFDZWINYQ2cJmIEDdU6QtdNJi9Ke9zxVCuUnRPLzkll54JlfYGyPrHsklR26WssSvthvdjv33qxMSqxXgy5Y+vFRg8h4QWlGdPSLwpUiKZfKvB+DraVrPD6/iwUyCKwor5q7O99NM/4GLfCHurNuJo6r+LVm5TD2QxhOT5rU1jN9tP9qSrZInCGmNl8zpaK5Gq3wlopn6tQqGaTfPIUPlyST77CJyvJZ1eSWnpxwseXnRRud5IqutKnIEkVXelTqLSGmuRTlKSWrvTZk6SWrvRRKtDv5rW+Ar7EV8jv9RXxpb49SS2bE4+zj9+/SZG8OH3YKYIv26QUrc0YtnxT2BJet42+5nj9G1WMsX3gjGnFbRTzBr7ijQrU30yJDmwzrUr+4BvTqsLKqnuTUohbqE1RaSxV5slXpbdw7C1Nb9XYXaHIIa56yx96ZNyB6u++pForLLbejI/NLdVz979l/LK3jF+O74TfVCsm1NCrd9SKOrBiM0X59PxRrw7dQ2t+SvsM6Cqq/Tnpq0h/jXkrNlkXyVBy/thKkvIwX7cjBepK7wEvtlzsOzhD8Cbvvj8leTNvQbSeb0C0kW9CtJlvQfQ4r0X0BF+lsCICZ97hzyDayjdnsCWixYrPWmxRpATRfXwPWBXBFkKqUK7bsy1yDdGvq7JsxVY4tKC2zDuxIvIh3uUz8m5ftfuYov3jKvJeo9K6sffQI0+KSrJikU/il3L9HuYXvYcXiXXSeRQ9nQ/zdxT38CPRpXbIlVhqpxyp3iPJPaV8l1jEc4Lr5Pyv3U2Knl/aKj6++9zFSqw0di+nterxXoZR5l2BGvi2bdXjaFLJ7nmPplXzbVGE+RHv344q7lZ15O8r6ifXFefLv//G3H/8DeeePkelMnjZTtNPo3D8a34F9cofKBSy/zBJIftv8LhT+v9E4X7jePQeSRl11LpqzZzUs6tvP+aS+uGD76QfTiZib6Mftry7RxW/VWv/OUnx+8Mkxe/TCR+s+F2DFb9r7tVEFb+RS6H4/Ud9y0XJlkFkwyAKTfDfpXI3RlCdRehemBYvBah05uyXu4iZ179cTIuSOoshrhbI7x1KqrUuzJjSwKT/BeMtQLaESZcr61vq7Daz1VRj5s2mmvpJW11NS1NTc42Jt9c31dfZGs32ZgymhrPrLHWNDfXNjfV1TRhZDbMxaUuIdbmyuaHF1tBostfwtha+pn7CwtdMTPJ8zWTDpL2pftLKo2x2DsSGqcEBDMFW085zcPI8kB4gXw+Jde6FLv6usFZnKeQWByqd+0BMgzyGac8Mnwo/DmUcfW+/padzBBcHsrlG7WTMZUENrsfH3Bhy/VtB9MZgmdO34y05j+uXS9PsyZl+S84023c65/nYtpzJKGtYE92y1uq2JhBXvPKkWr8d2PXbw1kvx6+5FLA1gbPWpuKsGFjFMOW3BqxixNRZAb22NVoKQKnzAITLiJT+GEg6pLQaon0ELoyZ1hI7xUzlgdcTI38FqfwzC1jp/1ITWTlrmiBXEuBKBK7k+ZURAR/Pr15/PvaueNUqXbUK8rF3QuRsEmcTONtzfkri54O8O8C7RX5R4hcFfjFCOWG+bt+BCDFP7q56jel6uwxo/P+BEr4FjvYt7ed4Tt7P8by8n+N5eT/HHnk/R4yj6ZQ4mm4rHG0B2G1qScbR7sp+d2UcbVnG0TDGpotCNLHNHX/A0WI4WpG+IoTGpTtCI9dLvfFhVUSFXBE1YTgq1AxEWBA4wmB8WBbJAreGMBx5eC6SDe4cwnDyyUAkF9x5hOHYYyqSD+5dhKHqwWJkt+yua3lyQHYXEAaLUD8aKQShCAmPz0f2gLuYMFQ/PBTRgruEMNQLDT2RvSCUEgbT40ORfeDeTxhOPGmPlIG7nDA0PnZFdODWE4ZTT2wRA7griCPmUNOJ0MnzkUMgEzGywUQO/4BAKbZFfCMCJe6rjVC0wRyqrXu859HMQ/ohDTokcMIEAhK/+urFgaoHrr9o/kXzL10P3nnwTshY84nqFcatfmMT+gc/m/58WqwdEoavi7XXBXTzrn1XsM6JtXOicV4yzgvG+W3uqYixsLPPGLG2VzRekIwXBOMFjHyde3ZANPZJxr6g8UrAeOX54Ihw9bo4OCYNYqxnEGM9g3ZhalYcnBXmneKgU3DdEQfviMYlybgkGJdepNmu8Xl0u8Yb0tANYXxCHJoQbJPiEHoG3BKHbonGWck4Kxhno0ja31oeu/66+W+aReNJyXhSMJ6MQmrHNsFf8QbVPrr15KiEaqSSavvSN23oQNUvDzw4/uD4J/yOWjQdIPg8CgiOSv2jwrUbYj+uVT+q1ZTYPyUapyXjtGCc3rI+X5Qd/PrAGGzs92nZxbyRakI4yl1qoIR6EtwNzKUTKqGloxYJz41Fg6eo5yfB4/kpZohW/TPZVoWEULVm5DQdalEhCq+A8V8cMmvO+15DZiTe22rOR/GMj/69gMyYbwAyU2WEzNQZITM2I2TGZYTMspIgM01GyCw7I2SWkxEyy80ImeVlhMzyM0Jmu3itbzdf4ivg9/oK+VJf0Q4gswzwWlrILDO8thkyywyv6TbDaxnD6jeF3ZsxrCHNXlHbD7svY9iKNHtFZQp7YPNeUXzltoC6N4Nr24UOq/hD3wh0uCUIhEtUvc20DvNH3pgWnsr2lW8LOkwCY/maDKCXbkfQYe2jYzsAvfRvCd0Z3jJ+xVvGP4CeCJXfWCsmoMO6HbXiQd7Em6coXxVv8R5Ez5L6n9K+Q+gqavg56TNmgA6Nm/ZvylByvjEFOmzaEXR42FvtPYzH5JEZgm9+u/b+U5Jv4Y8DvPjW6ZzEey+d8lIKgLIG0TN8KwYo4Uz7W+fSgQHQTrwD01m+W7G3E6Tfi+mFKNzZx1/kL3lp/jLee+koaq1vB+aUd2aCMLdx/k7exbv/I4XyrOE9vlp+0XcsA9xZ6z3qrXl0JwXkVOxAlPil3Gnq+CVvXRzkrOPvKp66pjioZMoAcpq2AXL+TLlXFL+8VXx8n3wPT8lS2O1NC3L6MlwP91agBj/aNshpTiqZ32tOCzYp4bL7/Ps7hrdS6sj/WFE/ua44X37ljbn/wTece/oclSBn2p27tko/Dbj2M/4PUa8ogcvVJJBzDY87pf8HCvcbx6PXtAnkVK9lJ7Xbh99Jux1PxN5Gu20HlFSvOZJAyT9KAiVrEz43y+Ou+I5glYSzBJWqVRHKEE+pLjU/ADQHNu9wZcFAp+WeJQp0IpcC6FzbtMPV7xTXhD52/i2Q3wB5BYSB6fatAc80C0StnzIEIRujvei0WWuidhOj9r6bZGPKLQ0NTWlsxDpQhKjB2aW4hV1TQ6O5yWyxNEUNzzpntmFeF9ub9EZ3JpfNzFoy2wXOZOTYZLE0Jqw4my0JA/SyieNYycYOHTmUscp1sjXNhsZ0RoUTNV6eHm/vk2vcZELtZG4xxWpsn7VPOuZncMjtVVze2T1mDRqsGm+/8nET1iZzY1PCxnNdY0rt46VMWB/eXHuLbLm+sRnbuc5c+1uO8Z7+qJHi+rrGuvqmhh3190CLqbnNK+8kHzMrXGuuNW+/2uZ4tetNZoV9+eaUaseLl9ZYuGzms95ca6mXa9OIUquzILpVhhZL3OaypSVmBz12CaA2GHLwVjQC7JvNLcd6/M32wXEw/SVLXVLzwCLwbRkJb5ENvFuaa02mRrlqLY3NzXXNTabmTVbQW1oamiwNjRaTxdxoarI0xweUuT7ess31DdGKOj3j/YNy4yqTjI78eYfzbcyip7kRbK75ZkPh3zvdDec8P5cGR++F0v5Ol7gboQRpVrcvF85NWF0ztqSF6jvSsVi+HV/tvjklMAA9s7B4qq7Kbl081To5arVZbjYO9rdNDl6cvHm5Zck+PDzbdf7K5YWGVr7jiuXq5XOLdV1d1gujrrrONrelu6G/Yb6+uWZg6c5C8/mGm61V407emaLRsdxWYexzuI2tx1NtMJ91OKZm7VHzv1HbyY1p7Ck3VmCFkOXudAklrDDvILmEVgnokoTZ6O14Z/okeBF7XJ+kmnrDgnYMzP9eqZVkuBwWNquVOI+gc8tFqcoh6TRISlID9adXH3EehWwSKiPbWqn/3S7Nx9oig7ifgJwG8g4QrEFSL2uQJJRHvt1V+c790F5lQMqB6IDogRiAbFe1JL4Q/w36JRlX4qfol9QTX29NvjwOfTECtXEtZKXVMhm8KuDj+ejYc1gkNiGNTgjysdcmcrzE8QLHP7dPS3ZH0O4J2D2i/Y5kvyPY78h2WLGWyRjWMhmTtUx+WIv+w1r0//dsorYWg9Ba/IMOzQ9r0b+va9GLDpRjTaCqCI2cCk0gJCU0gUCIaQKBO6YJBO6YOdt2UHlCckwZCNyyMtBgpBAEWRloLrIHhJgyELhLQAGoOrIX3KWyAtA+cO+XlX7KwB1TBgK3XlYAMoC7QlYAOgDuSkKlf1AYOQjuqpgOUDVIRIygQXr4a61C/37oALU/bReN3ZKxO2jsCxj7fuMSBoY+W/p8SRi59plXuD4uXhwXrJPixUlhela8OCvM3RYv3haNTsnoFIxOnMTZZ7Ro7JWMvUFjf8AIO4QIw6PiwDVp4BokMIBXpw/YBH5aHFCuvf9u9H/Qy0p1zXel1KOV8iukfDMo9OgSBIX6WLNh/ijv47z16H8n+j9guvPTsv5D10oJScVdyaOkXBLcecyVIpVU0FGLhC/IoqvF1Bd7wOOLYubqftUXpa2nkfAvpcbre+n/qsoCWqRC1Kb4mMEaQFgLCIye/hmh/LjnyU2oC3zCa+GFcC8Z+3DBHyD4TXF/jHwAb4pgAMVPvOByhbxukTsnceeE2IHjJJVCFSvFz+jUUrgVy/zhYyI6xUBkxnTkL6+3SwNjogRP8fQD5TYD8V/q3D0OTyblE58QSbXXRxLu7EQ4d07CvVU4frPelNJX7SXTIhLpdRXYLdPiUn2zknCLm3Gshc9KDpmwROWjvKSXWiScnUkpazbl+1a9lFHfKzvdyE0qSc7XbimlLafcTb7pR0DeNnPbVG73vkS4VN03GQNK6bv8bea0ayc5ychQFPHZ3RemOgY8oPB39sK/+n/e2nW2Rp5mLEfJecAAcXzd275rlsY5FCZ6Ykx/1eHR99ntvL51YcHpWLTO6q849IMuu/7K9IwLuR2z6MMzGtpz+E1JOfU99rv649hLP/Uf/hx+f/cOYF7E8onYpNrUjHvaM4Hn0qyTU7MzjvmGY9Zo7scmZh0Tx+asM/PxUzAPslwNubSgbE+fTuTTbXXp2+z2+WjZUSUMBgOeGVk2KMIP2Od5HN4xrx+etrpdKLhBv2wAv/ZZ2Hu/c95td0LFcdB4+svGJX6qxrGAcoiV/Y61ds5+7Lbz2MC5hsHGNstQf89AR69p+SAkNjhvnZi1QzpddrdtWt9hdVv1XU7HHOzhv4hywNOk1XnyRIyOhFm0KbvbDmun8OyLnoxNqBiSJ09gziVMo7Bhxm1fcjtb4OQAItUMnqMJUzN8mINCtlun3WF6zjXlgsEenzUIc7HmdB5HV8QaPBAgS/RAyMr54/610Q+ur10Xs0qlrNKNejFL95f0X7b94vxf9P6iV9SbJL1JzDL5K0Nswbr5z5r+XdNG/UenPj4lsnp/xQuKWalePStSRRJVJFBFLyj2j5n7R1aO+I8gp8DdEKlxiRoXqHEsdjztFzkUuluiugWq+zdFn5cKV4Y/032ue6aDAFkJvwhVSuegB/iaV9h/VcwfleAY93eH2KzVEf89/70X6mwh57ioPiGpTwjqEy9y8v899bHmo5yPc8ScMimnzG97odas3FzffX9uZc4/F1Jr/PwriGMW1RZJbRHUFjlA4X3HisPvwH7HRHWdpK4T1HWv1NzKjLArkcErZWroJYbNvj+5MunH/68ijJrOeaXSCNlmUWWRVBZBZXmlyloZXSfvj62M+ceQcH9oZcgf/cNrBKjF/KOmVd9VTPzqaKsRsV8XW87m0NXeMDM5ccuFh4g834an2mA8hCmnXZ7Ss8cn6GC+LqxxeSZQD9vsLleYnnDVhwtsjnmbx+m0z7trJz14p1MnPNadnXhqjYAR5XIshAsvOHjPrL3P4e5yeOb5TligJg9CPBwbYO6qkYaNfVHyS/JU32M8dkGeQam6YzNbzhPgeRI886zy9PD4nIO3z7rC1NJSmJmdmbfjacIw7XE5o3tbItcsdkyh0e2Zss/jacYwZbWGyQl8qYRJW5icwlOVYXLaeQOfuun8P5jPhlUe6y2POayyorjuMMmHyckwN+mZnbVOIZl2eqbC1LwbT4Gi1nOilEcRXwKfZXSpuG14OjScY5u2226NOzzuBY87rObtNlRyeYvTdNOSZ7c5N/mfIFu1yz5rt7nlyddC3AALd5ac/x2647dAvgDyP4BIQP4VyCsgL6Gf1JcG+y/1dobp/s6OsGq4+9yVzrDqbH9nZ19YfbWzt/ficJhp6x3sDKsv9rf2nUWebb2t7T1hVefIlf5W+WaCXwbhgSBPEvfGJ2vxZqpN0MGs23HLPn/L4zwDp/qAXARyCchlIP1AzkH5VUvwk7cH7YlPS8K9JeUt9N+4k3N4gJ12ztHw7EJ3HksBQaCXaZIMqW74mQiTTepDTKfwuzhCTIkQO0JMnv88/F8yp4TkI8QYheQjxBiETcdXIbY0QtCkPkFCTJa/U9DUiEytxNQKTG2IyfW3rZwT8t4RmTMSc0ZgzsRPlYuMTmJ0QuyIsCgF+PLQMOTJkKZ41bh2VNAOi5oRCY4xf0eI4fwdq2XrLpHZJzH7gowhwBgeHBKZwxJzWMAHKtQu9EFDnkyQaKGOi8wJiTkhbDqiXzvkSeBqIit3lVkd27CInE7idEGuMsBVilyVxFUFOVOAM4mcReIsfhYF3VXgz4tQDJkTytqzWrK2XygeEbOuSnDcCGbNBLJmxKxbUtYtf1toVwEqi6oSk1UmxBUHubIAV7bBi9wBiTsg4AOVQlX51Usi2+/2u1FpXjJqPw0Z5IbYQv/Silcouiyy/RIcw0F2IsBOiCwvsTzKIA+qrdJiskqFuOw/0XyoWTd/kLeWt4r+kLQWJZ2DKgffdy9VBf6hlbEIQRS1d5LJ7DVBqDs6yS9l5qdCKtbPhDT5qwfXVR8cXTsaIbJJLSYoX/YQIupC/+TKnFDUIh+i+rikPu5vDalL1wvRv/8j7cdaQV2KDjjZCKTYPympi9edGwdEdbmkLodzWQoP90aHqDZIakOmwPsRyc0XNGZ0rBui/LbMN1qBRIUHpiiPyg+j8sOo7EfXBfeTnvd71lUiUywxxQI+QrkFq4PrDfCuECHyyFJMUFj2yFYVfgcI9kSNuWeIUlLUruwwTMsiqqjVbWWtthm14xtrwt2F6OJEx7pV5hsmICA82A2kVT79EISHUeExGeVR+UlUfhKV0XtLtEU5kdkrMXsFfIRgOCeNIxVZ+BoIjKPclXvAivyLKzCJWjxMKSlqAG4EGgBRCKb1L0qsdoNE1ymrk1idvy1CEVw3g+dg2tD/9uOCT7ofdX+S+wiQBOQj06ftT9ufUZ+e/dVZWX428GxAuDzw2fDnw/IJYegqHKPXxaExaWhMGRcmTqkeKsF65d2Qe2ObIl8G1i8vfu2lhqC4vfI0fjeFew9YSorXqXEqwd6Vp4mjzEZNAZumZiGNd6k5SAPYa4gwDxKwlBRvy9PKUeah7ijYEqVcTuuh7mEUAjFAIagfYRQCsZQUz9G9dIJdkKejo+wS3Q9sgB6COecL9DDMOQN7DRFGQAKWkuIY/S6dYFbapmA8bQc2SU9BGlZ6GtIA9hoizIAELCXFWdpBJ9gC7VQwlzwF7qEXIY0F+g6kAew1RFgCCVhKioiikcawPzn//vlV5/2+lT5/3/0+eRBn71ptWN/zwcm1k/DcK8TE3x4dxDASB5mHroeux2b0tz6hYPbuE98jGNfIR6ZPXE9cT83ob0XjsflXzX/n+/sk/2euZy5AYdAxNCyMXBUHRqWB0c+8n3uVoTBSdJlKsH7qioINygNuhLoGPdxPXYceBvYaIoyBBCwlxQnKTiXYpLxkezK2cnsO2Ly8f/ckhTfwBvYaIrhBmpBHnjLFO/K4u5MYfgl2jzoDTd9Kd0B/vEd1Qn8Aew0RukAClpLiNfoGnWDjtFXBJmgemF0eM+PymAEGOBl9EyRgKSk65MHiiI0Zj4It0svA3qN/BGm46DPMlzJ7DRFaQQKWkmIHc1bBupnzCtbDXMCdx1yGNACQ+VJmryHCAEjAlCluGo3+PvQSoubQwzn5WVWOCXpWZR9DrwIa7WrVWo1Q0iwfoqZF0rSskiFNExDsidLfO0opKSpF9jXoTEQhWOlqlaQp3TBt2ERNhaSp2EHUbkV8szJ+rsKj/gEjag5KmoOZAo8gskcrFLSjY8MQ5bcReQDCg8uIPCTl0w9BeBwV0DMK8ydR+UlUfhqVV7kQl/Mn2R9mr3eLXJnElQn4eJmV7VeHCqrXD0sF1cLhXmFgWCgYEQtGpIKRYMF4oGBceHdKLJiWCqaDBQuBggXhtkdYXBIL7koFd/35IU63qkGvj4L++NMigesSuS6J6wpyFwLchWdTIjckcUNB7kaAuyGM2wR+UuSmJG7Kr0rEa3jSIXCtItcqca1BrjvAdT/Titxlibsc5K4GOPSEQlGtIjchcRMoHpuHvi0omtwbyq9aXZbyq4RD7c8qhfyLYv5FKf9iMH8okD8kDN8Q88el/PFgvj2QbxcmZ8T8m1L+TeHWrJQ/F8z3BPJRJfDm//n3pPx7+F0xQpGQagkI+NUxxJb7lyW2XNCdeeoW2F6R7ZXY3iA7EGAHhCvXRPa6xF4PsnyA5QU73qWdnZPYOTRK4xFbnjIC2ymynRLbGWR7A2zvs2GRHZTYwSA7FmBh22PBZhfZSYmdhHg5QIqVKbzzlBfYHpHtkdieINsfYPuFgVGRvSax14KsLcCiRp0Spm+J7KzEzgZZd4B1C567wrJXZH0S64OkyoTyho2bUnmD0DguTN4Uym/FjCA4A+VOwbUslr8nlb8Htg06sG2DDhjgndQ5YOcpGau/gO0XXMDvJxfk27D8shK97zpkNgHBotICNSLfq/DTboTi4ZYC7EuZ/W9gt+j/KTP8THPJQdxyELccxCsH8UIQn3zzaWM6GByyk/lSZlCUTgbGRtHXGxvoY2XX7lVVaDfGifZistoa2rVn/fZH3LpqHfmUrqpD2bvXBz48tXoqpK1dX5a0tcKxHqF/CD7ftMOSdjiovRHQogE7KWqnJO1UUDsX0M4J87dFrVPSorZ2S1pPUOsLaGX8PK4xgYpfchbaDtF15sWu4g3mo5x19bo6lFu47vpwbHUsQql2HwzpGjeWJV2j0DQA14VuXNSNS7rxoG4yoJsUpuZFnUPSOYI6T0CHBvhdUYcCo2HulXQ+1JT6LuhefVQ/I/5mB5okFyFvRDeYFyXlD5g/z9lQb6i/CmnR5y61+2CChHTGpCCxP/62VKEAwDmixKCoxFebL62XpdWoZeHIL4wdRXF3ZI9Gg3oBEb86UkyR7ajLFZQj0HcaHWJ2+ck3kVxEOC26wakLUAyuCG48QLJQyvCpycgu5KuCV20Veszk7I4QuewJmRQTFBvRxsVSglJH9sVFIGjE7SfJLhK+wONUTZFFUNgoQc8u+LDEL1QJQqvQFyen8bMhQuVX3WdXWPStTY2T8MmpoGfoMvJwhIiTk2XkUXBFyelkMdW3EVxx4iR5kkQtq6DnaYJ1H0E1p6bxSQXtpxexoKAL9BQWFPQKTZLnccXjVF1B5kSIOOki0bXk5+5rVjR+Deo9UuVn7qtX1H78d31AEMRKK9XKEp+yda3H6U9bSKCn69ssxD9YVO259D80Z7dz9D9y4P4V3Up2qoh/UlGdWfQ/5beSXbuJX++muvbQ4ezWgmvlxL+UM9cq6ZeVbcfs+4n/VtS6nzcRv60jkfBbk8qeQ/+2McfO0q8oFTrzioUzr3Lywb2fsVfQ/xcrq4Zf"))))