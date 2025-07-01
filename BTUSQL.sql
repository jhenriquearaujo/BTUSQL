
CREATE TABLE Funcao (
    FuncaoID INT PRIMARY KEY,
    DescricaoFuncao VARCHAR(100) NOT NULL
);


CREATE TABLE Contratante (
    CNPJ VARCHAR(18) PRIMARY KEY,
    NomeEstabelecimento VARCHAR(100),
    Telefone VARCHAR(20),
    Endereco VARCHAR(200),
    NomeResponsavel VARCHAR(100),
    TipoEstabelecimento VARCHAR(50)
);


CREATE TABLE Freelancer (
    CPF CHAR(11) PRIMARY KEY,
    Nome VARCHAR(100),
    Telefone VARCHAR(20),
    FuncaoID INT,
    Disponibilidade VARCHAR(50),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID)
);


CREATE TABLE Valor_Diaria_Hora (
    ValorID INT PRIMARY KEY,
    FuncaoID INT,
    Tipo VARCHAR(10), 
    Valor DECIMAL(10,2),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID)
);


CREATE TABLE Agendamento (
    AgendamentoID INT PRIMARY KEY,
    CNPJ VARCHAR(18),
    CPF CHAR(11),
    Data DATE,
    HoraInicio TIME,
    HoraFim TIME,
    Modalidade VARCHAR(10), 
    FuncaoID INT,
    Status VARCHAR(20),
    FOREIGN KEY (CNPJ) REFERENCES Contratante(CNPJ),
    FOREIGN KEY (CPF) REFERENCES Freelancer(CPF),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID)
);

CREATE TABLE Pagamento (
    PagamentoID INT PRIMARY KEY,
    CNPJ VARCHAR(18),
    CPF CHAR(11),
    FuncaoID INT,
    ValorID INT,
    DataPagamento DATE,
    Modalidade VARCHAR(10), 
    MetodoPagamento VARCHAR(20), 
    ValorCalculado DECIMAL(10,2),
    FOREIGN KEY (CNPJ) REFERENCES Contratante(CNPJ),
    FOREIGN KEY (CPF) REFERENCES Freelancer(CPF),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID),
    FOREIGN KEY (ValorID) REFERENCES Valor_Diaria_Hora(ValorID)
);


CREATE TABLE Funcao (
    FuncaoID INT PRIMARY KEY,
    DescricaoFuncao VARCHAR(100) NOT NULL
);


CREATE TABLE Contratante (
    CNPJ VARCHAR(18) PRIMARY KEY,
    NomeEstabelecimento VARCHAR(100),
    Telefone VARCHAR(20),
    Endereco VARCHAR(200),
    NomeResponsavel VARCHAR(100),
    TipoEstabelecimento VARCHAR(50)
);


CREATE TABLE Freelancer (
    CPF CHAR(11) PRIMARY KEY,
    Nome VARCHAR(100),
    Telefone VARCHAR(20),
    FuncaoID INT,
    Disponibilidade VARCHAR(50),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID)
);


CREATE TABLE Valor_Diaria_Hora (
    ValorID INT PRIMARY KEY,
    FuncaoID INT,
    Tipo VARCHAR(10), 
    Valor DECIMAL(10,2),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID)
);


CREATE TABLE Agendamento (
    AgendamentoID INT PRIMARY KEY,
    CNPJ VARCHAR(18),
    CPF CHAR(11),
    Data DATE,
    HoraInicio TIME,
    HoraFim TIME,
    Modalidade VARCHAR(10), 
    FuncaoID INT,
    Status VARCHAR(20),
    FOREIGN KEY (CNPJ) REFERENCES Contratante(CNPJ),
    FOREIGN KEY (CPF) REFERENCES Freelancer(CPF),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID)
);

CREATE TABLE Pagamento (
    PagamentoID INT PRIMARY KEY,
    CNPJ VARCHAR(18),
    CPF CHAR(11),
    FuncaoID INT,
    ValorID INT,
    DataPagamento DATE,
    Modalidade VARCHAR(10), 
    MetodoPagamento VARCHAR(20), 
    ValorCalculado DECIMAL(10,2),
    FOREIGN KEY (CNPJ) REFERENCES Contratante(CNPJ),
    FOREIGN KEY (CPF) REFERENCES Freelancer(CPF),
    FOREIGN KEY (FuncaoID) REFERENCES Funcao(FuncaoID),
    FOREIGN KEY (ValorID) REFERENCES Valor_Diaria_Hora(ValorID)
);

