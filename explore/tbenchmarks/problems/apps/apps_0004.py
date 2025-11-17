"""
apps_0004 problem from APPS dataset.
"""

from typing import List
from ...core.problem import Problem, TestCase


def create_apps_0004() -> Problem:
    """
    Create the apps_0004 problem.
    """
    # Visible tests (shown to the model)
    visible_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value='3\n11 23\n',
            expected_output=2,
            description="Test case 1: input=3\n11 23\n, expected=2\n"
        ),
        TestCase(
            name="test_case_2",
            input_value='5\n01 07\n',
            expected_output=0,
            description="Test case 2: input=5\n01 07\n, expected=0\n"
        ),
        TestCase(
            name="test_case_3",
            input_value='34\n09 24\n',
            expected_output=3,
            description="Test case 3: input=34\n09 24\n, expected=3\n"
        ),
    ]
    
    # Hidden tests (not shown to model, used for validation)
    hidden_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value='2\n14 37\n',
            expected_output=0,
            description="Test case 1: input=2\n14 37\n, expected=0\n"
        ),
        TestCase(
            name="test_case_2",
            input_value='14\n19 54\n',
            expected_output=9,
            description="Test case 2: input=14\n19 54\n, expected=9\n"
        ),
        TestCase(
            name="test_case_3",
            input_value='42\n15 44\n',
            expected_output=12,
            description="Test case 3: input=42\n15 44\n, expected=12\n"
        ),
        TestCase(
            name="test_case_4",
            input_value='46\n02 43\n',
            expected_output=1,
            description="Test case 4: input=46\n02 43\n, expected=1\n"
        ),
        TestCase(
            name="test_case_5",
            input_value='14\n06 41\n',
            expected_output=1,
            description="Test case 5: input=14\n06 41\n, expected=1\n"
        ),
        TestCase(
            name="test_case_6",
            input_value='26\n04 58\n',
            expected_output=26,
            description="Test case 6: input=26\n04 58\n, expected=26\n"
        ),
        TestCase(
            name="test_case_7",
            input_value='54\n16 47\n',
            expected_output=0,
            description="Test case 7: input=54\n16 47\n, expected=0\n"
        ),
        TestCase(
            name="test_case_8",
            input_value='38\n20 01\n',
            expected_output=3,
            description="Test case 8: input=38\n20 01\n, expected=3\n"
        ),
        TestCase(
            name="test_case_9",
            input_value='11\n02 05\n',
            expected_output=8,
            description="Test case 9: input=11\n02 05\n, expected=8\n"
        ),
        TestCase(
            name="test_case_10",
            input_value='55\n22 10\n',
            expected_output=5,
            description="Test case 10: input=55\n22 10\n, expected=5\n"
        ),
        TestCase(
            name="test_case_11",
            input_value='23\n10 08\n',
            expected_output=6,
            description="Test case 11: input=23\n10 08\n, expected=6\n"
        ),
        TestCase(
            name="test_case_12",
            input_value='23\n23 14\n',
            expected_output=9,
            description="Test case 12: input=23\n23 14\n, expected=9\n"
        ),
        TestCase(
            name="test_case_13",
            input_value='51\n03 27\n',
            expected_output=0,
            description="Test case 13: input=51\n03 27\n, expected=0\n"
        ),
        TestCase(
            name="test_case_14",
            input_value='35\n15 25\n',
            expected_output=13,
            description="Test case 14: input=35\n15 25\n, expected=13\n"
        ),
        TestCase(
            name="test_case_15",
            input_value='3\n12 15\n',
            expected_output=6,
            description="Test case 15: input=3\n12 15\n, expected=6\n"
        ),
        TestCase(
            name="test_case_16",
            input_value='47\n00 28\n',
            expected_output=3,
            description="Test case 16: input=47\n00 28\n, expected=3\n"
        ),
        TestCase(
            name="test_case_17",
            input_value='31\n13 34\n',
            expected_output=7,
            description="Test case 17: input=31\n13 34\n, expected=7\n"
        ),
        TestCase(
            name="test_case_18",
            input_value='59\n17 32\n',
            expected_output=0,
            description="Test case 18: input=59\n17 32\n, expected=0\n"
        ),
        TestCase(
            name="test_case_19",
            input_value='25\n11 03\n',
            expected_output=8,
            description="Test case 19: input=25\n11 03\n, expected=8\n"
        ),
        TestCase(
            name="test_case_20",
            input_value='9\n16 53\n',
            expected_output=4,
            description="Test case 20: input=9\n16 53\n, expected=4\n"
        ),
        TestCase(
            name="test_case_21",
            input_value='53\n04 06\n',
            expected_output=3,
            description="Test case 21: input=53\n04 06\n, expected=3\n"
        ),
        TestCase(
            name="test_case_22",
            input_value='37\n00 12\n',
            expected_output=5,
            description="Test case 22: input=37\n00 12\n, expected=5\n"
        ),
        TestCase(
            name="test_case_23",
            input_value='5\n13 10\n',
            expected_output=63,
            description="Test case 23: input=5\n13 10\n, expected=63\n"
        ),
        TestCase(
            name="test_case_24",
            input_value='50\n01 59\n',
            expected_output=10,
            description="Test case 24: input=50\n01 59\n, expected=10\n"
        ),
        TestCase(
            name="test_case_25",
            input_value='34\n06 13\n',
            expected_output=4,
            description="Test case 25: input=34\n06 13\n, expected=4\n"
        ),
        TestCase(
            name="test_case_26",
            input_value='2\n18 19\n',
            expected_output=1,
            description="Test case 26: input=2\n18 19\n, expected=1\n"
        ),
        TestCase(
            name="test_case_27",
            input_value='46\n06 16\n',
            expected_output=17,
            description="Test case 27: input=46\n06 16\n, expected=17\n"
        ),
        TestCase(
            name="test_case_28",
            input_value='14\n03 30\n',
            expected_output=41,
            description="Test case 28: input=14\n03 30\n, expected=41\n"
        ),
        TestCase(
            name="test_case_29",
            input_value='40\n13 37\n',
            expected_output=0,
            description="Test case 29: input=40\n13 37\n, expected=0\n"
        ),
        TestCase(
            name="test_case_30",
            input_value='24\n17 51\n',
            expected_output=0,
            description="Test case 30: input=24\n17 51\n, expected=0\n"
        ),
        TestCase(
            name="test_case_31",
            input_value='8\n14 57\n',
            expected_output=0,
            description="Test case 31: input=8\n14 57\n, expected=0\n"
        ),
        TestCase(
            name="test_case_32",
            input_value='52\n18 54\n',
            expected_output=2,
            description="Test case 32: input=52\n18 54\n, expected=2\n"
        ),
        TestCase(
            name="test_case_33",
            input_value='20\n15 52\n',
            expected_output=24,
            description="Test case 33: input=20\n15 52\n, expected=24\n"
        ),
        TestCase(
            name="test_case_34",
            input_value='20\n03 58\n',
            expected_output=30,
            description="Test case 34: input=20\n03 58\n, expected=30\n"
        ),
        TestCase(
            name="test_case_35",
            input_value='48\n07 11\n',
            expected_output=0,
            description="Test case 35: input=48\n07 11\n, expected=0\n"
        ),
        TestCase(
            name="test_case_36",
            input_value='32\n04 01\n',
            expected_output=2,
            description="Test case 36: input=32\n04 01\n, expected=2\n"
        ),
        TestCase(
            name="test_case_37",
            input_value='60\n08 15\n',
            expected_output=1,
            description="Test case 37: input=60\n08 15\n, expected=1\n"
        ),
        TestCase(
            name="test_case_38",
            input_value='44\n20 20\n',
            expected_output=4,
            description="Test case 38: input=44\n20 20\n, expected=4\n"
        ),
        TestCase(
            name="test_case_39",
            input_value='55\n15 35\n',
            expected_output=9,
            description="Test case 39: input=55\n15 35\n, expected=9\n"
        ),
        TestCase(
            name="test_case_40",
            input_value='55\n03 49\n',
            expected_output=11,
            description="Test case 40: input=55\n03 49\n, expected=11\n"
        ),
        TestCase(
            name="test_case_41",
            input_value='23\n16 39\n',
            expected_output=4,
            description="Test case 41: input=23\n16 39\n, expected=4\n"
        ),
        TestCase(
            name="test_case_42",
            input_value='7\n20 36\n',
            expected_output=7,
            description="Test case 42: input=7\n20 36\n, expected=7\n"
        ),
        TestCase(
            name="test_case_43",
            input_value='35\n16 42\n',
            expected_output=1,
            description="Test case 43: input=35\n16 42\n, expected=1\n"
        ),
        TestCase(
            name="test_case_44",
            input_value='35\n05 56\n',
            expected_output=21,
            description="Test case 44: input=35\n05 56\n, expected=21\n"
        ),
        TestCase(
            name="test_case_45",
            input_value='3\n17 45\n',
            expected_output=0,
            description="Test case 45: input=3\n17 45\n, expected=0\n"
        ),
        TestCase(
            name="test_case_46",
            input_value='47\n05 59\n',
            expected_output=6,
            description="Test case 46: input=47\n05 59\n, expected=6\n"
        ),
        TestCase(
            name="test_case_47",
            input_value='15\n10 13\n',
            expected_output=9,
            description="Test case 47: input=15\n10 13\n, expected=9\n"
        ),
        TestCase(
            name="test_case_48",
            input_value='59\n06 18\n',
            expected_output=9,
            description="Test case 48: input=59\n06 18\n, expected=9\n"
        ),
        TestCase(
            name="test_case_49",
            input_value='34\n17 18\n',
            expected_output=0,
            description="Test case 49: input=34\n17 18\n, expected=0\n"
        ),
        TestCase(
            name="test_case_50",
            input_value='18\n05 23\n',
            expected_output=2,
            description="Test case 50: input=18\n05 23\n, expected=2\n"
        ),
        TestCase(
            name="test_case_51",
            input_value='46\n17 21\n',
            expected_output=0,
            description="Test case 51: input=46\n17 21\n, expected=0\n"
        ),
        TestCase(
            name="test_case_52",
            input_value='30\n06 27\n',
            expected_output=0,
            description="Test case 52: input=30\n06 27\n, expected=0\n"
        ),
        TestCase(
            name="test_case_53",
            input_value='14\n18 40\n',
            expected_output=3,
            description="Test case 53: input=14\n18 40\n, expected=3\n"
        ),
        TestCase(
            name="test_case_54",
            input_value='58\n22 54\n',
            expected_output=6,
            description="Test case 54: input=58\n22 54\n, expected=6\n"
        ),
        TestCase(
            name="test_case_55",
            input_value='26\n19 44\n',
            expected_output=5,
            description="Test case 55: input=26\n19 44\n, expected=5\n"
        ),
        TestCase(
            name="test_case_56",
            input_value='10\n15 57\n',
            expected_output=0,
            description="Test case 56: input=10\n15 57\n, expected=0\n"
        ),
        TestCase(
            name="test_case_57",
            input_value='54\n20 47\n',
            expected_output=0,
            description="Test case 57: input=54\n20 47\n, expected=0\n"
        ),
        TestCase(
            name="test_case_58",
            input_value='22\n08 45\n',
            expected_output=3,
            description="Test case 58: input=22\n08 45\n, expected=3\n"
        ),
        TestCase(
            name="test_case_59",
            input_value='48\n18 08\n',
            expected_output=1,
            description="Test case 59: input=48\n18 08\n, expected=1\n"
        ),
        TestCase(
            name="test_case_60",
            input_value='32\n07 06\n',
            expected_output=0,
            description="Test case 60: input=32\n07 06\n, expected=0\n"
        ),
        TestCase(
            name="test_case_61",
            input_value='60\n19 19\n',
            expected_output=2,
            description="Test case 61: input=60\n19 19\n, expected=2\n"
        ),
        TestCase(
            name="test_case_62",
            input_value='45\n07 25\n',
            expected_output=0,
            description="Test case 62: input=45\n07 25\n, expected=0\n"
        ),
        TestCase(
            name="test_case_63",
            input_value='29\n12 39\n',
            expected_output=8,
            description="Test case 63: input=29\n12 39\n, expected=8\n"
        ),
        TestCase(
            name="test_case_64",
            input_value='13\n08 28\n',
            expected_output=3,
            description="Test case 64: input=13\n08 28\n, expected=3\n"
        ),
        TestCase(
            name="test_case_65",
            input_value='41\n21 42\n',
            expected_output=5,
            description="Test case 65: input=41\n21 42\n, expected=5\n"
        ),
        TestCase(
            name="test_case_66",
            input_value='41\n09 32\n',
            expected_output=3,
            description="Test case 66: input=41\n09 32\n, expected=3\n"
        ),
        TestCase(
            name="test_case_67",
            input_value='9\n21 45\n',
            expected_output=2,
            description="Test case 67: input=9\n21 45\n, expected=2\n"
        ),
        TestCase(
            name="test_case_68",
            input_value='37\n10 43\n',
            expected_output=5,
            description="Test case 68: input=37\n10 43\n, expected=5\n"
        ),
        TestCase(
            name="test_case_69",
            input_value='3\n20 50\n',
            expected_output=1,
            description="Test case 69: input=3\n20 50\n, expected=1\n"
        ),
        TestCase(
            name="test_case_70",
            input_value='47\n00 04\n',
            expected_output=1,
            description="Test case 70: input=47\n00 04\n, expected=1\n"
        ),
        TestCase(
            name="test_case_71",
            input_value='15\n13 10\n',
            expected_output=21,
            description="Test case 71: input=15\n13 10\n, expected=21\n"
        ),
        TestCase(
            name="test_case_72",
            input_value='15\n17 23\n',
            expected_output=0,
            description="Test case 72: input=15\n17 23\n, expected=0\n"
        ),
        TestCase(
            name="test_case_73",
            input_value='43\n22 13\n',
            expected_output=2,
            description="Test case 73: input=43\n22 13\n, expected=2\n"
        ),
        TestCase(
            name="test_case_74",
            input_value='27\n10 26\n',
            expected_output=6,
            description="Test case 74: input=27\n10 26\n, expected=6\n"
        ),
        TestCase(
            name="test_case_75",
            input_value='55\n22 24\n',
            expected_output=5,
            description="Test case 75: input=55\n22 24\n, expected=5\n"
        ),
        TestCase(
            name="test_case_76",
            input_value='55\n03 30\n',
            expected_output=11,
            description="Test case 76: input=55\n03 30\n, expected=11\n"
        ),
        TestCase(
            name="test_case_77",
            input_value='24\n23 27\n',
            expected_output=0,
            description="Test case 77: input=24\n23 27\n, expected=0\n"
        ),
        TestCase(
            name="test_case_78",
            input_value='52\n11 33\n',
            expected_output=3,
            description="Test case 78: input=52\n11 33\n, expected=3\n"
        ),
        TestCase(
            name="test_case_79",
            input_value='18\n22 48\n',
            expected_output=17,
            description="Test case 79: input=18\n22 48\n, expected=17\n"
        ),
        TestCase(
            name="test_case_80",
            input_value='1\n12 55\n',
            expected_output=8,
            description="Test case 80: input=1\n12 55\n, expected=8\n"
        ),
        TestCase(
            name="test_case_81",
            input_value='1\n04 27\n',
            expected_output=0,
            description="Test case 81: input=1\n04 27\n, expected=0\n"
        ),
        TestCase(
            name="test_case_82",
            input_value='1\n12 52\n',
            expected_output=5,
            description="Test case 82: input=1\n12 52\n, expected=5\n"
        ),
        TestCase(
            name="test_case_83",
            input_value='1\n20 16\n',
            expected_output=9,
            description="Test case 83: input=1\n20 16\n, expected=9\n"
        ),
        TestCase(
            name="test_case_84",
            input_value='1\n04 41\n',
            expected_output=4,
            description="Test case 84: input=1\n04 41\n, expected=4\n"
        ),
        TestCase(
            name="test_case_85",
            input_value='1\n20 21\n',
            expected_output=4,
            description="Test case 85: input=1\n20 21\n, expected=4\n"
        ),
        TestCase(
            name="test_case_86",
            input_value='1\n04 45\n',
            expected_output=8,
            description="Test case 86: input=1\n04 45\n, expected=8\n"
        ),
        TestCase(
            name="test_case_87",
            input_value='1\n12 18\n',
            expected_output=1,
            description="Test case 87: input=1\n12 18\n, expected=1\n"
        ),
        TestCase(
            name="test_case_88",
            input_value='1\n04 42\n',
            expected_output=5,
            description="Test case 88: input=1\n04 42\n, expected=5\n"
        ),
        TestCase(
            name="test_case_89",
            input_value='1\n02 59\n',
            expected_output=2,
            description="Test case 89: input=1\n02 59\n, expected=2\n"
        ),
        TestCase(
            name="test_case_90",
            input_value='1\n18 24\n',
            expected_output=7,
            description="Test case 90: input=1\n18 24\n, expected=7\n"
        ),
        TestCase(
            name="test_case_91",
            input_value='1\n02 04\n',
            expected_output=7,
            description="Test case 91: input=1\n02 04\n, expected=7\n"
        ),
        TestCase(
            name="test_case_92",
            input_value='1\n18 28\n',
            expected_output=1,
            description="Test case 92: input=1\n18 28\n, expected=1\n"
        ),
        TestCase(
            name="test_case_93",
            input_value='1\n18 01\n',
            expected_output=2,
            description="Test case 93: input=1\n18 01\n, expected=2\n"
        ),
        TestCase(
            name="test_case_94",
            input_value='1\n10 25\n',
            expected_output=8,
            description="Test case 94: input=1\n10 25\n, expected=8\n"
        ),
        TestCase(
            name="test_case_95",
            input_value='1\n02 49\n',
            expected_output=2,
            description="Test case 95: input=1\n02 49\n, expected=2\n"
        ),
        TestCase(
            name="test_case_96",
            input_value='1\n02 30\n',
            expected_output=3,
            description="Test case 96: input=1\n02 30\n, expected=3\n"
        ),
        TestCase(
            name="test_case_97",
            input_value='1\n18 54\n',
            expected_output=7,
            description="Test case 97: input=1\n18 54\n, expected=7\n"
        ),
        TestCase(
            name="test_case_98",
            input_value='1\n02 19\n',
            expected_output=2,
            description="Test case 98: input=1\n02 19\n, expected=2\n"
        ),
        TestCase(
            name="test_case_99",
            input_value='1\n05 25\n',
            expected_output=8,
            description="Test case 99: input=1\n05 25\n, expected=8\n"
        ),
        TestCase(
            name="test_case_100",
            input_value='60\n23 55\n',
            expected_output=6,
            description="Test case 100: input=60\n23 55\n, expected=6\n"
        ),
        TestCase(
            name="test_case_101",
            input_value='60\n08 19\n',
            expected_output=1,
            description="Test case 101: input=60\n08 19\n, expected=1\n"
        ),
        TestCase(
            name="test_case_102",
            input_value='60\n00 00\n',
            expected_output=7,
            description="Test case 102: input=60\n00 00\n, expected=7\n"
        ),
        TestCase(
            name="test_case_103",
            input_value='60\n08 24\n',
            expected_output=1,
            description="Test case 103: input=60\n08 24\n, expected=1\n"
        ),
        TestCase(
            name="test_case_104",
            input_value='60\n16 13\n',
            expected_output=9,
            description="Test case 104: input=60\n16 13\n, expected=9\n"
        ),
        TestCase(
            name="test_case_105",
            input_value='60\n08 21\n',
            expected_output=1,
            description="Test case 105: input=60\n08 21\n, expected=1\n"
        ),
        TestCase(
            name="test_case_106",
            input_value='60\n16 45\n',
            expected_output=9,
            description="Test case 106: input=60\n16 45\n, expected=9\n"
        ),
        TestCase(
            name="test_case_107",
            input_value='60\n08 26\n',
            expected_output=1,
            description="Test case 107: input=60\n08 26\n, expected=1\n"
        ),
        TestCase(
            name="test_case_108",
            input_value='60\n08 50\n',
            expected_output=1,
            description="Test case 108: input=60\n08 50\n, expected=1\n"
        ),
        TestCase(
            name="test_case_109",
            input_value='60\n05 21\n',
            expected_output=12,
            description="Test case 109: input=60\n05 21\n, expected=12\n"
        ),
        TestCase(
            name="test_case_110",
            input_value='60\n13 29\n',
            expected_output=6,
            description="Test case 110: input=60\n13 29\n, expected=6\n"
        ),
        TestCase(
            name="test_case_111",
            input_value='60\n05 18\n',
            expected_output=12,
            description="Test case 111: input=60\n05 18\n, expected=12\n"
        ),
        TestCase(
            name="test_case_112",
            input_value='60\n13 42\n',
            expected_output=6,
            description="Test case 112: input=60\n13 42\n, expected=6\n"
        ),
        TestCase(
            name="test_case_113",
            input_value='60\n05 07\n',
            expected_output=0,
            description="Test case 113: input=60\n05 07\n, expected=0\n"
        ),
        TestCase(
            name="test_case_114",
            input_value='60\n05 47\n',
            expected_output=0,
            description="Test case 114: input=60\n05 47\n, expected=0\n"
        ),
        TestCase(
            name="test_case_115",
            input_value='60\n21 55\n',
            expected_output=4,
            description="Test case 115: input=60\n21 55\n, expected=4\n"
        ),
        TestCase(
            name="test_case_116",
            input_value='60\n05 36\n',
            expected_output=12,
            description="Test case 116: input=60\n05 36\n, expected=12\n"
        ),
        TestCase(
            name="test_case_117",
            input_value='60\n21 08\n',
            expected_output=4,
            description="Test case 117: input=60\n21 08\n, expected=4\n"
        ),
        TestCase(
            name="test_case_118",
            input_value='60\n21 32\n',
            expected_output=4,
            description="Test case 118: input=60\n21 32\n, expected=4\n"
        ),
        TestCase(
            name="test_case_119",
            input_value='60\n16 31\n',
            expected_output=9,
            description="Test case 119: input=60\n16 31\n, expected=9\n"
        ),
        TestCase(
            name="test_case_120",
            input_value='5\n00 00\n',
            expected_output=73,
            description="Test case 120: input=5\n00 00\n, expected=73\n"
        ),
        TestCase(
            name="test_case_121",
            input_value='2\n06 58\n',
            expected_output=390,
            description="Test case 121: input=2\n06 58\n, expected=390\n"
        ),
        TestCase(
            name="test_case_122",
            input_value='60\n00 00\n',
            expected_output=7,
            description="Test case 122: input=60\n00 00\n, expected=7\n"
        ),
        TestCase(
            name="test_case_123",
            input_value='2\n00 00\n',
            expected_output=181,
            description="Test case 123: input=2\n00 00\n, expected=181\n"
        ),
        TestCase(
            name="test_case_124",
            input_value='10\n00 00\n',
            expected_output=37,
            description="Test case 124: input=10\n00 00\n, expected=37\n"
        ),
        TestCase(
            name="test_case_125",
            input_value='60\n01 00\n',
            expected_output=8,
            description="Test case 125: input=60\n01 00\n, expected=8\n"
        ),
        TestCase(
            name="test_case_126",
            input_value='12\n00 06\n',
            expected_output=31,
            description="Test case 126: input=12\n00 06\n, expected=31\n"
        ),
        TestCase(
            name="test_case_127",
            input_value='1\n00 01\n',
            expected_output=4,
            description="Test case 127: input=1\n00 01\n, expected=4\n"
        ),
        TestCase(
            name="test_case_128",
            input_value='5\n00 05\n',
            expected_output=74,
            description="Test case 128: input=5\n00 05\n, expected=74\n"
        ),
        TestCase(
            name="test_case_129",
            input_value='60\n01 01\n',
            expected_output=8,
            description="Test case 129: input=60\n01 01\n, expected=8\n"
        ),
        TestCase(
            name="test_case_130",
            input_value='11\n18 11\n',
            expected_output=2,
            description="Test case 130: input=11\n18 11\n, expected=2\n"
        ),
        TestCase(
            name="test_case_131",
            input_value='60\n01 15\n',
            expected_output=8,
            description="Test case 131: input=60\n01 15\n, expected=8\n"
        ),
        TestCase(
            name="test_case_132",
            input_value='10\n00 16\n',
            expected_output=38,
            description="Test case 132: input=10\n00 16\n, expected=38\n"
        ),
        TestCase(
            name="test_case_133",
            input_value='60\n00 59\n',
            expected_output=7,
            description="Test case 133: input=60\n00 59\n, expected=7\n"
        ),
        TestCase(
            name="test_case_134",
            input_value='30\n00 00\n',
            expected_output=13,
            description="Test case 134: input=30\n00 00\n, expected=13\n"
        ),
        TestCase(
            name="test_case_135",
            input_value='60\n01 05\n',
            expected_output=8,
            description="Test case 135: input=60\n01 05\n, expected=8\n"
        ),
        TestCase(
            name="test_case_136",
            input_value='4\n00 03\n',
            expected_output=4,
            description="Test case 136: input=4\n00 03\n, expected=4\n"
        ),
        TestCase(
            name="test_case_137",
            input_value='4\n00 00\n',
            expected_output=91,
            description="Test case 137: input=4\n00 00\n, expected=91\n"
        ),
        TestCase(
            name="test_case_138",
            input_value='60\n00 01\n',
            expected_output=7,
            description="Test case 138: input=60\n00 01\n, expected=7\n"
        ),
        TestCase(
            name="test_case_139",
            input_value='6\n00 03\n',
            expected_output=1,
            description="Test case 139: input=6\n00 03\n, expected=1\n"
        ),
        TestCase(
            name="test_case_140",
            input_value='13\n00 00\n',
            expected_output=1,
            description="Test case 140: input=13\n00 00\n, expected=1\n"
        ),
        TestCase(
            name="test_case_141",
            input_value='1\n18 01\n',
            expected_output=2,
            description="Test case 141: input=1\n18 01\n, expected=2\n"
        ),
        TestCase(
            name="test_case_142",
            input_value='5\n06 00\n',
            expected_output=145,
            description="Test case 142: input=5\n06 00\n, expected=145\n"
        ),
        TestCase(
            name="test_case_143",
            input_value='60\n04 08\n',
            expected_output=11,
            description="Test case 143: input=60\n04 08\n, expected=11\n"
        ),
        TestCase(
            name="test_case_144",
            input_value='5\n01 55\n',
            expected_output=96,
            description="Test case 144: input=5\n01 55\n, expected=96\n"
        ),
        TestCase(
            name="test_case_145",
            input_value='8\n00 08\n',
            expected_output=47,
            description="Test case 145: input=8\n00 08\n, expected=47\n"
        ),
        TestCase(
            name="test_case_146",
            input_value='23\n18 23\n',
            expected_output=2,
            description="Test case 146: input=23\n18 23\n, expected=2\n"
        ),
        TestCase(
            name="test_case_147",
            input_value='6\n00 06\n',
            expected_output=62,
            description="Test case 147: input=6\n00 06\n, expected=62\n"
        ),
        TestCase(
            name="test_case_148",
            input_value='59\n18 59\n',
            expected_output=2,
            description="Test case 148: input=59\n18 59\n, expected=2\n"
        ),
        TestCase(
            name="test_case_149",
            input_value='11\n00 10\n',
            expected_output=3,
            description="Test case 149: input=11\n00 10\n, expected=3\n"
        ),
        TestCase(
            name="test_case_150",
            input_value='10\n00 01\n',
            expected_output=37,
            description="Test case 150: input=10\n00 01\n, expected=37\n"
        ),
        TestCase(
            name="test_case_151",
            input_value='59\n00 00\n',
            expected_output=7,
            description="Test case 151: input=59\n00 00\n, expected=7\n"
        ),
        TestCase(
            name="test_case_152",
            input_value='10\n18 10\n',
            expected_output=2,
            description="Test case 152: input=10\n18 10\n, expected=2\n"
        ),
        TestCase(
            name="test_case_153",
            input_value='5\n00 01\n',
            expected_output=73,
            description="Test case 153: input=5\n00 01\n, expected=73\n"
        ),
        TestCase(
            name="test_case_154",
            input_value='1\n00 00\n',
            expected_output=3,
            description="Test case 154: input=1\n00 00\n, expected=3\n"
        ),
        TestCase(
            name="test_case_155",
            input_value='8\n00 14\n',
            expected_output=47,
            description="Test case 155: input=8\n00 14\n, expected=47\n"
        ),
        TestCase(
            name="test_case_156",
            input_value='60\n03 00\n',
            expected_output=10,
            description="Test case 156: input=60\n03 00\n, expected=10\n"
        ),
        TestCase(
            name="test_case_157",
            input_value='60\n00 10\n',
            expected_output=7,
            description="Test case 157: input=60\n00 10\n, expected=7\n"
        ),
        TestCase(
            name="test_case_158",
            input_value='5\n01 13\n',
            expected_output=87,
            description="Test case 158: input=5\n01 13\n, expected=87\n"
        ),
        TestCase(
            name="test_case_159",
            input_value='30\n02 43\n',
            expected_output=18,
            description="Test case 159: input=30\n02 43\n, expected=18\n"
        ),
        TestCase(
            name="test_case_160",
            input_value='17\n00 08\n',
            expected_output=3,
            description="Test case 160: input=17\n00 08\n, expected=3\n"
        ),
        TestCase(
            name="test_case_161",
            input_value='3\n00 00\n',
            expected_output=1,
            description="Test case 161: input=3\n00 00\n, expected=1\n"
        ),
        TestCase(
            name="test_case_162",
            input_value='60\n00 05\n',
            expected_output=7,
            description="Test case 162: input=60\n00 05\n, expected=7\n"
        ),
        TestCase(
            name="test_case_163",
            input_value='5\n18 05\n',
            expected_output=2,
            description="Test case 163: input=5\n18 05\n, expected=2\n"
        ),
        TestCase(
            name="test_case_164",
            input_value='30\n00 30\n',
            expected_output=14,
            description="Test case 164: input=30\n00 30\n, expected=14\n"
        ),
        TestCase(
            name="test_case_165",
            input_value='1\n00 06\n',
            expected_output=9,
            description="Test case 165: input=1\n00 06\n, expected=9\n"
        ),
        TestCase(
            name="test_case_166",
            input_value='55\n00 00\n',
            expected_output=7,
            description="Test case 166: input=55\n00 00\n, expected=7\n"
        ),
        TestCase(
            name="test_case_167",
            input_value='8\n02 08\n',
            expected_output=62,
            description="Test case 167: input=8\n02 08\n, expected=62\n"
        ),
        TestCase(
            name="test_case_168",
            input_value='7\n00 00\n',
            expected_output=9,
            description="Test case 168: input=7\n00 00\n, expected=9\n"
        ),
        TestCase(
            name="test_case_169",
            input_value='6\n08 06\n',
            expected_output=2,
            description="Test case 169: input=6\n08 06\n, expected=2\n"
        ),
        TestCase(
            name="test_case_170",
            input_value='48\n06 24\n',
            expected_output=16,
            description="Test case 170: input=48\n06 24\n, expected=16\n"
        ),
        TestCase(
            name="test_case_171",
            input_value='8\n06 58\n',
            expected_output=98,
            description="Test case 171: input=8\n06 58\n, expected=98\n"
        ),
        TestCase(
            name="test_case_172",
            input_value='3\n12 00\n',
            expected_output=1,
            description="Test case 172: input=3\n12 00\n, expected=1\n"
        ),
        TestCase(
            name="test_case_173",
            input_value='5\n01 06\n',
            expected_output=86,
            description="Test case 173: input=5\n01 06\n, expected=86\n"
        ),
        TestCase(
            name="test_case_174",
            input_value='2\n00 08\n',
            expected_output=185,
            description="Test case 174: input=2\n00 08\n, expected=185\n"
        ),
        TestCase(
            name="test_case_175",
            input_value='3\n18 03\n',
            expected_output=2,
            description="Test case 175: input=3\n18 03\n, expected=2\n"
        ),
        TestCase(
            name="test_case_176",
            input_value='1\n17 00\n',
            expected_output=0,
            description="Test case 176: input=1\n17 00\n, expected=0\n"
        ),
        TestCase(
            name="test_case_177",
            input_value='59\n00 48\n',
            expected_output=7,
            description="Test case 177: input=59\n00 48\n, expected=7\n"
        ),
        TestCase(
            name="test_case_178",
            input_value='5\n12 01\n',
            expected_output=49,
            description="Test case 178: input=5\n12 01\n, expected=49\n"
        ),
        TestCase(
            name="test_case_179",
            input_value='55\n01 25\n',
            expected_output=9,
            description="Test case 179: input=55\n01 25\n, expected=9\n"
        ),
        TestCase(
            name="test_case_180",
            input_value='2\n07 23\n',
            expected_output=0,
            description="Test case 180: input=2\n07 23\n, expected=0\n"
        ),
        TestCase(
            name="test_case_181",
            input_value='10\n01 10\n',
            expected_output=44,
            description="Test case 181: input=10\n01 10\n, expected=44\n"
        ),
        TestCase(
            name="test_case_182",
            input_value='2\n00 01\n',
            expected_output=2,
            description="Test case 182: input=2\n00 01\n, expected=2\n"
        ),
        TestCase(
            name="test_case_183",
            input_value='59\n00 01\n',
            expected_output=6,
            description="Test case 183: input=59\n00 01\n, expected=6\n"
        ),
        TestCase(
            name="test_case_184",
            input_value='5\n00 02\n',
            expected_output=1,
            description="Test case 184: input=5\n00 02\n, expected=1\n"
        ),
        TestCase(
            name="test_case_185",
            input_value='4\n01 02\n',
            expected_output=106,
            description="Test case 185: input=4\n01 02\n, expected=106\n"
        ),
        TestCase(
            name="test_case_186",
            input_value='5\n00 06\n',
            expected_output=74,
            description="Test case 186: input=5\n00 06\n, expected=74\n"
        ),
        TestCase(
            name="test_case_187",
            input_value='42\n00 08\n',
            expected_output=9,
            description="Test case 187: input=42\n00 08\n, expected=9\n"
        ),
        TestCase(
            name="test_case_188",
            input_value='60\n01 20\n',
            expected_output=8,
            description="Test case 188: input=60\n01 20\n, expected=8\n"
        ),
        TestCase(
            name="test_case_189",
            input_value='3\n06 00\n',
            expected_output=1,
            description="Test case 189: input=3\n06 00\n, expected=1\n"
        ),
        TestCase(
            name="test_case_190",
            input_value='4\n00 01\n',
            expected_output=1,
            description="Test case 190: input=4\n00 01\n, expected=1\n"
        ),
        TestCase(
            name="test_case_191",
            input_value='2\n00 06\n',
            expected_output=184,
            description="Test case 191: input=2\n00 06\n, expected=184\n"
        ),
        TestCase(
            name="test_case_192",
            input_value='1\n00 57\n',
            expected_output=0,
            description="Test case 192: input=1\n00 57\n, expected=0\n"
        ),
        TestCase(
            name="test_case_193",
            input_value='6\n00 00\n',
            expected_output=61,
            description="Test case 193: input=6\n00 00\n, expected=61\n"
        ),
        TestCase(
            name="test_case_194",
            input_value='5\n08 40\n',
            expected_output=9,
            description="Test case 194: input=5\n08 40\n, expected=9\n"
        ),
        TestCase(
            name="test_case_195",
            input_value='58\n00 55\n',
            expected_output=1,
            description="Test case 195: input=58\n00 55\n, expected=1\n"
        ),
        TestCase(
            name="test_case_196",
            input_value='2\n00 02\n',
            expected_output=182,
            description="Test case 196: input=2\n00 02\n, expected=182\n"
        ),
        TestCase(
            name="test_case_197",
            input_value='1\n08 01\n',
            expected_output=2,
            description="Test case 197: input=1\n08 01\n, expected=2\n"
        ),
        TestCase(
            name="test_case_198",
            input_value='10\n10 10\n',
            expected_output=14,
            description="Test case 198: input=10\n10 10\n, expected=14\n"
        ),
        TestCase(
            name="test_case_199",
            input_value='60\n01 11\n',
            expected_output=8,
            description="Test case 199: input=60\n01 11\n, expected=8\n"
        ),
        TestCase(
            name="test_case_200",
            input_value='2\n07 00\n',
            expected_output=0,
            description="Test case 200: input=2\n07 00\n, expected=0\n"
        ),
        TestCase(
            name="test_case_201",
            input_value='15\n00 03\n',
            expected_output=25,
            description="Test case 201: input=15\n00 03\n, expected=25\n"
        ),
        TestCase(
            name="test_case_202",
            input_value='6\n04 34\n',
            expected_output=106,
            description="Test case 202: input=6\n04 34\n, expected=106\n"
        ),
        TestCase(
            name="test_case_203",
            input_value='16\n00 16\n',
            expected_output=24,
            description="Test case 203: input=16\n00 16\n, expected=24\n"
        ),
        TestCase(
            name="test_case_204",
            input_value='2\n00 59\n',
            expected_output=1,
            description="Test case 204: input=2\n00 59\n, expected=1\n"
        ),
        TestCase(
            name="test_case_205",
            input_value='59\n00 08\n',
            expected_output=7,
            description="Test case 205: input=59\n00 08\n, expected=7\n"
        ),
        TestCase(
            name="test_case_206",
            input_value='10\n03 10\n',
            expected_output=56,
            description="Test case 206: input=10\n03 10\n, expected=56\n"
        ),
        TestCase(
            name="test_case_207",
            input_value='3\n08 03\n',
            expected_output=2,
            description="Test case 207: input=3\n08 03\n, expected=2\n"
        ),
        TestCase(
            name="test_case_208",
            input_value='20\n06 11\n',
            expected_output=37,
            description="Test case 208: input=20\n06 11\n, expected=37\n"
        ),
        TestCase(
            name="test_case_209",
            input_value='4\n01 00\n',
            expected_output=106,
            description="Test case 209: input=4\n01 00\n, expected=106\n"
        ),
        TestCase(
            name="test_case_210",
            input_value='38\n01 08\n',
            expected_output=12,
            description="Test case 210: input=38\n01 08\n, expected=12\n"
        ),
        TestCase(
            name="test_case_211",
            input_value='60\n00 06\n',
            expected_output=7,
            description="Test case 211: input=60\n00 06\n, expected=7\n"
        ),
        TestCase(
            name="test_case_212",
            input_value='5\n12 00\n',
            expected_output=49,
            description="Test case 212: input=5\n12 00\n, expected=49\n"
        ),
        TestCase(
            name="test_case_213",
            input_value='6\n01 42\n',
            expected_output=78,
            description="Test case 213: input=6\n01 42\n, expected=78\n"
        ),
        TestCase(
            name="test_case_214",
            input_value='4\n00 04\n',
            expected_output=92,
            description="Test case 214: input=4\n00 04\n, expected=92\n"
        ),
        TestCase(
            name="test_case_215",
            input_value='60\n04 05\n',
            expected_output=11,
            description="Test case 215: input=60\n04 05\n, expected=11\n"
        ),
        TestCase(
            name="test_case_216",
            input_value='1\n00 53\n',
            expected_output=6,
            description="Test case 216: input=1\n00 53\n, expected=6\n"
        ),
        TestCase(
            name="test_case_217",
            input_value='5\n08 05\n',
            expected_output=2,
            description="Test case 217: input=5\n08 05\n, expected=2\n"
        ),
        TestCase(
            name="test_case_218",
            input_value='60\n18 45\n',
            expected_output=1,
            description="Test case 218: input=60\n18 45\n, expected=1\n"
        ),
        TestCase(
            name="test_case_219",
            input_value='60\n06 23\n',
            expected_output=13,
            description="Test case 219: input=60\n06 23\n, expected=13\n"
        ),
        TestCase(
            name="test_case_220",
            input_value='6\n00 15\n',
            expected_output=3,
            description="Test case 220: input=6\n00 15\n, expected=3\n"
        ),
        TestCase(
            name="test_case_221",
            input_value='58\n00 06\n',
            expected_output=7,
            description="Test case 221: input=58\n00 06\n, expected=7\n"
        ),
        TestCase(
            name="test_case_222",
            input_value='2\n06 44\n',
            expected_output=383,
            description="Test case 222: input=2\n06 44\n, expected=383\n"
        ),
        TestCase(
            name="test_case_223",
            input_value='1\n08 00\n',
            expected_output=1,
            description="Test case 223: input=1\n08 00\n, expected=1\n"
        ),
        TestCase(
            name="test_case_224",
            input_value='10\n06 58\n',
            expected_output=78,
            description="Test case 224: input=10\n06 58\n, expected=78\n"
        ),
        TestCase(
            name="test_case_225",
            input_value='59\n00 58\n',
            expected_output=8,
            description="Test case 225: input=59\n00 58\n, expected=8\n"
        ),
        TestCase(
            name="test_case_226",
            input_value='1\n18 00\n',
            expected_output=1,
            description="Test case 226: input=1\n18 00\n, expected=1\n"
        ),
        TestCase(
            name="test_case_227",
            input_value='50\n00 42\n',
            expected_output=9,
            description="Test case 227: input=50\n00 42\n, expected=9\n"
        ),
        TestCase(
            name="test_case_228",
            input_value='30\n18 30\n',
            expected_output=2,
            description="Test case 228: input=30\n18 30\n, expected=2\n"
        ),
        TestCase(
            name="test_case_229",
            input_value='60\n21 59\n',
            expected_output=4,
            description="Test case 229: input=60\n21 59\n, expected=4\n"
        ),
        TestCase(
            name="test_case_230",
            input_value='2\n10 52\n',
            expected_output=87,
            description="Test case 230: input=2\n10 52\n, expected=87\n"
        ),
        TestCase(
            name="test_case_231",
            input_value='56\n00 00\n',
            expected_output=7,
            description="Test case 231: input=56\n00 00\n, expected=7\n"
        ),
        TestCase(
            name="test_case_232",
            input_value='16\n18 16\n',
            expected_output=2,
            description="Test case 232: input=16\n18 16\n, expected=2\n"
        ),
        TestCase(
            name="test_case_233",
            input_value='5\n01 05\n',
            expected_output=86,
            description="Test case 233: input=5\n01 05\n, expected=86\n"
        ),
        TestCase(
            name="test_case_234",
            input_value='5\n05 00\n',
            expected_output=133,
            description="Test case 234: input=5\n05 00\n, expected=133\n"
        ),
        TestCase(
            name="test_case_235",
            input_value='5\n23 59\n',
            expected_output=72,
            description="Test case 235: input=5\n23 59\n, expected=72\n"
        ),
        TestCase(
            name="test_case_236",
            input_value='7\n17 13\n',
            expected_output=0,
            description="Test case 236: input=7\n17 13\n, expected=0\n"
        ),
        TestCase(
            name="test_case_237",
            input_value='58\n00 00\n',
            expected_output=7,
            description="Test case 237: input=58\n00 00\n, expected=7\n"
        ),
        TestCase(
            name="test_case_238",
            input_value='15\n00 07\n',
            expected_output=0,
            description="Test case 238: input=15\n00 07\n, expected=0\n"
        ),
        TestCase(
            name="test_case_239",
            input_value='59\n08 00\n',
            expected_output=1,
            description="Test case 239: input=59\n08 00\n, expected=1\n"
        ),
        TestCase(
            name="test_case_240",
            input_value='46\n00 00\n',
            expected_output=8,
            description="Test case 240: input=46\n00 00\n, expected=8\n"
        ),
        TestCase(
            name="test_case_241",
            input_value='59\n01 05\n',
            expected_output=2,
            description="Test case 241: input=59\n01 05\n, expected=2\n"
        ),
        TestCase(
            name="test_case_242",
            input_value='2\n01 00\n',
            expected_output=211,
            description="Test case 242: input=2\n01 00\n, expected=211\n"
        ),
        TestCase(
            name="test_case_243",
            input_value='60\n00 24\n',
            expected_output=7,
            description="Test case 243: input=60\n00 24\n, expected=7\n"
        ),
        TestCase(
            name="test_case_244",
            input_value='10\n00 08\n',
            expected_output=37,
            description="Test case 244: input=10\n00 08\n, expected=37\n"
        ),
        TestCase(
            name="test_case_245",
            input_value='10\n00 06\n',
            expected_output=37,
            description="Test case 245: input=10\n00 06\n, expected=37\n"
        ),
        TestCase(
            name="test_case_246",
            input_value='60\n01 24\n',
            expected_output=8,
            description="Test case 246: input=60\n01 24\n, expected=8\n"
        ),
        TestCase(
            name="test_case_247",
            input_value='50\n00 10\n',
            expected_output=8,
            description="Test case 247: input=50\n00 10\n, expected=8\n"
        ),
        TestCase(
            name="test_case_248",
            input_value='2\n03 00\n',
            expected_output=271,
            description="Test case 248: input=2\n03 00\n, expected=271\n"
        ),
        TestCase(
            name="test_case_249",
            input_value='4\n19 04\n',
            expected_output=17,
            description="Test case 249: input=4\n19 04\n, expected=17\n"
        ),
        TestCase(
            name="test_case_250",
            input_value='25\n00 23\n',
            expected_output=16,
            description="Test case 250: input=25\n00 23\n, expected=16\n"
        ),
        TestCase(
            name="test_case_251",
            input_value='10\n01 01\n',
            expected_output=43,
            description="Test case 251: input=10\n01 01\n, expected=43\n"
        ),
    ]
    
    return Problem(
        name="apps_0004",
        description=r"""Jamie loves sleeping. One day, he decides that he needs to wake up at exactly hh: mm. However, he hates waking up, so he wants to make waking up less painful by setting the alarm at an UNLUCKY time (a time that does NOT contain the digit '7'). He will then press the snooze button every x minutes until hh: mm is reached, and only then he will wake up. He wants to know what is the LARGEST number of times he needs to press the snooze button.

A time is considered unlucky if it does NOT contain a digit '7'. For example, 00: 48 and 21: 34 are unlucky, while 13: 07 and 17: 27 are lucky.

Note that it is not necessary that the time set for the alarm and the wake-up time are on the same day. It is guaranteed that there is an unlucky time Jamie can set so that he can wake at hh: mm.

Formally, find the LARGEST possible non-negative integer y such that the time representation of the time x·y minutes before hh: mm does NOT contain the digit '7'.

Jamie uses 24-hours clock, so after 23: 59 comes 00: 00.


-----Input-----

The first line contains a single integer x (1 ≤ x ≤ 60).

The second line contains two two-digit integers, hh and mm (00 ≤ hh ≤ 23, 00 ≤ mm ≤ 59).


-----Output-----

Print the MAXIMUM number of times he needs to press the button.


-----Examples-----
Input
3
11 23

Output
2

Input
5
01 07

Output
0



-----Note-----

In the first sample, Jamie needs to wake up at 11:23. So, he can set his alarm at 11:17. He would press the snooze button when the alarm rings at 11:17 and at 11:20.

In the second sample, Jamie can set his alarm at exactly at 01:07 which is lucky.""",
        function_signature="def ok(mm):",
        visible_tests=visible_tests,
        hidden_tests=hidden_tests
    )