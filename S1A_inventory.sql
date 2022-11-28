-- ITEMS TABLE
CREATE TABLE items (
  item_name TEXT NOT NULL,
  item_ID TEXT,
  item_qty INTEGER NOT NULL,
  item_cost TEXT NOT NULL,
  suplname TEXT,
  suplemail TEXT,
  PRIMARY KEY("item_ID")
);

CREATE INDEX `item_name`
  ON `items` (`item_name`);

-- Example DATA
INSERT INTO "items" VALUES
('Item','ID#','10','$123','SupliersRUs','SRUs@email.com'),
('Item','ID#2','10','$123','SupliersRUs','SRUs@email.com');

-- ITEMS MOVEMENT
CREATE TABLE `item_mvt` (
  item_ID TEXT,
  mvt_date TEXT,
  mvt_direction TEXT NOT NULL,
  mvt_qty INTEGER NOT NULL,
  mvt_notes TEXT,
  PRIMARY KEY("item_ID", "mvt_date")
);

CREATE INDEX `mvt_direction`
  ON `item_mvt` (`mvt_direction`);