INSERT INTO Funcao VALUES (1, 'Garçom');
INSERT INTO Funcao VALUES (2, 'Cozinheiro');
INSERT INTO Funcao VALUES (3, 'Auxiliar de Cozinha');
INSERT INTO Funcao VALUES (4, 'Barista');
INSERT INTO Funcao VALUES (5, 'Chapeiro');
INSERT INTO Funcao VALUES (6, 'Limpeza');
INSERT INTO Funcao VALUES (7, 'Caixa');
INSERT INTO Funcao VALUES (8, 'Atendente');
INSERT INTO Funcao VALUES (9, 'Recepcionista');
INSERT INTO Funcao VALUES (10, 'Segurança');

INSERT INTO Contratante VALUES ('12345678000101', 'Bar do Zé', '44999990001', 'Rua das Flores, 100', 'José Silva', 'Bar');
INSERT INTO Contratante VALUES ('23456789000102', 'Lanchonete Sabor', '44999990002', 'Av. Brasil, 200', 'Ana Costa', 'Lanchonete');
INSERT INTO Contratante VALUES ('34567890000103', 'Restaurante Bom Gosto', '44999990003', 'Rua Central, 300', 'Carlos Lima', 'Restaurante');
INSERT INTO Contratante VALUES ('45678901000104', 'Burguer Master', '44999990004', 'Av. Paraná, 400', 'Maria Souza', 'Lanchonete');
INSERT INTO Contratante VALUES ('56789012000105', 'Pizzaria Massa Fina', '44999990005', 'Rua Itália, 500', 'Paulo Rocha', 'Restaurante');
INSERT INTO Contratante VALUES ('67890123000106', 'Churrasquinho do João', '44999990006', 'Rua Chile, 600', 'João Santos', 'Bar');
INSERT INTO Contratante VALUES ('78901234000107', 'Doce Sabor', '44999990007', 'Av. Getúlio Vargas, 700', 'Helena Dias', 'Restaurante');
INSERT INTO Contratante VALUES ('89012345000108', 'Boteco Central', '44999990008', 'Rua Goiás, 800', 'Roberto Alves', 'Bar');
INSERT INTO Contratante VALUES ('90123456000109', 'Pastel da Feira', '44999990009', 'Rua Pernambuco, 900', 'Juliana Torres', 'Lanchonete');
INSERT INTO Contratante VALUES ('01234567000110', 'Restaurante Bela Mesa', '44999990010', 'Av. Curitiba, 1000', 'Bruno Cardoso', 'Restaurante');

INSERT INTO Freelancer VALUES ('11111111111', 'Carlos Martins', '44999880001', 1, 'Noite');
INSERT INTO Freelancer VALUES ('22222222222', 'Ana Beatriz', '44999880002', 2, 'Tarde');
INSERT INTO Freelancer VALUES ('33333333333', 'Ricardo Silva', '44999880003', 3, 'Integral');
INSERT INTO Freelancer VALUES ('44444444444', 'Juliana Costa', '44999880004', 4, 'Manhã');
INSERT INTO Freelancer VALUES ('55555555555', 'Fernando Lima', '44999880005', 5, 'Noite');
INSERT INTO Freelancer VALUES ('66666666666', 'Camila Duarte', '44999880006', 6, 'Integral');
INSERT INTO Freelancer VALUES ('77777777777', 'Paulo Henrique', '44999880007', 7, 'Tarde');
INSERT INTO Freelancer VALUES ('88888888888', 'Luciana Borges', '44999880008', 8, 'Manhã');
INSERT INTO Freelancer VALUES ('99999999999', 'Tiago Menezes', '44999880009', 9, 'Noite');
INSERT INTO Freelancer VALUES ('00000000000', 'Marina Oliveira', '44999880010', 10, 'Integral');

