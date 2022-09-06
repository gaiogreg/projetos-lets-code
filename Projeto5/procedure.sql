CREATE PROCEDURE cadastra_usuario @email VARCHAR(50), @senha VARCHAR(50), @cpf_usuario CHAR(11), @nome_usuario VARCHAR(50), @sobrenome_usuario VARCHAR(50), @numero_telefone CHAR(12), @data_nascimento DATE, @usuario_id INT AS INSERT INTO usuarios(senha_usuario,email_usuario)   VALUES(@senha,@email); 
SET @usuario_id = SCOPE_IDENTITY(); INSERT INTO dados_pessoais(cpf_usuario,nome_usuario,sobrenome_usuario,numero_telefone,data_nascimento,usuario_id) VALUES(@cpf_usuario,@nome_usuario,@sobrenome_usuario,@numero_telefone,@data_nascimento,@usuario_id); 
GO
