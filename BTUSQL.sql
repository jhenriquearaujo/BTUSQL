
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