INSERT INTO Valor_Diaria_Hora VALUES (1, 1, 'hora', 20.00);
INSERT INTO Valor_Diaria_Hora VALUES (2, 1, 'diaria', 160.00);
INSERT INTO Valor_Diaria_Hora VALUES (3, 2, 'hora', 25.00);
INSERT INTO Valor_Diaria_Hora VALUES (4, 2, 'diaria', 200.00);
INSERT INTO Valor_Diaria_Hora VALUES (5, 3, 'hora', 18.00);
INSERT INTO Valor_Diaria_Hora VALUES (6, 3, 'diaria', 140.00);
INSERT INTO Valor_Diaria_Hora VALUES (7, 4, 'hora', 22.00);
INSERT INTO Valor_Diaria_Hora VALUES (8, 5, 'diaria', 180.00);
INSERT INTO Valor_Diaria_Hora VALUES (9, 6, 'hora', 15.00);
INSERT INTO Valor_Diaria_Hora VALUES (10, 7, 'hora', 17.00);

INSERT INTO Agendamento VALUES (1, '12345678000101', '11111111111', '2025-07-01', '18:00:00', '23:00:00', 'hora', 1, 'confirmado');
INSERT INTO Agendamento VALUES (2, '23456789000102', '22222222222', '2025-07-02', '12:00:00', '18:00:00', 'diaria', 2, 'pendente');
INSERT INTO Agendamento VALUES (3, '34567890000103', '33333333333', '2025-07-03', '10:00:00', '16:00:00', 'hora', 3, 'confirmado');
INSERT INTO Agendamento VALUES (4, '45678901000104', '44444444444', '2025-07-04', '08:00:00', '14:00:00', 'hora', 4, 'confirmado');
INSERT INTO Agendamento VALUES (5, '56789012000105', '55555555555', '2025-07-05', '17:00:00', '23:00:00', 'diaria', 5, 'cancelado');
INSERT INTO Agendamento VALUES (6, '67890123000106', '66666666666', '2025-07-06', '14:00:00', '20:00:00', 'hora', 6, 'confirmado');
INSERT INTO Agendamento VALUES (7, '78901234000107', '77777777777', '2025-07-07', '16:00:00', '22:00:00', 'hora', 7, 'pendente');
INSERT INTO Agendamento VALUES (8, '89012345000108', '88888888888', '2025-07-08', '13:00:00', '19:00:00', 'diaria', 8, 'confirmado');
INSERT INTO Agendamento VALUES (9, '90123456000109', '99999999999', '2025-07-09', '10:00:00', '16:00:00', 'hora', 9, 'pendente');
INSERT INTO Agendamento VALUES (10, '01234567000110', '00000000000', '2025-07-10', '09:00:00', '15:00:00', 'hora', 10, 'confirmado');

INSERT INTO Pagamento VALUES (1, '12345678000101', '11111111111', 1, 1, '2025-07-01', 'hora', 'PIX', 100.00);
INSERT INTO Pagamento VALUES (2, '23456789000102', '22222222222', 2, 4, '2025-07-02', 'diaria', 'dinheiro', 200.00);
INSERT INTO Pagamento VALUES (3, '34567890000103', '33333333333', 3, 5, '2025-07-03', 'hora', 'PIX', 108.00);
INSERT INTO Pagamento VALUES (4, '45678901000104', '44444444444', 4, 7, '2025-07-04', 'hora', 'transferência', 132.00);
INSERT INTO Pagamento VALUES (5, '56789012000105', '55555555555', 5, 8, '2025-07-05', 'diaria', 'dinheiro', 180.00);
INSERT INTO Pagamento VALUES (6, '67890123000106', '66666666666', 6, 9, '2025-07-06', 'hora', 'PIX', 90.00);
INSERT INTO Pagamento VALUES (7, '78901234000107', '77777777777', 7, 10, '2025-07-07', 'hora', 'cartão', 102.00);
INSERT INTO Pagamento VALUES (8, '89012345000108', '88888888888', 8, 10, '2025-07-08', 'diaria', 'transferência', 150.00);
INSERT INTO Pagamento VALUES (9, '90123456000109', '99999999999', 9, 9, '2025-07-09', 'hora', 'dinheiro', 80.00);
INSERT INTO Pagamento VALUES (10, '01234567000110', '00000000000', 10, 10, '2025-07-10', 'hora', 'PIX', 102.00);


