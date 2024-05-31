# # symbol = {
# #     "A": "기침을 한다.",
# #     "B": "열이 난다.",
# #     "C": "감기이다.",
# #     "D": "열이 일주일 이상 되었다.",
# #     "E": "폐렴이다.",
# #     "F": "가래가 짙다.",
# #     "G": "항생제를 처방한다.",
# #     "H": "콧물이 난다.",
# #     "I": "해열제를 처방한다.",
# # }
# #
# # rules = [
# #     {"조건": ["A", "B"], "결론": "C", "cf": 0.7},
# #     {"조건": ["D"], "결론": "E", "cf": 0.6},
# #     {"조건": ["F"], "결론": "G", "cf": 1.0},
# #     {"조건": ["H"], "결론": "C", "cf": 0.6},
# #     {"조건": ["B"], "결론": "I", "cf": 1.0}
# # ]
# #
# # def apply_rules(short):
# #     for rule in rules:
# #         conditions_met = all(condition in short for condition in rule["조건"])
# #         if conditions_met:
# #             short.append(rule["결론"])
# #             if rule["cf"] is not None:
# #                 short.append(rule["cf"])
# #
# # def cold_expert(short):
# #     apply_rules(short)
# #     return short
# #
# #
# # short = ["A", "B"]
# #
# # print("규칙:", [symbol[item] for item in short])
# #
# # result = cold_expert(short)
# #
# # if "C" in result:
# #     print("추론 결과:", symbol["C"])
#
# symbol = {
#     "A": "기침을 한다.",
#     "B": "열이 난다.",
#     "C": "감기이다.",
#     "D": "열이 일주일 이상 되었다.",
#     "E": "폐렴이다.",
#     "F": "가래가 짙다.",
#     "G": "항생제를 처방한다.",
#     "H": "콧물이 난다.",
#     "I": "해열제를 처방한다.",
# }
#
# rules = [
#     {"조건": ["A", "B"], "결론": "C", "cf": 0.7},
#     {"조건": ["H"], "결론": "C", "cf": 0.6}
# ]
#
# def apply_rules(short):
#     for rule in rules:
#         conditions_met = all(condition in short for condition in rule["조건"])
#         if conditions_met:
#             if "cf" in rule:
#                 short.append((rule["결론"], rule["cf"]))
#             else:
#                 short.append((rule["결론"], None))
#
# def cold_expert(short):
#     apply_rules(short)
#     return short
#
# def evaluate_result(result):
#     for item in result:
#         conclusion, cf = item if len(item) == 2 else (item[0], None)
#         if cf:
#             print(f"추론 결과: {symbol[conclusion]} (cf: {cf})")
#         else:
#             print(f"추론 결과: {symbol[conclusion]}")
#
# # 예시 입력
# short = ["A", "B"]
#
# print("입력:", [symbol[item] for item in short])
#
# result = cold_expert(short)
#
# if "C" in [item[0] for item in result]:
#     evaluate_result(result)

symbol = {
    "A": "기침을 한다.",
    "B": "열이 난다.",
    "C": "감기이다.",
    "D": "열이 일주일 이상 되었다.",
    "E": "폐렴이다.",
    "F": "가래가 짙다.",
    "G": "항생제를 처방한다.",
    "H": "콧물이 난다.",
    "I": "해열제를 처방한다.",
}

def apply_rules(short):
    cf_dict = {"A": 0.8, "D": 0.7, "H": 0.6}  # 사실에 따른 CF 값
    cf = min([cf_dict[item] for item in short if item in cf_dict]) * 0.7  # CF 값 계산

    # 사실에 따라 결론 및 CF 값 추가
    if "A" in short and "B" in short:
        short.append(("C", cf))
    if "D" in short:
        short.append(("E", (0.7 - 0.1) * 0.6))
    if "F" in short:
        short.append(("G", 1.0))
    if "H" in short:
        short.append(("C", (0.8 - 0.2) * 0.6))
    if "B" in short:
        short.append(("I", 1.0))

def cold_expert(short):
    apply_rules(short)
    return short

short = ["A", "B", "H", "F"]

print("입력:", [symbol[item] for item in short])

cold_expert(short)

if "C" in [item[0] for item in short]:
    print("감기이다")
