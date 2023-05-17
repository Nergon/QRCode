# A table for the capacity of each version of QR Code. The table is indexed by version number and mode.

QR_CODE_VERSIONS = {
    # (L, M, Q, H)
    # Version 1
    1: {
        "NUMERIC": [41, 34, 27, 17],
        "ALPHANUMERIC": [25, 20, 16, 10],
        "BYTE": [17, 14, 11, 7],
        "KANJI": [10, 8, 7, 4]
    },
    2: {
        "NUMERIC": [77, 63, 48, 34],
        "ALPHANUMERIC": [47, 38, 29, 20],
        "BYTE": [32, 26, 20, 14],
        "KANJI": [20, 16, 12, 8]
    },
    3: {
        "NUMERIC": [127, 101, 77, 58],
        "ALPHANUMERIC": [77, 61, 47, 35],
        "BYTE": [53, 42, 32, 24],
        "KANJI": [32, 26, 20, 15]
    },
    4: {
        "NUMERIC": [187, 149, 111, 82],
        "ALPHANUMERIC": [114, 90, 67, 50],
        "BYTE": [78, 62, 46, 34],
        "KANJI": [48, 38, 28, 21]
    },
    5: {
        "NUMERIC": [255, 202, 144, 106],
        "ALPHANUMERIC": [154, 122, 87, 64],
        "BYTE": [106, 84, 60, 44],
        "KANJI": [65, 52, 37, 27]
    },
    6: {
        "NUMERIC": [322, 255, 178, 139],
        "ALPHANUMERIC": [195, 154, 108, 84],
        "BYTE": [134, 106, 74, 58],
        "KANJI": [82, 65, 45, 36]
    },
    7: {
        "NUMERIC": [370, 293, 207, 154],
        "ALPHANUMERIC": [224, 178, 125, 93],
        "BYTE": [154, 122, 86, 64],
        "KANJI": [95, 75, 53, 39]
    },
    8: {
        "NUMERIC": [461, 365, 259, 202],
        "ALPHANUMERIC": [279, 221, 157, 122],
        "BYTE": [192, 152, 108, 84],
        "KANJI": [118, 93, 66, 52]
    },
    9: {
        "NUMERIC": [552, 432, 312, 235],
        "ALPHANUMERIC": [335, 262, 189, 143],
        "BYTE": [230, 180, 130, 98],
        "KANJI": [141, 111, 80, 60]
    },
    10: {
        "NUMERIC": [652, 513, 364, 288],
        "ALPHANUMERIC": [395, 311, 221, 174],
        "BYTE": [271, 213, 151, 119],
        "KANJI": [167, 131, 93, 74]
    },
    11: {
        "NUMERIC": [772, 604, 427, 331],
        "ALPHANUMERIC": [468, 366, 259, 200],
        "BYTE": [321, 251, 177, 137],
        "KANJI": [198, 155, 109, 85]
    },
    12: {
        "NUMERIC": [883, 691, 489, 374],
        "ALPHANUMERIC": [535, 419, 296, 227],
        "BYTE": [367, 287, 203, 155],
        "KANJI": [226, 177, 125, 96]
    },
    13: {
        "NUMERIC": [1022, 796, 580, 427],
        "ALPHANUMERIC": [619, 483, 352, 259],
        "BYTE": [425, 331, 241, 177],
        "KANJI": [262, 204, 149, 109]
    },
    14: {
        "NUMERIC": [1101, 871, 621, 468],
        "ALPHANUMERIC": [667, 528, 376, 283],
        "BYTE": [458, 362, 258, 194],
        "KANJI": [282, 223, 159, 120]
    },
    15: {
        "NUMERIC": [1250, 991, 703, 530],
        "ALPHANUMERIC": [758, 600, 426, 321],
        "BYTE": [520, 412, 292, 220],
        "KANJI": [320, 254, 180, 136]
    },
    16: {
        "NUMERIC": [1408, 1082, 775, 602],
        "ALPHANUMERIC": [854, 656, 470, 365],
        "BYTE": [586, 450, 322, 250],
        "KANJI": [361, 277, 198, 154]
    },
    17: {
        "NUMERIC": [1548, 1212, 876, 674],
        "ALPHANUMERIC": [938, 734, 531, 408],   
        "BYTE": [644, 504, 364, 280],
        "KANJI": [397, 310, 224, 173]
    },
    18: {
        "NUMERIC": [1725, 1346, 948, 746],
        "ALPHANUMERIC": [1046, 816, 574, 452],
        "BYTE": [718, 560, 394, 310],
        "KANJI": [442, 345, 243, 191]
    },
    19: {
        "NUMERIC": [1903, 1500, 1063, 813],
        "ALPHANUMERIC": [1153, 909, 644, 493],
        "BYTE": [792, 624, 442, 338],
        "KANJI": [488, 384, 272, 208]
    },
    20: {
        "NUMERIC": [2061, 1600, 1159, 919],
        "ALPHANUMERIC": [1249, 970, 702, 557],
        "BYTE": [858, 666, 482, 382],
        "KANJI": [528, 410, 297, 235]
    },
    21: {
        "NUMERIC": [2232, 1708, 1224, 969],
        "ALPHANUMERIC": [1352, 1035, 742, 587],
        "BYTE": [929, 711, 509, 403],
        "KANJI": [572, 438, 314, 248]
    },
    22: {
        "NUMERIC": [2409, 1872, 1358, 1056],
        "ALPHANUMERIC": [1460, 1134, 823, 640],
        "BYTE": [1003, 779, 565, 439],
        "KANJI": [618, 480, 348, 270]
    },
    23: {
        "NUMERIC": [2620, 2059, 1468, 1108],
        "ALPHANUMERIC": [1588, 1248, 890, 672],
        "BYTE": [1091, 857, 611, 461],
        "KANJI": [672, 528, 376, 284]
    },
    24: {
        "NUMERIC": [2812, 2188, 1588, 1228],
        "ALPHANUMERIC": [1704, 1326, 963, 744],
        "BYTE": [1171, 911, 661, 511],
        "KANJI": [721, 561, 407, 315]
    },
    25: {
        "NUMERIC": [3057, 2395, 1718, 1286],
        "ALPHANUMERIC": [1853, 1451, 1041, 779],
        "BYTE": [1273, 997, 715, 535],
        "KANJI": [784, 614, 440, 330]
    },
    26: {
        "NUMERIC": [3283, 2544, 1804, 1425],
        "ALPHANUMERIC": [1990, 1542, 1094, 864],
        "BYTE": [1367, 1059, 751, 593],
        "KANJI": [842, 652, 462, 365]
    },
    27: {
        "NUMERIC": [3517, 2701, 1933, 1501],
        "ALPHANUMERIC": [2132, 1637, 1172, 910],
        "BYTE": [1465, 1125, 805, 625],
        "KANJI": [902, 692, 496, 385]
    },
    28: {
        "NUMERIC": [3669, 2857, 2085, 1581],
        "ALPHANUMERIC": [2223, 1732, 1263, 958],
        "BYTE": [1528, 1190, 868, 658],
        "KANJI": [940, 732, 534, 405]
    },
    29: {
        "NUMERIC": [3909, 3035, 2181, 1677],
        "ALPHANUMERIC": [2369, 1839, 1322, 1016],
        "BYTE": [1628, 1264, 908, 698],
        "KANJI": [1002, 778, 559, 430]
    },
    30: {
        "NUMERIC": [4158, 3289, 2358, 1782],
        "ALPHANUMERIC": [2520, 1994, 1429, 1080],
        "BYTE": [1732, 1370, 982, 742],
        "KANJI": [1066, 843, 604, 457]
    },
    31: {
        "NUMERIC": [4417, 3486, 2473, 1897],
        "ALPHANUMERIC": [2677, 2113, 1499, 1150],
        "BYTE": [1840, 1452, 1030, 790],
        "KANJI": [1132, 894, 634, 486]
    },
    32: {
        "NUMERIC": [4686, 3693, 2670, 2022],
        "ALPHANUMERIC": [2840, 2238, 1618, 1226],
        "BYTE": [1952, 1538, 1112, 842],
        "KANJI": [1201, 947, 684, 518]
    },
    33: {
        "NUMERIC": [4965, 3909, 2805, 2157],
        "ALPHANUMERIC": [3009, 2369, 1700, 1307],
        "BYTE": [2068, 1628, 1168, 898],
        "KANJI": [1273, 1002, 719, 553]
    },
    34: {
        "NUMERIC": [5253, 4134, 2949, 2301],
        "ALPHANUMERIC": [3183, 2506, 1787, 1394],
        "BYTE": [2188, 1722, 1228, 958],
        "KANJI": [1347, 1060, 756, 590]
    },
    35: {
        "NUMERIC": [5529, 4343, 3081, 2361],
        "ALPHANUMERIC": [3351, 2632, 1867, 1431],
        "BYTE": [2395, 1809, 1283, 983],
        "KANJI": [1473, 1150, 790, 605]
    },
    36: {
        "NUMERIC": [5836, 4588, 3244, 2524],
        "ALPHANUMERIC": [3537, 2780, 1966, 1530],
        "BYTE": [2544, 1911, 1351, 1051],
        "KANJI": [1542, 1226, 832, 647]
    },
    37: {
        "NUMERIC": [6153, 4775, 3417, 2625],
        "ALPHANUMERIC": [3729, 2894, 2071, 1591],
        "BYTE": [2701, 1989, 1423, 1093],
        "KANJI": [1637, 1292, 876, 673]
    },
    38: {
        "NUMERIC": [6479, 5039, 3599, 2735],
        "ALPHANUMERIC": [3927, 3054, 2181, 1658],
        "BYTE": [2857, 2123, 1499, 1139],
        "KANJI": [1732, 1362, 923, 701]
    },
    39: {
        "NUMERIC": [6743, 5313, 3791, 2927],
        "ALPHANUMERIC": [4087, 3220, 2298, 1774],
        "BYTE": [3035, 2249, 1618, 1219],
        "KANJI": [1839, 1435, 972, 750]
    },
    40: {
        "NUMERIC": [7089, 5596, 3993, 3057],
        "ALPHANUMERIC": [4296, 3391, 2420, 1852],
        "BYTE": [3289, 2434, 1722, 1286],
        "KANJI": [1994, 1568, 1060, 816]
    }
}

