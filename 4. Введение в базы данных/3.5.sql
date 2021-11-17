/step/6

create table if not exists best_offer_sale
(id integer primary key,
name varchar(255),
dt_start datetime not null,
dt_finish datetime not null)
Engine=InnoDB;

/step/9

ALTER TABLE `client`
  DROP FOREIGN KEY fk_client_source1,
  DROP COLUMN code,
  DROP COLUMN source_id;

/step/10

DROP TABLE source;

/step/11

ALTER TABLE `sale_has_good`
  ADD COLUMN num INT NOT NULL,
  ADD COLUMN price DECIMAL(18,2) NOT NULL;
  
/step/12

ALTER TABLE `client`
  ADD COLUMN source_id INT null,
  ADD CONSTRAINT fk_source_id FOREIGN KEY (source_id) REFERENCES source(id);
