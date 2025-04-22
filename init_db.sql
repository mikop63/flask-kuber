CREATE DATABASE flask_notes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE flask_notes;

CREATE TABLE Notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    text TEXT NOT NULL,
    create_at DATETIME NOT NULL
);

INSERT INTO Notes (author, text, create_at)
VALUES ('admin', 'Hello, this is note at admin. Write your first note!', NOW());