# Alphanumeric Encoding Table for QR Code
ALPHANUMERIC_TABLE = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 18,
    "J": 19,
    "K": 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27,
    "S": 28,
    "T": 29,
    "U": 30,
    "V": 31,
    "W": 32,
    "X": 33,
    "Y": 34,
    "Z": 35,
    " ": 36,
    "$": 37,
    "%": 38,
    "*": 39,
    "+": 40,
    "-": 41,
    ".": 42,
    "/": 43,
    ":": 44
}

# Maximum number of data codewords for each version and error correction level
MAX_DATA_CODEWORDS = {
    # [L, M, Q, H]
    1: [19, 16, 13, 9],
    2: [34, 28, 22, 16],
    3: [55, 44, 34, 26],
    4: [80, 64, 48, 36],
    5: [108, 86, 62, 46],
    6: [136, 108, 76, 60],
    7: [156, 124, 88, 66],
    8: [194, 154, 110, 86],
    9: [232, 182, 132, 100],
    10: [274, 216, 154, 122],
    11: [324, 254, 180, 140],
    12: [370, 290, 206, 158],
    13: [428, 334, 244, 180],
    14: [461, 365, 261, 197],
    15: [523, 415, 295, 223],
    16: [589, 453, 325, 253],
    17: [647, 507, 367, 283],
    18: [721, 563, 397, 313],
    19: [795, 627, 445, 341],
    20: [861, 669, 485, 385],
    21: [932, 714, 512, 406],
    22: [1006, 782, 568, 442],
    23: [1094, 860, 614, 464],
    24: [1174, 914, 664, 514],
    25: [1276, 1000, 718, 538],
    26: [1370, 1062, 754, 596],
    27: [1468, 1128, 808, 628],
    28: [1531, 1193, 871, 661],
    29: [1631, 1267, 911, 701],
    30: [1735, 1373, 985, 745],
    31: [1843, 1455, 1033, 793],
    32: [1955, 1541, 1115, 845],
    33: [2071, 1631, 1171, 901],
    34: [2191, 1725, 1231, 961],
    35: [2306, 1812, 1286, 986],
    36: [2434, 1914, 1354, 1054],
    37: [2566, 1992, 1426, 1096],
    38: [2702, 2102, 1502, 1142],
    39: [2812, 2216, 1582, 1222],
    40: [2956, 2334, 1666, 1276]
}


