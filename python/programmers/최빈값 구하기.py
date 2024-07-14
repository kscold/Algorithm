# def solution(array):
#     set_array = list(set(array))
#     result = {}
#     for item in set_array:
#         result[item] = array.count(item)
#
#     values_list = list(result.values())
#     max_value = max(list(result.values()))
#     key_list = list(result.keys())
#
#     if values_list.count(max_value) > 1:
#         answer = -1
#     else:
#        index = values_list.index(max_value)
#        answer = key_list[index]
#
#     return answer
#
#
# print(solution([1, 2, 3, 3, 3, 4]))
# print(solution([1, 1, 2, 2]))
# print(solution([1]))


# def solution(records, k, date):
#     # 날짜를 정수형으로 변환하는 함수
#     def parse_int_date(date):
#         year, month, day = map(int, date.split('-'))
#         return year * 10000 + month * 100 + day
#
#     # 날짜를 k일 이전으로 계산하는 함수
#     def parse_start_date(k, date):
#         year, month, day = map(int, date.split('-'))
#         while k > 1:  # k-1일 이전 날짜 계산
#             k -= 1
#             day -= 1
#             if day == 0:
#                 day = 30  # 모든 달은 30일까지 있다고 가정
#                 month -= 1
#                 if month == 0:
#                     month = 12
#                     year -= 1
#         start_date = f"{year:04d}{month:02d}{day:02d}"
#         return int(start_date)
#
#     end_date = parse_int_date(date)  # 기준 날짜를 정수형으로 변환
#     start_date = parse_start_date(k, date)  # k일 이전의 시작 날짜 계산
#
#     # 기간 내의 기록 필터링
#     filtered_records = list()
#     for record in records:
#         record_date, record_user_id, record_product_id = record.split()
#         record_date_int = parse_int_date(record_date)
#         if start_date <= record_date_int <= end_date:
#             filtered_records.append((record_date, record_user_id, record_product_id))
#
#     if not filtered_records:  # 기간 내 기록이 없으면 "no result" 반환
#         return ["no result"]
#
#     # 상품별 재구매율 계산을 위한 데이터 구조 초기화
#     product_user_dict = dict()
#     product_buy_dict = dict()
#     product_rebuy_dict = dict()
#
#     # 필터링된 기록을 바탕으로 재구매율 계산
#     for _, period_user_id, period_product_id in filtered_records:
#         if period_product_id not in product_user_dict:
#             product_user_dict[period_product_id] = set()
#             product_buy_dict[period_product_id] = 0
#             product_rebuy_dict[period_product_id] = 0
#         if period_user_id in product_user_dict[period_product_id]:
#             product_rebuy_dict[period_product_id] += 1
#         product_user_dict[period_product_id].add(period_user_id)
#         product_buy_dict[period_product_id] += 1
#
#     # 각 상품의 재구매율을 계산
#     product_repurchase_rate = {}
#     for product_id in product_buy_dict:
#         if product_buy_dict[product_id] > 1:
#             repurchase_rate = (product_rebuy_dict[product_id] / len(product_user_dict[product_id])) * 100
#         else:
#             repurchase_rate = 0
#         product_repurchase_rate[product_id] = repurchase_rate
#
#     # 정렬을 위한 리스트 생성
#     products = []
#     for product_id in product_repurchase_rate:
#         products.append((product_repurchase_rate[product_id], product_buy_dict[product_id], product_id))
#
#     # 정렬: 재구매율(내림차순), 총 구매 횟수(내림차순), 상품 ID(오름차순)
#     products.sort(key=lambda x: (-x[0], -x[1], x[2]))
#
#     # 정렬된 상품 ID 리스트 생성
#     sorted_products = [pid for _, _, pid in products]
#
#     return sorted_products
#
#
# # 입력 예시
# # records = [
# #     "2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1",
# #     "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3",
# #     "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1",
# #     "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3",
# #     "2020-03-06 uid1 pid4"
# # ]
# # k = 10
# # date = "2020-03-05"
#
# records = [
#     "2020-02-02 uid141 pid141",
#     "2020-02-03 uid141 pid32",
#     "2020-02-04 uid32 pid32",
#     "2020-02-05 uid32 pid141"
# ]
# k = 10
# date = "2020-02-05"
#
# # records = [
# #     "2020-01-01 uid1000 pid5000"
# # ]
# # k = 10
# # date = "2020-01-11"
#
# # 실행
# print(solution(records, k, date))


