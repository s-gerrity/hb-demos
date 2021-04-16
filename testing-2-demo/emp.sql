BEGIN TRANSACTION;
CREATE TABLE department (
	dept_code VARCHAR(5) NOT NULL, 
	dept VARCHAR(20) NOT NULL, 
	phone VARCHAR(20), 
	PRIMARY KEY (dept_code), 
	UNIQUE (dept)
);
INSERT INTO "department" VALUES('fin','Finance','555-1000');
INSERT INTO "department" VALUES('legal','Legal','555-2222');
INSERT INTO "department" VALUES('mktg','Marketing','555-9999');
CREATE TABLE employee (
	id SERIAL NOT NULL, 
	name VARCHAR(20) NOT NULL, 
	state VARCHAR(2) NOT NULL, 
	dept_code VARCHAR(5), 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(dept_code) REFERENCES department (dept_code)
);
INSERT INTO "employee" VALUES(1,'Leonard','CA','legal');
INSERT INTO "employee" VALUES(2,'Liz','CA','legal');
INSERT INTO "employee" VALUES(3,'Maggie','CA','mktg');
INSERT INTO "employee" VALUES(4,'Nadine','CA',NULL);
COMMIT;
