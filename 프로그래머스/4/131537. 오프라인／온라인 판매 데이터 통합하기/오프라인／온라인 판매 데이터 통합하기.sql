-- 코드를 입력하세요
SELECT
    DATE_FORMAT(A.SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
    A.PRODUCT_ID,
    A.USER_ID,
    A.SALES_AMOUNT
FROM (SELECT
            SALES_DATE,
            PRODUCT_ID,
            USER_ID,
            SALES_AMOUNT
        FROM ONLINE_SALE

        UNION ALL

        SELECT
            SALES_DATE,
            PRODUCT_ID,
            NULL AS USER_ID,
            SALES_AMOUNT
        FROM OFFLINE_SALE) A
WHERE SALES_DATE like '2022-03-%'  
# GROUP BY PRODUCT_ID, USER_ID
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC