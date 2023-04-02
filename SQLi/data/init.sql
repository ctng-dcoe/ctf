CREATE TABLE users (
  id INT(11) NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO users (username, password) VALUES
  ('admin', 'password'),
  ('bob', 'password'),
  ('jeff', 'password'),
  ('chris', 'password'),
  ('paul', 'password'),
  ('ctcyber{Inj3kt3d}', 'ctcyberfoo');
