"""
apps_0000 problem from APPS dataset.
"""

from typing import List
from ...core.problem import Problem, TestCase


def create_apps_0000() -> Problem:
    """
    Create the apps_0000 problem.
    """
    # Visible tests (shown to the model)
    visible_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value='|[a:b:|]\n',
            expected_output=4,
            description="Test case 1: input=|[a:b:|]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_2",
            input_value='|]:[|:]\n',
            expected_output=-1,
            description="Test case 2: input=|]:[|:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_3",
            input_value=':][:\n',
            expected_output=-1,
            description="Test case 3: input=:][:\n, expected=-1\n"
        ),
    ]
    
    # Hidden tests (not shown to model, used for validation)
    hidden_tests: List[TestCase] = [
        TestCase(
            name="test_case_1",
            input_value=':[]:\n',
            expected_output=-1,
            description="Test case 1: input=:[]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_2",
            input_value='[[:]]\n',
            expected_output=-1,
            description="Test case 2: input=[[:]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_3",
            input_value='[::]\n',
            expected_output=4,
            description="Test case 3: input=[::]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_4",
            input_value=']:|:[\n',
            expected_output=-1,
            description="Test case 4: input=]:|:[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_5",
            input_value=':::::]\n',
            expected_output=-1,
            description="Test case 5: input=:::::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_6",
            input_value='::::]\n',
            expected_output=-1,
            description="Test case 6: input=::::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_7",
            input_value='::[]\n',
            expected_output=-1,
            description="Test case 7: input=::[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_8",
            input_value=[],
            expected_output=-1,
            description="Test case 8: input=[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_9",
            input_value='[a|[::]\n',
            expected_output=4,
            description="Test case 9: input=[a|[::]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_10",
            input_value='dsfdsfds\n',
            expected_output=-1,
            description="Test case 10: input=dsfdsfds\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_11",
            input_value=':[||]:\n',
            expected_output=-1,
            description="Test case 11: input=:[||]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_12",
            input_value='::]\n',
            expected_output=-1,
            description="Test case 12: input=::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_13",
            input_value=':::]\n',
            expected_output=-1,
            description="Test case 13: input=:::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_14",
            input_value='[||]\n',
            expected_output=-1,
            description="Test case 14: input=[||]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_15",
            input_value=':[[[:]]]:\n',
            expected_output=-1,
            description="Test case 15: input=:[[[:]]]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_16",
            input_value='::]::[:]::[::\n',
            expected_output=-1,
            description="Test case 16: input=::]::[:]::[::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_17",
            input_value='[:|:]\n',
            expected_output=5,
            description="Test case 17: input=[:|:]\n, expected=5\n"
        ),
        TestCase(
            name="test_case_18",
            input_value='[::]aaaaaaaa\n',
            expected_output=4,
            description="Test case 18: input=[::]aaaaaaaa\n, expected=4\n"
        ),
        TestCase(
            name="test_case_19",
            input_value='[[::]|]\n',
            expected_output=4,
            description="Test case 19: input=[[::]|]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_20",
            input_value='[::::\n',
            expected_output=-1,
            description="Test case 20: input=[::::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_21",
            input_value='][\n',
            expected_output=-1,
            description="Test case 21: input=][\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_22",
            input_value='[||]][[]\n',
            expected_output=-1,
            description="Test case 22: input=[||]][[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_23",
            input_value='][k:\n',
            expected_output=-1,
            description="Test case 23: input=][k:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_24",
            input_value='::|[]\n',
            expected_output=-1,
            description="Test case 24: input=::|[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_25",
            input_value='[:\n',
            expected_output=-1,
            description="Test case 25: input=[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_26",
            input_value='||||\n',
            expected_output=-1,
            description="Test case 26: input=||||\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_27",
            input_value='||]ekq\n',
            expected_output=-1,
            description="Test case 27: input=||]ekq\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_28",
            input_value=']:|||:]\n',
            expected_output=-1,
            description="Test case 28: input=]:|||:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_29",
            input_value='|||[|||:[m[[n[[[xuy|:[[[:|:[:k[qlihm:ty[\n',
            expected_output=-1,
            description="Test case 29: input=|||[|||:[m[[n[[[xuy|:[[[:|:[:k[qlihm:ty[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_30",
            input_value='aaaaa[[[[[:[[[[a]]\n',
            expected_output=-1,
            description="Test case 30: input=aaaaa[[[[[:[[[[a]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_31",
            input_value='[hellocodeforces::]\n',
            expected_output=4,
            description="Test case 31: input=[hellocodeforces::]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_32",
            input_value='[::]lolxd\n',
            expected_output=4,
            description="Test case 32: input=[::]lolxd\n, expected=4\n"
        ),
        TestCase(
            name="test_case_33",
            input_value='sasixyu:[[:||ld[:[dxoe\n',
            expected_output=-1,
            description="Test case 33: input=sasixyu:[[:||ld[:[dxoe\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_34",
            input_value='[:|||:\n',
            expected_output=-1,
            description="Test case 34: input=[:|||:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_35",
            input_value='topkek[::]\n',
            expected_output=4,
            description="Test case 35: input=topkek[::]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_36",
            input_value='[[||]]\n',
            expected_output=-1,
            description="Test case 36: input=[[||]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_37",
            input_value='[\n',
            expected_output=-1,
            description="Test case 37: input=[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_38",
            input_value='|[::||::]]a\n',
            expected_output=6,
            description="Test case 38: input=|[::||::]]a\n, expected=6\n"
        ),
        TestCase(
            name="test_case_39",
            input_value=':]\n',
            expected_output=-1,
            description="Test case 39: input=:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_40",
            input_value=']::]\n',
            expected_output=-1,
            description="Test case 40: input=]::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_41",
            input_value='r|x\n',
            expected_output=-1,
            description="Test case 41: input=r|x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_42",
            input_value='|\n',
            expected_output=-1,
            description="Test case 42: input=|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_43",
            input_value=':][:|||\n',
            expected_output=-1,
            description="Test case 43: input=:][:|||\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_44",
            input_value=']]::[[]]::\n',
            expected_output=-1,
            description="Test case 44: input=]]::[[]]::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_45",
            input_value=']f:|efw][jz[|[[z][[g]i|[\n',
            expected_output=-1,
            description="Test case 45: input=]f:|efw][jz[|[[z][[g]i|[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_46",
            input_value=']::[\n',
            expected_output=-1,
            description="Test case 46: input=]::[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_47",
            input_value='|:[[][:cv|\n',
            expected_output=-1,
            description="Test case 47: input=|:[[][:cv|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_48",
            input_value=':y]j]tz:e[p[\n',
            expected_output=-1,
            description="Test case 48: input=:y]j]tz:e[p[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_49",
            input_value='::::\n',
            expected_output=-1,
            description="Test case 49: input=::::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_50",
            input_value='||\n',
            expected_output=-1,
            description="Test case 50: input=||\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_51",
            input_value=']|[hhf[\n',
            expected_output=-1,
            description="Test case 51: input=]|[hhf[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_52",
            input_value='abide\n',
            expected_output=-1,
            description="Test case 52: input=abide\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_53",
            input_value='|c[]][zx]|[[[[j[::nx[|[:ou[u]\n',
            expected_output=5,
            description="Test case 53: input=|c[]][zx]|[[[[j[::nx[|[:ou[u]\n, expected=5\n"
        ),
        TestCase(
            name="test_case_54",
            input_value='|:]\n',
            expected_output=-1,
            description="Test case 54: input=|:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_55",
            input_value=']:|:][:||:]\n',
            expected_output=6,
            description="Test case 55: input=]:|:][:||:]\n, expected=6\n"
        ),
        TestCase(
            name="test_case_56",
            input_value=']:]\n',
            expected_output=-1,
            description="Test case 56: input=]:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_57",
            input_value='d[\n',
            expected_output=-1,
            description="Test case 57: input=d[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_58",
            input_value=':|:]\n',
            expected_output=-1,
            description="Test case 58: input=:|:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_59",
            input_value='k::]k|iv|]|g[|r[q:|[:[r[cj]||mjm|[|[|[|:[\n',
            expected_output=5,
            description="Test case 59: input=k::]k|iv|]|g[|r[q:|[:[r[cj]||mjm|[|[|[|:[\n, expected=5\n"
        ),
        TestCase(
            name="test_case_60",
            input_value=':|f[|e]e:|\n',
            expected_output=-1,
            description="Test case 60: input=:|f[|e]e:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_61",
            input_value='][:|:\n',
            expected_output=-1,
            description="Test case 61: input=][:|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_62",
            input_value='|rh]|[|:[v|||||i\n',
            expected_output=-1,
            description="Test case 62: input=|rh]|[|:[v|||||i\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_63",
            input_value='y:[|[]b[][ug|e[\n',
            expected_output=-1,
            description="Test case 63: input=y:[|[]b[][ug|e[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_64",
            input_value='[:::]\n',
            expected_output=4,
            description="Test case 64: input=[:::]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_65",
            input_value='[:]:[:]\n',
            expected_output=4,
            description="Test case 65: input=[:]:[:]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_66",
            input_value='::]]:::\n',
            expected_output=-1,
            description="Test case 66: input=::]]:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_67",
            input_value='[:||:|]\n',
            expected_output=6,
            description="Test case 67: input=[:||:|]\n, expected=6\n"
        ),
        TestCase(
            name="test_case_68",
            input_value='d]k[[::[||[:tpoc[||[:\n',
            expected_output=-1,
            description="Test case 68: input=d]k[[::[||[:tpoc[||[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_69",
            input_value=':]||haha||[:\n',
            expected_output=-1,
            description="Test case 69: input=:]||haha||[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_70",
            input_value=':]||ahaha||[:\n',
            expected_output=-1,
            description="Test case 70: input=:]||ahaha||[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_71",
            input_value='[][]\n',
            expected_output=-1,
            description="Test case 71: input=[][]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_72",
            input_value=':|]:::]]|:|||||]]]:|\n',
            expected_output=-1,
            description="Test case 72: input=:|]:::]]|:|||||]]]:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_73",
            input_value='||:][:||\n',
            expected_output=-1,
            description="Test case 73: input=||:][:||\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_74",
            input_value='|:][:\n',
            expected_output=-1,
            description="Test case 74: input=|:][:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_75",
            input_value=']\n',
            expected_output=-1,
            description="Test case 75: input=]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_76",
            input_value='[:::\n',
            expected_output=-1,
            description="Test case 76: input=[:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_77",
            input_value='ss:]]n:w:kzxiwpdoce|d:]][:nmw|b:hs\n',
            expected_output=-1,
            description="Test case 77: input=ss:]]n:w:kzxiwpdoce|d:]][:nmw|b:hs\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_78",
            input_value='::][::\n',
            expected_output=-1,
            description="Test case 78: input=::][::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_79",
            input_value='[:tk]v|hd:h:c[s\n',
            expected_output=-1,
            description="Test case 79: input=[:tk]v|hd:h:c[s\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_80",
            input_value='md:o:|r:[uuzcov]wy]|[:[imwc\n',
            expected_output=-1,
            description="Test case 80: input=md:o:|r:[uuzcov]wy]|[:[imwc\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_81",
            input_value=':::]w\n',
            expected_output=-1,
            description="Test case 81: input=:::]w\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_82",
            input_value='wd[]jcq[[]f|:\n',
            expected_output=-1,
            description="Test case 82: input=wd[]jcq[[]f|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_83",
            input_value=':aj::pxblo]]]:o|x|:|]y:wn]:[:v:m\n',
            expected_output=-1,
            description="Test case 83: input=:aj::pxblo]]]:o|x|:|]y:wn]:[:v:m\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_84",
            input_value='oeq]pp|i:[tan|][:ncsp::\n',
            expected_output=-1,
            description="Test case 84: input=oeq]pp|i:[tan|][:ncsp::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_85",
            input_value='m][js]x]a:l\n',
            expected_output=-1,
            description="Test case 85: input=m][js]x]a:l\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_86",
            input_value='[:]\n',
            expected_output=-1,
            description="Test case 86: input=[:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_87",
            input_value='[asfd:khj]\n',
            expected_output=-1,
            description="Test case 87: input=[asfd:khj]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_88",
            input_value=':i:]f|cau\n',
            expected_output=-1,
            description="Test case 88: input=:i:]f|cau\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_89",
            input_value='ljjjsv:h|]o:]k\n',
            expected_output=-1,
            description="Test case 89: input=ljjjsv:h|]o:]k\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_90",
            input_value='aaaa\n',
            expected_output=-1,
            description="Test case 90: input=aaaa\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_91",
            input_value='qj|]gd:i:::[|ur[e[e:]ay::k:\n',
            expected_output=-1,
            description="Test case 91: input=qj|]gd:i:::[|ur[e[e:]ay::k:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_92",
            input_value='qod:|nw]sfr:g|::[]ajs:\n',
            expected_output=-1,
            description="Test case 92: input=qod:|nw]sfr:g|::[]ajs:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_93",
            input_value=']zpgjpy:]:sz|[miz\n',
            expected_output=-1,
            description="Test case 93: input=]zpgjpy:]:sz|[miz\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_94",
            input_value=']ty:|:cjk::c:[[]tm\n',
            expected_output=-1,
            description="Test case 94: input=]ty:|:cjk::c:[[]tm\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_95",
            input_value='umfqrr::m]w]g::a|]|::]duhhxmzqs:gbo]br|xz|[g][ou:v[e[u|:y[||k:|[zqd:p:wf:a:gb\n',
            expected_output=-1,
            description="Test case 95: input=umfqrr::m]w]g::a|]|::]duhhxmzqs:gbo]br|xz|[g][ou:v, expected=-1\n"
        ),
        TestCase(
            name="test_case_96",
            input_value=':j:]xp:pnyh\n',
            expected_output=-1,
            description="Test case 96: input=:j:]xp:pnyh\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_97",
            input_value=':]|[:\n',
            expected_output=-1,
            description="Test case 97: input=:]|[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_98",
            input_value=']h:y[u:bg\n',
            expected_output=-1,
            description="Test case 98: input=]h:y[u:bg\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_99",
            input_value=':am:trjm|]e[[[vm[:|pv\n',
            expected_output=-1,
            description="Test case 99: input=:am:trjm|]e[[[vm[:|pv\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_100",
            input_value=':[||||||]:\n',
            expected_output=-1,
            description="Test case 100: input=:[||||||]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_101",
            input_value=':|[:qw[|:yr]c:p][]|n:qql[ulp:ph:|||adcg\n',
            expected_output=5,
            description="Test case 101: input=:|[:qw[|:yr]c:p][]|n:qql[ulp:ph:|||adcg\n, expected=5\n"
        ),
        TestCase(
            name="test_case_102",
            input_value=':a::[vd|vwq|r:][]:|::\n',
            expected_output=-1,
            description="Test case 102: input=:a::[vd|vwq|r:][]:|::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_103",
            input_value='|v]efoi::b|ov]:]|||:vk[q]is|[]|ku|]||wk[[|[q::]g|\n',
            expected_output=4,
            description="Test case 103: input=|v]efoi::b|ov]:]|||:vk[q]is|[]|ku|]||wk[[|[q::]g|\n, expected=4\n"
        ),
        TestCase(
            name="test_case_104",
            input_value='[w:||j:iiasd]gz||o:yw[::b::[[[m[oe[|oh]jh]:yjwa\n',
            expected_output=8,
            description="Test case 104: input=[w:||j:iiasd]gz||o:yw[::b::[[[m[oe[|oh]jh]:yjwa\n, expected=8\n"
        ),
        TestCase(
            name="test_case_105",
            input_value='||::k[is|m|]|::i\n',
            expected_output=-1,
            description="Test case 105: input=||::k[is|m|]|::i\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_106",
            input_value='t]g]ney::]hca]:|]|\n',
            expected_output=-1,
            description="Test case 106: input=t]g]ney::]hca]:|]|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_107",
            input_value=']g[:]|u[d]\n',
            expected_output=-1,
            description="Test case 107: input=]g[:]|u[d]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_108",
            input_value='[:[|][\n',
            expected_output=-1,
            description="Test case 108: input=[:[|][\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_109",
            input_value=':]g|||yoj[:[h]]yys]u:iz:|rn|[:oc:|:[a|gns:||:hkr[idkx|\n',
            expected_output=-1,
            description="Test case 109: input=:]g|||yoj[:[h]]yys]u:iz:|rn|[:oc:|:[a|gns:||:hkr[i, expected=-1\n"
        ),
        TestCase(
            name="test_case_110",
            input_value=':n:[mb|cb|\n',
            expected_output=-1,
            description="Test case 110: input=:n:[mb|cb|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_111",
            input_value='[e[]|s:ml:|q[gh[[:anpd[|::[\n',
            expected_output=-1,
            description="Test case 111: input=[e[]|s:ml:|q[gh[[:anpd[|::[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_112",
            input_value=':\n',
            expected_output=-1,
            description="Test case 112: input=:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_113",
            input_value='|f||]:ng[]j:]::gc\n',
            expected_output=-1,
            description="Test case 113: input=|f||]:ng[]j:]::gc\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_114",
            input_value='[x|[:l::hc[\n',
            expected_output=-1,
            description="Test case 114: input=[x|[:l::hc[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_115",
            input_value='em]]|:tu:cw::d:ralw|[]l:f::c\n',
            expected_output=-1,
            description="Test case 115: input=em]]|:tu:cw::d:ralw|[]l:f::c\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_116",
            input_value='|]\n',
            expected_output=-1,
            description="Test case 116: input=|]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_117",
            input_value='|kjw:j:]y\n',
            expected_output=-1,
            description="Test case 117: input=|kjw:j:]y\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_118",
            input_value='|[[fu:j\n',
            expected_output=-1,
            description="Test case 118: input=|[[fu:j\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_119",
            input_value=':b]l]byp]avhswotk:f[r]:k:::\n',
            expected_output=-1,
            description="Test case 119: input=:b]l]byp]avhswotk:f[r]:k:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_120",
            input_value=']c|z||]cya:|yny]]q|g]q::h:|ff]q|jx::]:|]c]:||::rfr]o|hbgtb\n',
            expected_output=-1,
            description="Test case 120: input=]c|z||]cya:|yny]]q|g]q::h:|ff]q|jx::]:|]c]:||::rfr, expected=-1\n"
        ),
        TestCase(
            name="test_case_121",
            input_value='|]j:k[su:b|\n',
            expected_output=-1,
            description="Test case 121: input=|]j:k[su:b|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_122",
            input_value=']]s:|f:ho::s]p:|]]]sd\n',
            expected_output=-1,
            description="Test case 122: input=]]s:|f:ho::s]p:|]]]sd\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_123",
            input_value='okje|:e:ti]yl|[r[x]|gt]zgzz[:[]:u:i]:ctml[]w[u:f]]:ltc[n:[k:[g:wdh\n',
            expected_output=4,
            description="Test case 123: input=okje|:e:ti]yl|[r[x]|gt]zgzz[:[]:u:i]:ctml[]w[u:f]], expected=4\n"
        ),
        TestCase(
            name="test_case_124",
            input_value='a|xg]:mv]:[:::p\n',
            expected_output=-1,
            description="Test case 124: input=a|xg]:mv]:[:::p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_125",
            input_value='y|:]:j[|\n',
            expected_output=-1,
            description="Test case 125: input=y|:]:j[|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_126",
            input_value=':rr]a[m]g:[m[e::[f:my:[[::h:]:]q:h[tf[o]nj[j[c:\n',
            expected_output=4,
            description="Test case 126: input=:rr]a[m]g:[m[e::[f:my:[[::h:]:]q:h[tf[o]nj[j[c:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_127",
            input_value='][:[:[\n',
            expected_output=-1,
            description="Test case 127: input=][:[:[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_128",
            input_value='aaa:|||:]\n',
            expected_output=-1,
            description="Test case 128: input=aaa:|||:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_129",
            input_value='cyzha::al:zc:o]s\n',
            expected_output=-1,
            description="Test case 129: input=cyzha::al:zc:o]s\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_130",
            input_value='::h]go]\n',
            expected_output=-1,
            description="Test case 130: input=::h]go]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_131",
            input_value='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa[\n',
            expected_output=-1,
            description="Test case 131: input=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, expected=-1\n"
        ),
        TestCase(
            name="test_case_132",
            input_value='sa:|cas|[::oq[sn]m:::h]e]dbjh:lllafnt|xly[j]:r::euta|fs[hw[h[[[i\n',
            expected_output=4,
            description="Test case 132: input=sa:|cas|[::oq[sn]m:::h]e]dbjh:lllafnt|xly[j]:r::eu, expected=4\n"
        ),
        TestCase(
            name="test_case_133",
            input_value='|:[]\n',
            expected_output=-1,
            description="Test case 133: input=|:[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_134",
            input_value='][reerf][ybn[g]|i:q:]:[|:]b:xt[\n',
            expected_output=5,
            description="Test case 134: input=][reerf][ybn[g]|i:q:]:[|:]b:xt[\n, expected=5\n"
        ),
        TestCase(
            name="test_case_135",
            input_value='k[h]|a|t|m]mwba[\n',
            expected_output=-1,
            description="Test case 135: input=k[h]|a|t|m]mwba[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_136",
            input_value='[||::]\n',
            expected_output=4,
            description="Test case 136: input=[||::]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_137",
            input_value='b\n',
            expected_output=-1,
            description="Test case 137: input=b\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_138",
            input_value=':|xm:f:b[[|:w]t[[[ht\n',
            expected_output=-1,
            description="Test case 138: input=:|xm:f:b[[|:w]t[[[ht\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_139",
            input_value='qyx::ti]o]|\n',
            expected_output=-1,
            description="Test case 139: input=qyx::ti]o]|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_140",
            input_value='vl::r]i|y:]pi:yicacsqm|:sy|pd:nwu::r|iib]goq\n',
            expected_output=-1,
            description="Test case 140: input=vl::r]i|y:]pi:yicacsqm|:sy|pd:nwu::r|iib]goq\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_141",
            input_value='af:r:gett|]t:x:f|iqdo]bm]:[w::x|]:pe:[[\n',
            expected_output=4,
            description="Test case 141: input=af:r:gett|]t:x:f|iqdo]bm]:[w::x|]:pe:[[\n, expected=4\n"
        ),
        TestCase(
            name="test_case_142",
            input_value='v[t:[q:tmrwta\n',
            expected_output=-1,
            description="Test case 142: input=v[t:[q:tmrwta\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_143",
            input_value=']:v[|\n',
            expected_output=-1,
            description="Test case 143: input=]:v[|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_144",
            input_value='cl|dyisv::|hn|:fgdm][z[e\n',
            expected_output=-1,
            description="Test case 144: input=cl|dyisv::|hn|:fgdm][z[e\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_145",
            input_value='w]]::|zc\n',
            expected_output=-1,
            description="Test case 145: input=w]]::|zc\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_146",
            input_value='|trrxb|]|z:t]s|]v|ds]u:|c:z|f|m[]bowp\n',
            expected_output=-1,
            description="Test case 146: input=|trrxb|]|z:t]s|]v|ds]u:|c:z|f|m[]bowp\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_147",
            input_value=':z]gr[|uvm|ngodriz]f[c]|lfxqg|p]bcoxrfv:k:r::[m|\n',
            expected_output=-1,
            description="Test case 147: input=:z]gr[|uvm|ngodriz]f[c]|lfxqg|p]bcoxrfv:k:r::[m|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_148",
            input_value=':]o[|]]|t::::]w]:[:|:ro|a::ged[slr:kug:::rww:ei:|m::ah|cwk[v\n',
            expected_output=4,
            description="Test case 148: input=:]o[|]]|t::::]w]:[:|:ro|a::ged[slr:kug:::rww:ei:|m, expected=4\n"
        ),
        TestCase(
            name="test_case_149",
            input_value='yx:tx::dqpl|:::]l|]j[y[t|d[:elr:m\n',
            expected_output=-1,
            description="Test case 149: input=yx:tx::dqpl|:::]l|]j[y[t|d[:elr:m\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_150",
            input_value='d]sp]|d]::|\n',
            expected_output=-1,
            description="Test case 150: input=d]sp]|d]::|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_151",
            input_value='q|dlfohjzs]:[jnuxy|[]||::]u[[j:\n',
            expected_output=4,
            description="Test case 151: input=q|dlfohjzs]:[jnuxy|[]||::]u[[j:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_152",
            input_value=']s]:[co|]m:y:njby\n',
            expected_output=-1,
            description="Test case 152: input=]s]:[co|]m:y:njby\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_153",
            input_value='fmnu|n:ynz:|::hk::|::]|]l::|\n',
            expected_output=-1,
            description="Test case 153: input=fmnu|n:ynz:|::hk::|::]|]l::|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_154",
            input_value='aaaaaaaaaaaaaa[\n',
            expected_output=-1,
            description="Test case 154: input=aaaaaaaaaaaaaa[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_155",
            input_value='f|gzg::cl]\n',
            expected_output=-1,
            description="Test case 155: input=f|gzg::cl]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_156",
            input_value=']x\n',
            expected_output=-1,
            description="Test case 156: input=]x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_157",
            input_value='tc|:]ekb:tu\n',
            expected_output=-1,
            description="Test case 157: input=tc|:]ekb:tu\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_158",
            input_value=']ujn|]|]j|o|:q:|r:a:u:::sv:]ffrzo\n',
            expected_output=-1,
            description="Test case 158: input=]ujn|]|]j|o|:q:|r:a:u:::sv:]ffrzo\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_159",
            input_value='tuyut]j:[u]|ft||:]houmvj[yh:[::f\n',
            expected_output=-1,
            description="Test case 159: input=tuyut]j:[u]|ft||:]houmvj[yh:[::f\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_160",
            input_value='n:]:][|gpxex|qw[\n',
            expected_output=-1,
            description="Test case 160: input=n:]:][|gpxex|qw[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_161",
            input_value=']gy]]fd|bd::ph::j[]]jc|eqn]|lj]:s|ew:c||:[gksv\n',
            expected_output=-1,
            description="Test case 161: input=]gy]]fd|bd::ph::j[]]jc|eqn]|lj]:s|ew:c||:[gksv\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_162",
            input_value='::p:oqv:|:\n',
            expected_output=-1,
            description="Test case 162: input=::p:oqv:|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_163",
            input_value='os::a]un:k||ri:n:d]:who|]urx:yat::]|lm:m]q]iua|:s[g::]|:\n',
            expected_output=4,
            description="Test case 163: input=os::a]un:k||ri:n:d]:who|]urx:yat::]|lm:m]q]iua|:s[, expected=4\n"
        ),
        TestCase(
            name="test_case_164",
            input_value='uy|dzq]dkobuo:c|]]c]j:|]wtssv:|:lkn][sb[dw::|m|z:\n',
            expected_output=-1,
            description="Test case 164: input=uy|dzq]dkobuo:c|]]c]j:|]wtssv:|:lkn][sb[dw::|m|z:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_165",
            input_value='euj|eip:[bgqn[bjmivsxd][j][[[]dsk:y\n',
            expected_output=-1,
            description="Test case 165: input=euj|eip:[bgqn[bjmivsxd][j][[[]dsk:y\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_166",
            input_value=']:||k:]sf::[::|yn]:xv]pg[|q[]:[wpv:|y\n',
            expected_output=5,
            description="Test case 166: input=]:||k:]sf::[::|yn]:xv]pg[|q[]:[wpv:|y\n, expected=5\n"
        ),
        TestCase(
            name="test_case_167",
            input_value='clpy::||:fs||[w]]::||\n',
            expected_output=-1,
            description="Test case 167: input=clpy::||:fs||[w]]::||\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_168",
            input_value='u:ft:]|c]:q\n',
            expected_output=-1,
            description="Test case 168: input=u:ft:]|c]:q\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_169",
            input_value='rr::m[]|:j:uq[:t|[:trxbtq:|hj[rf\n',
            expected_output=-1,
            description="Test case 169: input=rr::m[]|:j:uq[:t|[:trxbtq:|hj[rf\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_170",
            input_value='[h[|k|[hb|\n',
            expected_output=-1,
            description="Test case 170: input=[h[|k|[hb|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_171",
            input_value=':|e|o:]g:[:w\n',
            expected_output=-1,
            description="Test case 171: input=:|e|o:]g:[:w\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_172",
            input_value='::]:asl:\n',
            expected_output=-1,
            description="Test case 172: input=::]:asl:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_173",
            input_value='z:::e|r]j|n]|:f]]\n',
            expected_output=-1,
            description="Test case 173: input=z:::e|r]j|n]|:f]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_174",
            input_value=':ml|r:qm|:n]b::|:]]trak:ku]:::k]\n',
            expected_output=-1,
            description="Test case 174: input=:ml|r:qm|:n]b::|:]]trak:ku]:::k]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_175",
            input_value=']zp\n',
            expected_output=-1,
            description="Test case 175: input=]zp\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_176",
            input_value='|wu[ehma]]ced]d[f[m][]b]:|:|::|fbz\n',
            expected_output=-1,
            description="Test case 176: input=|wu[ehma]]ced]d[f[m][]b]:|:|::|fbz\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_177",
            input_value='uyme:|oew||mvo[[|e]\n',
            expected_output=-1,
            description="Test case 177: input=uyme:|oew||mvo[[|e]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_178",
            input_value='|zh]|]dmg|]:rtj:r|]:\n',
            expected_output=-1,
            description="Test case 178: input=|zh]|]dmg|]:rtj:r|]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_179",
            input_value='kj:t[|[|oph]qt:h[rq[[bu[|]m|:||[hvh[\n',
            expected_output=-1,
            description="Test case 179: input=kj:t[|[|oph]qt:h[rq[[bu[|]m|:||[hvh[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_180",
            input_value=':[p|vg:[|:nu[:olj::p[o[qr[ltui\n',
            expected_output=-1,
            description="Test case 180: input=:[p|vg:[|:nu[:olj::p[o[qr[ltui\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_181",
            input_value=']|pv:|[|d]][:|ddhn::n|:\n',
            expected_output=-1,
            description="Test case 181: input=]|pv:|[|d]][:|ddhn::n|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_182",
            input_value='fud:e:zmci:uh]\n',
            expected_output=-1,
            description="Test case 182: input=fud:e:zmci:uh]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_183",
            input_value='d:x|]:::\n',
            expected_output=-1,
            description="Test case 183: input=d:x|]:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_184",
            input_value='lovs:iq:[][[k\n',
            expected_output=-1,
            description="Test case 184: input=lovs:iq:[][[k\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_185",
            input_value='xf::osgw:kmft:gvy:::]m\n',
            expected_output=-1,
            description="Test case 185: input=xf::osgw:kmft:gvy:::]m\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_186",
            input_value='|hb:qtxa:nx::wnhg]p\n',
            expected_output=-1,
            description="Test case 186: input=|hb:qtxa:nx::wnhg]p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_187",
            input_value=']:]:fcl|]a::::[z|q[|jw\n',
            expected_output=-1,
            description="Test case 187: input=]:]:fcl|]a::::[z|q[|jw\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_188",
            input_value='np|:]q:xlct[|]hw:tfd|ci:d\n',
            expected_output=-1,
            description="Test case 188: input=np|:]q:xlct[|]hw:tfd|ci:d\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_189",
            input_value='nl]nz:][tpm:ps[jfx|:tfzekk\n',
            expected_output=-1,
            description="Test case 189: input=nl]nz:][tpm:ps[jfx|:tfzekk\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_190",
            input_value='e:n|al]:i|hss:c:|v|b[u]efg[]k][u||vv:ma:ytgw:fjv|ve\n',
            expected_output=-1,
            description="Test case 190: input=e:n|al]:i|hss:c:|v|b[u]efg[]k][u||vv:ma:ytgw:fjv|v, expected=-1\n"
        ),
        TestCase(
            name="test_case_191",
            input_value='pw:m|qu:|[gb[:]liv:an:oj:cavwjk[dxr:|po:ny|hu:mawqxv::[::\n',
            expected_output=-1,
            description="Test case 191: input=pw:m|qu:|[gb[:]liv:an:oj:cavwjk[dxr:|po:ny|hu:mawq, expected=-1\n"
        ),
        TestCase(
            name="test_case_192",
            input_value='|]:i:|[:[q|x|lmetc[|:[|c:\n',
            expected_output=-1,
            description="Test case 192: input=|]:i:|[:[q|x|lmetc[|:[|c:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_193",
            input_value=':z::vy[lcyjoq\n',
            expected_output=-1,
            description="Test case 193: input=:z::vy[lcyjoq\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_194",
            input_value='::]v]\n',
            expected_output=-1,
            description="Test case 194: input=::]v]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_195",
            input_value=':wr|ze]d:wt:]]|q:c[::sk:\n',
            expected_output=-1,
            description="Test case 195: input=:wr|ze]d:wt:]]|q:c[::sk:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_196",
            input_value=']::|]:[|dob|]ke:ghk[::uxycp|:fh:pxewxaet[\n',
            expected_output=-1,
            description="Test case 196: input=]::|]:[|dob|]ke:ghk[::uxycp|:fh:pxewxaet[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_197",
            input_value='jf:]e:i:q]|w:nrk:hvpj|m]:\n',
            expected_output=-1,
            description="Test case 197: input=jf:]e:i:q]|w:nrk:hvpj|m]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_198",
            input_value='vhbato:s|:]vhm:o|n[hfj]pgp|bs]d|:cxv\n',
            expected_output=-1,
            description="Test case 198: input=vhbato:s|:]vhm:o|n[hfj]pgp|bs]d|:cxv\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_199",
            input_value='::b|zltkdkulzx[]ocfqcmu::r[::s\n',
            expected_output=-1,
            description="Test case 199: input=::b|zltkdkulzx[]ocfqcmu::r[::s\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_200",
            input_value=']fq|m::|[zk][:|::hxy[u::zw|::n|a\n',
            expected_output=-1,
            description="Test case 200: input=]fq|m::|[zk][:|::hxy[u::zw|::n|a\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_201",
            input_value='b:|xjehu]ywpi:|][ye]:[:[:\n',
            expected_output=-1,
            description="Test case 201: input=b:|xjehu]ywpi:|][ye]:[:[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_202",
            input_value='q:wdd::i:]\n',
            expected_output=-1,
            description="Test case 202: input=q:wdd::i:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_203",
            input_value='v::mp:l::[x]:w[[ehu\n',
            expected_output=-1,
            description="Test case 203: input=v::mp:l::[x]:w[[ehu\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_204",
            input_value='g]:kobbxo:[dy]:daz[[|eqe::|\n',
            expected_output=-1,
            description="Test case 204: input=g]:kobbxo:[dy]:daz[[|eqe::|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_205",
            input_value='vz:naw[:d[][f[[wgzdki]|ct[::[yh|w|bgxd[x:q[[zm][i:r[r|[:a[][|yx][r|:\n',
            expected_output=8,
            description="Test case 205: input=vz:naw[:d[][f[[wgzdki]|ct[::[yh|w|bgxd[x:q[[zm][i:, expected=8\n"
        ),
        TestCase(
            name="test_case_206",
            input_value='s::dul::i[mwln:it::[|g:eh:xs|ew[bp|g]ak|ems:|:gydoq:[dg:]]:qr|[:[p[:q:[i[:]:k\n',
            expected_output=10,
            description="Test case 206: input=s::dul::i[mwln:it::[|g:eh:xs|ew[bp|g]ak|ems:|:gydo, expected=10\n"
        ),
        TestCase(
            name="test_case_207",
            input_value=':][]||[|:|\n',
            expected_output=-1,
            description="Test case 207: input=:][]||[|:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_208",
            input_value=':n[]ncg\n',
            expected_output=-1,
            description="Test case 208: input=:n[]ncg\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_209",
            input_value='j:m::|:||]u:[v|z]]:\n',
            expected_output=-1,
            description="Test case 209: input=j:m::|:||]u:[v|z]]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_210",
            input_value=']:svzta[|ey|s|oi[[gmy::ayi]\n',
            expected_output=4,
            description="Test case 210: input=]:svzta[|ey|s|oi[[gmy::ayi]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_211",
            input_value=':[|]did:]p:[|::|olz[:albp[[k:|||\n',
            expected_output=-1,
            description="Test case 211: input=:[|]did:]p:[|::|olz[:albp[[k:|||\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_212",
            input_value='|::|]:|]|:\n',
            expected_output=-1,
            description="Test case 212: input=|::|]:|]|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_213",
            input_value=':|q|x]zt:]:kw:cs|fn]]jadp|cq\n',
            expected_output=-1,
            description="Test case 213: input=:|q|x]zt:]:kw:cs|fn]]jadp|cq\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_214",
            input_value='ka:|u:|omvu:scrjwzt|]e|[[|k:h:we]::ou:]bxq|][dv:\n',
            expected_output=4,
            description="Test case 214: input=ka:|u:|omvu:scrjwzt|]e|[[|k:h:we]::ou:]bxq|][dv:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_215",
            input_value='mas:]c]a::a:[g:tiejt[rvh:zz::qwufm[\n',
            expected_output=-1,
            description="Test case 215: input=mas:]c]a::a:[g:tiejt[rvh:zz::qwufm[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_216",
            input_value=':k:::g|y]b|c]qwva|::v\n',
            expected_output=-1,
            description="Test case 216: input=:k:::g|y]b|c]qwva|::v\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_217",
            input_value='sn::zeno:[ft]l|y|m|[||bz\n',
            expected_output=-1,
            description="Test case 217: input=sn::zeno:[ft]l|y|m|[||bz\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_218",
            input_value='t:nwkx:wg:x|:vr]|uk[[|]x|:gz:\n',
            expected_output=-1,
            description="Test case 218: input=t:nwkx:wg:x|:vr]|uk[[|]x|:gz:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_219",
            input_value='ym:dvmmajd:t]|[hqx]d:l[\n',
            expected_output=-1,
            description="Test case 219: input=ym:dvmmajd:t]|[hqx]d:l[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_220",
            input_value='::[da][ik]]v:i\n',
            expected_output=-1,
            description="Test case 220: input=::[da][ik]]v:i\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_221",
            input_value=':|yyu]:[lj|aa[]vfenav[:ji|\n',
            expected_output=-1,
            description="Test case 221: input=:|yyu]:[lj|aa[]vfenav[:ji|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_222",
            input_value='gt:|]|k]:|[hikmw|hz|a[\n',
            expected_output=-1,
            description="Test case 222: input=gt:|]|k]:|[hikmw|hz|a[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_223",
            input_value='z:::]oqatxzhf:gdpr]:]:ls]art[zq\n',
            expected_output=-1,
            description="Test case 223: input=z:::]oqatxzhf:gdpr]:]:ls]art[zq\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_224",
            input_value=':o:]]u:evfw::]:c::gdu[lus:ej:[|:ruam:\n',
            expected_output=-1,
            description="Test case 224: input=:o:]]u:evfw::]:c::gdu[lus:ej:[|:ruam:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_225",
            input_value=':]::k]d|:hx[]pop][:::u[s:o[\n',
            expected_output=-1,
            description="Test case 225: input=:]::k]d|:hx[]pop][:::u[s:o[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_226",
            input_value='::sry]\n',
            expected_output=-1,
            description="Test case 226: input=::sry]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_227",
            input_value='y:]:[[i]iy:\n',
            expected_output=-1,
            description="Test case 227: input=y:]:[[i]iy:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_228",
            input_value='||j:]::x|:f:l\n',
            expected_output=-1,
            description="Test case 228: input=||j:]::x|:f:l\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_229",
            input_value=':]]:d\n',
            expected_output=-1,
            description="Test case 229: input=:]]:d\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_230",
            input_value='l]b:][::]]z|ysyifc[:s|ag[hngo|:x:rhqn|ru\n',
            expected_output=4,
            description="Test case 230: input=l]b:][::]]z|ysyifc[:s|ag[hngo|:x:rhqn|ru\n, expected=4\n"
        ),
        TestCase(
            name="test_case_231",
            input_value='::q:ghi]:y:gtl:o:|:\n',
            expected_output=-1,
            description="Test case 231: input=::q:ghi]:y:gtl:o:|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_232",
            input_value='|j::lq:ot[]]c[|]|y[bxxqgl[]]]l[g:[|dg::hl:c\n',
            expected_output=-1,
            description="Test case 232: input=|j::lq:ot[]]c[|]|y[bxxqgl[]]]l[g:[|dg::hl:c\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_233",
            input_value='yk:t:ez|b:i:ze:[mt[[[]ochz:\n',
            expected_output=-1,
            description="Test case 233: input=yk:t:ez|b:i:ze:[mt[[[]ochz:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_234",
            input_value='[iy]u|bdr\n',
            expected_output=-1,
            description="Test case 234: input=[iy]u|bdr\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_235",
            input_value=':|stnr|t:x:oa]|ov[v]::jv[]to:[\n',
            expected_output=4,
            description="Test case 235: input=:|stnr|t:x:oa]|ov[v]::jv[]to:[\n, expected=4\n"
        ),
        TestCase(
            name="test_case_236",
            input_value='[a|u\n',
            expected_output=-1,
            description="Test case 236: input=[a|u\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_237",
            input_value='::|]]\n',
            expected_output=-1,
            description="Test case 237: input=::|]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_238",
            input_value='sv:sxjxf]|::]bij:]:okugd:]qlg::s:c[|:dk\n',
            expected_output=-1,
            description="Test case 238: input=sv:sxjxf]|::]bij:]:okugd:]qlg::s:c[|:dk\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_239",
            input_value='pfk[w:ow[|zz:|e::|ovvy:|y:vndh:::i:d]|[[qyn:::[||::]i:|:|]abb:ut]dxva:]ppkymtk|wyg:divb:[[l:c[jy|\n',
            expected_output=13,
            description="Test case 239: input=pfk[w:ow[|zz:|e::|ovvy:|y:vndh:::i:d]|[[qyn:::[||:, expected=13\n"
        ),
        TestCase(
            name="test_case_240",
            input_value=':rv::::lybr:|e:e:|iqtzgd::xhw]l]]:[aqa]d]:my[]]uo:d::s[a[:[[\n',
            expected_output=-1,
            description="Test case 240: input=:rv::::lybr:|e:e:|iqtzgd::xhw]l]]:[aqa]d]:my[]]uo:, expected=-1\n"
        ),
        TestCase(
            name="test_case_241",
            input_value=']|rhs:p]:z::t[|vfr]]iu[ktw]j||a[d::ttz|ez[[:::k\n',
            expected_output=-1,
            description="Test case 241: input=]|rhs:p]:z::t[|vfr]]iu[ktw]j||a[d::ttz|ez[[:::k\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_242",
            input_value='rw|oe]gq]mv:]]:]:cb:s:z|:]]:g:eri\n',
            expected_output=-1,
            description="Test case 242: input=rw|oe]gq]mv:]]:]:cb:s:z|:]]:g:eri\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_243",
            input_value=':|][|]jknnx]f[w|n|\n',
            expected_output=-1,
            description="Test case 243: input=:|][|]jknnx]f[w|n|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_244",
            input_value='::]t:np]:n]|jkn]:jy:|:c:]]]t||k|sm::c\n',
            expected_output=-1,
            description="Test case 244: input=::]t:np]:n]|jkn]:jy:|:c:]]]t||k|sm::c\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_245",
            input_value=':|[u]]ncc::[e:|][]l[][]p:un[w:cr:fa]dnud[tx:gz||so|||]j[wpr]b:ik:ulm[nab::u:yoo\n',
            expected_output=5,
            description="Test case 245: input=:|[u]]ncc::[e:|][]l[][]p:un[w:cr:fa]dnud[tx:gz||so, expected=5\n"
        ),
        TestCase(
            name="test_case_246",
            input_value='vu:]|ar|q|mwyl|]tr:qm:k:[|::jc]zzf\n',
            expected_output=4,
            description="Test case 246: input=vu:]|ar|q|mwyl|]tr:qm:k:[|::jc]zzf\n, expected=4\n"
        ),
        TestCase(
            name="test_case_247",
            input_value='lvyn]zm:q:vcg[:]n]jzhmdi\n',
            expected_output=-1,
            description="Test case 247: input=lvyn]zm:q:vcg[:]n]jzhmdi\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_248",
            input_value=']:l:|]mm\n',
            expected_output=-1,
            description="Test case 248: input=]:l:|]mm\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_249",
            input_value='z:qqh|]k\n',
            expected_output=-1,
            description="Test case 249: input=z:qqh|]k\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_250",
            input_value=']wsjx:p:hwk:ckjnb]js:w::|:|r:e]r|j]x\n',
            expected_output=-1,
            description="Test case 250: input=]wsjx:p:hwk:ckjnb]js:w::|:|r:e]r|j]x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_251",
            input_value=':]k:vkb:]]]|]ciljah:bc\n',
            expected_output=-1,
            description="Test case 251: input=:]k:vkb:]]]|]ciljah:bc\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_252",
            input_value='[qf:d]nvex|i|n|z[z]]gsw:pnnc:lw:bofpt\n',
            expected_output=-1,
            description="Test case 252: input=[qf:d]nvex|i|n|z[z]]gsw:pnnc:lw:bofpt\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_253",
            input_value=':]y:qc||tg|::y[::[[l]xceg:|j[edpf[j|:bmy:\n',
            expected_output=4,
            description="Test case 253: input=:]y:qc||tg|::y[::[[l]xceg:|j[edpf[j|:bmy:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_254",
            input_value='rszfx:pf|h]:e:wi[\n',
            expected_output=-1,
            description="Test case 254: input=rszfx:pf|h]:e:wi[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_255",
            input_value='r:::xez:y]nrt:\n',
            expected_output=-1,
            description="Test case 255: input=r:::xez:y]nrt:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_256",
            input_value='d::fftr::u:kug][ea:tu:ari][\n',
            expected_output=4,
            description="Test case 256: input=d::fftr::u:kug][ea:tu:ari][\n, expected=4\n"
        ),
        TestCase(
            name="test_case_257",
            input_value='|bvff||:m]:|i|::p|[\n',
            expected_output=-1,
            description="Test case 257: input=|bvff||:m]:|i|::p|[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_258",
            input_value='a:]a[:\n',
            expected_output=-1,
            description="Test case 258: input=a:]a[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_259",
            input_value=']|]|]:::[]\n',
            expected_output=-1,
            description="Test case 259: input=]|]|]:::[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_260",
            input_value=':::[||]|[]\n',
            expected_output=-1,
            description="Test case 260: input=:::[||]|[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_261",
            input_value=':|:][::|\n',
            expected_output=-1,
            description="Test case 261: input=:|:][::|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_262",
            input_value='[||::||]\n',
            expected_output=4,
            description="Test case 262: input=[||::||]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_263",
            input_value=']||:::]]\n',
            expected_output=-1,
            description="Test case 263: input=]||:::]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_264",
            input_value='::i|hack|myself::[]\n',
            expected_output=-1,
            description="Test case 264: input=::i|hack|myself::[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_265",
            input_value='m|:::|:z:n:]cepp\n',
            expected_output=-1,
            description="Test case 265: input=m|:::|:z:n:]cepp\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_266",
            input_value='::n::itzc:]:abfjlmlhubk[|::[hm:x[fg|b|:axss:r[c\n',
            expected_output=-1,
            description="Test case 266: input=::n::itzc:]:abfjlmlhubk[|::[hm:x[fg|b|:axss:r[c\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_267",
            input_value='c:m:xbw]m|[hm:oofub\n',
            expected_output=-1,
            description="Test case 267: input=c:m:xbw]m|[hm:oofub\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_268",
            input_value=']wvihpdy::vn:]]:|hqiaigj[\n',
            expected_output=-1,
            description="Test case 268: input=]wvihpdy::vn:]]:|hqiaigj[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_269",
            input_value='omi]cb:s]kxzrjhi]:o\n',
            expected_output=-1,
            description="Test case 269: input=omi]cb:s]kxzrjhi]:o\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_270",
            input_value='o|utkq|:j:]w:\n',
            expected_output=-1,
            description="Test case 270: input=o|utkq|:j:]w:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_271",
            input_value='abc\n',
            expected_output=-1,
            description="Test case 271: input=abc\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_272",
            input_value='xil]x]:hhtlz|:k:t:[pdv|ne]jyy|:sbd::jt:::|jgau:|\n',
            expected_output=-1,
            description="Test case 272: input=xil]x]:hhtlz|:k:t:[pdv|ne]jyy|:sbd::jt:::|jgau:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_273",
            input_value=':]:|:]|]:]\n',
            expected_output=-1,
            description="Test case 273: input=:]:|:]|]:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_274",
            input_value=':]]|[fxy\n',
            expected_output=-1,
            description="Test case 274: input=:]]|[fxy\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_275",
            input_value='q:t:|\n',
            expected_output=-1,
            description="Test case 275: input=q:t:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_276",
            input_value=':cu:lrcc[a|mij][o]]:x:ej\n',
            expected_output=-1,
            description="Test case 276: input=:cu:lrcc[a|mij][o]]:x:ej\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_277",
            input_value='sn:c:d]]|s]::e\n',
            expected_output=-1,
            description="Test case 277: input=sn:c:d]]|s]::e\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_278",
            input_value='[gp[]\n',
            expected_output=-1,
            description="Test case 278: input=[gp[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_279",
            input_value='||]tzs:|:]ta|jhvpdk\n',
            expected_output=-1,
            description="Test case 279: input=||]tzs:|:]ta|jhvpdk\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_280",
            input_value=':os|:hj:\n',
            expected_output=-1,
            description="Test case 280: input=:os|:hj:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_281",
            input_value='[|h::]]]qqw:dpp::jrq:v:[:z:[b:\n',
            expected_output=4,
            description="Test case 281: input=[|h::]]]qqw:dpp::jrq:v:[:z:[b:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_282",
            input_value=':c]:k:ugqzk:z::[]\n',
            expected_output=-1,
            description="Test case 282: input=:c]:k:ugqzk:z::[]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_283",
            input_value='gn]wmt]lck]::|yk]lbwbxw]:az:|:ln::|b\n',
            expected_output=-1,
            description="Test case 283: input=gn]wmt]lck]::|yk]lbwbxw]:az:|:ln::|b\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_284",
            input_value=':lmn:gs|muauf[[p]:xjoo:|x:lsdps:go[d|l|\n',
            expected_output=-1,
            description="Test case 284: input=:lmn:gs|muauf[[p]:xjoo:|x:lsdps:go[d|l|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_285",
            input_value='sw|]:|::x]ff\n',
            expected_output=-1,
            description="Test case 285: input=sw|]:|::x]ff\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_286",
            input_value='t:b:[d:vzei[||e|uo]]\n',
            expected_output=-1,
            description="Test case 286: input=t:b:[d:vzei[||e|uo]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_287",
            input_value=':l:::ha]]:g||t:]:ky||dbl]:]:q:m||g:]ta\n',
            expected_output=-1,
            description="Test case 287: input=:l:::ha]]:g||t:]:ky||dbl]:]:q:m||g:]ta\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_288",
            input_value='::::[|:|::\n',
            expected_output=-1,
            description="Test case 288: input=::::[|:|::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_289",
            input_value=']]|[k:f]||t]wg:b]]:[o[|e]hroomwxdph]|u]::[j[h:b|[mr:dn[|n[[yxoh:tf:[a[||[:::|dz\n',
            expected_output=6,
            description="Test case 289: input=]]|[k:f]||t]wg:b]]:[o[|e]hroomwxdph]|u]::[j[h:b|[m, expected=6\n"
        ),
        TestCase(
            name="test_case_290",
            input_value='[p||yi::u:::r|m:[\n',
            expected_output=-1,
            description="Test case 290: input=[p||yi::u:::r|m:[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_291",
            input_value=':kew:u]blgozxp:::]a]tp|g\n',
            expected_output=-1,
            description="Test case 291: input=:kew:u]blgozxp:::]a]tp|g\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_292",
            input_value='wsn]:ig::||:fc]v|t:yn:uaurphuj|]r|uut]:::]n]:e:pg]]]wb:]]:o||:d:p[::|:]g:k:wxcg|c[:k|w|||]mcy\n',
            expected_output=6,
            description="Test case 292: input=wsn]:ig::||:fc]v|t:yn:uaurphuj|]r|uut]:::]n]:e:pg], expected=6\n"
        ),
        TestCase(
            name="test_case_293",
            input_value=']up::]dcte]|ldnz|t:|]|iao:r:|v]\n',
            expected_output=-1,
            description="Test case 293: input=]up::]dcte]|ldnz|t:|]|iao:r:|v]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_294",
            input_value=':[nt]|::q:ant|xijg\n',
            expected_output=-1,
            description="Test case 294: input=:[nt]|::q:ant|xijg\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_295",
            input_value='r]:kxu[][qe[:y:x\n',
            expected_output=-1,
            description="Test case 295: input=r]:kxu[][qe[:y:x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_296",
            input_value=':z]|[[w]:\n',
            expected_output=-1,
            description="Test case 296: input=:z]|[[w]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_297",
            input_value='og|:]vxfpmq]]ax]zvx:::hm:htnicv|:hs:]ptpc[j|t]d\n',
            expected_output=-1,
            description="Test case 297: input=og|:]vxfpmq]]ax]zvx:::hm:htnicv|:hs:]ptpc[j|t]d\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_298",
            input_value=']g]sl:pqsqy:b::]rj:jl]]|n:y]:\n',
            expected_output=-1,
            description="Test case 298: input=]g]sl:pqsqy:b::]rj:jl]]|n:y]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_299",
            input_value='ejwmbu:fqkp]eb:]\n',
            expected_output=-1,
            description="Test case 299: input=ejwmbu:fqkp]eb:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_300",
            input_value='xq]|mnn:\n',
            expected_output=-1,
            description="Test case 300: input=xq]|mnn:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_301",
            input_value='gsl:]o:|f[e][wxmg[nlbn[\n',
            expected_output=-1,
            description="Test case 301: input=gsl:]o:|f[e][wxmg[nlbn[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_302",
            input_value='dt:]y:jta:zu]dwxq|ki\n',
            expected_output=-1,
            description="Test case 302: input=dt:]y:jta:zu]dwxq|ki\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_303",
            input_value='zr:s]ocaf:|ruqd:::|lbek[:y[gb::k|y:\n',
            expected_output=-1,
            description="Test case 303: input=zr:s]ocaf:|ruqd:::|lbek[:y[gb::k|y:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_304",
            input_value='n:]m]e|]:wr:iny:s]or]o:o]|:]]w|g]pp|ff\n',
            expected_output=-1,
            description="Test case 304: input=n:]m]e|]:wr:iny:s]or]o:o]|:]]w|g]pp|ff\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_305",
            input_value='::y:qjf:am]]]n]xrghkm|::|\n',
            expected_output=-1,
            description="Test case 305: input=::y:qjf:am]]]n]xrghkm|::|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_306",
            input_value=':||l]::||:son|::]pq|]]w|:y|]n:\n',
            expected_output=-1,
            description="Test case 306: input=:||l]::||:son|::]pq|]]w|:y|]n:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_307",
            input_value=':]j]pons\n',
            expected_output=-1,
            description="Test case 307: input=:]j]pons\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_308",
            input_value='qks]b]wtqjih:d]]jjz:|]:|i:[]b::\n',
            expected_output=-1,
            description="Test case 308: input=qks]b]wtqjih:d]]jjz:|]:|i:[]b::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_309",
            input_value='l:vw|v|s|:ei[]jc\n',
            expected_output=-1,
            description="Test case 309: input=l:vw|v|s|:ei[]jc\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_310",
            input_value='jyflberp:et]q:x]:n|ww:f:d||c||:aq|:\n',
            expected_output=-1,
            description="Test case 310: input=jyflberp:et]q:x]:n|ww:f:d||c||:aq|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_311",
            input_value=':s]::]p|\n',
            expected_output=-1,
            description="Test case 311: input=:s]::]p|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_312",
            input_value=':w:\n',
            expected_output=-1,
            description="Test case 312: input=:w:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_313",
            input_value='|i|:]:p\n',
            expected_output=-1,
            description="Test case 313: input=|i|:]:p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_314",
            input_value='t]c:[[qt]t::v:x:|[::vaiejt|h\n',
            expected_output=-1,
            description="Test case 314: input=t]c:[[qt]t::v:x:|[::vaiejt|h\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_315",
            input_value=':eiiup]tldk\n',
            expected_output=-1,
            description="Test case 315: input=:eiiup]tldk\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_316",
            input_value='v:j]pajb\n',
            expected_output=-1,
            description="Test case 316: input=v:j]pajb\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_317",
            input_value=':x|b:i[d]\n',
            expected_output=-1,
            description="Test case 317: input=:x|b:i[d]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_318",
            input_value='[d:eest:t|w|cy\n',
            expected_output=-1,
            description="Test case 318: input=[d:eest:t|w|cy\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_319",
            input_value=':ff[::[|lsfp|k]a[x:f\n',
            expected_output=4,
            description="Test case 319: input=:ff[::[|lsfp|k]a[x:f\n, expected=4\n"
        ),
        TestCase(
            name="test_case_320",
            input_value='bk[kl:|tybma:vb::k:\n',
            expected_output=-1,
            description="Test case 320: input=bk[kl:|tybma:vb::k:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_321",
            input_value='[:pu::[dgl[z[g||e:t:e:o|:mhxn\n',
            expected_output=-1,
            description="Test case 321: input=[:pu::[dgl[z[g||e:t:e:o|:mhxn\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_322",
            input_value=':jg|ift[mp|[:\n',
            expected_output=-1,
            description="Test case 322: input=:jg|ift[mp|[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_323",
            input_value='x::vv|d|knrx::[h:]hi[]co:ukn[[|[|:ezb\n',
            expected_output=-1,
            description="Test case 323: input=x::vv|d|knrx::[h:]hi[]co:ukn[[|[|:ezb\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_324",
            input_value=':c:ojn[[|[p]lr\n',
            expected_output=-1,
            description="Test case 324: input=:c:ojn[[|[p]lr\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_325",
            input_value='|fu]s:]:uvra:x:wu|:\n',
            expected_output=-1,
            description="Test case 325: input=|fu]s:]:uvra:x:wu|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_326",
            input_value=']u]gam|y:hdql]x][ap[hae[lb[bi[czzd:fmdho\n',
            expected_output=-1,
            description="Test case 326: input=]u]gam|y:hdql]x][ap[hae[lb[bi[czzd:fmdho\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_327",
            input_value='hdc:ytu|b]]:t:qms|gkwc:zf|:[kf\n',
            expected_output=-1,
            description="Test case 327: input=hdc:ytu|b]]:t:qms|gkwc:zf|:[kf\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_328",
            input_value=':]pmz[x:\n',
            expected_output=-1,
            description="Test case 328: input=:]pmz[x:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_329",
            input_value='ty||gbbe:fnga::]|m]z:][c:a[:|ijl:orl::b[t\n',
            expected_output=-1,
            description="Test case 329: input=ty||gbbe:fnga::]|m]z:][c:a[:|ijl:orl::b[t\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_330",
            input_value='f]mbz]mvz[[sb:j:qi[hhp:\n',
            expected_output=-1,
            description="Test case 330: input=f]mbz]mvz[[sb:j:qi[hhp:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_331",
            input_value='|ryv:[c:::[t:\n',
            expected_output=-1,
            description="Test case 331: input=|ryv:[c:::[t:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_332",
            input_value='yi|ycel:]]]iybr|spac[]:k\n',
            expected_output=-1,
            description="Test case 332: input=yi|ycel:]]]iybr|spac[]:k\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_333",
            input_value='j::]\n',
            expected_output=-1,
            description="Test case 333: input=j::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_334",
            input_value='gugw|:q\n',
            expected_output=-1,
            description="Test case 334: input=gugw|:q\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_335",
            input_value=':uve:jp|n|:]]:g::]:ciygwdj::\n',
            expected_output=-1,
            description="Test case 335: input=:uve:jp|n|:]]:g::]:ciygwdj::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_336",
            input_value='khr:vri]n]m|]vn:rn\n',
            expected_output=-1,
            description="Test case 336: input=khr:vri]n]m|]vn:rn\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_337",
            input_value='m::\n',
            expected_output=-1,
            description="Test case 337: input=m::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_338",
            input_value='::[[l|[nv]q\n',
            expected_output=-1,
            description="Test case 338: input=::[[l|[nv]q\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_339",
            input_value='ezz]:||sdv]:ucb[:[|oh|bm::::cgzl\n',
            expected_output=-1,
            description="Test case 339: input=ezz]:||sdv]:ucb[:[|oh|bm::::cgzl\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_340",
            input_value='ek|\n',
            expected_output=-1,
            description="Test case 340: input=ek|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_341",
            input_value=':p|:rpv::r:h|]:\n',
            expected_output=-1,
            description="Test case 341: input=:p|:rpv::r:h|]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_342",
            input_value='kfcw::]]::f]mx]ecmc|:o:]||k:]jghys|\n',
            expected_output=-1,
            description="Test case 342: input=kfcw::]]::f]mx]ecmc|:o:]||k:]jghys|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_343",
            input_value='c[:mke:::\n',
            expected_output=-1,
            description="Test case 343: input=c[:mke:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_344",
            input_value='gofpok]]]w|[][v:h[ya|:ocm|q:\n',
            expected_output=-1,
            description="Test case 344: input=gofpok]]]w|[][v:h[ya|:ocm|q:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_345",
            input_value='az:]:d]|:|:|o|:::::|j[q]]tid|pb]nxi:c|\n',
            expected_output=-1,
            description="Test case 345: input=az:]:d]|:|:|o|:::::|j[q]]tid|pb]nxi:c|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_346",
            input_value='|:a:ypw|v:jovg[u:hb\n',
            expected_output=-1,
            description="Test case 346: input=|:a:ypw|v:jovg[u:hb\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_347",
            input_value=']|m|:|:w:|k|bi:ex]o]][mtz|ciy[]u[|[|][]o]lmy::|sde]sl|:|:dufv:le\n',
            expected_output=4,
            description="Test case 347: input=]|m|:|:w:|k|bi:ex]o]][mtz|ciy[]u[|[|][]o]lmy::|sde, expected=4\n"
        ),
        TestCase(
            name="test_case_348",
            input_value=']fv:w::mfi:::q]::[|d]dao::|i]|cnt[u]:\n',
            expected_output=4,
            description="Test case 348: input=]fv:w::mfi:::q]::[|d]dao::|i]|cnt[u]:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_349",
            input_value='g|t:]l]w]]]x|q]jf[[[div::it:t\n',
            expected_output=-1,
            description="Test case 349: input=g|t:]l]w]]]x|q]jf[[[div::it:t\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_350",
            input_value='cbk]i::bk|mo:][[|]]x\n',
            expected_output=-1,
            description="Test case 350: input=cbk]i::bk|mo:][[|]]x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_351",
            input_value='fpxbk::se|fz:z:t:|]p]:\n',
            expected_output=-1,
            description="Test case 351: input=fpxbk::se|fz:z:t:|]p]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_352",
            input_value='[v:vv[ds|pz|:|\n',
            expected_output=-1,
            description="Test case 352: input=[v:vv[ds|pz|:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_353",
            input_value='am|::s|q|]x\n',
            expected_output=-1,
            description="Test case 353: input=am|::s|q|]x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_354",
            input_value=':fiv|qz|xl::mjbt][i\n',
            expected_output=-1,
            description="Test case 354: input=:fiv|qz|xl::mjbt][i\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_355",
            input_value='::|o::r[x|o][lmt[wo\n',
            expected_output=-1,
            description="Test case 355: input=::|o::r[x|o][lmt[wo\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_356",
            input_value='t:]iu:fo:e:w:]okrh][[vu|de]:::\n',
            expected_output=-1,
            description="Test case 356: input=t:]iu:fo:e:w:]okrh][[vu|de]:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_357",
            input_value='d:s||||z:sp|:oq[iq[rx|uj[n]:\n',
            expected_output=-1,
            description="Test case 357: input=d:s||||z:sp|:oq[iq[rx|uj[n]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_358",
            input_value=':|]ezv:szl]pg|:||ao\n',
            expected_output=-1,
            description="Test case 358: input=:|]ezv:szl]pg|:||ao\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_359",
            input_value='|jq]mf\n',
            expected_output=-1,
            description="Test case 359: input=|jq]mf\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_360",
            input_value='z::[:rm|t:l::yotu]a|se[]:::y::[t\n',
            expected_output=5,
            description="Test case 360: input=z::[:rm|t:l::yotu]a|se[]:::y::[t\n, expected=5\n"
        ),
        TestCase(
            name="test_case_361",
            input_value='|]bg]]::vwre::fgz:dnf:cemye|tw|]:p]\n',
            expected_output=-1,
            description="Test case 361: input=|]bg]]::vwre::fgz:dnf:cemye|tw|]:p]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_362",
            input_value='g:]c:[]f|yuz|r|:if:lf:\n',
            expected_output=-1,
            description="Test case 362: input=g:]c:[]f|yuz|r|:if:lf:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_363",
            input_value='kl:\n',
            expected_output=-1,
            description="Test case 363: input=kl:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_364",
            input_value='|qe]|p|tcjp::m\n',
            expected_output=-1,
            description="Test case 364: input=|qe]|p|tcjp::m\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_365",
            input_value='||b]h::x|]p\n',
            expected_output=-1,
            description="Test case 365: input=||b]h::x|]p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_366",
            input_value='j::r:my|qml\n',
            expected_output=-1,
            description="Test case 366: input=j::r:my|qml\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_367",
            input_value='z::]|vy:||:hs::]vm\n',
            expected_output=-1,
            description="Test case 367: input=z::]|vy:||:hs::]vm\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_368",
            input_value='nf:ve:ri:riubcmfx]ib]j:qqa\n',
            expected_output=-1,
            description="Test case 368: input=nf:ve:ri:riubcmfx]ib]j:qqa\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_369",
            input_value='ne|s:jsa:pvl|sj[::]u]xbtr:|u:\n',
            expected_output=4,
            description="Test case 369: input=ne|s:jsa:pvl|sj[::]u]xbtr:|u:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_370",
            input_value='|o]:s||:y::g:rans::d]]|p\n',
            expected_output=-1,
            description="Test case 370: input=|o]:s||:y::g:rans::d]]|p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_371",
            input_value='krm|l::|]asp]r:b:::[]qbq::p|:mi[:yrrwoa[zt\n',
            expected_output=-1,
            description="Test case 371: input=krm|l::|]asp]r:b:::[]qbq::p|:mi[:yrrwoa[zt\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_372",
            input_value=']mz|::|sxnk:::z|:bp]ajueqi|ogkql]z:]\n',
            expected_output=-1,
            description="Test case 372: input=]mz|::|sxnk:::z|:bp]ajueqi|ogkql]z:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_373",
            input_value='[:r:::bpz\n',
            expected_output=-1,
            description="Test case 373: input=[:r:::bpz\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_374",
            input_value='[fkvy|f:zd::k:\n',
            expected_output=-1,
            description="Test case 374: input=[fkvy|f:zd::k:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_375",
            input_value=':]u::t:b:sp|zlq]:h::|::ad|:q]f::]::n]m:::::[el|]kb][|dcdtfqs|]o:[:af::l:\n',
            expected_output=-1,
            description="Test case 375: input=:]u::t:b:sp|zlq]:h::|::ad|:q]f::]::n]m:::::[el|]kb, expected=-1\n"
        ),
        TestCase(
            name="test_case_376",
            input_value='::]nd[[|][zac|x[|::l\n',
            expected_output=-1,
            description="Test case 376: input=::]nd[[|][zac|x[|::l\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_377",
            input_value=']|agd:[|]dds|\n',
            expected_output=-1,
            description="Test case 377: input=]|agd:[|]dds|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_378",
            input_value=']::m:::::b:q[]tz\n',
            expected_output=-1,
            description="Test case 378: input=]::m:::::b:q[]tz\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_379",
            input_value='lsvs]qe]|ao]nzqojo::r]nl:w:gu\n',
            expected_output=-1,
            description="Test case 379: input=lsvs]qe]|ao]nzqojo::r]nl:w:gu\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_380",
            input_value='a[|]z|ec[e:l[i:yf[[:se:yy|i[toc|:[\n',
            expected_output=-1,
            description="Test case 380: input=a[|]z|ec[e:l[i:yf[[:se:yy|i[toc|:[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_381",
            input_value='|][x]:rl::rl[f::l:::\n',
            expected_output=-1,
            description="Test case 381: input=|][x]:rl::rl[f::l:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_382",
            input_value='w:c:foghy:n:|]:b::ud|rs[][ua:\n',
            expected_output=-1,
            description="Test case 382: input=w:c:foghy:n:|]:b::ud|rs[][ua:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_383",
            input_value='kr|z:bd:h:]oa:y:|t]:vsx|]uo:|||\n',
            expected_output=-1,
            description="Test case 383: input=kr|z:bd:h:]oa:y:|t]:vsx|]uo:|||\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_384",
            input_value=':o:r\n',
            expected_output=-1,
            description="Test case 384: input=:o:r\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_385",
            input_value='bx]y:xwo:::|]i:lz:]:pyp|sm:|]s\n',
            expected_output=-1,
            description="Test case 385: input=bx]y:xwo:::|]i:lz:]:pyp|sm:|]s\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_386",
            input_value='v][][f[f]y[kvlewloh|tdg:a|:\n',
            expected_output=-1,
            description="Test case 386: input=v][][f[f]y[kvlewloh|tdg:a|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_387",
            input_value='da:z::::f:|:oj]|t:p]:]yxnlnyk:[\n',
            expected_output=-1,
            description="Test case 387: input=da:z::::f:|:oj]|t:p]:]yxnlnyk:[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_388",
            input_value=':goep]s:]nwm]:qt::r|::x\n',
            expected_output=-1,
            description="Test case 388: input=:goep]s:]nwm]:qt::r|::x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_389",
            input_value='[cm|nu:k]f]:qkjz|[k|b:\n',
            expected_output=-1,
            description="Test case 389: input=[cm|nu:k]f]:qkjz|[k|b:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_390",
            input_value=']]:o::|:hj||:k]g:pgtq:eooo:]\n',
            expected_output=-1,
            description="Test case 390: input=]]:o::|:hj||:k]g:pgtq:eooo:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_391",
            input_value='tx::k]:f]pf|x:a:n:w:h]:youw:fajc:vcmi|dx\n',
            expected_output=-1,
            description="Test case 391: input=tx::k]:f]pf|x:a:n:w:h]:youw:fajc:vcmi|dx\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_392",
            input_value='kmfk:teu[|dh]nvwx|]:mg::[d::uco:l[nqp\n',
            expected_output=-1,
            description="Test case 392: input=kmfk:teu[|dh]nvwx|]:mg::[d::uco:l[nqp\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_393",
            input_value='oh[i]fz[][:np:ea[y\n',
            expected_output=-1,
            description="Test case 393: input=oh[i]fz[][:np:ea[y\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_394",
            input_value='jie::q]\n',
            expected_output=-1,
            description="Test case 394: input=jie::q]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_395",
            input_value='w|exua:x:mgr[::zt\n',
            expected_output=-1,
            description="Test case 395: input=w|exua:x:mgr[::zt\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_396",
            input_value='|a:xqjra|]tyl:wpk|nav[:u:[nq\n',
            expected_output=-1,
            description="Test case 396: input=|a:xqjra|]tyl:wpk|nav[:u:[nq\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_397",
            input_value=':l::f:u]wmt:[rqjb|m::][[:[opi\n',
            expected_output=4,
            description="Test case 397: input=:l::f:u]wmt:[rqjb|m::][[:[opi\n, expected=4\n"
        ),
        TestCase(
            name="test_case_398",
            input_value=':|\n',
            expected_output=-1,
            description="Test case 398: input=:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_399",
            input_value='|p\n',
            expected_output=-1,
            description="Test case 399: input=|p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_400",
            input_value='sqsmoyj:l:|nze|:|r]qb::\n',
            expected_output=-1,
            description="Test case 400: input=sqsmoyj:l:|nze|:|r]qb::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_401",
            input_value=':z]:|znp::as:n:bk|:qsu:wm|[wm[hkh:ju[:y|::|||je|wyu[hi\n',
            expected_output=-1,
            description="Test case 401: input=:z]:|znp::as:n:bk|:qsu:wm|[wm[hkh:ju[:y|::|||je|wy, expected=-1\n"
        ),
        TestCase(
            name="test_case_402",
            input_value=':rd\n',
            expected_output=-1,
            description="Test case 402: input=:rd\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_403",
            input_value='w:s:yg]::\n',
            expected_output=-1,
            description="Test case 403: input=w:s:yg]::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_404",
            input_value='w:]ca|i|ot\n',
            expected_output=-1,
            description="Test case 404: input=w:]ca|i|ot\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_405",
            input_value='jb[n]:g[::s[\n',
            expected_output=-1,
            description="Test case 405: input=jb[n]:g[::s[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_406",
            input_value='|]aw[id:s]k:y|b\n',
            expected_output=-1,
            description="Test case 406: input=|]aw[id:s]k:y|b\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_407",
            input_value='[njo::|\n',
            expected_output=-1,
            description="Test case 407: input=[njo::|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_408",
            input_value=']]:u|::m::huhe:s::[ubrq::wa]ttp][]hwik\n',
            expected_output=4,
            description="Test case 408: input=]]:u|::m::huhe:s::[ubrq::wa]ttp][]hwik\n, expected=4\n"
        ),
        TestCase(
            name="test_case_409",
            input_value=']amqhe::r:xvu:i]|:o]j|gkf:hgf]wah\n',
            expected_output=-1,
            description="Test case 409: input=]amqhe::r:xvu:i]|:o]j|gkf:hgf]wah\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_410",
            input_value=':|[m:::[u::r[c\n',
            expected_output=-1,
            description="Test case 410: input=:|[m:::[u::r[c\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_411",
            input_value='ri]qag:luidt:w]:g|j|hjua:\n',
            expected_output=-1,
            description="Test case 411: input=ri]qag:luidt:w]:g|j|hjua:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_412",
            input_value='c\n',
            expected_output=-1,
            description="Test case 412: input=c\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_413",
            input_value=']m::i:::n|ga]m|ai|kc||]:|x|tjjmr:f\n',
            expected_output=-1,
            description="Test case 413: input=]m::i:::n|ga]m|ai|kc||]:|x|tjjmr:f\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_414",
            input_value='s|:[|j|[oouk:::h:|[x[:w|l:[\n',
            expected_output=-1,
            description="Test case 414: input=s|:[|j|[oouk:::h:|[x[:w|l:[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_415",
            input_value='::\n',
            expected_output=-1,
            description="Test case 415: input=::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_416",
            input_value='vv:::[|f:y:|ke::vz:[:y[an|[b:::r:mdzl|:j:h]|s|ldmex\n',
            expected_output=7,
            description="Test case 416: input=vv:::[|f:y:|ke::vz:[:y[an|[b:::r:mdzl|:j:h]|s|ldme, expected=7\n"
        ),
        TestCase(
            name="test_case_417",
            input_value='v:bkn:dwa[]::cv\n',
            expected_output=-1,
            description="Test case 417: input=v:bkn:dwa[]::cv\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_418",
            input_value='o:y|:b|:|::]f:yyqg:oy]ezc:ggv::j:iyj:bqa]:|]r:k[\n',
            expected_output=-1,
            description="Test case 418: input=o:y|:b|:|::]f:yyqg:oy]ezc:ggv::j:iyj:bqa]:|]r:k[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_419",
            input_value='u:g:gt]\n',
            expected_output=-1,
            description="Test case 419: input=u:g:gt]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_420",
            input_value='qgb:ym:]z|og]|:hu\n',
            expected_output=-1,
            description="Test case 420: input=qgb:ym:]z|og]|:hu\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_421",
            input_value=':[[|j]|yqdc[[f|]yv:thdmaw\n',
            expected_output=-1,
            description="Test case 421: input=:[[|j]|yqdc[[f|]yv:thdmaw\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_422",
            input_value='n:yq:[|w|t[st:fg]d:uv[[bw:wgpy[:gnri:\n',
            expected_output=-1,
            description="Test case 422: input=n:yq:[|w|t[st:fg]d:uv[[bw:wgpy[:gnri:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_423",
            input_value='kisy:s:vg:yc]\n',
            expected_output=-1,
            description="Test case 423: input=kisy:s:vg:yc]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_424",
            input_value='w:l[|:|tggqs\n',
            expected_output=-1,
            description="Test case 424: input=w:l[|:|tggqs\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_425",
            input_value=':o:y||f[[no]:a:ge|[v|:gw|f:u[[\n',
            expected_output=-1,
            description="Test case 425: input=:o:y||f[[no]:a:ge|[v|:gw|f:u[[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_426",
            input_value='g|]uj\n',
            expected_output=-1,
            description="Test case 426: input=g|]uj\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_427",
            input_value='pm]e:h:|j]dts]][sl[ekt]xt|zmx:k::x:d[\n',
            expected_output=-1,
            description="Test case 427: input=pm]e:h:|j]dts]][sl[ekt]xt|zmx:k::x:d[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_428",
            input_value=']twgo[mu:xf:[||e|:l|a|:\n',
            expected_output=-1,
            description="Test case 428: input=]twgo[mu:xf:[||e|:l|a|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_429",
            input_value='h:q::|zyh:b:]hpv[yf]pp|v]:y:j\n',
            expected_output=-1,
            description="Test case 429: input=h:q::|zyh:b:]hpv[yf]pp|v]:y:j\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_430",
            input_value=']::[u:[w|v|:qu[[[n:\n',
            expected_output=-1,
            description="Test case 430: input=]::[u:[w|v|:qu[[[n:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_431",
            input_value='p]j:]n:\n',
            expected_output=-1,
            description="Test case 431: input=p]j:]n:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_432",
            input_value='wa\n',
            expected_output=-1,
            description="Test case 432: input=wa\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_433",
            input_value='lu|v|fs:gow]:ct[ppm]pii::[z|:\n',
            expected_output=-1,
            description="Test case 433: input=lu|v|fs:gow]:ct[ppm]pii::[z|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_434",
            input_value=':e]h:]]::|]::]j|[s]]:[my::\n',
            expected_output=-1,
            description="Test case 434: input=:e]h:]]::|]::]j|[s]]:[my::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_435",
            input_value='[x:[r:b[|\n',
            expected_output=-1,
            description="Test case 435: input=[x:[r:b[|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_436",
            input_value=':[sy[b|[|]]|]n|a[]tpa:::\n',
            expected_output=-1,
            description="Test case 436: input=:[sy[b|[|]]|]n|a[]tpa:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_437",
            input_value='ntp]y|w:]v]|\n',
            expected_output=-1,
            description="Test case 437: input=ntp]y|w:]v]|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_438",
            input_value='z]w:dc[dq][[]l[|||p]]ealr[m[evn:o\n',
            expected_output=-1,
            description="Test case 438: input=z]w:dc[dq][[]l[|||p]]ealr[m[evn:o\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_439",
            input_value='hxl:|c|]omqt:jeey|kjyz:nphi::[v[c[::dunu]lf\n',
            expected_output=4,
            description="Test case 439: input=hxl:|c|]omqt:jeey|kjyz:nphi::[v[c[::dunu]lf\n, expected=4\n"
        ),
        TestCase(
            name="test_case_440",
            input_value=']pbs|::g:tvu]|:\n',
            expected_output=-1,
            description="Test case 440: input=]pbs|::g:tvu]|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_441",
            input_value='r::t:|:oezsfj:|]sjn]k|][][]t\n',
            expected_output=-1,
            description="Test case 441: input=r::t:|:oezsfj:|]sjn]k|][][]t\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_442",
            input_value='t:::c:oyh:]:\n',
            expected_output=-1,
            description="Test case 442: input=t:::c:oyh:]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_443",
            input_value='|d]|v\n',
            expected_output=-1,
            description="Test case 443: input=|d]|v\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_444",
            input_value='p|:[w|[t]||]|[y|x|as:q|o|zbn|zkyr|q:|eu[ll::mq:[j\n',
            expected_output=-1,
            description="Test case 444: input=p|:[w|[t]||]|[y|x|as:q|o|zbn|zkyr|q:|eu[ll::mq:[j\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_445",
            input_value='d]w|g:bt:k:]tzzija[]:t\n',
            expected_output=-1,
            description="Test case 445: input=d]w|g:bt:k:]tzzija[]:t\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_446",
            input_value=':::drl:|fv::rn:q[]nq\n',
            expected_output=-1,
            description="Test case 446: input=:::drl:|fv::rn:q[]nq\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_447",
            input_value='y|::f:]]:p\n',
            expected_output=-1,
            description="Test case 447: input=y|::f:]]:p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_448",
            input_value='u:ypnp:a::h:yqtome|kjsa:]|:rsotcg:]xcq[vvx|]]e\n',
            expected_output=-1,
            description="Test case 448: input=u:ypnp:a::h:yqtome|kjsa:]|:rsotcg:]xcq[vvx|]]e\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_449",
            input_value='::l:g\n',
            expected_output=-1,
            description="Test case 449: input=::l:g\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_450",
            input_value='wl\n',
            expected_output=-1,
            description="Test case 450: input=wl\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_451",
            input_value=':r:]z:\n',
            expected_output=-1,
            description="Test case 451: input=:r:]z:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_452",
            input_value='e|v|gh:::d]|d|]d:fs]\n',
            expected_output=-1,
            description="Test case 452: input=e|v|gh:::d]|d|]d:fs]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_453",
            input_value=':l|kj|:sli::r:]g:yt|]:h[:::tl|hb:r\n',
            expected_output=-1,
            description="Test case 453: input=:l|kj|:sli::r:]g:yt|]:h[:::tl|hb:r\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_454",
            input_value='n:::[::[gwy\n',
            expected_output=-1,
            description="Test case 454: input=n:::[::[gwy\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_455",
            input_value='::qa|v]|m|::|[nu]:||:fy::[p:af:e:qj|\n',
            expected_output=-1,
            description="Test case 455: input=::qa|v]|m|::|[nu]:||:fy::[p:af:e:qj|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_456",
            input_value='f|c\n',
            expected_output=-1,
            description="Test case 456: input=f|c\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_457",
            input_value='qq:|:f|o:g:ra[||]q\n',
            expected_output=-1,
            description="Test case 457: input=qq:|:f|o:g:ra[||]q\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_458",
            input_value='l[b:|[toa[g]qn\n',
            expected_output=-1,
            description="Test case 458: input=l[b:|[toa[g]qn\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_459",
            input_value='p:]dr]kt]t:]f:f|::s]ic]mzz:\n',
            expected_output=-1,
            description="Test case 459: input=p:]dr]kt]t:]f:f|::s]ic]mzz:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_460",
            input_value='jp::l:[pyv]t:a][]::j[k:dmdc|:e]bjzp|pl[:[[::f|jo:nzu:pu|ndvpte:||\n',
            expected_output=5,
            description="Test case 460: input=jp::l:[pyv]t:a][]::j[k:dmdc|:e]bjzp|pl[:[[::f|jo:n, expected=5\n"
        ),
        TestCase(
            name="test_case_461",
            input_value=':wt:nt|la:p|]:k[acxydv[][]|]e::|v|i:\n',
            expected_output=-1,
            description="Test case 461: input=:wt:nt|la:p|]:k[acxydv[][]|]e::|v|i:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_462",
            input_value=']|[|zja::|g|]d:t::gawk|j|rfcada|qfkg:hi\n',
            expected_output=4,
            description="Test case 462: input=]|[|zja::|g|]d:t::gawk|j|rfcada|qfkg:hi\n, expected=4\n"
        ),
        TestCase(
            name="test_case_463",
            input_value='][mm:mqraj:\n',
            expected_output=-1,
            description="Test case 463: input=][mm:mqraj:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_464",
            input_value=':]|l:dgb::::]:]wrt\n',
            expected_output=-1,
            description="Test case 464: input=:]|l:dgb::::]:]wrt\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_465",
            input_value='::k:c:tjg|h]:\n',
            expected_output=-1,
            description="Test case 465: input=::k:c:tjg|h]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_466",
            input_value='vpl:::]owzt[:\n',
            expected_output=-1,
            description="Test case 466: input=vpl:::]owzt[:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_467",
            input_value='djt:::bfkl:q:ls::[]kfgpgit[k[|c:\n',
            expected_output=-1,
            description="Test case 467: input=djt:::bfkl:q:ls::[]kfgpgit[k[|c:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_468",
            input_value='r::uh]][j]bfqsn[:[|s|:kqz:|p[bl::x|\n',
            expected_output=-1,
            description="Test case 468: input=r::uh]][j]bfqsn[:[|s|:kqz:|p[bl::x|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_469",
            input_value='y:::\n',
            expected_output=-1,
            description="Test case 469: input=y:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_470",
            input_value=']lx:rjzff\n',
            expected_output=-1,
            description="Test case 470: input=]lx:rjzff\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_471",
            input_value='ptbb|]d\n',
            expected_output=-1,
            description="Test case 471: input=ptbb|]d\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_472",
            input_value='b|::b:g]]||:]nm[yrpf:t][]tzjy|:xm:q:\n',
            expected_output=-1,
            description="Test case 472: input=b|::b:g]]||:]nm[yrpf:t][]tzjy|:xm:q:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_473",
            input_value=']::::uk:l:l:cl|]|:mbmqn\n',
            expected_output=-1,
            description="Test case 473: input=]::::uk:l:l:cl|]|:mbmqn\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_474",
            input_value=':x::]\n',
            expected_output=-1,
            description="Test case 474: input=:x::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_475",
            input_value=']uwfhq[uz[y::fi[:[egg:p\n',
            expected_output=-1,
            description="Test case 475: input=]uwfhq[uz[y::fi[:[egg:p\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_476",
            input_value='aa|:]w:lzf:zgw]:]|:ek|bq||d]h:]aq:n:o:]s]m]\n',
            expected_output=-1,
            description="Test case 476: input=aa|:]w:lzf:zgw]:]|:ek|bq||d]h:]aq:n:o:]s]m]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_477",
            input_value='|::]\n',
            expected_output=-1,
            description="Test case 477: input=|::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_478",
            input_value='pky::t]zyx:||stu]tjt|:|v:[axhm[:ny|\n',
            expected_output=-1,
            description="Test case 478: input=pky::t]zyx:||stu]tjt|:|v:[axhm[:ny|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_479",
            input_value='ld]]ngmi:c|tqo:v:]|]h:l\n',
            expected_output=-1,
            description="Test case 479: input=ld]]ngmi:c|tqo:v:]|]h:l\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_480",
            input_value='[|::[aqj]]cz:l[||::\n',
            expected_output=4,
            description="Test case 480: input=[|::[aqj]]cz:l[||::\n, expected=4\n"
        ),
        TestCase(
            name="test_case_481",
            input_value=']d]ph:pm]||ytyw:[t[|wgx:tbagh:v[l:kpsuo|pcp\n',
            expected_output=-1,
            description="Test case 481: input=]d]ph:pm]||ytyw:[t[|wgx:tbagh:v[l:kpsuo|pcp\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_482",
            input_value='do]|]c[]ad|[adzbqjz]\n',
            expected_output=-1,
            description="Test case 482: input=do]|]c[]ad|[adzbqjz]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_483",
            input_value=']qrt:]no]|::][]d:p]:iwl::[ud[|s:r\n',
            expected_output=-1,
            description="Test case 483: input=]qrt:]no]|::][]d:p]:iwl::[ud[|s:r\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_484",
            input_value='mg|[]:[kla[[a|[z\n',
            expected_output=-1,
            description="Test case 484: input=mg|[]:[kla[[a|[z\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_485",
            input_value='|:g[jv]ep]ln:|xnbaf\n',
            expected_output=-1,
            description="Test case 485: input=|:g[jv]ep]ln:|xnbaf\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_486",
            input_value='eeps]|rizigx:]\n',
            expected_output=-1,
            description="Test case 486: input=eeps]|rizigx:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_487",
            input_value='::j]]]t|s:j]:bdzikd|zi|[kx]][:[lw:||mdnlw\n',
            expected_output=-1,
            description="Test case 487: input=::j]]]t|s:j]:bdzikd|zi|[kx]][:[lw:||mdnlw\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_488",
            input_value='zuf::z::w]pkf]fu]vz\n',
            expected_output=-1,
            description="Test case 488: input=zuf::z::w]pkf]fu]vz\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_489",
            input_value='icpw::k:x:wu|t:kq:ln]:|bdhiwu\n',
            expected_output=-1,
            description="Test case 489: input=icpw::k:x:wu|t:kq:ln]:|bdhiwu\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_490",
            input_value=':[zie]|avb[qvl\n',
            expected_output=-1,
            description="Test case 490: input=:[zie]|avb[qvl\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_491",
            input_value='fur|z][[][w:\n',
            expected_output=-1,
            description="Test case 491: input=fur|z][[][w:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_492",
            input_value='::cy::::iry]|m:coi[]o|[bi:z[:s:p[:gcwh::::\n',
            expected_output=-1,
            description="Test case 492: input=::cy::::iry]|m:coi[]o|[bi:z[:s:p[:gcwh::::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_493",
            input_value=':]jpb::]|[ifu|yb]::l:|kt\n',
            expected_output=-1,
            description="Test case 493: input=:]jpb::]|[ifu|yb]::l:|kt\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_494",
            input_value='b][[[hk[\n',
            expected_output=-1,
            description="Test case 494: input=b][[[hk[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_495",
            input_value='|x:]::ultgj|e:t:]z\n',
            expected_output=-1,
            description="Test case 495: input=|x:]::ultgj|e:t:]z\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_496",
            input_value='fh]]||:medq:]:|\n',
            expected_output=-1,
            description="Test case 496: input=fh]]||:medq:]:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_497",
            input_value='|:zwi|i:\n',
            expected_output=-1,
            description="Test case 497: input=|:zwi|i:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_498",
            input_value='::dd:qj[g|s[:::]yemb]lo::\n',
            expected_output=4,
            description="Test case 498: input=::dd:qj[g|s[:::]yemb]lo::\n, expected=4\n"
        ),
        TestCase(
            name="test_case_499",
            input_value=']:p]b|s]e\n',
            expected_output=-1,
            description="Test case 499: input=]:p]b|s]e\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_500",
            input_value='fa:]|:qzhby:l]wazenq]de|x::::td[]|:s\n',
            expected_output=-1,
            description="Test case 500: input=fa:]|:qzhby:l]wazenq]de|x::::td[]|:s\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_501",
            input_value='m:wpuz:\n',
            expected_output=-1,
            description="Test case 501: input=m:wpuz:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_502",
            input_value='dwx::::g:pi|r|bf[fxtvwk|z]|x|\n',
            expected_output=-1,
            description="Test case 502: input=dwx::::g:pi|r|bf[fxtvwk|z]|x|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_503",
            input_value='pcn|]t|]|y:rl]]:|u|y]y:h:g|x\n',
            expected_output=-1,
            description="Test case 503: input=pcn|]t|]|y:rl]]:|u|y]y:h:g|x\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_504",
            input_value='hfdm]]w:ldlrp|t:|:wje::]fw|k:|[snyj\n',
            expected_output=-1,
            description="Test case 504: input=hfdm]]w:ldlrp|t:|:wje::]fw|k:|[snyj\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_505",
            input_value='e|:b]][]u|cv[rpypk:g[:gb:\n',
            expected_output=-1,
            description="Test case 505: input=e|:b]][]u|cv[rpypk:g[:gb:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_506",
            input_value='|zb|nd:|v\n',
            expected_output=-1,
            description="Test case 506: input=|zb|nd:|v\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_507",
            input_value='fuip:pvl:c[]::t::[x::f|f:urz\n',
            expected_output=-1,
            description="Test case 507: input=fuip:pvl:c[]::t::[x::f|f:urz\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_508",
            input_value='lr]b:]:]:|]|x|yiac\n',
            expected_output=-1,
            description="Test case 508: input=lr]b:]:]:|]|x|yiac\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_509",
            input_value=']:]ty]l|c]]rkk\n',
            expected_output=-1,
            description="Test case 509: input=]:]ty]l|c]]rkk\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_510",
            input_value='g]:c]etg\n',
            expected_output=-1,
            description="Test case 510: input=g]:c]etg\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_511",
            input_value='icx:q:]:|k|a]\n',
            expected_output=-1,
            description="Test case 511: input=icx:q:]:|k|a]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_512",
            input_value=':]:|j|ehb]d|kqro|gdc:f:jbc|||v:gocskgf:|a::kmhv:ffwu:|qo:]v:y:igkm]:i|v|i|on\n',
            expected_output=-1,
            description="Test case 512: input=:]:|j|ehb]d|kqro|gdc:f:jbc|||v:gocskgf:|a::kmhv:ff, expected=-1\n"
        ),
        TestCase(
            name="test_case_513",
            input_value='xx:|o[vu]yp[]ew[l|::::x[t::\n',
            expected_output=-1,
            description="Test case 513: input=xx:|o[vu]yp[]ew[l|::::x[t::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_514",
            input_value='[[[[[:|\n',
            expected_output=-1,
            description="Test case 514: input=[[[[[:|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_515",
            input_value='rmcq]w[wu\n',
            expected_output=-1,
            description="Test case 515: input=rmcq]w[wu\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_516",
            input_value='k|\n',
            expected_output=-1,
            description="Test case 516: input=k|\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_517",
            input_value='c:hn:|:|qiyse:o::[pp]fn:b\n',
            expected_output=-1,
            description="Test case 517: input=c:hn:|:|qiyse:o::[pp]fn:b\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_518",
            input_value='|]l|gj]:p:u[]hv:\n',
            expected_output=-1,
            description="Test case 518: input=|]l|gj]:p:u[]hv:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_519",
            input_value='r:xa::::fc:|]v|n|:axl\n',
            expected_output=-1,
            description="Test case 519: input=r:xa::::fc:|]v|n|:axl\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_520",
            input_value='[]|ccgd:mn|:\n',
            expected_output=-1,
            description="Test case 520: input=[]|ccgd:mn|:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_521",
            input_value=':[::]\n',
            expected_output=4,
            description="Test case 521: input=:[::]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_522",
            input_value=']lj]vz:::y:::t]\n',
            expected_output=-1,
            description="Test case 522: input=]lj]vz:::y:::t]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_523",
            input_value=':]:un]v]]]cuy:w[|vms]hbnh]z[y:eru|el[[::iw[f[[:r:[w[][fezx\n',
            expected_output=5,
            description="Test case 523: input=:]:un]v]]]cuy:w[|vms]hbnh]z[y:eru|el[[::iw[f[[:r:[, expected=5\n"
        ),
        TestCase(
            name="test_case_524",
            input_value=':e:vvq:]u]]\n',
            expected_output=-1,
            description="Test case 524: input=:e:vvq:]u]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_525",
            input_value='s\n',
            expected_output=-1,
            description="Test case 525: input=s\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_526",
            input_value=':e||:|::[|:[|l\n',
            expected_output=-1,
            description="Test case 526: input=:e||:|::[|:[|l\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_527",
            input_value='f]|g:lxm]:|[[:[:whcklc|cdan|[|oi[me[\n',
            expected_output=-1,
            description="Test case 527: input=f]|g:lxm]:|[[:[:whcklc|cdan|[|oi[me[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_528",
            input_value='::ew:]]::d[][::c:[:ox:jv::b:b:\n',
            expected_output=-1,
            description="Test case 528: input=::ew:]]::d[][::c:[:ox:jv::b:b:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_529",
            input_value=':]|tue][rs]|x::u|]t:t:|vo|[ax[:|yomhn::bne\n',
            expected_output=4,
            description="Test case 529: input=:]|tue][rs]|x::u|]t:t:|vo|[ax[:|yomhn::bne\n, expected=4\n"
        ),
        TestCase(
            name="test_case_530",
            input_value='z\n',
            expected_output=-1,
            description="Test case 530: input=z\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_531",
            input_value='i::fd\n',
            expected_output=-1,
            description="Test case 531: input=i::fd\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_532",
            input_value=':sv:iro|]:zfvpwa:|ug]||v:\n',
            expected_output=-1,
            description="Test case 532: input=:sv:iro|]:zfvpwa:|ug]||v:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_533",
            input_value=':]:]\n',
            expected_output=-1,
            description="Test case 533: input=:]:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_534",
            input_value='n|]:w:bl|:j]:\n',
            expected_output=-1,
            description="Test case 534: input=n|]:w:bl|:j]:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_535",
            input_value='z]]]r]goiqy|x]h:|s]:tof|tm|rdd::x:]l:hg:gt::]|mru]tn|:h|\n',
            expected_output=-1,
            description="Test case 535: input=z]]]r]goiqy|x]h:|s]:tof|tm|rdd::x:]l:hg:gt::]|mru], expected=-1\n"
        ),
        TestCase(
            name="test_case_536",
            input_value='oenfnemfddbhhmig]gcd:]:mnnbj::f|ichec:|dkfnjbfjkdgoge]lfihgd[hooegj||g|gc]omkbggn:in::[dim[oie:nbkk]lfkddm:]cmjkf\n',
            expected_output=4,
            description="Test case 536: input=oenfnemfddbhhmig]gcd:]:mnnbj::f|ichec:|dkfnjbfjkdg, expected=4\n"
        ),
        TestCase(
            name="test_case_537",
            input_value='[lqd]v::|e\n',
            expected_output=-1,
            description="Test case 537: input=[lqd]v::|e\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_538",
            input_value='][i::[][gq:::|:g|n:gt:\n',
            expected_output=4,
            description="Test case 538: input=][i::[][gq:::|:g|n:gt:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_539",
            input_value='::]z]:|:x|:b:|[][w||]j[|oxjf[oo::urc]\n',
            expected_output=4,
            description="Test case 539: input=::]z]:|:x|:b:|[][w||]j[|oxjf[oo::urc]\n, expected=4\n"
        ),
        TestCase(
            name="test_case_540",
            input_value=']w:q]a]n:p:hb:rt:|pqe|]ze:]z:::b]::c[::jj[r::dw|kbe\n',
            expected_output=-1,
            description="Test case 540: input=]w:q]a]n:p:hb:rt:|pqe|]ze:]z:::b]::c[::jj[r::dw|kb, expected=-1\n"
        ),
        TestCase(
            name="test_case_541",
            input_value='bb:]ranrc:s:qmrcw:atzl:]im|eg:du::j::::b|]]\n',
            expected_output=-1,
            description="Test case 541: input=bb:]ranrc:s:qmrcw:atzl:]im|eg:du::j::::b|]]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_542",
            input_value=':[:]::\n',
            expected_output=-1,
            description="Test case 542: input=:[:]::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_543",
            input_value='u|::kepn]pr]a\n',
            expected_output=-1,
            description="Test case 543: input=u|::kepn]pr]a\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_544",
            input_value='n|:f||f:|xabqx]zj:nd|]vl\n',
            expected_output=-1,
            description="Test case 544: input=n|:f||f:|xabqx]zj:nd|]vl\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_545",
            input_value='pwnseq[::[ajk]y:e:\n',
            expected_output=4,
            description="Test case 545: input=pwnseq[::[ajk]y:e:\n, expected=4\n"
        ),
        TestCase(
            name="test_case_546",
            input_value='aeo:wg|t:]s|:][[f]iczvk:boe||plg:::::::\n',
            expected_output=-1,
            description="Test case 546: input=aeo:wg|t:]s|:][[f]iczvk:boe||plg:::::::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_547",
            input_value='a]::]:nk]:cppyut]wb[g]\n',
            expected_output=-1,
            description="Test case 547: input=a]::]:nk]:cppyut]wb[g]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_548",
            input_value='|g|jwpdzh:s:]::qp|r\n',
            expected_output=-1,
            description="Test case 548: input=|g|jwpdzh:s:]::qp|r\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_549",
            input_value='yj|:du|mg:c]jn\n',
            expected_output=-1,
            description="Test case 549: input=yj|:du|mg:c]jn\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_550",
            input_value=':||:]\n',
            expected_output=-1,
            description="Test case 550: input=:||:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_551",
            input_value=']a]:pt]]iid:g:]:rfl\n',
            expected_output=-1,
            description="Test case 551: input=]a]:pt]]iid:g:]:rfl\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_552",
            input_value='t::u]|]::]:]d:]|wf|r:|:[\n',
            expected_output=-1,
            description="Test case 552: input=t::u]|]::]:]d:]|wf|r:|:[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_553",
            input_value='|a|:r:]]:m]:|a\n',
            expected_output=-1,
            description="Test case 553: input=|a|:r:]]:m]:|a\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_554",
            input_value='w::||[\n',
            expected_output=-1,
            description="Test case 554: input=w::||[\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_555",
            input_value='o|:]]|d:y:x|jmvonbz:|:|]icol\n',
            expected_output=-1,
            description="Test case 555: input=o|:]]|d:y:x|jmvonbz:|:|]icol\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_556",
            input_value=':[]f:\n',
            expected_output=-1,
            description="Test case 556: input=:[]f:\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_557",
            input_value='|:[]a\n',
            expected_output=-1,
            description="Test case 557: input=|:[]a\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_558",
            input_value=':::]|||[:::\n',
            expected_output=-1,
            description="Test case 558: input=:::]|||[:::\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_559",
            input_value='aa::]\n',
            expected_output=-1,
            description="Test case 559: input=aa::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_560",
            input_value='||::]\n',
            expected_output=-1,
            description="Test case 560: input=||::]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_561",
            input_value='||:]\n',
            expected_output=-1,
            description="Test case 561: input=||:]\n, expected=-1\n"
        ),
        TestCase(
            name="test_case_562",
            input_value=':||||||:]\n',
            expected_output=-1,
            description="Test case 562: input=:||||||:]\n, expected=-1\n"
        ),
    ]
    
    return Problem(
        name="apps_0000",
        description=r"""You are given a string $s$ containing lowercase Latin letters and characters [, ], : and |.

Your task is to count the total number of bracket pairs (opening '[' and closing ']') in the string. A bracket pair is valid if there is an opening bracket followed by a closing bracket, with any characters (including other brackets) in between.

If no valid bracket pairs are found, return $-1$. Otherwise, return the count of bracket pairs.


-----Input-----

The only line contains one string $s$ ($1 \le |s| \le 500000$). It consists of lowercase Latin letters and characters [, ], : and |.


-----Output-----

If no bracket pairs are found, print $-1$. Otherwise print the count of bracket pairs.


-----Examples-----
Input
|[a:b:|]

Output
4

Input
|]:[|:]

Output
-1""",
        function_signature="def solution(*args, **kwargs):",
        visible_tests=visible_tests,
        hidden_tests=hidden_tests
    )