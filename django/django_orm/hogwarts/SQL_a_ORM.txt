INSERT INTO hogwarts_sqlw.Wizard (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');

INSERT INTO hogwarts_sqlw.Wizard (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');

SELECT * FROM hogwarts_sqlw.wizard;

SELECT * FROM hogwarts_sqlw.wizard where id=1;

select * from hogwarts_sqlw.wizard
where house="Gryffindor";

update hogwarts_sqlw.wizard set year='6' where id=1;

-- SELECT * FROM hogwarts_sqlw.wizard;