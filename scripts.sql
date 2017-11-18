-- Script ORACLE para publicar dados da view usr_otif.ARZ_NOTAS_OTIF nas tabela do OTIF
--1 Estabelecimentos
--select * from business_unit_businessunit
insert into business_unit_businessunit(cd_unit, unit)
select distinct CD_ESTAB, ds_estab from usr_otif.ARZ_NOTAS_OTIF
where cd_estab not in (select cd_unit from business_unit_businessunit);
commit;
--2 Clientes
--select * from cliente_cliente;
insert into cliente_cliente(nm_ab_cli, ds_classe_cli, hr_lim_carga, hr_lim_lib)
select distinct nm_ab_cliente, ds_canal, '','' from usr_otif.ARZ_NOTAS_OTIF
where nm_ab_cliente not in (select nm_ab_cli from cliente_cliente);
commit;
--3 Carregamentos
--select * from pedido_carregamento
insert into pedido_carregamento(nr_nota_fis, nr_pedido, ds_ord_compra, dt_saida, ds_transp, business_unit_id, cliente_id)
select distinct NR_NOTA, NR_PEDIDO, NR_ORDEM_COMPRA, DT_SAIDA, NM_TRANSPORTADOR, bu.id, cc.id
from usr_otif.ARZ_NOTAS_OTIF no
inner join business_unit_businessunit bu on no.cd_estab = bu.cd_unit
inner join cliente_cliente cc on no.nm_ab_Cliente = cc.nm_ab_cli
where NR_NOTA not in (select nr_nota_fis from pedido_carregamento);
commit;
--4 Itens
--select * from pedido_item;
insert into pedido_item(cd_produto, ds_produto, un_embalagem, qt_embalagem, qt_pilha, qt_carregada, business_unit_id, carregamento_id)
select no.cd_produto, no.ds_produto, no.sg_emb, no.qt_emb, no.qt_pilha, 0, bu.id, pc.id
from usr_otif.ARZ_NOTAS_OTIF no
inner join business_unit_businessunit bu on no.cd_estab = bu.cd_unit
inner join pedido_carregamento pc on no.nr_nota = pc.nr_nota_fis
where not exists(
                 select cd_produto from pedido_item where cd_produto = no.cd_produto
                 and carregamento_id = pc.id
                 );
commit

--fix carregamento statuses to add new status : Sem programação - 18/11/2017
update pedido_carregamento set ds_status_carrega = ds_status_carrega+1