--CREATE DATABASE maryflixdb;

USE maryflixdb

CREATE TABLE usuarios (
    usuario_id INT IDENTITY (1,1) PRIMARY KEY,
    senha_usuario VARCHAR(50) NOT NULL,
    email_usuario VARCHAR(50) NOT NULL,
);

CREATE TABLE planos(
    plano_id INT IDENTITY (1,1) PRIMARY KEY,
    plano_nome VARCHAR(15) NOT NULL,
    valor_plano FLOAT NOT NULL,
    quantidade_telas INT NOT NULL,
    resolucao_maxima VARCHAR(10) NOT NULL,
    meses_duracao_plano INT NOT NULL
);

CREATE TABLE contratos(
    contrato_id INT IDENTITY (1,1) PRIMARY KEY,
    usuario_id INT FOREIGN KEY REFERENCES usuarios(usuario_id),
    plano_id INT FOREIGN KEY REFERENCES planos(plano_id),
    vigencia_plano DATE,
    data_cobranca INT,
    status_contrato BIT
);

CREATE TABLE pagamentos(
    pagamento_id INT IDENTITY (1,1) PRIMARY KEY,
    contrato_id INT FOREIGN KEY REFERENCES contratos(contrato_id),
    forma_pagamento VARCHAR(50) NOT NULL,
    data_pagamento DATETIME NOT NULL,
    valor_pago FLOAT NOT NULL
);

CREATE TABLE titulos(
    titulo_id INT IDENTITY (1,1) PRIMARY KEY,
    nome_titulo VARCHAR(255) NOT NULL,
    tempo_duracao INT,
    elenco VARCHAR(255),
    direcao VARCHAR(255),
    pais VARCHAR(255),
    produtora VARCHAR(255),
    idioma VARCHAR(255),
    data_estreia DATE
);

CREATE TABLE historico_clientes (
    id_historico INT IDENTITY (1,1) PRIMARY KEY,
    usuario_id INT FOREIGN KEY REFERENCES usuarios(usuario_id),
    titulo_id INT FOREIGN KEY REFERENCES titulos(titulo_id),
    pedido_datetime DATETIME,
    tipo_pedido BIT
    );

CREATE TABLE avaliacoes(
    avaliacao_id INT IDENTITY (1,1) PRIMARY KEY,
    usuario_id INT FOREIGN KEY REFERENCES usuarios(usuario_id),
    titulo_id INT FOREIGN KEY REFERENCES titulos(titulo_id),
    pontuacao INT,
    data_avaliacao DATETIME
);

CREATE TABLE dados_pessoais (
    cpf_usuario CHAR(11) PRIMARY KEY,
    nome_usuario VARCHAR(50) NOT NULL,
    sobrenome_usuario VARCHAR(50) NOT NULL,
    numero_telefone CHAR(12),
    data_nascimento DATE,
    usuario_id INT FOREIGN KEY REFERENCES usuarios(usuario_id)
);

-- POPULANDO O BANCO DE DADOS

INSERT INTO usuarios (senha_usuario, email_usuario)
VALUES
('banana123', 'mariana_banana@gmail.com'),
('abacaxi321', 'greg_abacaxi@gmail.com'),
('arrozcomfeijao123', 'joao_pe_de_feijao@gmail.com'),
('joaquina123', 'maria_joaquina@gmail.com'),
('avassalador321', 'avassaladores@gmail.com'),
('guigojunior123', 'guigo_junior@gmail.com'),
('ademar456', 'ademar_silva@hotmail..com'),
('rogerio654', 'rogerio_carlos@outlook.com'),
('andressa123', 'andressa_mor@outlook.com'),
('marquinhos789', 'marcos_2@outlook.com'),
('larissa321', 'lari.amorzinho@outlook.com'),
('roger654', 'roger@outlook.com'),
('maria!123', 'maria23@gmail.com'),
('senhaaa', 'felipe_assis@gmail.com'),
('danilosoares15', 'danilo@gmail.com');

INSERT INTO dados_pessoais(cpf_usuario, nome_usuario, sobrenome_usuario, numero_telefone, data_nascimento, usuario_id)
VALUES (12345678901, 'Mariana', 'Moutinho', '011970707070', '1994-05-20', 1),
(23456789012, 'Greg', 'Gaio', '019970707070', '1997-04-09', 2),
(98765432109, 'Joao', 'Ferraz', '011987654321', '1994-06-26', 3),
(55522233388, 'Maria', 'Joaquina', '011965778924', '1990-10-27', 4),
(23456787777, 'Ava', 'Salador', '019966332244', '1999-04-09', 5),
(98765432559, 'Guilherme', 'Santos', '011987658888', '1993-07-16', 6),
(15258147931, 'Ademar', 'Guia', '032854784736', '1987-02-24', 7),
(13579792837, 'Rogerio', 'Miranda', '022237685746', '1985-07-11', 8),
(66665432109, 'Andressa', 'Lira', '011987645622', '1990-12-01', 9),
(48574629381, 'Marcos', 'Lima', '051987485746', '1981-02-23', 10),
(85730485731, 'Larissa', 'Manoela', '031976475648', '1975-12-05', 11),
(74296049872, 'Roger', 'Guedes', '081912385736', '1981-09-23', 12),
(15384756931, 'Maria', 'Lucia', '021943702270', '1992-03-11', 13),
(58999999837, 'Felipe', 'Assis', '041943723070', '1990-02-23', 14),
(13748577772, 'Danilo', 'Soares', '018985543321', '1996-11-10', 15);

