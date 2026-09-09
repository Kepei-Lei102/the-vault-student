"""Every SQL statement in the SQL card, run for real.

Builds the databases from the past papers in an in-memory SQLite database
(the engine inside every phone), runs each paper's query, and prints what
comes back. Run it: python3 sql-worked-examples.py
"""
import sqlite3

db = sqlite3.connect(":memory:")
cur = db.cursor()
cur.execute("PRAGMA foreign_keys = ON;")   # referential integrity: off by default in SQLite, on in this script

def run(title, sql):
    print(f"\n-- {title}\n{sql.strip()}")
    cur.execute(sql)
    rows = cur.fetchall()
    if cur.description:
        print("   columns:", [d[0] for d in cur.description])
        for r in rows:
            print("  ", r)
    return rows

# ---------- DDL: June 2023 Paper 11 Q2(b)(iii) — define BIRD_TYPE ----------
cur.executescript("""
CREATE TABLE BIRD_TYPE(
    BirdID  CHAR(4) NOT NULL,
    Name    VARCHAR(20),
    Size    VARCHAR(6),
    PRIMARY KEY (BirdID)
);
CREATE TABLE PERSON(
    PersonID     VARCHAR(6) NOT NULL,
    FirstName    VARCHAR(20),
    LastName     VARCHAR(20),
    EmailAddress VARCHAR(50),
    PRIMARY KEY (PersonID)
);
CREATE TABLE BIRD_SEEN(
    SeenID   INTEGER NOT NULL,
    BirdID   CHAR(4),
    Date     DATE,
    Location VARCHAR(30),
    PersonID VARCHAR(6),
    PRIMARY KEY (SeenID),
    FOREIGN KEY (BirdID)   REFERENCES BIRD_TYPE(BirdID),
    FOREIGN KEY (PersonID) REFERENCES PERSON(PersonID)
);
INSERT INTO BIRD_TYPE VALUES ('0123','Blackbird','Medium'),('0035','Jay','Large'),
                             ('0004','Raven','Large'),('0085','Robin','Small');
INSERT INTO PERSON VALUES ('J_123','Jun','Li','jun@example.com'),('A_007','Ana','Ruiz','ana@example.com');
INSERT INTO BIRD_SEEN VALUES
  (1,'0123','2023-04-01','Park','J_123'),
  (2,'0035','2023-04-02','Wood','J_123'),
  (3,'0004','2023-04-02','Cliff','J_123'),
  (4,'0085','2023-04-03','Garden','A_007'),
  (5,'0085','2023-04-05','Garden','J_123');
""")

run("J23/11 Q2(b)(iv) — count by size for person J_123 (scheme's comma-join form)", """
SELECT BIRD_TYPE.Size, COUNT(BIRD_TYPE.BirdID) AS NumberOfBirds
FROM BIRD_TYPE, BIRD_SEEN
WHERE BIRD_SEEN.PersonID = 'J_123'
AND BIRD_TYPE.BirdID = BIRD_SEEN.BirdID
GROUP BY BIRD_TYPE.Size;
""")
run("same query, INNER JOIN form", """
SELECT BIRD_TYPE.Size, COUNT(BIRD_TYPE.BirdID) AS NumberOfBirds
FROM BIRD_TYPE INNER JOIN BIRD_SEEN ON BIRD_TYPE.BirdID = BIRD_SEEN.BirdID
WHERE BIRD_SEEN.PersonID = 'J_123'
GROUP BY BIRD_TYPE.Size;
""")

