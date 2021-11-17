-- creates the table unique_id on your MySQL server.
CREATE TABEL IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
