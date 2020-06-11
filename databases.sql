-- will be using this for the databases

-- will be used to store the settings of each day
create table EnigmaSettings(
Day DATE, PRIMARY KEY,
-- will hold 2 chars: first will be the letter, 2nd what it is being replaced as
plugboard1 varchar(2), 
plugboard2 varchar(2),
plugboard3 varchar(2),
plugboard4 varchar(2),
plugboard5 varchar(2),
plugboard6 varchar(2),
plugboard7 varchar(2),
plugboard8 varchar(2),
plugboard9 varchar(2),
plugboard10 varchar(2),
rotor1 int,
rotor2 int,
rotor3 int,
refelector  varchar(1),
PRIMARY KEY (Day)
);

-- will be used for Bombe
