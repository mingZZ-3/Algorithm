# select A.CAR_ID, A.CAR_TYPE,
#     ROUND((A.DAILY_FEE - (A.DAILY_FEE * C.DISCOUNT_RATE / 100)) * 30) as fee
# from (SELECT * 
#         from CAR_RENTAL_COMPANY_CAR
#         where CAR_TYPE in ('세단', 'SUV')) A
# LEFT JOIN (
#     select CAR_ID, MAX(END_DATE) as END_DATE 
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     group by CAR_ID) B
#     ON A.CAR_ID = B.CAR_ID
# LEFT JOIN (
#     select CAR_TYPE, DISCOUNT_RATE
#     from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
#     where DURATION_TYPE = '30일 이상') C
#     ON A.CAR_TYPE = C.CAR_TYPE
# having (B.END_DATE is NULL or B.END_DATE < '20221101')
#     and fee >= 500000
#     and fee < 2000000
# ORDER BY fee desc, A.car_type asc, A.car_id desc

SELECT CAR_ID, CAR_TYPE, fee
FROM (
    select A.CAR_ID, A.CAR_TYPE, B.END_DATE,
        ROUND((A.DAILY_FEE - (A.DAILY_FEE * C.DISCOUNT_RATE / 100)) * 30) as fee
    from (SELECT * 
            from CAR_RENTAL_COMPANY_CAR
            where CAR_TYPE in ('세단', 'SUV')) A
        LEFT JOIN (
            select CAR_ID, MAX(END_DATE) as END_DATE 
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            group by CAR_ID) B
            ON A.CAR_ID = B.CAR_ID
        LEFT JOIN (
            select CAR_TYPE, DISCOUNT_RATE
            from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
            where DURATION_TYPE = '30일 이상') C
            ON A.CAR_TYPE = C.CAR_TYPE
) X
WHERE (END_DATE IS NULL OR END_DATE < '2022-11-01')
  AND fee BETWEEN 500000 AND 1999999
ORDER BY fee DESC, CAR_TYPE ASC, CAR_ID DESC;