SELECT  
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
    and CAR_ID in (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
                GROUP BY CAR_ID
                HAVING COUNT(*) >= 5)
GROUP BY car_id, MONTH(START_DATE)
HAVING RECORDS > 0
ORDER BY MONTH ASC, CAR_ID DESC