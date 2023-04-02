CREATE TABLE customers (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO customers (name, email) VALUES
  ('John Doe', 'john@example.com'),
  ('Jane Doe', 'jane@example.com');
