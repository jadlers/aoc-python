#!/usr/bin/env python3

import fileinput
import re
import sys

lines = [x.strip() for x in fileinput.input()]

RULES = True
R = {}  # ch | sub_rules, is_sub_rules


def valid_rule(s, rule, pos=0, depth=0):
    "Returns if the rule matches and number of chars in match"

    # print(f"{depth}\ts={s} (pos={pos}: {s[pos:]})")

    if len(s) == 0:
        return True

    elif not rule[1]:  # Single char
        ch = rule[0]
        if s[pos] == ch:
            return True, 1
        else:
            return False, 1

    elif rule[1]:  # The rule is one or more lists of subrules
        for subrule_list in rule[0]:
            # print(f"Next subrule_list: {subrule_list}")
            valid = True
            pos_ = pos
            for r in subrule_list:
                # print(f"Checking rule {r} ({R[r][0]}) against {s[pos_:]}")
                valid, read_chars = valid_rule(s, R[r], pos_, depth + 1)
                pos_ += read_chars
                # print(f"valid={valid} read_chars={read_chars} updated pos_={pos_}")
                if not valid:
                    break

            if valid:
                # print(f"it is {subrule_list}")
                return True, pos_ - pos
            # else:
            #     print(f"it's not {subrule_list}")

    return False, 0


def validate(s, rule):
    valid = False
    print(f"s={s} rule={rule[0]}")
    if rule[1]:  # Sub-rules
        for sub_paths in rule[0]:
            print("New sub path", sub_paths)
            valid = True
            for (i, r) in enumerate(sub_paths):
                is_sub_path = R[r][1]
                if not is_sub_path and s[i] != R[r][0]:
                    print(s[i:], r, R[r])
                    # Not valid
                    break
            if valid:
                return True

        # print("complex")
    elif not rule[1] and s[0] == rule[0]:
        print("Match")
        # print(f"s={s} rule={rule}")
        return True

    return False


# print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())

p1 = 0
for line in lines:
    if not line:
        RULES = False
        continue

    # print(line)

    if RULES:
        # print(chs)
        # R[i] =
        # print(line)
        id_, chs = line.split(":")
        id_ = int(id_)
        if re.search("\d+", chs):  # Sub-rules
            # print("nums")
            rule_groups = [[int(y) for y in x.split()] for x in chs.split("|")]
            # print(rule_groups)
            R[id_] = (rule_groups, True)
        else:  # Single char
            # print("chs")
            ch = re.search("\w", chs)[0]
            R[id_] = (ch, False)
    else:
        # print(f"validate({line}, {R[0]})")
        valid, length = valid_rule(line, R[0])
        if valid and len(line) == length:
            p1 += 1
            print(line)
        # break

    # print(line)
# print(R)

print("p1:", p1)
