CREATE DATABASE IF NOT EXISTS academia_dev
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE academia_dev;

CREATE TABLE planos (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
valor_mensalidade DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

RENAME TABLE planos TO tabela_planos;

CREATE TABLE tabela_alunos (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
data_matricula DATE NOT NULL,
ativo BOOLEAN DEFAULT 0, -- 1: ativo / 0: inativo
plano_id INT,
FOREIGN KEY (plano_id) REFERENCES tabela_planos(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO tabela_planos (nome, valor_mensalidade)
VALUES
('Mensal', 120.00),
('Trimestral', 99.00),
('Anual', 79.00);

-- SELECT * FROM tabela_planos;

INSERT INTO tabela_alunos (nome, data_matricula, ativo, plano_id)
VALUES
('Bruno Almeida', '2025-01-15', 1, 3),
('Carla Mendes', '2025-02-03', 1, 1),
('Diego Rocha', '2024-11-20', 0, 2),
('Elaine Dias', '2025-03-10', 1, 3),
('Fábio Nunes', '2025-01-28', 1, 1);

-- SELECT * FROM tabela_alunos;