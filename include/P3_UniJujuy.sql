SELECT university,
    career,
    TO_DATE(inscription_date, 'YYYY/MM/DD') AS inscription_date,
    NULL AS first_name,
    nombre AS last_name,
    sexo AS gender,
    birth_date AS age,
    NULL AS postal_code,
    location,
    email
FROM jujuy_utn
WHERE (
        TO_DATE(inscription_date, 'YYYY/MM/DD') BETWEEN '2020/09/01' AND '2021/02/01'
    )
    AND university LIKE '%jujuy';