# Table with the number of blocks, codewords per block and nuber of data codewords in each block for each version and error correction level
BLOCKS_TABLE = {
    # [L, M, Q, H]
    1: [
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 19,
                "EC_CODEWORDS": 7
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 10
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 13
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 9,
                "EC_CODEWORDS": 17
            },
            # Group 2
            2: None
        }
    ],
    2: [
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 34,
                "EC_CODEWORDS": 10
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 28,
                "EC_CODEWORDS": 16
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 22,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: None
        }
    ],
    3: [
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 55,
                "EC_CODEWORDS": 15
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 44,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 17,
                "EC_CODEWORDS": 18
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: None
        }
    ],
    4: [
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 80,
                "EC_CODEWORDS": 20
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 32,
                "EC_CODEWORDS": 18
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 9,
                "EC_CODEWORDS": 16
            },
            # Group 2
            2: None
        }
    ],
    5: [
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 108,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 43,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 18
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 18
            }
        }
    ],
    6: [
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 68,
                "EC_CODEWORDS": 18
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 27,
                "EC_CODEWORDS": 16
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 19,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: None
        }
    ],
    7: [
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 78,
                "EC_CODEWORDS": 20
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 31,
                "EC_CODEWORDS": 18
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 14,
                "EC_CODEWORDS": 18
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 18
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 14,
                "EC_CODEWORDS": 26
            }
        }
    ],
    8: [
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 97,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 38,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 39,
                "EC_CODEWORDS": 22
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 18,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 19,
                "EC_CODEWORDS": 22
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 14,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 26
            }
        }
    ],
    9: [
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 36,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 37,
                "EC_CODEWORDS": 22
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 20
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 17,
                "EC_CODEWORDS": 20
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 12,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 24
            }
        }
    ],
    10: [
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 68,
                "EC_CODEWORDS": 18
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 69,
                "EC_CODEWORDS": 18
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 43,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 44,
                "EC_CODEWORDS": 26
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 19,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 20,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 28
            }
        }
    ],
    11: [
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 81,
                "EC_CODEWORDS": 20
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 50,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 51,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 22,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 23,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 12,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 8,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 24
            }
        }
    ],
    12: [
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 92,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 93,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 36,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 37,
                "EC_CODEWORDS": 22
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 20,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 21,
                "EC_CODEWORDS": 26
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 14,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 28
            }
        }
    ],
    13: [
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 107,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 8,
                "DATA_CODEWORDS": 37,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 38,
                "EC_CODEWORDS": 22
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 8,
                "DATA_CODEWORDS": 20,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 21,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 12,
                "DATA_CODEWORDS": 11,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 12,
                "EC_CODEWORDS": 22
            }
        }
    ],
    14: [
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 115,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 40,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 41,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 20
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 17,
                "EC_CODEWORDS": 20
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 12,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 24
            }
        }
    ],
    15: [
        {
            # Group 1
            1: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 87,
                "EC_CODEWORDS": 22
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 88,
                "EC_CODEWORDS": 22
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 41,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 42,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 12,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 24
            }
        }
    ],
    16: [
        {
            # Group 1
            1: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 98,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 99,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 45,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 15,
                "DATA_CODEWORDS": 19,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 20,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 13,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 28
            }
        }
    ],
    17: [
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 107,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 108,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 22,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 15,
                "DATA_CODEWORDS": 23,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 14,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 28
            }
        }
    ],
    18: [
        {
            # Group 1
            1: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 120,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 121,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 9,
                "DATA_CODEWORDS": 43,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 44,
                "EC_CODEWORDS": 26
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 22,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 23,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 14,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 28
            }
        }
    ],
    19: [
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 113,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 114,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 44,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 45,
                "EC_CODEWORDS": 26
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 21,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 22,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 9,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: {
                "BLOCKS": 16,
                "DATA_CODEWORDS": 14,
                "EC_CODEWORDS": 26
            }
        }
    ],
    20: [
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 107,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 108,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 41,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 13,
                "DATA_CODEWORDS": 42,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 15,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 15,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 28
            }
        }
    ],
    21: [
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 117,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 42,
                "EC_CODEWORDS": 26
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 22,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 23,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 17,
                "EC_CODEWORDS": 30
            }
        }
    ],
    22: [
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 111,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 112,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 16,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 34,
                "DATA_CODEWORDS": 13,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: None
        }
    ],
    23: [
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 121,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 122,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 48,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 16,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    24: [
        {
            # Group 1
            1: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 117,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 118,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 45,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 16,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 30,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 17,
                "EC_CODEWORDS": 30
            }
        }
    ],
    25: [
        {
            # Group 1
            1: {
                "BLOCKS": 8,
                "DATA_CODEWORDS": 106,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 107,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 8,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 13,
                "DATA_CODEWORDS": 48,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 22,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 22,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 13,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    26: [
        {
            # Group 1
            1: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 114,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 115,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 28,
                "DATA_CODEWORDS": 22,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 23,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 33,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 17,
                "EC_CODEWORDS": 30
            }
        }
    ],
    27: [
        {
            # Group 1
            1: {
                "BLOCKS": 8,
                "DATA_CODEWORDS": 122,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 123,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 22,
                "DATA_CODEWORDS": 45,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 8,
                "DATA_CODEWORDS": 23,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 26,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 12,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 28,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    28: [
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 117,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 118,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 45,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 23,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 31,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 31,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    29: [
        {
            # Group 1
            1: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 117,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 21,
                "DATA_CODEWORDS": 45,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 23,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 37,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 26,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    30: [
        {
            # Group 1
            1: {
                "BLOCKS": 5,
                "DATA_CODEWORDS": 115,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 48,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 15,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 25,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 23,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 25,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    31: [
        {
            # Group 1
            1: {
                "BLOCKS": 13,
                "DATA_CODEWORDS": 115,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 3,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 29,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 42,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 23,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 28,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    32: [
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 115,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: None
        },
        {
            # Group 1
            1: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 23,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 35,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 35,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    33: [
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 115,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 21,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 29,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 11,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 46,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    34: [
        {
            # Group 1
            1: {
                "BLOCKS": 13,
                "DATA_CODEWORDS": 115,
                "EC_CODEWORDS": 28
            },
            # Group 2
            2: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 116,
                "EC_CODEWORDS": 28
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 23,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 44,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 59,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 1,
                "DATA_CODEWORDS": 17,
                "EC_CODEWORDS": 30
            }
        }
    ],
    35: [
        {
            # Group 1
            1: {
                "BLOCKS": 12,
                "DATA_CODEWORDS": 121,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 122,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 12,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 26,
                "DATA_CODEWORDS": 48,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 39,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 22,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 41,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    36: [
        {
            # Group 1
            1: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 121,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 122,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 34,
                "DATA_CODEWORDS": 48,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 46,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 2,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 64,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    37: [
        {
            # Group 1
            1: {
                "BLOCKS": 17,
                "DATA_CODEWORDS": 122,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 123,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 29,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 49,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 24,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 46,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    38: [
        {
            # Group 1
            1: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 122,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 18,
                "DATA_CODEWORDS": 123,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 13,
                "DATA_CODEWORDS": 46,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 32,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 48,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 14,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 42,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 32,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    39: [
        {
            # Group 1
            1: {
                "BLOCKS": 20,
                "DATA_CODEWORDS": 117,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 4,
                "DATA_CODEWORDS": 118,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 40,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 7,
                "DATA_CODEWORDS": 48,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 43,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 22,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 10,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 67,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ],
    40: [
        {
            # Group 1
            1: {
                "BLOCKS": 19,
                "DATA_CODEWORDS": 118,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 6,
                "DATA_CODEWORDS": 119,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 18,
                "DATA_CODEWORDS": 47,
                "EC_CODEWORDS": 24
            },
            # Group 2
            2: {
                "BLOCKS": 31,
                "DATA_CODEWORDS": 48,
                "EC_CODEWORDS": 24
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 34,
                "DATA_CODEWORDS": 24,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 34,
                "DATA_CODEWORDS": 25,
                "EC_CODEWORDS": 30
            }
        },
        {
            # Group 1
            1: {
                "BLOCKS": 20,
                "DATA_CODEWORDS": 15,
                "EC_CODEWORDS": 30
            },
            # Group 2
            2: {
                "BLOCKS": 61,
                "DATA_CODEWORDS": 16,
                "EC_CODEWORDS": 30
            }
        }
    ]
}

REMAINDER_BITS = {
    1: 0,
    2: 7,
    3: 7,
    4: 7,
    5: 7,
    6: 7,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 3,
    15: 3,
    16: 3,
    17: 3,
    18: 3,
    19: 3,
    20: 3,
    21: 4,
    22: 4,
    23: 4,
    24: 4,
    25: 4,
    26: 4,
    27: 4,
    28: 3,
    29: 3,
    30: 3,
    31: 3,
    32: 3,
    33: 3,
    34: 3,
    35: 0,
    36: 0,
    37: 0,
    38: 0,
    39: 0,
    40: 0
}

ALIGNMENT_PATTERN_POSITIONS = {
    1: [],
    2: [6, 18],
    3: [6, 22],
    4: [6, 26],
    5: [6, 30],
    6: [6, 34],
    7: [6, 22, 38],
    8: [6, 24, 42],
    9: [6, 26, 46],
    10: [6, 28, 50],
    11: [6, 30, 54],
    12: [6, 32, 58],
    13: [6, 34, 62],
    14: [6, 26, 46, 66],
    15: [6, 26, 48, 70],
    16: [6, 26, 50, 74],
    17: [6, 30, 54, 78],
    18: [6, 30, 56, 82],
    19: [6, 30, 58, 86],
    20: [6, 34, 62, 90],
    21: [6, 28, 50, 72, 94],
    22: [6, 26, 50, 74, 98],
    23: [6, 30, 54, 78, 102],
    24: [6, 28, 54, 80, 106],
    25: [6, 32, 58, 84, 110],
    26: [6, 30, 58, 86, 114],
    27: [6, 34, 62, 90, 118],
    28: [6, 26, 50, 74, 98, 122],
    29: [6, 30, 54, 78, 102, 126],
    30: [6, 26, 52, 78, 104, 130],
    31: [6, 30, 56, 82, 108, 134],
    32: [6, 34, 60, 86, 112, 138],
    33: [6, 30, 58, 86, 114, 142],
    34: [6, 34, 62, 90, 118, 146],
    35: [6, 30, 54, 78, 102, 126, 150],
    36: [6, 24, 50, 76, 102, 128, 154],
    37: [6, 28, 54, 80, 106, 132, 158],
    38: [6, 32, 58, 84, 110, 136, 162],
    39: [6, 26, 54, 82, 110, 138, 166],
    40: [6, 30, 58, 86, 114, 142, 170]
}