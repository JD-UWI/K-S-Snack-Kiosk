-- ITEMS TABLE
CREATE TABLE items (
  ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  item_ID VARCHAR(45) NOT NULL,
  item_name VARCHAR(45),
  item_qty INTEGER NOT NULL,
  item_cost FLOAT NOT NULL,
  suplname VARCHAR(45),
  suplemail VARCHAR(45)
);

CREATE INDEX `item_name`
  ON `items` (`item_name`);

-- Example DATA
INSERT INTO "items" VALUES
(NULL,'ID#','Item1',10,101.00,'SupliersRUs','SRUs@email.com'),
(NULL,'ID#2','Item2',15,115.23,'SupliersRUs','SRUs@email.com');


  -- NOTIFICATIONS TABLE
CREATE TABLE notifications (
  notif_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  notif VARCHAR(45) DEFAULT 'Notification',
  val INTEGER NOT NULL
);


-- Example DATA
INSERT INTO "notifications" VALUES
(NULL,'Notification',20),
(NULL,'This is a notification', 30);

