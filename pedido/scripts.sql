insert into pedido_item( dt_atlz	,cd_estab	,nm_ab_cliente,nr_nota_fis,dt_saida,hr_grade	,cd_produto
	,un_embalagem,qt_embalagem,qt_pilha,qt_carregada,qt_falta,id_motivo,qt_pallet	,vl_base_multa
	,vl_multa	,base_id	,usr_atlz_id)  
select dt_atlz ,cd_estab, nm_ab_cliente, nr_nota_fis, null,hr_grade, cd_produto, un_embalagem, qt_embalagem, cast(qt_pilha as text)||"/"||cast(qt_embalagem as text), 0,0,null,0,0,0,1,1
from p2.pedido_pedido


insert into pedido_base(dt_atlz,cd_estab,nm_ab_cliente,nr_nota_fis,nr_pedido,ds_ord_compra,
ds_placa,ds_transp,nr_lacre,dt_hr_chegada,dt_hr_ini_carga,dt_hr_fim_carga,ds_obs_carga,
id_no_show,vl_fixo,vl_base_multa,vl_multa,dt_hr_liberacao,usr_atlz_id)
select dt_atlz, cd_estab, nm_ab_cliente, nr_nota_fis, nr_pedido, ds_ord_compra, '','BRAPELCO','',null,null,null,'Test database','N', 0,0,0,null,1

from p2.pedido_pedido