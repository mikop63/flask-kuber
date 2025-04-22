CREATE TABLE IF NOT EXISTS Notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    text TEXT NOT NULL,
    filename VARCHAR(255) NULL,
    create_at DATETIME NOT NULL
);

INSERT INTO Notes (author, text, create_at)
VALUES ('admin', 'Hello, this is note at admin. Write your first note!', NOW());
