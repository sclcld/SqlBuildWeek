use secondauto;

/*1)------------------------------------------------------------------------------------*/
/*Marca e Colore delle Auto che costano più di 10.000 €*/
select distinct marca, colore, prezzo from auto where prezzo > 35000 order by marca;

/*2)------------------------------------------------------------------------------------*/
/*Tutti i proprietari di un’auto di colore ROSSO*/
with last_trx_auto as (select aut.auto_id, MAX(trz.data) as data from transazione trz join auto aut on trz.auto_id = aut.auto_id where trz.tipo = "VENDITA" and aut.colore = "Rosso" group by aut.auto_id)

select clt.nome, clt.cognome, aut.auto_id, aut.colore, aut.prezzo from transazione trz 
join last_trx_auto lta on trz.auto_id = lta.auto_id and trz.data = lta.data 
join auto aut on lta.auto_id = aut.auto_id
join cliente clt on clt.cliente_id = trz.cliente_id order by transazione_id;

/*3)------------------------------------------------------------------------------------*/
/*Costo totale di tutte le auto con Cilindrata superiore a 1600lo c14*/
select SUM(prezzo) costo_totale from auto aut where auto_id NOT IN (
select distinct auto_id from transazione trz where trz.tipo = "VENDITA") and cilindrata > 2000;

/*4)------------------------------------------------------------------------------------*/
/*Targa e Nome del proprietario delle Auto in una concessionaria della Città di Roma*/
with last_trx_auto as (select trz.auto_id, MAX(trz.data) as data from transazione trz where trz.tipo = "VENDITA" group by trz.auto_id)

select aut.targa, clt.nome, clt.cognome, atv.data from transazione trz 
join last_trx_auto atv on trz.auto_id = atv.auto_id and atv.data = trz.data
join concessionaria cns  on trz.concessionaria_id = cns.concessionaria_id 
join auto aut on atv.auto_id = aut.auto_id
join cliente clt on trz.cliente_id = clt.cliente_id
where cns.città = "ROMA";

/*5)------------------------------------------------------------------------------------*/
/*Per ogni Concessionaria, il numero di Auto*/

select COUNT(cns.numero )as auto, cns.numero  from deposito dpt 
join concessionaria cns on dpt.concessionaria_id = cns.concessionaria_id 
where dpt.auto_id 
not in (select trz.auto_id as data from transazione trz where trz.tipo = "VENDITA" group by trz.auto_id)
group by cns.concessionaria_id

/*6)------------------------------------------------------------------------------------*/
/*Il Responsabile di Concessionaria di tutte le auto con Cambio Automatico e Anno Acquisto 2010*/
