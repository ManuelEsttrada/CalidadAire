                                      
                                      
/*VALUES measure TABLE*/              
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (9,'PM2.5','μg/m³');
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (8,'PM10','μg/m³');
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (7,'Ozone','ppb');
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (2,'Carbone_Monoxide','ppb');
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (12,'Temperature','ºC');
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (3,'Humidity','%');
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (13,'Device_Mode',NULL);
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (1,'Battery','%');
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (1000,'ICARS',NULL);
INSERT INTO measure (idSmability,kindMeasure,units) VALUES (1001,'AQUI',NULL);
                                      
SELECT * FROM measure;                
                                      
/*VALUES user TABLE*/                 
INSERT INTO userdata(username) VALUES ('ADMIN');
INSERT INTO userdata(username) VALUES ('GUEST');
                                      
SELECT * FROM userdata;               
                                      
/*VALUES sensor TABLE*/               
INSERT INTO LocationData (Place,Latitude,Longitude) VALUES ('Universidad Iberoamericana',19.371111,-99.263556);
INSERT INTO LocationData (Place,Latitude,Longitude) VALUES ('Amecameca',19.11666666,-98.76666666);
                                      
SELECT * FROM LocationData;           
                                      
/*VALUES sensor TABLE*/               
INSERT INTO sensor (Alias,Token,DeviceMode,idLocation) VALUES ('IBERO1',1,0,1);
INSERT INTO sensor (Alias,Token,DeviceMode,idLocation) VALUES ('IBERO2',2,0,1);
INSERT INTO sensor (Alias,Token,DeviceMode,idLocation) VALUES ('IBERO4',4,0,2);
                                      
SELECT * FROM sensor;                 

SELECT * FROM report;                 
DELETE FROM Report;                   
ALTER TABLE Report AUTO_INCREMENT = 1;

SELECT * FROM report;                 
DELETE FROM Report;                   
ALTER TABLE Report AUTO_INCREMENT = 1;
