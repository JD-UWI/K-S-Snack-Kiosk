-- ITEMS TABLE
CREATE TABLE items (
  ID NOT NULL PRIMARY KEY AUTOINCREMENT,
  item_ID VARCHAR(45) NOT NULL IDENTITY(Item101,3),
  item_name VARCHAR(45) NOT NULL ,
  item_qty INTEGER NOT NULL,
  item_cost VARCHAR(45) NOT NULL,
  suplname VARCHAR(45),
  suplemail VARCHAR(45),
);

CREATE INDEX `item_name`
  ON `items` (`item_name`);

-- Example DATA
INSERT INTO "items" VALUES
(NULL,NULL,'Item1',10,101.00,'SupliersRUs','SRUs@email.com'),
(NULL,NULL,'Item2',15,115.23,'SupliersRUs','SRUs@email.com');

-- ITEMS MOVEMENT
CREATE TABLE `item_mvt` (
  mvt_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  item_ID INTEGER,
  mvt_date TEXT,
  mvt_direction VARCHAR(45) NOT NULL,
  mvt_qty INTEGER NOT NULL,
  mvt_notes VARCHAR(45),
);

CREATE INDEX `mvt_direction`
  ON `item_mvt` (`mvt_direction`);