/step/4

SELECT COUNT(project_name) FROM project;

/step/5

SELECT
  category,
  count(product_name)
FROM store
GROUP BY category;

/step/6

SELECT category, sum(price * sold_num) vr FROM store GROUP BY category ORDER by vr DESC LIMIT 5;

/step/7

SELECT count(project_name), sum(budget) , avg(datediff(project_finish, project_start)) FROM project;
