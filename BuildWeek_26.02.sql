drop schema if exists secondauto;

create schema secondauto;

use secondauto;

create table concessionaria (
concessionaria_id int auto_increment primary key ,
città varchar(50) NOT NULL,
indirizzo varchar(100) ,
numero int ,
telefono varchar(15) ,
responsabile varchar(50) 
);

create table auto(
auto_id int auto_increment primary key ,
marca varchar(50) ,
targa varchar(15) NOT NULL ,
colore varchar (20) ,
cilindrata varchar(20) ,
tipo_cambio varchar(20) ,
prezzo decimal (7,2) NOT NULL 
);

create table cliente(
cliente_id int auto_increment primary key ,
nome varchar (50) ,
cognome varchar (50) ,
residenza varchar (100) ,
recapito varchar(20) 
);

create table deposito(
deposito_id int auto_increment primary key ,
auto_id int NOT NULL,
concessionaria_id int NOT NULL ,
data_ingresso date NOT NULL,
data_uscita date ,
foreign key (auto_id) references auto(auto_id),
foreign key (concessionaria_id) references concessionaria(concessionaria_id)
);

create table transazione(
transazione_id int auto_increment primary key ,
cliente_id int NOT NULL ,
auto_id int NOT NULL ,
data date NOT NULL ,
tipo varchar(50) NOT NULL,
prezzo decimal(7,2) NOT NULL,
concessionaria_id int NOT NULL,
foreign key (cliente_id) references cliente(cliente_id),
foreign key (auto_id) references auto(auto_id),
foreign key (concessionaria_id) references concessionaria(concessionaria_id)
);



insert into concessionaria(città,indirizzo,numero, telefono,responsabile) value
('Milano', 'Via Garibaldi', '23', '02 1234567', 'Giovanni Rossi'),
('Roma', 'Via Veneto', '56', '06 9876543', 'Maria Bianchi'),
('Napoli', 'Corso Umberto', '12', '081 1122334', 'Antonio Verdi'),
('Torino', 'Piazza Castello', '8', '011 4455667', 'Laura Russo'),
('Firenze', 'Via dei Tornabuoni', '33', '055 7788990', 'Marco Conti'),
('Palermo', 'Via Roma', '45', '091 3344556', 'Elena Esposito'),
('Genova', 'Piazza De Ferrari', '20', '010 6677889', 'Luca Ferraro'),
('Bologna', 'Via Rizzoli', '72', '051 2233445', 'Federica Galli'),
('Bari', 'Corso Vittorio Emanuele', '5', '080 9988776', 'Francesco Leone'),
('Catania', 'Via Etnea', '123', '095 5566778', 'Giulia De Luca'),
('Venezia', 'Calle Larga', '10', '041 1122334', 'Andrea Marchesi'),
('Verona', 'Corso Porta Nuova', '78', '045 7788990', 'Martina Barbieri'),
('Messina', 'Via Garibaldi', '34', '090 3344556', 'Simone Greco'),
('Padova', 'Piazza dei Signori', '7', '049 6677889', 'Francesca Amato'),
('Trieste', 'Piazza Unità dItalia', '1', '040 2233445', 'Davide Moretti'),
('Taranto', 'Via DAquino', '89', '099 9988776', 'Sara Longo'),
('Brescia', 'Corso Zanardelli', '56', '030 5566778', 'Matteo Marini'),
('Reggio Calabria', 'Via Marina', '78', '0965 112233', 'Chiara Russo'),
('Modena', 'Via Emilia', '112', '059 7788990', 'Stefano Ferrari'),
('Prato', 'Piazza San Francesco', '3', '0574 334455', 'Alessia Costa'),
('Parma', 'Strada Garibaldi', '67', '0521 667788', 'Luca Rossi'),
('Cagliari', 'Via Roma', '67', '070 2233445', 'Sofia De Santis'),
('Livorno', 'Via Grande', '56', '0586 998877', 'Marco De Angelis'),
('Perugia', 'Piazza IV Novembre', '10', '075 5566778', 'Giulia Marchetti'),
('Foggia', 'Corso Vittorio Emanuele', '20', '0881 112233', 'Giovanni Mancini'),
('Salerno', 'Via Lungomare', '45', '089 3344556', 'Chiara Esposito'),
('Sassari', 'Via Roma', '23', '079 6677889', 'Francesco Russo'),
('Latina', 'Via dei Volsci', '90', '0773 223344', 'Martina Galli'),
('Giugliano in Campania', 'Via Napoli', '56', '081 9988776', 'Marco De Luca'),
('Monza', 'Via XX Settembre', '34', '039 5566778', 'Anna Rossi'),
('Siracusa', 'Corso Gelone', '12', '0931 112233', 'Laura Greco'),
('Pescara', 'Via Abruzzo', '45', '085 3344556', 'Antonio Martini'),
('Bergamo', 'Piazza Vecchia', '10', '035 6677889', 'Sara Bianchi'),
('Forlì', 'Via Emilia', '67', '0543 223344', 'Lorenzo Moretti'),
('Trento', 'Via dei Mille', '23', '0461 998877', 'Eleonora Colombo'),
('Vicenza', 'Corso Palladio', '56', '0444 112233', 'Matteo Rizzo'),
('Terni', 'Via Garibaldi', '67', '0744 334455', 'Valentina Santini'),
('Bolzano', 'Piazza Walther', '12', '0471 556677', 'Andrea Esposito'),
('Novara', 'Corso Roma', '45', '0321 112233', 'Lucia Rossi'),
('Ancona', 'Via della Vittoria', '20', '071 3344556', 'Francesco Moretti'),
('Andria', 'Via Trani', '56', '0883 6677889', 'Anna Colombo'),
('Udine', 'Piazza della Libertà', '8', '0432 223344', 'Luca Martini'),
('Cesena', 'Via Emilia', '90', '0547 998877', 'Martina Ferrari'),
('Lecce', 'Via XX Settembre', '67', '0832 112233', 'Giovanni Russo'),
('Pesaro', 'Piazza del Popolo', '34', '0721 3344556', 'Maria Conti'),
('Barletta', 'Corso Vittorio Emanuele', '67', '0882 6677889', 'Chiara Moretti'),
('La Spezia', 'Via XXV Aprile', '56', '0187 223344', 'Marco Barbieri'),
('Savona', 'Corso Italia', '23', '019 998877', 'Elena Galli'),
('Benevento', 'Via Roma', '78', '0824 112233', 'Francesco De Luca'),
('Brindisi', 'Via Colombo', '45', '0831 3344556', 'Giulia Russo'),
('Piacenza', 'Piazza Cavalli', '10', '0523 6677889', 'Matteo Marchesi'),
('Asti', 'Corso Alfieri', '56', '0141 223344', 'Martina Greco'),
('Ragusa', 'Via Roma', '45', '0932 998877', 'Luca Esposito')
;

/*Non 10.000 che non avevamo record*/
select * from auto where prezzo > 25000;

select distinct clt.cliente_id, clt.nome, clt.cognome, clt.residenza, clt.recapito from auto aut join transazione trz on aut.auto_id = trz.auto_id
join cliente clt on clt.cliente_id = trz.cliente_id where aut.colore = "Rosso" order by clt.nome asc;





