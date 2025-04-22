CREATE TABLE IF NOT EXISTS Notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    text TEXT NOT NULL,
    create_at DATETIME NOT NULL
);

INSERT INTO Notes (author, text, create_at)
VALUES ('admin', 'Hello, this is note at admin. Write your first note!', NOW());