INSERT INTO titulos(nome_titulo, tempo_duracao, elenco, direcao, pais, produtora, idioma, data_estreia)
VALUES
('Harry Potter and the Philosopher''s Stone', 152, 'Daniel Radcliffe, Rupert Grint, Emma Watson, John Cleese, Robbie Coltrane, Warwick Davis', 'Chris Columbus', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2001-11-04'),
('Harry Potter and the Chamber of Secrets', 161, 'Daniel Radcliffe, Rupert Grint, Emma Watson, Kenneth Branagh, John Cleese, Robbie Coltrane', 'Chris Columbus', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2002-11-03'),
('Harry Potter and the Prisoner of Azkaban', 142, 'Daniel Radcliffe, Rupert Grint, Emma Watson, Robbie Coltrane, Michael Gambon, Richard Griffiths', 'Alfonso Cuarón', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2004-05-23'),
('Harry Potter and the Goblet of Fire', 157, 'Daniel Radcliffe, Rupert Grint, Emma Watson, Robbie Coltrane, Ralph Fiennes, Michael Gambon', 'Mike Newell', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2005-11-06'),
('Harry Potter and the Order of the Phoenix', 138, 'Daniel Radcliffe, Rupert Grint, Emma Watson, Helena Bonham Carter, Robbie Coltrane, Warwick Davis', 'David Yates', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2007-06-28'),
('Harry Potter and the Half-Blood Prince', 153, 'Daniel Radcliffe, Rupert Grint, Emma Watson, Jim Broadbent, Helena Bonham Carter, Robbie Coltrane', 'David Yates', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2009-07-07'),
('Harry Potter and the Deathly Hallows – Part 1', 146, 'Daniel Radcliffe, Rupert Grint, Emma Watson, Helena Bonham Carter, Robbie Coltrane, Warwick Davis', 'David Yates', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2010-11-11'),
('Harry Potter and the Deathly Hallows – Part 2', 130, 'Daniel Radcliffe, Rupert Grint, Emma Watson, Helena Bonham Carter, Robbie Coltrane, Warwick Davis', 'David Yates', 'United Kingdom, United States', 'Warner Bros. Pictures', 'English', '2011-07-07');


INSERT INTO avaliacoes(usuario_id, titulo_id, pontuacao, data_avaliacao)
VALUES
 (1, 1, 2, '2022-08-16 17:23:15')
,(1, 3, 4, '2022-08-16 20:14:11')
,(2, 1, 3, '2022-04-16 10:30:23')
,(2, 2, 4, '2022-02-22 14:10:50')
,(3, 1, 4, '2021-09-10 12:40:25')
,(3, 2, 4, '2020-10-22 14:55:08')
;

INSERT INTO historico_clientes (usuario_id, titulo_id, pedido_datetime, tipo_pedido)
VALUES
(1, 1, '2022-08-16 09:25:02', 1),
(1, 1, '2022-08-16 12:17:01', 0),
(2, 2, '2022-02-22 07:10:10', 1),
(2, 2, '2022-02-22 09:20:02', 0),
(3, 1, '2021-09-10 10:00:02', 1),
(3, 1, '2021-09-10 12:25:10', 0);

INSERT INTO planos(plano_nome, valor_plano, quantidade_telas, resolucao_maxima, meses_duracao_plano)
VALUES
('BASICO MENSAL', 15.99, 1, 'FHD', 1),
('BASICO ANUAL', 149.99, 1, 'FHD', 12),
('PREMIUM MENSAL', 39.99, 4, '4K', 1),
('PREMIUM ANUAL', 349.99, 4, '4K', 12);

INSERT INTO contratos(usuario_id, plano_id, vigencia_plano, data_cobranca, status_contrato)
VALUES
(1, 1, '2022-09-16', 5, 1),
(2, 3, '2022-09-01', 15, 1),
(3, 4, '2023-02-01', 10, 1),
(3, 1, '2022-01-29', 10, 0),
(4, 3, '2022-12-25', 15, 1),
(5, 2, '2023-08-10', 12, 1),
(6, 1, '2022-09-10', 12, 1),
(7, 4, '2023-07-10', 7, 1),
(8, 3,'2022-12-10', 10, 1),
(9, 3,'2023-07-13' , 05, 1),
(10, 4,'2022-08-22' , 25, 1),
(11, 2,'2023-08-11' , 20, 1),
(12, 3, '2022-09-12', 10, 1),
(13, 4, '2023-05-23', 15, 1),
(14, 2, '2022-09-06', 10, 1),
(15, 4, '2023-04-11', 05, 1);

INSERT INTO pagamentos(contrato_id, forma_pagamento, data_pagamento, valor_pago)
VALUES
(1, 'BOLETO', '2022-08-05', 15.99),
(2, 'DEBITO AUTOMATICO','2022-07-15', 39.99),
(3, 'BOLETO','2022-02-13', 366.66),
(4, 'PIX', '2022-01-10', 15.99),
(5, 'DEBITO AUTOMATICO', '2022-06-12', 15.99),
(6, 'PIX','2023-09-03', 50.00),
(7, 'BOLETO','2022-02-13', 367.66),
(8, 'PIX', '2022-07-07', 349.99), 
(9, 'BOLETO','2022-11-10', 39.99), 
(10, 'BOLETO','2022-08-05', 39.99),
(11, 'BOLETO', '2022-05-08', 15.99),
(12, 'CARTAO DE CREDITO', '2022-12-08', 149.99),
(13, 'DEBITO AUTOMATICO', '2022-10-10', 39.99),
(14, 'DEBITO AUTOMATICO', '2022-08-25', 349.99),
(15, 'PIX','2022-06-11', 150.00),
(16, 'BOLETO','2022-05-13', 360.00);
