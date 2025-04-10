create table conversas(
id INT auto_increment primary key not null,
numero_contato varchar(30) not null,
mensagem_enviada TEXT not null,
resposta_bot TEXT not null
);


INSERT INTO Conversas (numero_contato, mensagem_enviada, resposta_bot)
VALUES ('+55 61 8456-0772', 'Olá, tudo bem?', 'Estou bem, e você?');


SELECT * FROM conversas;
