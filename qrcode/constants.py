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