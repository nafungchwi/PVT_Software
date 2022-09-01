BEGIN TRANSACTION;
CREATE TABLE addresses (
  samples text,
  molecular_weight real,
  specific_gravity real,
  alpha real,
  nitrogen real,
  carbondioxide real,
  hydrogen_sulphide real,
  carbon_one real,
  carbon_two real,
  carbon_three real,
  i_carbon_four real,
  n_carbon_four real,
  i_carbon_five real,
  n_carbon_five real,
  carbon_six real,
  carbon_seven_plus real
  );
INSERT INTO "addresses" VALUES('CCE',235.0,25.3,23.6,2.5,2.1,1.6,15.0,41.0,10.0,23.0,14.0,18.0,17.0,11.0,7.0);
COMMIT;
