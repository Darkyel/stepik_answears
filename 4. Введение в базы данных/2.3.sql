/step/4

SELECT good.name good_name, category.name category_name FROM category_has_good
  INNER JOIN category
    ON category_has_good.category_id = category.id
  INNER JOIN good
    ON category_has_good.good_id = good.id
ORDER BY good_name, category_name;

/step/5

SELECT first_name , last_name, count(sale.id) as new_sale_num  FROM sale 
INNER JOIN client ON sale.client_id = client.id 
INNER JOIN status ON sale.status_id = status.id
WHERE(status.name ='new') 
GROUP BY first_name, last_name;

/step/7

SELECT good.name good_name, category.name category_name
FROM category_has_good 
LEFT JOIN category ON category_has_good.category_id = category.id
RIGHT JOIN good ON category_has_good.good_id = good.id
GROUP BY good_name, category_name;

/step/8

SELECT good.name as good_name, category.name as category_name FROM good
  LEFT OUTER JOIN category_has_good on category_has_good.good_id = good.id
    LEFT OUTER JOIN category on category.id = category_has_good.category_id
UNION
SELECT good.name as good_name, category.name as category_name FROM good
  RIGHT OUTER JOIN category_has_good on category_has_good.good_id = good.id
    RIGHT OUTER JOIN category on category.id = category_has_good.category_id
ORDER BY good_name, category_name;

/step/9

SELECT source.name, sum(sale.sale_sum) FROM source
 LEFT OUTER JOIN client ON source.id = client.source_id
  LEFT OUTER JOIN sale ON client.id = sale.client_id
    GROUP BY source.name;
    
/step/10

SELECT good.name AS good_name FROM good
INNER JOIN category_has_good
  ON good.id = category_has_good.good_id
    INNER JOIN category
    ON
    category_has_good.category_id = category.id
    WHERE category.name = 'Cakes'
UNION
SELECT good.name AS good_name FROM good
INNER JOIN sale_has_good ON good.id = sale_has_good.good_id
    INNER JOIN sale ON sale_has_good.sale_id = sale.id
    INNER JOIN status ON sale.status_id = status.id
    WHERE status.name = 'delivering';
    
/step/11

SELECT category.name AS name, COUNT(sale.id) AS sale_num FROM category
  LEFT OUTER JOIN category_has_good ON category.id = category_has_good.category_id
  LEFT OUTER JOIN good ON category_has_good.good_id = good.id
    LEFT OUTER JOIN sale_has_good ON good.id = sale_has_good.good_id
    LEFT OUTER JOIN sale ON sale_has_good.sale_id = sale.id
    GROUP BY category.name;
    
/step/12

SELECT source.name FROM source
  WHERE NOT EXISTS (SELECT * FROM client WHERE client.source_id = source.id)
UNION
SELECT source.name FROM source
    INNER JOIN client ON client.source_id = source.id
    INNER JOIN sale ON sale.client_id = client.id
    INNER JOIN status ON status.id = sale.status_id WHERE status.name = "rejected";
