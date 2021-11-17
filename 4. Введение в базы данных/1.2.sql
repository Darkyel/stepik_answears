/step/5

SELECT * FROM billing WHERE payer_email = "vasya@mail.com";

/step/8

INSERT INTO billing(payer_email, recipient_email, sum, currency, billing_date, comment) 
VALUES ('pasha@mail.com', 'katya@mail.com', '300.00', 'EUR', '2016-02-14', 'Valentines day present)');

/step/9

UPDATE billing SET payer_email = 'igor@mail.com' WHERE payer_email = 'alex@mail.com';

/step/10

delete from billing
where ( payer_email ='' or payer_email is null )
or ( recipient_email = '' or recipient_email is null )
