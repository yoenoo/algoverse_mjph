"""
apps_0001 problem from APPS dataset.
"""

from typing import List
from ...core.problem import Problem, TestCase


def create_apps_0001() -> Problem:
    """
    Create the apps_0001 problem.
    """
    # Visible tests (shown to the model)
    visible_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value=100,
            expected_output=99,
            description="Test case 1: input=100\n, expected=99\n"
        ),
        TestCase(
            name="test_case_2",
            input_value=48,
            expected_output=48,
            description="Test case 2: input=48\n, expected=48\n"
        ),
        TestCase(
            name="test_case_3",
            input_value=521,
            expected_output=499,
            description="Test case 3: input=521\n, expected=499\n"
        ),
    ]
    
    # Hidden tests (not shown to model, used for validation)
    hidden_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value=1,
            expected_output=1,
            description="Test case 1: input=1\n, expected=1\n"
        ),
        TestCase(
            name="test_case_2",
            input_value=2,
            expected_output=2,
            description="Test case 2: input=2\n, expected=2\n"
        ),
        TestCase(
            name="test_case_3",
            input_value=3,
            expected_output=3,
            description="Test case 3: input=3\n, expected=3\n"
        ),
        TestCase(
            name="test_case_4",
            input_value=39188,
            expected_output=38999,
            description="Test case 4: input=39188\n, expected=38999\n"
        ),
        TestCase(
            name="test_case_5",
            input_value=5,
            expected_output=5,
            description="Test case 5: input=5\n, expected=5\n"
        ),
        TestCase(
            name="test_case_6",
            input_value=6,
            expected_output=6,
            description="Test case 6: input=6\n, expected=6\n"
        ),
        TestCase(
            name="test_case_7",
            input_value=7,
            expected_output=7,
            description="Test case 7: input=7\n, expected=7\n"
        ),
        TestCase(
            name="test_case_8",
            input_value=8,
            expected_output=8,
            description="Test case 8: input=8\n, expected=8\n"
        ),
        TestCase(
            name="test_case_9",
            input_value=9,
            expected_output=9,
            description="Test case 9: input=9\n, expected=9\n"
        ),
        TestCase(
            name="test_case_10",
            input_value=10,
            expected_output=9,
            description="Test case 10: input=10\n, expected=9\n"
        ),
        TestCase(
            name="test_case_11",
            input_value=59999154,
            expected_output=59998999,
            description="Test case 11: input=59999154\n, expected=59998999\n"
        ),
        TestCase(
            name="test_case_12",
            input_value=1000,
            expected_output=999,
            description="Test case 12: input=1000\n, expected=999\n"
        ),
        TestCase(
            name="test_case_13",
            input_value=10000,
            expected_output=9999,
            description="Test case 13: input=10000\n, expected=9999\n"
        ),
        TestCase(
            name="test_case_14",
            input_value=100000,
            expected_output=99999,
            description="Test case 14: input=100000\n, expected=99999\n"
        ),
        TestCase(
            name="test_case_15",
            input_value=1000000,
            expected_output=999999,
            description="Test case 15: input=1000000\n, expected=999999\n"
        ),
        TestCase(
            name="test_case_16",
            input_value=10000000,
            expected_output=9999999,
            description="Test case 16: input=10000000\n, expected=9999999\n"
        ),
        TestCase(
            name="test_case_17",
            input_value=100000000,
            expected_output=99999999,
            description="Test case 17: input=100000000\n, expected=99999999\n"
        ),
        TestCase(
            name="test_case_18",
            input_value=1000000000,
            expected_output=999999999,
            description="Test case 18: input=1000000000\n, expected=999999999\n"
        ),
        TestCase(
            name="test_case_19",
            input_value=10000000000,
            expected_output=9999999999,
            description="Test case 19: input=10000000000\n, expected=9999999999\n"
        ),
        TestCase(
            name="test_case_20",
            input_value=100000000000,
            expected_output=99999999999,
            description="Test case 20: input=100000000000\n, expected=99999999999\n"
        ),
        TestCase(
            name="test_case_21",
            input_value=1000000000000,
            expected_output=999999999999,
            description="Test case 21: input=1000000000000\n, expected=999999999999\n"
        ),
        TestCase(
            name="test_case_22",
            input_value=10000000000000,
            expected_output=9999999999999,
            description="Test case 22: input=10000000000000\n, expected=9999999999999\n"
        ),
        TestCase(
            name="test_case_23",
            input_value=100000000000000,
            expected_output=99999999999999,
            description="Test case 23: input=100000000000000\n, expected=99999999999999\n"
        ),
        TestCase(
            name="test_case_24",
            input_value=1000000000000000,
            expected_output=999999999999999,
            description="Test case 24: input=1000000000000000\n, expected=999999999999999\n"
        ),
        TestCase(
            name="test_case_25",
            input_value=10000000000000000,
            expected_output=9999999999999999,
            description="Test case 25: input=10000000000000000\n, expected=9999999999999999\n"
        ),
        TestCase(
            name="test_case_26",
            input_value=100000000000000000,
            expected_output=99999999999999999,
            description="Test case 26: input=100000000000000000\n, expected=99999999999999999\n"
        ),
        TestCase(
            name="test_case_27",
            input_value=1000000000000000000,
            expected_output=999999999999999999,
            description="Test case 27: input=1000000000000000000\n, expected=999999999999999999\n"
        ),
        TestCase(
            name="test_case_28",
            input_value=999999990,
            expected_output=999999989,
            description="Test case 28: input=999999990\n, expected=999999989\n"
        ),
        TestCase(
            name="test_case_29",
            input_value=666666899789879,
            expected_output=599999999999999,
            description="Test case 29: input=666666899789879\n, expected=599999999999999\n"
        ),
        TestCase(
            name="test_case_30",
            input_value=65499992294999000,
            expected_output=59999999999999999,
            description="Test case 30: input=65499992294999000\n, expected=59999999999999999\n"
        ),
        TestCase(
            name="test_case_31",
            input_value=9879100000000099,
            expected_output=8999999999999999,
            description="Test case 31: input=9879100000000099\n, expected=8999999999999999\n"
        ),
        TestCase(
            name="test_case_32",
            input_value=9991919190909919,
            expected_output=9989999999999999,
            description="Test case 32: input=9991919190909919\n, expected=9989999999999999\n"
        ),
        TestCase(
            name="test_case_33",
            input_value=978916546899999999,
            expected_output=899999999999999999,
            description="Test case 33: input=978916546899999999\n, expected=899999999999999999\n"
        ),
        TestCase(
            name="test_case_34",
            input_value=5684945999999999,
            expected_output=4999999999999999,
            description="Test case 34: input=5684945999999999\n, expected=4999999999999999\n"
        ),
        TestCase(
            name="test_case_35",
            input_value=999999999999999999,
            expected_output=999999999999999999,
            description="Test case 35: input=999999999999999999\n, expected=999999999999999999\n"
        ),
        TestCase(
            name="test_case_36",
            input_value=999999999999990999,
            expected_output=999999999999989999,
            description="Test case 36: input=999999999999990999\n, expected=999999999999989999\n"
        ),
        TestCase(
            name="test_case_37",
            input_value=999999999999999990,
            expected_output=999999999999999989,
            description="Test case 37: input=999999999999999990\n, expected=999999999999999989\n"
        ),
        TestCase(
            name="test_case_38",
            input_value=909999999999999999,
            expected_output=899999999999999999,
            description="Test case 38: input=909999999999999999\n, expected=899999999999999999\n"
        ),
        TestCase(
            name="test_case_39",
            input_value=199999999999999999,
            expected_output=199999999999999999,
            description="Test case 39: input=199999999999999999\n, expected=199999999999999999\n"
        ),
        TestCase(
            name="test_case_40",
            input_value=299999999999999999,
            expected_output=299999999999999999,
            description="Test case 40: input=299999999999999999\n, expected=299999999999999999\n"
        ),
        TestCase(
            name="test_case_41",
            input_value=999999990009999999,
            expected_output=999999989999999999,
            description="Test case 41: input=999999990009999999\n, expected=999999989999999999\n"
        ),
        TestCase(
            name="test_case_42",
            input_value=999000000001999999,
            expected_output=998999999999999999,
            description="Test case 42: input=999000000001999999\n, expected=998999999999999999\n"
        ),
        TestCase(
            name="test_case_43",
            input_value=999999999991,
            expected_output=999999999989,
            description="Test case 43: input=999999999991\n, expected=999999999989\n"
        ),
        TestCase(
            name="test_case_44",
            input_value=999999999992,
            expected_output=999999999989,
            description="Test case 44: input=999999999992\n, expected=999999999989\n"
        ),
        TestCase(
            name="test_case_45",
            input_value=79320,
            expected_output=78999,
            description="Test case 45: input=79320\n, expected=78999\n"
        ),
        TestCase(
            name="test_case_46",
            input_value=99004,
            expected_output=98999,
            description="Test case 46: input=99004\n, expected=98999\n"
        ),
        TestCase(
            name="test_case_47",
            input_value=99088,
            expected_output=98999,
            description="Test case 47: input=99088\n, expected=98999\n"
        ),
        TestCase(
            name="test_case_48",
            input_value=99737,
            expected_output=98999,
            description="Test case 48: input=99737\n, expected=98999\n"
        ),
        TestCase(
            name="test_case_49",
            input_value=29652,
            expected_output=28999,
            description="Test case 49: input=29652\n, expected=28999\n"
        ),
        TestCase(
            name="test_case_50",
            input_value=59195,
            expected_output=58999,
            description="Test case 50: input=59195\n, expected=58999\n"
        ),
        TestCase(
            name="test_case_51",
            input_value=19930,
            expected_output=19899,
            description="Test case 51: input=19930\n, expected=19899\n"
        ),
        TestCase(
            name="test_case_52",
            input_value=49533,
            expected_output=48999,
            description="Test case 52: input=49533\n, expected=48999\n"
        ),
        TestCase(
            name="test_case_53",
            input_value=69291,
            expected_output=68999,
            description="Test case 53: input=69291\n, expected=68999\n"
        ),
        TestCase(
            name="test_case_54",
            input_value=59452,
            expected_output=58999,
            description="Test case 54: input=59452\n, expected=58999\n"
        ),
        TestCase(
            name="test_case_55",
            input_value=11,
            expected_output=9,
            description="Test case 55: input=11\n, expected=9\n"
        ),
        TestCase(
            name="test_case_56",
            input_value=110,
            expected_output=99,
            description="Test case 56: input=110\n, expected=99\n"
        ),
        TestCase(
            name="test_case_57",
            input_value=111,
            expected_output=99,
            description="Test case 57: input=111\n, expected=99\n"
        ),
        TestCase(
            name="test_case_58",
            input_value=119,
            expected_output=99,
            description="Test case 58: input=119\n, expected=99\n"
        ),
        TestCase(
            name="test_case_59",
            input_value=118,
            expected_output=99,
            description="Test case 59: input=118\n, expected=99\n"
        ),
        TestCase(
            name="test_case_60",
            input_value=1100,
            expected_output=999,
            description="Test case 60: input=1100\n, expected=999\n"
        ),
        TestCase(
            name="test_case_61",
            input_value=1199,
            expected_output=999,
            description="Test case 61: input=1199\n, expected=999\n"
        ),
        TestCase(
            name="test_case_62",
            input_value=1109,
            expected_output=999,
            description="Test case 62: input=1109\n, expected=999\n"
        ),
        TestCase(
            name="test_case_63",
            input_value=1190,
            expected_output=999,
            description="Test case 63: input=1190\n, expected=999\n"
        ),
        TestCase(
            name="test_case_64",
            input_value=12,
            expected_output=9,
            description="Test case 64: input=12\n, expected=9\n"
        ),
        TestCase(
            name="test_case_65",
            input_value=120,
            expected_output=99,
            description="Test case 65: input=120\n, expected=99\n"
        ),
        TestCase(
            name="test_case_66",
            input_value=121,
            expected_output=99,
            description="Test case 66: input=121\n, expected=99\n"
        ),
        TestCase(
            name="test_case_67",
            input_value=129,
            expected_output=99,
            description="Test case 67: input=129\n, expected=99\n"
        ),
        TestCase(
            name="test_case_68",
            input_value=128,
            expected_output=99,
            description="Test case 68: input=128\n, expected=99\n"
        ),
        TestCase(
            name="test_case_69",
            input_value=1200,
            expected_output=999,
            description="Test case 69: input=1200\n, expected=999\n"
        ),
        TestCase(
            name="test_case_70",
            input_value=1299,
            expected_output=999,
            description="Test case 70: input=1299\n, expected=999\n"
        ),
        TestCase(
            name="test_case_71",
            input_value=1209,
            expected_output=999,
            description="Test case 71: input=1209\n, expected=999\n"
        ),
        TestCase(
            name="test_case_72",
            input_value=1290,
            expected_output=999,
            description="Test case 72: input=1290\n, expected=999\n"
        ),
        TestCase(
            name="test_case_73",
            input_value=13,
            expected_output=9,
            description="Test case 73: input=13\n, expected=9\n"
        ),
        TestCase(
            name="test_case_74",
            input_value=130,
            expected_output=99,
            description="Test case 74: input=130\n, expected=99\n"
        ),
        TestCase(
            name="test_case_75",
            input_value=131,
            expected_output=99,
            description="Test case 75: input=131\n, expected=99\n"
        ),
        TestCase(
            name="test_case_76",
            input_value=139,
            expected_output=99,
            description="Test case 76: input=139\n, expected=99\n"
        ),
        TestCase(
            name="test_case_77",
            input_value=138,
            expected_output=99,
            description="Test case 77: input=138\n, expected=99\n"
        ),
        TestCase(
            name="test_case_78",
            input_value=1300,
            expected_output=999,
            description="Test case 78: input=1300\n, expected=999\n"
        ),
        TestCase(
            name="test_case_79",
            input_value=1399,
            expected_output=999,
            description="Test case 79: input=1399\n, expected=999\n"
        ),
        TestCase(
            name="test_case_80",
            input_value=1309,
            expected_output=999,
            description="Test case 80: input=1309\n, expected=999\n"
        ),
        TestCase(
            name="test_case_81",
            input_value=1390,
            expected_output=999,
            description="Test case 81: input=1390\n, expected=999\n"
        ),
        TestCase(
            name="test_case_82",
            input_value=14,
            expected_output=9,
            description="Test case 82: input=14\n, expected=9\n"
        ),
        TestCase(
            name="test_case_83",
            input_value=140,
            expected_output=99,
            description="Test case 83: input=140\n, expected=99\n"
        ),
        TestCase(
            name="test_case_84",
            input_value=141,
            expected_output=99,
            description="Test case 84: input=141\n, expected=99\n"
        ),
        TestCase(
            name="test_case_85",
            input_value=149,
            expected_output=99,
            description="Test case 85: input=149\n, expected=99\n"
        ),
        TestCase(
            name="test_case_86",
            input_value=148,
            expected_output=99,
            description="Test case 86: input=148\n, expected=99\n"
        ),
        TestCase(
            name="test_case_87",
            input_value=1400,
            expected_output=999,
            description="Test case 87: input=1400\n, expected=999\n"
        ),
        TestCase(
            name="test_case_88",
            input_value=1499,
            expected_output=999,
            description="Test case 88: input=1499\n, expected=999\n"
        ),
        TestCase(
            name="test_case_89",
            input_value=1409,
            expected_output=999,
            description="Test case 89: input=1409\n, expected=999\n"
        ),
        TestCase(
            name="test_case_90",
            input_value=1490,
            expected_output=999,
            description="Test case 90: input=1490\n, expected=999\n"
        ),
        TestCase(
            name="test_case_91",
            input_value=15,
            expected_output=9,
            description="Test case 91: input=15\n, expected=9\n"
        ),
        TestCase(
            name="test_case_92",
            input_value=150,
            expected_output=99,
            description="Test case 92: input=150\n, expected=99\n"
        ),
        TestCase(
            name="test_case_93",
            input_value=151,
            expected_output=99,
            description="Test case 93: input=151\n, expected=99\n"
        ),
        TestCase(
            name="test_case_94",
            input_value=159,
            expected_output=99,
            description="Test case 94: input=159\n, expected=99\n"
        ),
        TestCase(
            name="test_case_95",
            input_value=158,
            expected_output=99,
            description="Test case 95: input=158\n, expected=99\n"
        ),
        TestCase(
            name="test_case_96",
            input_value=1500,
            expected_output=999,
            description="Test case 96: input=1500\n, expected=999\n"
        ),
        TestCase(
            name="test_case_97",
            input_value=1599,
            expected_output=999,
            description="Test case 97: input=1599\n, expected=999\n"
        ),
        TestCase(
            name="test_case_98",
            input_value=1509,
            expected_output=999,
            description="Test case 98: input=1509\n, expected=999\n"
        ),
        TestCase(
            name="test_case_99",
            input_value=1590,
            expected_output=999,
            description="Test case 99: input=1590\n, expected=999\n"
        ),
        TestCase(
            name="test_case_100",
            input_value=16,
            expected_output=9,
            description="Test case 100: input=16\n, expected=9\n"
        ),
        TestCase(
            name="test_case_101",
            input_value=160,
            expected_output=99,
            description="Test case 101: input=160\n, expected=99\n"
        ),
        TestCase(
            name="test_case_102",
            input_value=161,
            expected_output=99,
            description="Test case 102: input=161\n, expected=99\n"
        ),
        TestCase(
            name="test_case_103",
            input_value=169,
            expected_output=99,
            description="Test case 103: input=169\n, expected=99\n"
        ),
        TestCase(
            name="test_case_104",
            input_value=168,
            expected_output=99,
            description="Test case 104: input=168\n, expected=99\n"
        ),
        TestCase(
            name="test_case_105",
            input_value=1600,
            expected_output=999,
            description="Test case 105: input=1600\n, expected=999\n"
        ),
        TestCase(
            name="test_case_106",
            input_value=1699,
            expected_output=999,
            description="Test case 106: input=1699\n, expected=999\n"
        ),
        TestCase(
            name="test_case_107",
            input_value=1609,
            expected_output=999,
            description="Test case 107: input=1609\n, expected=999\n"
        ),
        TestCase(
            name="test_case_108",
            input_value=1690,
            expected_output=999,
            description="Test case 108: input=1690\n, expected=999\n"
        ),
        TestCase(
            name="test_case_109",
            input_value=17,
            expected_output=9,
            description="Test case 109: input=17\n, expected=9\n"
        ),
        TestCase(
            name="test_case_110",
            input_value=170,
            expected_output=99,
            description="Test case 110: input=170\n, expected=99\n"
        ),
        TestCase(
            name="test_case_111",
            input_value=171,
            expected_output=99,
            description="Test case 111: input=171\n, expected=99\n"
        ),
        TestCase(
            name="test_case_112",
            input_value=179,
            expected_output=99,
            description="Test case 112: input=179\n, expected=99\n"
        ),
        TestCase(
            name="test_case_113",
            input_value=178,
            expected_output=99,
            description="Test case 113: input=178\n, expected=99\n"
        ),
        TestCase(
            name="test_case_114",
            input_value=1700,
            expected_output=999,
            description="Test case 114: input=1700\n, expected=999\n"
        ),
        TestCase(
            name="test_case_115",
            input_value=1799,
            expected_output=999,
            description="Test case 115: input=1799\n, expected=999\n"
        ),
        TestCase(
            name="test_case_116",
            input_value=1709,
            expected_output=999,
            description="Test case 116: input=1709\n, expected=999\n"
        ),
        TestCase(
            name="test_case_117",
            input_value=1790,
            expected_output=999,
            description="Test case 117: input=1790\n, expected=999\n"
        ),
        TestCase(
            name="test_case_118",
            input_value=18,
            expected_output=18,
            description="Test case 118: input=18\n, expected=18\n"
        ),
        TestCase(
            name="test_case_119",
            input_value=180,
            expected_output=99,
            description="Test case 119: input=180\n, expected=99\n"
        ),
        TestCase(
            name="test_case_120",
            input_value=181,
            expected_output=99,
            description="Test case 120: input=181\n, expected=99\n"
        ),
        TestCase(
            name="test_case_121",
            input_value=189,
            expected_output=189,
            description="Test case 121: input=189\n, expected=189\n"
        ),
        TestCase(
            name="test_case_122",
            input_value=188,
            expected_output=99,
            description="Test case 122: input=188\n, expected=99\n"
        ),
        TestCase(
            name="test_case_123",
            input_value=1800,
            expected_output=999,
            description="Test case 123: input=1800\n, expected=999\n"
        ),
        TestCase(
            name="test_case_124",
            input_value=1899,
            expected_output=1899,
            description="Test case 124: input=1899\n, expected=1899\n"
        ),
        TestCase(
            name="test_case_125",
            input_value=1809,
            expected_output=999,
            description="Test case 125: input=1809\n, expected=999\n"
        ),
        TestCase(
            name="test_case_126",
            input_value=1890,
            expected_output=999,
            description="Test case 126: input=1890\n, expected=999\n"
        ),
        TestCase(
            name="test_case_127",
            input_value=19,
            expected_output=19,
            description="Test case 127: input=19\n, expected=19\n"
        ),
        TestCase(
            name="test_case_128",
            input_value=190,
            expected_output=189,
            description="Test case 128: input=190\n, expected=189\n"
        ),
        TestCase(
            name="test_case_129",
            input_value=191,
            expected_output=189,
            description="Test case 129: input=191\n, expected=189\n"
        ),
        TestCase(
            name="test_case_130",
            input_value=199,
            expected_output=199,
            description="Test case 130: input=199\n, expected=199\n"
        ),
        TestCase(
            name="test_case_131",
            input_value=198,
            expected_output=198,
            description="Test case 131: input=198\n, expected=198\n"
        ),
        TestCase(
            name="test_case_132",
            input_value=1900,
            expected_output=1899,
            description="Test case 132: input=1900\n, expected=1899\n"
        ),
        TestCase(
            name="test_case_133",
            input_value=1999,
            expected_output=1999,
            description="Test case 133: input=1999\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_134",
            input_value=1909,
            expected_output=1899,
            description="Test case 134: input=1909\n, expected=1899\n"
        ),
        TestCase(
            name="test_case_135",
            input_value=1990,
            expected_output=1989,
            description="Test case 135: input=1990\n, expected=1989\n"
        ),
        TestCase(
            name="test_case_136",
            input_value=20,
            expected_output=19,
            description="Test case 136: input=20\n, expected=19\n"
        ),
        TestCase(
            name="test_case_137",
            input_value=200,
            expected_output=199,
            description="Test case 137: input=200\n, expected=199\n"
        ),
        TestCase(
            name="test_case_138",
            input_value=201,
            expected_output=199,
            description="Test case 138: input=201\n, expected=199\n"
        ),
        TestCase(
            name="test_case_139",
            input_value=209,
            expected_output=199,
            description="Test case 139: input=209\n, expected=199\n"
        ),
        TestCase(
            name="test_case_140",
            input_value=208,
            expected_output=199,
            description="Test case 140: input=208\n, expected=199\n"
        ),
        TestCase(
            name="test_case_141",
            input_value=2000,
            expected_output=1999,
            description="Test case 141: input=2000\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_142",
            input_value=2099,
            expected_output=1999,
            description="Test case 142: input=2099\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_143",
            input_value=2009,
            expected_output=1999,
            description="Test case 143: input=2009\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_144",
            input_value=2090,
            expected_output=1999,
            description="Test case 144: input=2090\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_145",
            input_value=21,
            expected_output=19,
            description="Test case 145: input=21\n, expected=19\n"
        ),
        TestCase(
            name="test_case_146",
            input_value=210,
            expected_output=199,
            description="Test case 146: input=210\n, expected=199\n"
        ),
        TestCase(
            name="test_case_147",
            input_value=211,
            expected_output=199,
            description="Test case 147: input=211\n, expected=199\n"
        ),
        TestCase(
            name="test_case_148",
            input_value=219,
            expected_output=199,
            description="Test case 148: input=219\n, expected=199\n"
        ),
        TestCase(
            name="test_case_149",
            input_value=218,
            expected_output=199,
            description="Test case 149: input=218\n, expected=199\n"
        ),
        TestCase(
            name="test_case_150",
            input_value=2100,
            expected_output=1999,
            description="Test case 150: input=2100\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_151",
            input_value=2199,
            expected_output=1999,
            description="Test case 151: input=2199\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_152",
            input_value=2109,
            expected_output=1999,
            description="Test case 152: input=2109\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_153",
            input_value=2190,
            expected_output=1999,
            description="Test case 153: input=2190\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_154",
            input_value=22,
            expected_output=19,
            description="Test case 154: input=22\n, expected=19\n"
        ),
        TestCase(
            name="test_case_155",
            input_value=220,
            expected_output=199,
            description="Test case 155: input=220\n, expected=199\n"
        ),
        TestCase(
            name="test_case_156",
            input_value=221,
            expected_output=199,
            description="Test case 156: input=221\n, expected=199\n"
        ),
        TestCase(
            name="test_case_157",
            input_value=229,
            expected_output=199,
            description="Test case 157: input=229\n, expected=199\n"
        ),
        TestCase(
            name="test_case_158",
            input_value=228,
            expected_output=199,
            description="Test case 158: input=228\n, expected=199\n"
        ),
        TestCase(
            name="test_case_159",
            input_value=2200,
            expected_output=1999,
            description="Test case 159: input=2200\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_160",
            input_value=2299,
            expected_output=1999,
            description="Test case 160: input=2299\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_161",
            input_value=2209,
            expected_output=1999,
            description="Test case 161: input=2209\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_162",
            input_value=2290,
            expected_output=1999,
            description="Test case 162: input=2290\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_163",
            input_value=23,
            expected_output=19,
            description="Test case 163: input=23\n, expected=19\n"
        ),
        TestCase(
            name="test_case_164",
            input_value=230,
            expected_output=199,
            description="Test case 164: input=230\n, expected=199\n"
        ),
        TestCase(
            name="test_case_165",
            input_value=231,
            expected_output=199,
            description="Test case 165: input=231\n, expected=199\n"
        ),
        TestCase(
            name="test_case_166",
            input_value=239,
            expected_output=199,
            description="Test case 166: input=239\n, expected=199\n"
        ),
        TestCase(
            name="test_case_167",
            input_value=238,
            expected_output=199,
            description="Test case 167: input=238\n, expected=199\n"
        ),
        TestCase(
            name="test_case_168",
            input_value=2300,
            expected_output=1999,
            description="Test case 168: input=2300\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_169",
            input_value=2399,
            expected_output=1999,
            description="Test case 169: input=2399\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_170",
            input_value=2309,
            expected_output=1999,
            description="Test case 170: input=2309\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_171",
            input_value=2390,
            expected_output=1999,
            description="Test case 171: input=2390\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_172",
            input_value=24,
            expected_output=19,
            description="Test case 172: input=24\n, expected=19\n"
        ),
        TestCase(
            name="test_case_173",
            input_value=240,
            expected_output=199,
            description="Test case 173: input=240\n, expected=199\n"
        ),
        TestCase(
            name="test_case_174",
            input_value=241,
            expected_output=199,
            description="Test case 174: input=241\n, expected=199\n"
        ),
        TestCase(
            name="test_case_175",
            input_value=249,
            expected_output=199,
            description="Test case 175: input=249\n, expected=199\n"
        ),
        TestCase(
            name="test_case_176",
            input_value=248,
            expected_output=199,
            description="Test case 176: input=248\n, expected=199\n"
        ),
        TestCase(
            name="test_case_177",
            input_value=2400,
            expected_output=1999,
            description="Test case 177: input=2400\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_178",
            input_value=2499,
            expected_output=1999,
            description="Test case 178: input=2499\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_179",
            input_value=2409,
            expected_output=1999,
            description="Test case 179: input=2409\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_180",
            input_value=2490,
            expected_output=1999,
            description="Test case 180: input=2490\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_181",
            input_value=25,
            expected_output=19,
            description="Test case 181: input=25\n, expected=19\n"
        ),
        TestCase(
            name="test_case_182",
            input_value=250,
            expected_output=199,
            description="Test case 182: input=250\n, expected=199\n"
        ),
        TestCase(
            name="test_case_183",
            input_value=251,
            expected_output=199,
            description="Test case 183: input=251\n, expected=199\n"
        ),
        TestCase(
            name="test_case_184",
            input_value=259,
            expected_output=199,
            description="Test case 184: input=259\n, expected=199\n"
        ),
        TestCase(
            name="test_case_185",
            input_value=258,
            expected_output=199,
            description="Test case 185: input=258\n, expected=199\n"
        ),
        TestCase(
            name="test_case_186",
            input_value=2500,
            expected_output=1999,
            description="Test case 186: input=2500\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_187",
            input_value=2599,
            expected_output=1999,
            description="Test case 187: input=2599\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_188",
            input_value=2509,
            expected_output=1999,
            description="Test case 188: input=2509\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_189",
            input_value=2590,
            expected_output=1999,
            description="Test case 189: input=2590\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_190",
            input_value=26,
            expected_output=19,
            description="Test case 190: input=26\n, expected=19\n"
        ),
        TestCase(
            name="test_case_191",
            input_value=260,
            expected_output=199,
            description="Test case 191: input=260\n, expected=199\n"
        ),
        TestCase(
            name="test_case_192",
            input_value=261,
            expected_output=199,
            description="Test case 192: input=261\n, expected=199\n"
        ),
        TestCase(
            name="test_case_193",
            input_value=269,
            expected_output=199,
            description="Test case 193: input=269\n, expected=199\n"
        ),
        TestCase(
            name="test_case_194",
            input_value=268,
            expected_output=199,
            description="Test case 194: input=268\n, expected=199\n"
        ),
        TestCase(
            name="test_case_195",
            input_value=2600,
            expected_output=1999,
            description="Test case 195: input=2600\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_196",
            input_value=2699,
            expected_output=1999,
            description="Test case 196: input=2699\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_197",
            input_value=2609,
            expected_output=1999,
            description="Test case 197: input=2609\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_198",
            input_value=2690,
            expected_output=1999,
            description="Test case 198: input=2690\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_199",
            input_value=27,
            expected_output=19,
            description="Test case 199: input=27\n, expected=19\n"
        ),
        TestCase(
            name="test_case_200",
            input_value=270,
            expected_output=199,
            description="Test case 200: input=270\n, expected=199\n"
        ),
        TestCase(
            name="test_case_201",
            input_value=271,
            expected_output=199,
            description="Test case 201: input=271\n, expected=199\n"
        ),
        TestCase(
            name="test_case_202",
            input_value=279,
            expected_output=199,
            description="Test case 202: input=279\n, expected=199\n"
        ),
        TestCase(
            name="test_case_203",
            input_value=278,
            expected_output=199,
            description="Test case 203: input=278\n, expected=199\n"
        ),
        TestCase(
            name="test_case_204",
            input_value=2700,
            expected_output=1999,
            description="Test case 204: input=2700\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_205",
            input_value=2799,
            expected_output=1999,
            description="Test case 205: input=2799\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_206",
            input_value=2709,
            expected_output=1999,
            description="Test case 206: input=2709\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_207",
            input_value=2790,
            expected_output=1999,
            description="Test case 207: input=2790\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_208",
            input_value=28,
            expected_output=28,
            description="Test case 208: input=28\n, expected=28\n"
        ),
        TestCase(
            name="test_case_209",
            input_value=280,
            expected_output=199,
            description="Test case 209: input=280\n, expected=199\n"
        ),
        TestCase(
            name="test_case_210",
            input_value=281,
            expected_output=199,
            description="Test case 210: input=281\n, expected=199\n"
        ),
        TestCase(
            name="test_case_211",
            input_value=289,
            expected_output=289,
            description="Test case 211: input=289\n, expected=289\n"
        ),
        TestCase(
            name="test_case_212",
            input_value=288,
            expected_output=199,
            description="Test case 212: input=288\n, expected=199\n"
        ),
        TestCase(
            name="test_case_213",
            input_value=2800,
            expected_output=1999,
            description="Test case 213: input=2800\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_214",
            input_value=2899,
            expected_output=2899,
            description="Test case 214: input=2899\n, expected=2899\n"
        ),
        TestCase(
            name="test_case_215",
            input_value=2809,
            expected_output=1999,
            description="Test case 215: input=2809\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_216",
            input_value=2890,
            expected_output=1999,
            description="Test case 216: input=2890\n, expected=1999\n"
        ),
        TestCase(
            name="test_case_217",
            input_value=29,
            expected_output=29,
            description="Test case 217: input=29\n, expected=29\n"
        ),
        TestCase(
            name="test_case_218",
            input_value=290,
            expected_output=289,
            description="Test case 218: input=290\n, expected=289\n"
        ),
        TestCase(
            name="test_case_219",
            input_value=291,
            expected_output=289,
            description="Test case 219: input=291\n, expected=289\n"
        ),
        TestCase(
            name="test_case_220",
            input_value=299,
            expected_output=299,
            description="Test case 220: input=299\n, expected=299\n"
        ),
        TestCase(
            name="test_case_221",
            input_value=298,
            expected_output=298,
            description="Test case 221: input=298\n, expected=298\n"
        ),
        TestCase(
            name="test_case_222",
            input_value=2900,
            expected_output=2899,
            description="Test case 222: input=2900\n, expected=2899\n"
        ),
        TestCase(
            name="test_case_223",
            input_value=2999,
            expected_output=2999,
            description="Test case 223: input=2999\n, expected=2999\n"
        ),
        TestCase(
            name="test_case_224",
            input_value=2909,
            expected_output=2899,
            description="Test case 224: input=2909\n, expected=2899\n"
        ),
        TestCase(
            name="test_case_225",
            input_value=2990,
            expected_output=2989,
            description="Test case 225: input=2990\n, expected=2989\n"
        ),
        TestCase(
            name="test_case_226",
            input_value=999,
            expected_output=999,
            description="Test case 226: input=999\n, expected=999\n"
        ),
        TestCase(
            name="test_case_227",
            input_value=999,
            expected_output=999,
            description="Test case 227: input=999\n, expected=999\n"
        ),
        TestCase(
            name="test_case_228",
            input_value=890,
            expected_output=889,
            description="Test case 228: input=890\n, expected=889\n"
        ),
        TestCase(
            name="test_case_229",
            input_value=995,
            expected_output=989,
            description="Test case 229: input=995\n, expected=989\n"
        ),
        TestCase(
            name="test_case_230",
            input_value=999,
            expected_output=999,
            description="Test case 230: input=999\n, expected=999\n"
        ),
        TestCase(
            name="test_case_231",
            input_value=989,
            expected_output=989,
            description="Test case 231: input=989\n, expected=989\n"
        ),
        TestCase(
            name="test_case_232",
            input_value=999,
            expected_output=999,
            description="Test case 232: input=999\n, expected=999\n"
        ),
        TestCase(
            name="test_case_233",
            input_value=999,
            expected_output=999,
            description="Test case 233: input=999\n, expected=999\n"
        ),
        TestCase(
            name="test_case_234",
            input_value=991,
            expected_output=989,
            description="Test case 234: input=991\n, expected=989\n"
        ),
        TestCase(
            name="test_case_235",
            input_value=999,
            expected_output=999,
            description="Test case 235: input=999\n, expected=999\n"
        ),
        TestCase(
            name="test_case_236",
            input_value=9929,
            expected_output=9899,
            description="Test case 236: input=9929\n, expected=9899\n"
        ),
        TestCase(
            name="test_case_237",
            input_value=4999,
            expected_output=4999,
            description="Test case 237: input=4999\n, expected=4999\n"
        ),
        TestCase(
            name="test_case_238",
            input_value=9690,
            expected_output=8999,
            description="Test case 238: input=9690\n, expected=8999\n"
        ),
        TestCase(
            name="test_case_239",
            input_value=8990,
            expected_output=8989,
            description="Test case 239: input=8990\n, expected=8989\n"
        ),
        TestCase(
            name="test_case_240",
            input_value=9982,
            expected_output=9899,
            description="Test case 240: input=9982\n, expected=9899\n"
        ),
        TestCase(
            name="test_case_241",
            input_value=9999,
            expected_output=9999,
            description="Test case 241: input=9999\n, expected=9999\n"
        ),
        TestCase(
            name="test_case_242",
            input_value=1993,
            expected_output=1989,
            description="Test case 242: input=1993\n, expected=1989\n"
        ),
        TestCase(
            name="test_case_243",
            input_value=9367,
            expected_output=8999,
            description="Test case 243: input=9367\n, expected=8999\n"
        ),
        TestCase(
            name="test_case_244",
            input_value=8939,
            expected_output=8899,
            description="Test case 244: input=8939\n, expected=8899\n"
        ),
        TestCase(
            name="test_case_245",
            input_value=9899,
            expected_output=9899,
            description="Test case 245: input=9899\n, expected=9899\n"
        ),
        TestCase(
            name="test_case_246",
            input_value=99999,
            expected_output=99999,
            description="Test case 246: input=99999\n, expected=99999\n"
        ),
        TestCase(
            name="test_case_247",
            input_value=93929,
            expected_output=89999,
            description="Test case 247: input=93929\n, expected=89999\n"
        ),
        TestCase(
            name="test_case_248",
            input_value=99999,
            expected_output=99999,
            description="Test case 248: input=99999\n, expected=99999\n"
        ),
        TestCase(
            name="test_case_249",
            input_value=38579,
            expected_output=29999,
            description="Test case 249: input=38579\n, expected=29999\n"
        ),
        TestCase(
            name="test_case_250",
            input_value=79096,
            expected_output=78999,
            description="Test case 250: input=79096\n, expected=78999\n"
        ),
        TestCase(
            name="test_case_251",
            input_value=72694,
            expected_output=69999,
            description="Test case 251: input=72694\n, expected=69999\n"
        ),
        TestCase(
            name="test_case_252",
            input_value=99999,
            expected_output=99999,
            description="Test case 252: input=99999\n, expected=99999\n"
        ),
        TestCase(
            name="test_case_253",
            input_value=99999,
            expected_output=99999,
            description="Test case 253: input=99999\n, expected=99999\n"
        ),
        TestCase(
            name="test_case_254",
            input_value=99992,
            expected_output=99989,
            description="Test case 254: input=99992\n, expected=99989\n"
        ),
        TestCase(
            name="test_case_255",
            input_value=27998,
            expected_output=19999,
            description="Test case 255: input=27998\n, expected=19999\n"
        ),
        TestCase(
            name="test_case_256",
            input_value=460999,
            expected_output=399999,
            description="Test case 256: input=460999\n, expected=399999\n"
        ),
        TestCase(
            name="test_case_257",
            input_value=999999,
            expected_output=999999,
            description="Test case 257: input=999999\n, expected=999999\n"
        ),
        TestCase(
            name="test_case_258",
            input_value=999999,
            expected_output=999999,
            description="Test case 258: input=999999\n, expected=999999\n"
        ),
        TestCase(
            name="test_case_259",
            input_value=998999,
            expected_output=998999,
            description="Test case 259: input=998999\n, expected=998999\n"
        ),
        TestCase(
            name="test_case_260",
            input_value=999999,
            expected_output=999999,
            description="Test case 260: input=999999\n, expected=999999\n"
        ),
        TestCase(
            name="test_case_261",
            input_value=999929,
            expected_output=999899,
            description="Test case 261: input=999929\n, expected=999899\n"
        ),
        TestCase(
            name="test_case_262",
            input_value=999999,
            expected_output=999999,
            description="Test case 262: input=999999\n, expected=999999\n"
        ),
        TestCase(
            name="test_case_263",
            input_value=999999,
            expected_output=999999,
            description="Test case 263: input=999999\n, expected=999999\n"
        ),
        TestCase(
            name="test_case_264",
            input_value=979199,
            expected_output=899999,
            description="Test case 264: input=979199\n, expected=899999\n"
        ),
        TestCase(
            name="test_case_265",
            input_value=999999,
            expected_output=999999,
            description="Test case 265: input=999999\n, expected=999999\n"
        ),
        TestCase(
            name="test_case_266",
            input_value=9899999,
            expected_output=9899999,
            description="Test case 266: input=9899999\n, expected=9899999\n"
        ),
        TestCase(
            name="test_case_267",
            input_value=9699959,
            expected_output=8999999,
            description="Test case 267: input=9699959\n, expected=8999999\n"
        ),
        TestCase(
            name="test_case_268",
            input_value=9999999,
            expected_output=9999999,
            description="Test case 268: input=9999999\n, expected=9999999\n"
        ),
        TestCase(
            name="test_case_269",
            input_value=9997099,
            expected_output=9989999,
            description="Test case 269: input=9997099\n, expected=9989999\n"
        ),
        TestCase(
            name="test_case_270",
            input_value=8992091,
            expected_output=8989999,
            description="Test case 270: input=8992091\n, expected=8989999\n"
        ),
        TestCase(
            name="test_case_271",
            input_value=9599295,
            expected_output=8999999,
            description="Test case 271: input=9599295\n, expected=8999999\n"
        ),
        TestCase(
            name="test_case_272",
            input_value=2999902,
            expected_output=2999899,
            description="Test case 272: input=2999902\n, expected=2999899\n"
        ),
        TestCase(
            name="test_case_273",
            input_value=9999953,
            expected_output=9999899,
            description="Test case 273: input=9999953\n, expected=9999899\n"
        ),
        TestCase(
            name="test_case_274",
            input_value=9999999,
            expected_output=9999999,
            description="Test case 274: input=9999999\n, expected=9999999\n"
        ),
        TestCase(
            name="test_case_275",
            input_value=9590999,
            expected_output=8999999,
            description="Test case 275: input=9590999\n, expected=8999999\n"
        ),
    ]
    
    return Problem(
        name="apps_0001",
        description=r"""Anton has the integer x. He is interested in finding the positive integer, which doesn't exceed x, that has the MINIMUM sum of digits.

Your task is to help Anton and to find the integer that interests him. If there are several such integers, determine the SMALLEST of them. 


-----Input-----

The first line contains the positive integer x (1 ≤ x ≤ 10^18) — the integer which Anton has. 


-----Output-----

Print the positive integer which doesn't exceed x and has the MINIMUM sum of digits. If there are several such integers, print the SMALLEST of them. Printed integer must not contain leading zeros.


-----Examples-----
Input
100

Output
99

Input
48

Output
48

Input
521

Output
499""",
        function_signature="def solution(*args, **kwargs):",
        visible_tests=visible_tests,
        hidden_tests=hidden_tests
    )