# ---------- Nov 2021 Paper 12 Q6 — PLANTSALES ----------
cur.executescript("""
CREATE TABLE PLANT(PlantName VARCHAR(30) PRIMARY KEY, QuantityInStock INTEGER, Cost REAL);
CREATE TABLE CUSTOMER(CustomerID VARCHAR(6) PRIMARY KEY, FirstName VARCHAR(20), LastName VARCHAR(20), Address VARCHAR(60), Email VARCHAR(50));
CREATE TABLE PURCHASE(PurchaseID VARCHAR(6) PRIMARY KEY, CustomerID VARCHAR(6), FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID));
CREATE TABLE PURCHASE_ITEM(PurchaseID VARCHAR(6), PlantName VARCHAR(30), Quantity INTEGER,
    PRIMARY KEY (PurchaseID, PlantName),
    FOREIGN KEY (PurchaseID) REFERENCES PURCHASE(PurchaseID),
    FOREIGN KEY (PlantName) REFERENCES PLANT(PlantName));
INSERT INTO PLANT VALUES ('Rose',40,4.50),('Lavender',80,2.20),('Fern',15,6.00);
INSERT INTO CUSTOMER VALUES ('C001','Mei','Chen','1 Jinli Rd','mei@example.com');
INSERT INTO PURCHASE VALUES ('3011A','C001'),('3012B','C001');
INSERT INTO PURCHASE_ITEM VALUES ('3011A','Rose',3),('3011A','Lavender',10),('3012B','Fern',1);
""")
run("N21/12 Q6(c)(i) — total items in purchase 3011A", """
SELECT SUM(Quantity)
FROM PURCHASE_ITEM
WHERE PurchaseID = '3011A';
""")
run("N21/12 Q6(c)(ii) — DDL: add an order-date field", "ALTER TABLE PURCHASE ADD OrderDate DATE;")
run("check the new column exists", "SELECT * FROM PURCHASE;")

# ---------- June 2024 Paper 11 Q6(c) — FARMING ----------
cur.executescript("""
CREATE TABLE PLAYER(PlayerID CHAR(6) PRIMARY KEY, Name VARCHAR(20));
CREATE TABLE EVENT(PlayerID CHAR(6), EventID INTEGER, Category VARCHAR(10), Points INTEGER);
INSERT INTO PLAYER VALUES ('000123','Ada'),('000124','Bo'),('000125','Cy');
INSERT INTO EVENT VALUES ('000123',3,'Build',100),('000124',1,'Grow',36),('000123',4,'Grow',22),
                         ('000123',7,'Create',158),('000125',3,'Grow',85),('000125',4,'Build',69);
""")
run("J24/11 Q6(c)(ii) — events completed per player", """
SELECT PlayerID, COUNT(EventID)
FROM EVENT
GROUP BY PlayerID;
""")

# ---------- Nov 2025 Paper 12 Q4 — SHIPPING ----------
cur.executescript("""
CREATE TABLE SHIP(ShipID CHAR(4) PRIMARY KEY, Type VARCHAR(10), Capacity INTEGER, ShipName VARCHAR(20));
CREATE TABLE CONTAINER(ContainerID CHAR(6) PRIMARY KEY, Type VARCHAR(10), Weight REAL, OwnerName VARCHAR(30), ShipID CHAR(4),
    FOREIGN KEY (ShipID) REFERENCES SHIP(ShipID));
INSERT INTO SHIP VALUES ('S001','Feeder',800,'Caledonia'),('S002','Panamax',4000,'Ideal-X');
INSERT INTO CONTAINER VALUES ('C10001','Dry',12.5,'Acme','S001'),('C10002','Reefer',18.0,'Acme','S001'),
                             ('C10003','Dry',9.0,'Zed','S002'),('C10004','Tank',22.0,'Zed','S001');
""")
run("N25/12 Q4(c) — containers on the ship named Caledonia", """
SELECT COUNT(ContainerID)
FROM CONTAINER INNER JOIN SHIP ON CONTAINER.ShipID = SHIP.ShipID
WHERE ShipName = 'Caledonia';
""")
run("N25/12 Q4(b) — DDL: last-inspection date", "ALTER TABLE CONTAINER ADD InspectionDate DATE;")

# ---------- Nov 2024 Paper 13 Q4(b) — ICECREAM ----------
cur.executescript("""
CREATE TABLE SALE(SaleID INTEGER PRIMARY KEY, BatchID VARCHAR(6), CustomerID VARCHAR(6), Quantity INTEGER, Date DATE);
INSERT INTO SALE VALUES (1,'KlV12','0034E',20,'2023-03-01'),(2,'RlC14','0034E',5,'2023-11-30'),
                        (3,'TYL1','0034E',8,'2024-01-04'),(4,'KlV12','0099A',50,'2023-06-06');
""")
run("N24/13 Q4(b) — total sold to 0034E in 2023 (ISO dates; the scheme's #dd/mm/yyyy# is Access syntax)", """
SELECT SUM(Quantity)
FROM SALE
WHERE CustomerID = '0034E'
AND Date >= '2023-01-01' AND Date <= '2023-12-31';
""")