# records(날짜 사용자id 상품id)#k 재구매 기간 # date 기준 날짜(끝나는 기간)
def solution(records, k, date):
    # "2020-02-02"
    def parse_int_date(date):
        year, month, day = map(str, date.split("-"))
        return int(year + month + day)  # 20200202

    def parse_start_date(k, date):
        start_year, start_month, start_day = map(int, date.split("-"))
        while k > 1:
            k -= 1
            start_day -= 1
            if start_day == 0:
                start_day = 30  # 30일
                start_month -= 1
                if start_month == 0:
                    start_month = 12  # 12개월
                    start_year -= 1
        return int(f"{start_year:04d}{start_month:02d}{start_day:02d}")

    start_date = parse_start_date(k, date)
    end_date = parse_int_date(date)

    period_records = list()
    for record in records:
        record_date, record_user_id, record_product_id = record.split()
        curr_date = parse_int_date(record_date)

        # 시작 기간과 끝나는 기간 사이에 record_int_date
        if start_date <= curr_date and curr_date <= end_date:
            period_records.append((record_user_id, record_product_id))

    if not period_records:
        return ["no result"]
        # 상품을 기준으로 산 유저, 구매, 재구매 정보를 만든

    products_user_dict = dict()
    products_buy_dict = dict()
    products_rebuy_dict = dict()
    for period_user_id, period_product_id in period_records:
        if period_product_id not in products_user_dict:  # 상품 유저 딕셔너리 초기화
            products_user_dict[period_product_id] = set()  # 충복을 허용하지 않고 유저 정보를 저장
            products_buy_dict[period_product_id] = 0
            products_rebuy_dict[period_product_id] = 0

        if period_user_id in products_user_dict[period_product_id]:  # 상품-유저 정보에 상품 key가 존재하면
            products_rebuy_dict[period_product_id] += 1  # 상품 재구매 횟수 추가

        products_user_dict[period_product_id].add(period_user_id)  # 세트에 유저 정보 추가
        products_buy_dict[period_product_id] += 1  # 구매 횟수 추가

    products_rebuy_rate = dict()
    for buy_product_id in products_buy_dict:
        if products_rebuy_dict[buy_product_id] > 1:  # 상품을 구매한 횟수가 1번 이상이면
            rebuy_rate = (products_rebuy_dict[buy_product_id] / len(products_user_dict[buy_product_id])) * 100
        else:
            rebuy_rate = 0
        products_rebuy_rate[buy_product_id] = rebuy_rate

    # 재구매율이 높은 순서, 재구매율이 같을 때 -> 구매 횟수가 많을 때, 총 구매 횟수가 같다면 상품 1d가 낮은 순 정렬
    products_sort = []
    for product_id in products_buy_dict:
        rebuy_rate = products_rebuy_rate[product_id]
        product_number = int(product_id[3:])
        products_sort.append((rebuy_rate, products_buy_dict[product_id], product_number, product_id))

    # 재구매율(내림차순), 구매 횟수(내림차순), 상품 1d 낮은 순(오름차순)
    products_sort.sort(key=lambda x: (-x[0], -x[1], [2]))
    answer = list()
    for _, _, _, product_id in products_sort:
        answer.append(product_id)

    return answer


records = [

    "2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1",
    "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3",
    "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1",
    "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3",
    "2020-03-06 uid1 pid4"
]

k = 10
date = "2020-03-05"

print(solution(records, k, date))

records = [
    "2020-01-01 uid1000 pid5000"
]
k = 10
date = "2020-01-11"

# 실행
print(solution(records, k, date))  # 기대 결과: ["no result"]

records = [
    "2020-02-02 uid141 pid141",
    "2020-02-03 uid141 pid32",
    "2020-02-04 uid32 pid32",
    "2020-02-05 uid32 pid141"
]
k = 10
date = "2020-02-05"

# 실행
print(solution(records, k, date))  # 기대 결과: ["pid32", "pid141"]
