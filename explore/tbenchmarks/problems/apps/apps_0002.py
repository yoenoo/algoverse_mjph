"""
apps_0002 problem from APPS dataset.
"""

from typing import List
from ...core.problem import Problem, TestCase


def create_apps_0002() -> Problem:
    """
    Create the apps_0002 problem.
    """
    # Visible tests (shown to the model)
    visible_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value=4,
            expected_output=1,
            description="Test case 1: input=4\n, expected=1\n"
        ),
        TestCase(
            name="test_case_2",
            input_value=201,
            expected_output=99,
            description="Test case 2: input=201\n, expected=99\n"
        ),
        TestCase(
            name="test_case_3",
            input_value=4000,
            expected_output=1000,
            description="Test case 3: input=4000\n, expected=1000\n"
        ),
    ]
    
    # Hidden tests (not shown to model, used for validation)
    hidden_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value=9,
            expected_output=1,
            description="Test case 1: input=9\n, expected=1\n"
        ),
        TestCase(
            name="test_case_2",
            input_value=10,
            expected_output=10,
            description="Test case 2: input=10\n, expected=10\n"
        ),
        TestCase(
            name="test_case_3",
            input_value=1,
            expected_output=1,
            description="Test case 3: input=1\n, expected=1\n"
        ),
        TestCase(
            name="test_case_4",
            input_value=100000000,
            expected_output=100000000,
            description="Test case 4: input=100000000\n, expected=100000000\n"
        ),
        TestCase(
            name="test_case_5",
            input_value=900000000,
            expected_output=100000000,
            description="Test case 5: input=900000000\n, expected=100000000\n"
        ),
        TestCase(
            name="test_case_6",
            input_value=999999999,
            expected_output=1,
            description="Test case 6: input=999999999\n, expected=1\n"
        ),
        TestCase(
            name="test_case_7",
            input_value=1000000000,
            expected_output=1000000000,
            description="Test case 7: input=1000000000\n, expected=1000000000\n"
        ),
        TestCase(
            name="test_case_8",
            input_value=9999999,
            expected_output=1,
            description="Test case 8: input=9999999\n, expected=1\n"
        ),
        TestCase(
            name="test_case_9",
            input_value=100000001,
            expected_output=99999999,
            description="Test case 9: input=100000001\n, expected=99999999\n"
        ),
        TestCase(
            name="test_case_10",
            input_value=3660,
            expected_output=340,
            description="Test case 10: input=3660\n, expected=340\n"
        ),
        TestCase(
            name="test_case_11",
            input_value=21,
            expected_output=9,
            description="Test case 11: input=21\n, expected=9\n"
        ),
        TestCase(
            name="test_case_12",
            input_value=900000001,
            expected_output=99999999,
            description="Test case 12: input=900000001\n, expected=99999999\n"
        ),
        TestCase(
            name="test_case_13",
            input_value=62911,
            expected_output=7089,
            description="Test case 13: input=62911\n, expected=7089\n"
        ),
        TestCase(
            name="test_case_14",
            input_value=11,
            expected_output=9,
            description="Test case 14: input=11\n, expected=9\n"
        ),
        TestCase(
            name="test_case_15",
            input_value=940302010,
            expected_output=59697990,
            description="Test case 15: input=940302010\n, expected=59697990\n"
        ),
        TestCase(
            name="test_case_16",
            input_value=91,
            expected_output=9,
            description="Test case 16: input=91\n, expected=9\n"
        ),
        TestCase(
            name="test_case_17",
            input_value=101,
            expected_output=99,
            description="Test case 17: input=101\n, expected=99\n"
        ),
        TestCase(
            name="test_case_18",
            input_value=1090,
            expected_output=910,
            description="Test case 18: input=1090\n, expected=910\n"
        ),
        TestCase(
            name="test_case_19",
            input_value=987654321,
            expected_output=12345679,
            description="Test case 19: input=987654321\n, expected=12345679\n"
        ),
        TestCase(
            name="test_case_20",
            input_value=703450474,
            expected_output=96549526,
            description="Test case 20: input=703450474\n, expected=96549526\n"
        ),
        TestCase(
            name="test_case_21",
            input_value=1091,
            expected_output=909,
            description="Test case 21: input=1091\n, expected=909\n"
        ),
        TestCase(
            name="test_case_22",
            input_value=89,
            expected_output=1,
            description="Test case 22: input=89\n, expected=1\n"
        ),
        TestCase(
            name="test_case_23",
            input_value=109,
            expected_output=91,
            description="Test case 23: input=109\n, expected=91\n"
        ),
        TestCase(
            name="test_case_24",
            input_value=190,
            expected_output=10,
            description="Test case 24: input=190\n, expected=10\n"
        ),
        TestCase(
            name="test_case_25",
            input_value=19,
            expected_output=1,
            description="Test case 25: input=19\n, expected=1\n"
        ),
        TestCase(
            name="test_case_26",
            input_value=8,
            expected_output=1,
            description="Test case 26: input=8\n, expected=1\n"
        ),
        TestCase(
            name="test_case_27",
            input_value=482,
            expected_output=18,
            description="Test case 27: input=482\n, expected=18\n"
        ),
        TestCase(
            name="test_case_28",
            input_value=1,
            expected_output=1,
            description="Test case 28: input=1\n, expected=1\n"
        ),
        TestCase(
            name="test_case_29",
            input_value=2,
            expected_output=1,
            description="Test case 29: input=2\n, expected=1\n"
        ),
        TestCase(
            name="test_case_30",
            input_value=3,
            expected_output=1,
            description="Test case 30: input=3\n, expected=1\n"
        ),
        TestCase(
            name="test_case_31",
            input_value=4,
            expected_output=1,
            description="Test case 31: input=4\n, expected=1\n"
        ),
        TestCase(
            name="test_case_32",
            input_value=5,
            expected_output=1,
            description="Test case 32: input=5\n, expected=1\n"
        ),
        TestCase(
            name="test_case_33",
            input_value=6,
            expected_output=1,
            description="Test case 33: input=6\n, expected=1\n"
        ),
        TestCase(
            name="test_case_34",
            input_value=7,
            expected_output=1,
            description="Test case 34: input=7\n, expected=1\n"
        ),
        TestCase(
            name="test_case_35",
            input_value=8,
            expected_output=1,
            description="Test case 35: input=8\n, expected=1\n"
        ),
        TestCase(
            name="test_case_36",
            input_value=9,
            expected_output=1,
            description="Test case 36: input=9\n, expected=1\n"
        ),
        TestCase(
            name="test_case_37",
            input_value=10,
            expected_output=10,
            description="Test case 37: input=10\n, expected=10\n"
        ),
        TestCase(
            name="test_case_38",
            input_value=11,
            expected_output=9,
            description="Test case 38: input=11\n, expected=9\n"
        ),
        TestCase(
            name="test_case_39",
            input_value=12,
            expected_output=8,
            description="Test case 39: input=12\n, expected=8\n"
        ),
        TestCase(
            name="test_case_40",
            input_value=13,
            expected_output=7,
            description="Test case 40: input=13\n, expected=7\n"
        ),
        TestCase(
            name="test_case_41",
            input_value=14,
            expected_output=6,
            description="Test case 41: input=14\n, expected=6\n"
        ),
        TestCase(
            name="test_case_42",
            input_value=15,
            expected_output=5,
            description="Test case 42: input=15\n, expected=5\n"
        ),
        TestCase(
            name="test_case_43",
            input_value=16,
            expected_output=4,
            description="Test case 43: input=16\n, expected=4\n"
        ),
        TestCase(
            name="test_case_44",
            input_value=17,
            expected_output=3,
            description="Test case 44: input=17\n, expected=3\n"
        ),
        TestCase(
            name="test_case_45",
            input_value=18,
            expected_output=2,
            description="Test case 45: input=18\n, expected=2\n"
        ),
        TestCase(
            name="test_case_46",
            input_value=19,
            expected_output=1,
            description="Test case 46: input=19\n, expected=1\n"
        ),
        TestCase(
            name="test_case_47",
            input_value=20,
            expected_output=10,
            description="Test case 47: input=20\n, expected=10\n"
        ),
        TestCase(
            name="test_case_48",
            input_value=21,
            expected_output=9,
            description="Test case 48: input=21\n, expected=9\n"
        ),
        TestCase(
            name="test_case_49",
            input_value=22,
            expected_output=8,
            description="Test case 49: input=22\n, expected=8\n"
        ),
        TestCase(
            name="test_case_50",
            input_value=23,
            expected_output=7,
            description="Test case 50: input=23\n, expected=7\n"
        ),
        TestCase(
            name="test_case_51",
            input_value=24,
            expected_output=6,
            description="Test case 51: input=24\n, expected=6\n"
        ),
        TestCase(
            name="test_case_52",
            input_value=25,
            expected_output=5,
            description="Test case 52: input=25\n, expected=5\n"
        ),
        TestCase(
            name="test_case_53",
            input_value=26,
            expected_output=4,
            description="Test case 53: input=26\n, expected=4\n"
        ),
        TestCase(
            name="test_case_54",
            input_value=27,
            expected_output=3,
            description="Test case 54: input=27\n, expected=3\n"
        ),
        TestCase(
            name="test_case_55",
            input_value=28,
            expected_output=2,
            description="Test case 55: input=28\n, expected=2\n"
        ),
        TestCase(
            name="test_case_56",
            input_value=29,
            expected_output=1,
            description="Test case 56: input=29\n, expected=1\n"
        ),
        TestCase(
            name="test_case_57",
            input_value=30,
            expected_output=10,
            description="Test case 57: input=30\n, expected=10\n"
        ),
        TestCase(
            name="test_case_58",
            input_value=31,
            expected_output=9,
            description="Test case 58: input=31\n, expected=9\n"
        ),
        TestCase(
            name="test_case_59",
            input_value=32,
            expected_output=8,
            description="Test case 59: input=32\n, expected=8\n"
        ),
        TestCase(
            name="test_case_60",
            input_value=33,
            expected_output=7,
            description="Test case 60: input=33\n, expected=7\n"
        ),
        TestCase(
            name="test_case_61",
            input_value=34,
            expected_output=6,
            description="Test case 61: input=34\n, expected=6\n"
        ),
        TestCase(
            name="test_case_62",
            input_value=35,
            expected_output=5,
            description="Test case 62: input=35\n, expected=5\n"
        ),
        TestCase(
            name="test_case_63",
            input_value=36,
            expected_output=4,
            description="Test case 63: input=36\n, expected=4\n"
        ),
        TestCase(
            name="test_case_64",
            input_value=37,
            expected_output=3,
            description="Test case 64: input=37\n, expected=3\n"
        ),
        TestCase(
            name="test_case_65",
            input_value=38,
            expected_output=2,
            description="Test case 65: input=38\n, expected=2\n"
        ),
        TestCase(
            name="test_case_66",
            input_value=39,
            expected_output=1,
            description="Test case 66: input=39\n, expected=1\n"
        ),
        TestCase(
            name="test_case_67",
            input_value=40,
            expected_output=10,
            description="Test case 67: input=40\n, expected=10\n"
        ),
        TestCase(
            name="test_case_68",
            input_value=41,
            expected_output=9,
            description="Test case 68: input=41\n, expected=9\n"
        ),
        TestCase(
            name="test_case_69",
            input_value=42,
            expected_output=8,
            description="Test case 69: input=42\n, expected=8\n"
        ),
        TestCase(
            name="test_case_70",
            input_value=43,
            expected_output=7,
            description="Test case 70: input=43\n, expected=7\n"
        ),
        TestCase(
            name="test_case_71",
            input_value=44,
            expected_output=6,
            description="Test case 71: input=44\n, expected=6\n"
        ),
        TestCase(
            name="test_case_72",
            input_value=45,
            expected_output=5,
            description="Test case 72: input=45\n, expected=5\n"
        ),
        TestCase(
            name="test_case_73",
            input_value=46,
            expected_output=4,
            description="Test case 73: input=46\n, expected=4\n"
        ),
        TestCase(
            name="test_case_74",
            input_value=47,
            expected_output=3,
            description="Test case 74: input=47\n, expected=3\n"
        ),
        TestCase(
            name="test_case_75",
            input_value=48,
            expected_output=2,
            description="Test case 75: input=48\n, expected=2\n"
        ),
        TestCase(
            name="test_case_76",
            input_value=49,
            expected_output=1,
            description="Test case 76: input=49\n, expected=1\n"
        ),
        TestCase(
            name="test_case_77",
            input_value=50,
            expected_output=10,
            description="Test case 77: input=50\n, expected=10\n"
        ),
        TestCase(
            name="test_case_78",
            input_value=51,
            expected_output=9,
            description="Test case 78: input=51\n, expected=9\n"
        ),
        TestCase(
            name="test_case_79",
            input_value=52,
            expected_output=8,
            description="Test case 79: input=52\n, expected=8\n"
        ),
        TestCase(
            name="test_case_80",
            input_value=53,
            expected_output=7,
            description="Test case 80: input=53\n, expected=7\n"
        ),
        TestCase(
            name="test_case_81",
            input_value=54,
            expected_output=6,
            description="Test case 81: input=54\n, expected=6\n"
        ),
        TestCase(
            name="test_case_82",
            input_value=55,
            expected_output=5,
            description="Test case 82: input=55\n, expected=5\n"
        ),
        TestCase(
            name="test_case_83",
            input_value=56,
            expected_output=4,
            description="Test case 83: input=56\n, expected=4\n"
        ),
        TestCase(
            name="test_case_84",
            input_value=57,
            expected_output=3,
            description="Test case 84: input=57\n, expected=3\n"
        ),
        TestCase(
            name="test_case_85",
            input_value=58,
            expected_output=2,
            description="Test case 85: input=58\n, expected=2\n"
        ),
        TestCase(
            name="test_case_86",
            input_value=59,
            expected_output=1,
            description="Test case 86: input=59\n, expected=1\n"
        ),
        TestCase(
            name="test_case_87",
            input_value=60,
            expected_output=10,
            description="Test case 87: input=60\n, expected=10\n"
        ),
        TestCase(
            name="test_case_88",
            input_value=61,
            expected_output=9,
            description="Test case 88: input=61\n, expected=9\n"
        ),
        TestCase(
            name="test_case_89",
            input_value=62,
            expected_output=8,
            description="Test case 89: input=62\n, expected=8\n"
        ),
        TestCase(
            name="test_case_90",
            input_value=63,
            expected_output=7,
            description="Test case 90: input=63\n, expected=7\n"
        ),
        TestCase(
            name="test_case_91",
            input_value=64,
            expected_output=6,
            description="Test case 91: input=64\n, expected=6\n"
        ),
        TestCase(
            name="test_case_92",
            input_value=65,
            expected_output=5,
            description="Test case 92: input=65\n, expected=5\n"
        ),
        TestCase(
            name="test_case_93",
            input_value=66,
            expected_output=4,
            description="Test case 93: input=66\n, expected=4\n"
        ),
        TestCase(
            name="test_case_94",
            input_value=67,
            expected_output=3,
            description="Test case 94: input=67\n, expected=3\n"
        ),
        TestCase(
            name="test_case_95",
            input_value=68,
            expected_output=2,
            description="Test case 95: input=68\n, expected=2\n"
        ),
        TestCase(
            name="test_case_96",
            input_value=69,
            expected_output=1,
            description="Test case 96: input=69\n, expected=1\n"
        ),
        TestCase(
            name="test_case_97",
            input_value=70,
            expected_output=10,
            description="Test case 97: input=70\n, expected=10\n"
        ),
        TestCase(
            name="test_case_98",
            input_value=71,
            expected_output=9,
            description="Test case 98: input=71\n, expected=9\n"
        ),
        TestCase(
            name="test_case_99",
            input_value=72,
            expected_output=8,
            description="Test case 99: input=72\n, expected=8\n"
        ),
        TestCase(
            name="test_case_100",
            input_value=73,
            expected_output=7,
            description="Test case 100: input=73\n, expected=7\n"
        ),
        TestCase(
            name="test_case_101",
            input_value=74,
            expected_output=6,
            description="Test case 101: input=74\n, expected=6\n"
        ),
        TestCase(
            name="test_case_102",
            input_value=75,
            expected_output=5,
            description="Test case 102: input=75\n, expected=5\n"
        ),
        TestCase(
            name="test_case_103",
            input_value=76,
            expected_output=4,
            description="Test case 103: input=76\n, expected=4\n"
        ),
        TestCase(
            name="test_case_104",
            input_value=77,
            expected_output=3,
            description="Test case 104: input=77\n, expected=3\n"
        ),
        TestCase(
            name="test_case_105",
            input_value=78,
            expected_output=2,
            description="Test case 105: input=78\n, expected=2\n"
        ),
        TestCase(
            name="test_case_106",
            input_value=79,
            expected_output=1,
            description="Test case 106: input=79\n, expected=1\n"
        ),
        TestCase(
            name="test_case_107",
            input_value=80,
            expected_output=10,
            description="Test case 107: input=80\n, expected=10\n"
        ),
        TestCase(
            name="test_case_108",
            input_value=81,
            expected_output=9,
            description="Test case 108: input=81\n, expected=9\n"
        ),
        TestCase(
            name="test_case_109",
            input_value=82,
            expected_output=8,
            description="Test case 109: input=82\n, expected=8\n"
        ),
        TestCase(
            name="test_case_110",
            input_value=83,
            expected_output=7,
            description="Test case 110: input=83\n, expected=7\n"
        ),
        TestCase(
            name="test_case_111",
            input_value=84,
            expected_output=6,
            description="Test case 111: input=84\n, expected=6\n"
        ),
        TestCase(
            name="test_case_112",
            input_value=85,
            expected_output=5,
            description="Test case 112: input=85\n, expected=5\n"
        ),
        TestCase(
            name="test_case_113",
            input_value=86,
            expected_output=4,
            description="Test case 113: input=86\n, expected=4\n"
        ),
        TestCase(
            name="test_case_114",
            input_value=87,
            expected_output=3,
            description="Test case 114: input=87\n, expected=3\n"
        ),
        TestCase(
            name="test_case_115",
            input_value=88,
            expected_output=2,
            description="Test case 115: input=88\n, expected=2\n"
        ),
        TestCase(
            name="test_case_116",
            input_value=89,
            expected_output=1,
            description="Test case 116: input=89\n, expected=1\n"
        ),
        TestCase(
            name="test_case_117",
            input_value=90,
            expected_output=10,
            description="Test case 117: input=90\n, expected=10\n"
        ),
        TestCase(
            name="test_case_118",
            input_value=91,
            expected_output=9,
            description="Test case 118: input=91\n, expected=9\n"
        ),
        TestCase(
            name="test_case_119",
            input_value=92,
            expected_output=8,
            description="Test case 119: input=92\n, expected=8\n"
        ),
        TestCase(
            name="test_case_120",
            input_value=93,
            expected_output=7,
            description="Test case 120: input=93\n, expected=7\n"
        ),
        TestCase(
            name="test_case_121",
            input_value=94,
            expected_output=6,
            description="Test case 121: input=94\n, expected=6\n"
        ),
        TestCase(
            name="test_case_122",
            input_value=95,
            expected_output=5,
            description="Test case 122: input=95\n, expected=5\n"
        ),
        TestCase(
            name="test_case_123",
            input_value=96,
            expected_output=4,
            description="Test case 123: input=96\n, expected=4\n"
        ),
        TestCase(
            name="test_case_124",
            input_value=97,
            expected_output=3,
            description="Test case 124: input=97\n, expected=3\n"
        ),
        TestCase(
            name="test_case_125",
            input_value=98,
            expected_output=2,
            description="Test case 125: input=98\n, expected=2\n"
        ),
        TestCase(
            name="test_case_126",
            input_value=99,
            expected_output=1,
            description="Test case 126: input=99\n, expected=1\n"
        ),
        TestCase(
            name="test_case_127",
            input_value=100,
            expected_output=100,
            description="Test case 127: input=100\n, expected=100\n"
        ),
        TestCase(
            name="test_case_128",
            input_value=100,
            expected_output=100,
            description="Test case 128: input=100\n, expected=100\n"
        ),
        TestCase(
            name="test_case_129",
            input_value=100,
            expected_output=100,
            description="Test case 129: input=100\n, expected=100\n"
        ),
        TestCase(
            name="test_case_130",
            input_value=1000,
            expected_output=1000,
            description="Test case 130: input=1000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_131",
            input_value=1000,
            expected_output=1000,
            description="Test case 131: input=1000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_132",
            input_value=1000,
            expected_output=1000,
            description="Test case 132: input=1000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_133",
            input_value=10000,
            expected_output=10000,
            description="Test case 133: input=10000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_134",
            input_value=10000,
            expected_output=10000,
            description="Test case 134: input=10000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_135",
            input_value=101,
            expected_output=99,
            description="Test case 135: input=101\n, expected=99\n"
        ),
        TestCase(
            name="test_case_136",
            input_value=110,
            expected_output=90,
            description="Test case 136: input=110\n, expected=90\n"
        ),
        TestCase(
            name="test_case_137",
            input_value=1001,
            expected_output=999,
            description="Test case 137: input=1001\n, expected=999\n"
        ),
        TestCase(
            name="test_case_138",
            input_value=1100,
            expected_output=900,
            description="Test case 138: input=1100\n, expected=900\n"
        ),
        TestCase(
            name="test_case_139",
            input_value=1010,
            expected_output=990,
            description="Test case 139: input=1010\n, expected=990\n"
        ),
        TestCase(
            name="test_case_140",
            input_value=10010,
            expected_output=9990,
            description="Test case 140: input=10010\n, expected=9990\n"
        ),
        TestCase(
            name="test_case_141",
            input_value=10100,
            expected_output=9900,
            description="Test case 141: input=10100\n, expected=9900\n"
        ),
        TestCase(
            name="test_case_142",
            input_value=102,
            expected_output=98,
            description="Test case 142: input=102\n, expected=98\n"
        ),
        TestCase(
            name="test_case_143",
            input_value=120,
            expected_output=80,
            description="Test case 143: input=120\n, expected=80\n"
        ),
        TestCase(
            name="test_case_144",
            input_value=1002,
            expected_output=998,
            description="Test case 144: input=1002\n, expected=998\n"
        ),
        TestCase(
            name="test_case_145",
            input_value=1200,
            expected_output=800,
            description="Test case 145: input=1200\n, expected=800\n"
        ),
        TestCase(
            name="test_case_146",
            input_value=1020,
            expected_output=980,
            description="Test case 146: input=1020\n, expected=980\n"
        ),
        TestCase(
            name="test_case_147",
            input_value=10020,
            expected_output=9980,
            description="Test case 147: input=10020\n, expected=9980\n"
        ),
        TestCase(
            name="test_case_148",
            input_value=10200,
            expected_output=9800,
            description="Test case 148: input=10200\n, expected=9800\n"
        ),
        TestCase(
            name="test_case_149",
            input_value=108,
            expected_output=92,
            description="Test case 149: input=108\n, expected=92\n"
        ),
        TestCase(
            name="test_case_150",
            input_value=180,
            expected_output=20,
            description="Test case 150: input=180\n, expected=20\n"
        ),
        TestCase(
            name="test_case_151",
            input_value=1008,
            expected_output=992,
            description="Test case 151: input=1008\n, expected=992\n"
        ),
        TestCase(
            name="test_case_152",
            input_value=1800,
            expected_output=200,
            description="Test case 152: input=1800\n, expected=200\n"
        ),
        TestCase(
            name="test_case_153",
            input_value=1080,
            expected_output=920,
            description="Test case 153: input=1080\n, expected=920\n"
        ),
        TestCase(
            name="test_case_154",
            input_value=10080,
            expected_output=9920,
            description="Test case 154: input=10080\n, expected=9920\n"
        ),
        TestCase(
            name="test_case_155",
            input_value=10800,
            expected_output=9200,
            description="Test case 155: input=10800\n, expected=9200\n"
        ),
        TestCase(
            name="test_case_156",
            input_value=109,
            expected_output=91,
            description="Test case 156: input=109\n, expected=91\n"
        ),
        TestCase(
            name="test_case_157",
            input_value=190,
            expected_output=10,
            description="Test case 157: input=190\n, expected=10\n"
        ),
        TestCase(
            name="test_case_158",
            input_value=1009,
            expected_output=991,
            description="Test case 158: input=1009\n, expected=991\n"
        ),
        TestCase(
            name="test_case_159",
            input_value=1900,
            expected_output=100,
            description="Test case 159: input=1900\n, expected=100\n"
        ),
        TestCase(
            name="test_case_160",
            input_value=1090,
            expected_output=910,
            description="Test case 160: input=1090\n, expected=910\n"
        ),
        TestCase(
            name="test_case_161",
            input_value=10090,
            expected_output=9910,
            description="Test case 161: input=10090\n, expected=9910\n"
        ),
        TestCase(
            name="test_case_162",
            input_value=10900,
            expected_output=9100,
            description="Test case 162: input=10900\n, expected=9100\n"
        ),
        TestCase(
            name="test_case_163",
            input_value=200,
            expected_output=100,
            description="Test case 163: input=200\n, expected=100\n"
        ),
        TestCase(
            name="test_case_164",
            input_value=200,
            expected_output=100,
            description="Test case 164: input=200\n, expected=100\n"
        ),
        TestCase(
            name="test_case_165",
            input_value=2000,
            expected_output=1000,
            description="Test case 165: input=2000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_166",
            input_value=2000,
            expected_output=1000,
            description="Test case 166: input=2000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_167",
            input_value=2000,
            expected_output=1000,
            description="Test case 167: input=2000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_168",
            input_value=20000,
            expected_output=10000,
            description="Test case 168: input=20000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_169",
            input_value=20000,
            expected_output=10000,
            description="Test case 169: input=20000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_170",
            input_value=201,
            expected_output=99,
            description="Test case 170: input=201\n, expected=99\n"
        ),
        TestCase(
            name="test_case_171",
            input_value=210,
            expected_output=90,
            description="Test case 171: input=210\n, expected=90\n"
        ),
        TestCase(
            name="test_case_172",
            input_value=2001,
            expected_output=999,
            description="Test case 172: input=2001\n, expected=999\n"
        ),
        TestCase(
            name="test_case_173",
            input_value=2100,
            expected_output=900,
            description="Test case 173: input=2100\n, expected=900\n"
        ),
        TestCase(
            name="test_case_174",
            input_value=2010,
            expected_output=990,
            description="Test case 174: input=2010\n, expected=990\n"
        ),
        TestCase(
            name="test_case_175",
            input_value=20010,
            expected_output=9990,
            description="Test case 175: input=20010\n, expected=9990\n"
        ),
        TestCase(
            name="test_case_176",
            input_value=20100,
            expected_output=9900,
            description="Test case 176: input=20100\n, expected=9900\n"
        ),
        TestCase(
            name="test_case_177",
            input_value=202,
            expected_output=98,
            description="Test case 177: input=202\n, expected=98\n"
        ),
        TestCase(
            name="test_case_178",
            input_value=220,
            expected_output=80,
            description="Test case 178: input=220\n, expected=80\n"
        ),
        TestCase(
            name="test_case_179",
            input_value=2002,
            expected_output=998,
            description="Test case 179: input=2002\n, expected=998\n"
        ),
        TestCase(
            name="test_case_180",
            input_value=2200,
            expected_output=800,
            description="Test case 180: input=2200\n, expected=800\n"
        ),
        TestCase(
            name="test_case_181",
            input_value=2020,
            expected_output=980,
            description="Test case 181: input=2020\n, expected=980\n"
        ),
        TestCase(
            name="test_case_182",
            input_value=20020,
            expected_output=9980,
            description="Test case 182: input=20020\n, expected=9980\n"
        ),
        TestCase(
            name="test_case_183",
            input_value=20200,
            expected_output=9800,
            description="Test case 183: input=20200\n, expected=9800\n"
        ),
        TestCase(
            name="test_case_184",
            input_value=208,
            expected_output=92,
            description="Test case 184: input=208\n, expected=92\n"
        ),
        TestCase(
            name="test_case_185",
            input_value=280,
            expected_output=20,
            description="Test case 185: input=280\n, expected=20\n"
        ),
        TestCase(
            name="test_case_186",
            input_value=2008,
            expected_output=992,
            description="Test case 186: input=2008\n, expected=992\n"
        ),
        TestCase(
            name="test_case_187",
            input_value=2800,
            expected_output=200,
            description="Test case 187: input=2800\n, expected=200\n"
        ),
        TestCase(
            name="test_case_188",
            input_value=2080,
            expected_output=920,
            description="Test case 188: input=2080\n, expected=920\n"
        ),
        TestCase(
            name="test_case_189",
            input_value=20080,
            expected_output=9920,
            description="Test case 189: input=20080\n, expected=9920\n"
        ),
        TestCase(
            name="test_case_190",
            input_value=20800,
            expected_output=9200,
            description="Test case 190: input=20800\n, expected=9200\n"
        ),
        TestCase(
            name="test_case_191",
            input_value=209,
            expected_output=91,
            description="Test case 191: input=209\n, expected=91\n"
        ),
        TestCase(
            name="test_case_192",
            input_value=290,
            expected_output=10,
            description="Test case 192: input=290\n, expected=10\n"
        ),
        TestCase(
            name="test_case_193",
            input_value=2009,
            expected_output=991,
            description="Test case 193: input=2009\n, expected=991\n"
        ),
        TestCase(
            name="test_case_194",
            input_value=2900,
            expected_output=100,
            description="Test case 194: input=2900\n, expected=100\n"
        ),
        TestCase(
            name="test_case_195",
            input_value=2090,
            expected_output=910,
            description="Test case 195: input=2090\n, expected=910\n"
        ),
        TestCase(
            name="test_case_196",
            input_value=20090,
            expected_output=9910,
            description="Test case 196: input=20090\n, expected=9910\n"
        ),
        TestCase(
            name="test_case_197",
            input_value=20900,
            expected_output=9100,
            description="Test case 197: input=20900\n, expected=9100\n"
        ),
        TestCase(
            name="test_case_198",
            input_value=800,
            expected_output=100,
            description="Test case 198: input=800\n, expected=100\n"
        ),
        TestCase(
            name="test_case_199",
            input_value=800,
            expected_output=100,
            description="Test case 199: input=800\n, expected=100\n"
        ),
        TestCase(
            name="test_case_200",
            input_value=8000,
            expected_output=1000,
            description="Test case 200: input=8000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_201",
            input_value=8000,
            expected_output=1000,
            description="Test case 201: input=8000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_202",
            input_value=8000,
            expected_output=1000,
            description="Test case 202: input=8000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_203",
            input_value=80000,
            expected_output=10000,
            description="Test case 203: input=80000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_204",
            input_value=80000,
            expected_output=10000,
            description="Test case 204: input=80000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_205",
            input_value=801,
            expected_output=99,
            description="Test case 205: input=801\n, expected=99\n"
        ),
        TestCase(
            name="test_case_206",
            input_value=810,
            expected_output=90,
            description="Test case 206: input=810\n, expected=90\n"
        ),
        TestCase(
            name="test_case_207",
            input_value=8001,
            expected_output=999,
            description="Test case 207: input=8001\n, expected=999\n"
        ),
        TestCase(
            name="test_case_208",
            input_value=8100,
            expected_output=900,
            description="Test case 208: input=8100\n, expected=900\n"
        ),
        TestCase(
            name="test_case_209",
            input_value=8010,
            expected_output=990,
            description="Test case 209: input=8010\n, expected=990\n"
        ),
        TestCase(
            name="test_case_210",
            input_value=80010,
            expected_output=9990,
            description="Test case 210: input=80010\n, expected=9990\n"
        ),
        TestCase(
            name="test_case_211",
            input_value=80100,
            expected_output=9900,
            description="Test case 211: input=80100\n, expected=9900\n"
        ),
        TestCase(
            name="test_case_212",
            input_value=802,
            expected_output=98,
            description="Test case 212: input=802\n, expected=98\n"
        ),
        TestCase(
            name="test_case_213",
            input_value=820,
            expected_output=80,
            description="Test case 213: input=820\n, expected=80\n"
        ),
        TestCase(
            name="test_case_214",
            input_value=8002,
            expected_output=998,
            description="Test case 214: input=8002\n, expected=998\n"
        ),
        TestCase(
            name="test_case_215",
            input_value=8200,
            expected_output=800,
            description="Test case 215: input=8200\n, expected=800\n"
        ),
        TestCase(
            name="test_case_216",
            input_value=8020,
            expected_output=980,
            description="Test case 216: input=8020\n, expected=980\n"
        ),
        TestCase(
            name="test_case_217",
            input_value=80020,
            expected_output=9980,
            description="Test case 217: input=80020\n, expected=9980\n"
        ),
        TestCase(
            name="test_case_218",
            input_value=80200,
            expected_output=9800,
            description="Test case 218: input=80200\n, expected=9800\n"
        ),
        TestCase(
            name="test_case_219",
            input_value=808,
            expected_output=92,
            description="Test case 219: input=808\n, expected=92\n"
        ),
        TestCase(
            name="test_case_220",
            input_value=880,
            expected_output=20,
            description="Test case 220: input=880\n, expected=20\n"
        ),
        TestCase(
            name="test_case_221",
            input_value=8008,
            expected_output=992,
            description="Test case 221: input=8008\n, expected=992\n"
        ),
        TestCase(
            name="test_case_222",
            input_value=8800,
            expected_output=200,
            description="Test case 222: input=8800\n, expected=200\n"
        ),
        TestCase(
            name="test_case_223",
            input_value=8080,
            expected_output=920,
            description="Test case 223: input=8080\n, expected=920\n"
        ),
        TestCase(
            name="test_case_224",
            input_value=80080,
            expected_output=9920,
            description="Test case 224: input=80080\n, expected=9920\n"
        ),
        TestCase(
            name="test_case_225",
            input_value=80800,
            expected_output=9200,
            description="Test case 225: input=80800\n, expected=9200\n"
        ),
        TestCase(
            name="test_case_226",
            input_value=809,
            expected_output=91,
            description="Test case 226: input=809\n, expected=91\n"
        ),
        TestCase(
            name="test_case_227",
            input_value=890,
            expected_output=10,
            description="Test case 227: input=890\n, expected=10\n"
        ),
        TestCase(
            name="test_case_228",
            input_value=8009,
            expected_output=991,
            description="Test case 228: input=8009\n, expected=991\n"
        ),
        TestCase(
            name="test_case_229",
            input_value=8900,
            expected_output=100,
            description="Test case 229: input=8900\n, expected=100\n"
        ),
        TestCase(
            name="test_case_230",
            input_value=8090,
            expected_output=910,
            description="Test case 230: input=8090\n, expected=910\n"
        ),
        TestCase(
            name="test_case_231",
            input_value=80090,
            expected_output=9910,
            description="Test case 231: input=80090\n, expected=9910\n"
        ),
        TestCase(
            name="test_case_232",
            input_value=80900,
            expected_output=9100,
            description="Test case 232: input=80900\n, expected=9100\n"
        ),
        TestCase(
            name="test_case_233",
            input_value=900,
            expected_output=100,
            description="Test case 233: input=900\n, expected=100\n"
        ),
        TestCase(
            name="test_case_234",
            input_value=900,
            expected_output=100,
            description="Test case 234: input=900\n, expected=100\n"
        ),
        TestCase(
            name="test_case_235",
            input_value=9000,
            expected_output=1000,
            description="Test case 235: input=9000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_236",
            input_value=9000,
            expected_output=1000,
            description="Test case 236: input=9000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_237",
            input_value=9000,
            expected_output=1000,
            description="Test case 237: input=9000\n, expected=1000\n"
        ),
        TestCase(
            name="test_case_238",
            input_value=90000,
            expected_output=10000,
            description="Test case 238: input=90000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_239",
            input_value=90000,
            expected_output=10000,
            description="Test case 239: input=90000\n, expected=10000\n"
        ),
        TestCase(
            name="test_case_240",
            input_value=901,
            expected_output=99,
            description="Test case 240: input=901\n, expected=99\n"
        ),
        TestCase(
            name="test_case_241",
            input_value=910,
            expected_output=90,
            description="Test case 241: input=910\n, expected=90\n"
        ),
        TestCase(
            name="test_case_242",
            input_value=9001,
            expected_output=999,
            description="Test case 242: input=9001\n, expected=999\n"
        ),
        TestCase(
            name="test_case_243",
            input_value=9100,
            expected_output=900,
            description="Test case 243: input=9100\n, expected=900\n"
        ),
        TestCase(
            name="test_case_244",
            input_value=9010,
            expected_output=990,
            description="Test case 244: input=9010\n, expected=990\n"
        ),
        TestCase(
            name="test_case_245",
            input_value=90010,
            expected_output=9990,
            description="Test case 245: input=90010\n, expected=9990\n"
        ),
        TestCase(
            name="test_case_246",
            input_value=90100,
            expected_output=9900,
            description="Test case 246: input=90100\n, expected=9900\n"
        ),
        TestCase(
            name="test_case_247",
            input_value=902,
            expected_output=98,
            description="Test case 247: input=902\n, expected=98\n"
        ),
        TestCase(
            name="test_case_248",
            input_value=920,
            expected_output=80,
            description="Test case 248: input=920\n, expected=80\n"
        ),
        TestCase(
            name="test_case_249",
            input_value=9002,
            expected_output=998,
            description="Test case 249: input=9002\n, expected=998\n"
        ),
        TestCase(
            name="test_case_250",
            input_value=9200,
            expected_output=800,
            description="Test case 250: input=9200\n, expected=800\n"
        ),
        TestCase(
            name="test_case_251",
            input_value=9020,
            expected_output=980,
            description="Test case 251: input=9020\n, expected=980\n"
        ),
        TestCase(
            name="test_case_252",
            input_value=90020,
            expected_output=9980,
            description="Test case 252: input=90020\n, expected=9980\n"
        ),
        TestCase(
            name="test_case_253",
            input_value=90200,
            expected_output=9800,
            description="Test case 253: input=90200\n, expected=9800\n"
        ),
        TestCase(
            name="test_case_254",
            input_value=908,
            expected_output=92,
            description="Test case 254: input=908\n, expected=92\n"
        ),
        TestCase(
            name="test_case_255",
            input_value=980,
            expected_output=20,
            description="Test case 255: input=980\n, expected=20\n"
        ),
        TestCase(
            name="test_case_256",
            input_value=9008,
            expected_output=992,
            description="Test case 256: input=9008\n, expected=992\n"
        ),
        TestCase(
            name="test_case_257",
            input_value=9800,
            expected_output=200,
            description="Test case 257: input=9800\n, expected=200\n"
        ),
        TestCase(
            name="test_case_258",
            input_value=9080,
            expected_output=920,
            description="Test case 258: input=9080\n, expected=920\n"
        ),
        TestCase(
            name="test_case_259",
            input_value=90080,
            expected_output=9920,
            description="Test case 259: input=90080\n, expected=9920\n"
        ),
        TestCase(
            name="test_case_260",
            input_value=90800,
            expected_output=9200,
            description="Test case 260: input=90800\n, expected=9200\n"
        ),
        TestCase(
            name="test_case_261",
            input_value=909,
            expected_output=91,
            description="Test case 261: input=909\n, expected=91\n"
        ),
        TestCase(
            name="test_case_262",
            input_value=990,
            expected_output=10,
            description="Test case 262: input=990\n, expected=10\n"
        ),
        TestCase(
            name="test_case_263",
            input_value=9009,
            expected_output=991,
            description="Test case 263: input=9009\n, expected=991\n"
        ),
        TestCase(
            name="test_case_264",
            input_value=9900,
            expected_output=100,
            description="Test case 264: input=9900\n, expected=100\n"
        ),
        TestCase(
            name="test_case_265",
            input_value=9090,
            expected_output=910,
            description="Test case 265: input=9090\n, expected=910\n"
        ),
        TestCase(
            name="test_case_266",
            input_value=90090,
            expected_output=9910,
            description="Test case 266: input=90090\n, expected=9910\n"
        ),
        TestCase(
            name="test_case_267",
            input_value=90900,
            expected_output=9100,
            description="Test case 267: input=90900\n, expected=9100\n"
        ),
        TestCase(
            name="test_case_268",
            input_value=92651241,
            expected_output=7348759,
            description="Test case 268: input=92651241\n, expected=7348759\n"
        ),
    ]
    
    return Problem(
        name="apps_0002",
        description=r"""Apart from having lots of holidays throughout the year, residents of Berland also have whole lucky years. Year is considered lucky if it has no more than 1 non-zero digit in its number. So years 100, 40000, 5 are lucky and 12, 3001 and 12345 are not.

You are given current year in Berland. Your task is to find how long ago was the PREVIOUS lucky year (i.e., how many years have passed since the last lucky year).


-----Input-----

The first line contains integer number n (1 ≤ n ≤ 10^9) — current year in Berland.


-----Output-----

Output amount of years from the PREVIOUS lucky year to the current year.


-----Examples-----
Input
4

Output
1

Input
201

Output
99

Input
4000

Output
1000



-----Note-----

In the first example next lucky year is 5. In the second one — 300. In the third — 5000.""",
        function_signature="def main():",
        visible_tests=visible_tests,
        hidden_tests=hidden_tests
    )