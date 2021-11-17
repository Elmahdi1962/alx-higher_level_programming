-- creates the table unique_id on your MySQL server.
CREATE TABEL IF NOT EXISTS unique_idunique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
);