# ---------- IGCSE 0478: Nov 2024 Paper 23 Q11 — BuildStock ----------
cur.executescript("""
CREATE TABLE BuildStock(MtNo CHAR(4) PRIMARY KEY, Name VARCHAR(20), InStock BOOLEAN, WeightKg INTEGER, PricePerBag REAL, NumberBags INTEGER);
INSERT INTO BuildStock VALUES
 ('MT01','Builders sand',1,50,4.50,50),('MT02','Sharp sand',1,25,3.50,21),('MT03','Red sand',0,50,2.75,0),
 ('MT04','Cement',0,25,6.85,0),('MT05','Chippings',1,50,35.00,50),('MT06','Cobbles',0,75,67.35,0),
 ('MT07','Pebbles small',1,50,34.50,3),('MT08','Pebbles medium',1,25,25.50,10),('MT12','Pebbles large',1,75,62.75,20),
 ('MT15','Washed gravel',1,50,12.75,12),('MT16','Pea gravel',1,100,15.95,24);
""")
run("0478 N24/23 Q11(a) — 75 kg bags, cheapest first", """
SELECT MtNo, Name
FROM BuildStock
WHERE WeightKg = 75
ORDER BY PricePerBag;
""")
run("0478 N24/23 Q11(b)(i) — out of stock", """
SELECT Name
FROM BuildStock
WHERE InStock = FALSE;
""")
run("the same information from a different field", "SELECT Name FROM BuildStock WHERE NumberBags = 0;")

# ---------- IGCSE 0478: Nov 2023 Paper 23 Q9 — PheasantList ----------
cur.executescript("""
CREATE TABLE PheasantList(Species VARCHAR(30) PRIMARY KEY, Description VARCHAR(60), NumberBirds INTEGER, Breeding BOOLEAN, Young INTEGER);
INSERT INTO PheasantList VALUES
 ('Edwards','blue-black with white tail',5,1,2),('Japanese green','dark green with pale grey tail',2,1,0),
 ('Reeves','golden, white and red scaled plumage',4,1,3),('Crawfords Kalij','glossy blue-black plumage',4,0,0),
 ('Crested fireback','blue-black with black tail',3,0,0),('True silver','white laced top half and black lower half',7,1,4),
 ('Siamese fireback','grey plumage with crimson legs and feet',5,0,0),('Mikado','iridescent plumage with white striped wings',3,1,0),
 ('Red junglefowl','many colours',2,1,1),('Himalayan monal','many colours with metallic green crest',3,1,0),
 ('White eared','white with ear tufts',5,1,2),('Brown eared','brown with ear tufts',9,1,5),
 ('Ring necked','long tail with white ring neck',2,1,1),('Golden','rainbow coloured',3,1,0);
""")
run("0478 N23/23 Q9(c) — more than six birds", """
SELECT Species, Description
FROM PheasantList
WHERE NumberBirds > 6;
""")
run("0478 N23/23 Q9(d) — breeding but no young this year", """
SELECT Species
FROM PheasantList
WHERE Breeding = TRUE AND Young = 0;
""")

# ---------- The statements every app runs ----------
run("INSERT — a new sighting", "INSERT INTO BIRD_SEEN VALUES (6,'0035','2023-05-01','Wood','A_007');")
run("UPDATE — correct a location", "UPDATE BIRD_SEEN SET Location = 'Old Wood' WHERE SeenID = 6;")
run("DELETE — remove it again", "DELETE FROM BIRD_SEEN WHERE SeenID = 6;")
run("nested query — people who have seen a Large bird", """
SELECT DISTINCT PersonID
FROM BIRD_SEEN
WHERE BirdID IN (SELECT BirdID FROM BIRD_TYPE WHERE Size = 'Large');
""")
try:
    cur.execute("INSERT INTO BIRD_SEEN VALUES (7,'9999','2023-05-02','Nowhere','J_123');")
except sqlite3.IntegrityError as e:
    print("\n-- inserting a sighting of BirdID 9999 (no such bird):", e)

db.commit()
