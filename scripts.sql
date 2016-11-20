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



UPDATE pedido_ITEM
SET
      base_id = (SELECT id
                 FROM pedido_BAse b
           WHERE B.CD_ESTAB = pedido_ITEM.CD_ESTAB AND B.NM_AB_CLIENTE=pedido_ITEM.NM_AB_CLIENTE AND B.NR_NOTA_FIS= pedido_item.NR_Nota_fis)

WHERE
    EXISTS (
        SELECT *
        FROM pedido_BAse b
        WHERE B.CD_ESTAB = pedido_item.CD_ESTAB AND B.NM_AB_CLIENTE=pedido_item.NM_AB_CLIENTE AND B.NR_NOTA_FIS =pedido_item.nr_nota_fis
    )

insert into grade_grade (nm_ab_cli,
hr_grade_seg,
hr_grade_ter ,
hr_grade_qua ,
hr_grade_qui ,
hr_grade_sex ,
hr_grade_sab ,
hr_grade_dom )
select 'SBJAR','0:00:00' ,'0:00:00' ,'0:00:00' ,'0:00:00' ,'0:00:00' ,'0:00:00' ,'0:00:00'
union
select 'SBJAR','1:00:00' ,'1:00:00' ,'1:00:00' ,'1:00:00' ,'1:00:00' ,'1:00:00' ,'1:00:00'
union
select 'SBJAR','2:00:00' ,'2:00:00' ,'2:00:00' ,'2:00:00' ,'2:00:00' ,'2:00:00' ,'2:00:00'
union
select 'SBJAR','3:00:00' ,'3:00:00' ,'3:00:00' ,'3:00:00' ,'3:00:00' ,'3:00:00' ,'3:00:00'
union
select 'SBJAR','4:00:00' ,'4:00:00' ,'4:00:00' ,'4:00:00' ,'4:00:00' ,'4:00:00' ,'4:00:00'
union
select 'SBJAR','5:00:00' ,'5:00:00' ,'5:00:00' ,'5:00:00' ,'5:00:00' ,'5:00:00' ,'5:00:00'
union
select 'SBJAR','6:00:00' ,'6:00:00' ,'6:00:00' ,'6:00:00' ,'6:00:00' ,'6:00:00' ,'6:00:00'
union
select 'SBJAR','7:00:00' ,'7:00:00' ,'7:00:00' ,'7:00:00' ,'7:00:00' ,'7:00:00' ,'7:00:00'
union
select 'SBJAR','8:00:00' ,'8:00:00' ,'8:00:00' ,'8:00:00' ,'8:00:00' ,'8:00:00' ,'8:00:00'
union
select 'SBJAR','9:00:00' ,'9:00:00' ,'9:00:00' ,'9:00:00' ,'9:00:00' ,'9:00:00' ,'9:00:00'
union
select 'SBJAR','10:00:00','10:00:00','10:00:00','10:00:00','10:00:00','10:00:00','10:00:00'
union
select 'SBJAR','11:00:00','11:00:00','11:00:00','11:00:00','11:00:00','11:00:00','11:00:00'
union
select 'SBJAR','12:00:00','12:00:00','12:00:00','12:00:00','12:00:00','12:00:00','12:00:00'
union
select 'SBJAR','13:00:00','13:00:00','13:00:00','13:00:00','13:00:00','13:00:00','13:00:00'
union
select 'SBJAR','14:00:00','14:00:00','14:00:00','14:00:00','14:00:00','14:00:00','14:00:00'
union
select 'SBJAR','15:00:00','15:00:00','15:00:00','15:00:00','15:00:00','15:00:00','15:00:00'
union
select 'SBJAR','16:00:00','16:00:00','16:00:00','16:00:00','16:00:00','16:00:00','16:00:00'
union
select 'SBJAR','17:00:00','17:00:00','17:00:00','17:00:00','17:00:00','17:00:00','17:00:00'
union
select 'SBJAR','18:00:00','18:00:00','18:00:00','18:00:00','18:00:00','18:00:00','18:00:00'
union
select 'SBJAR','19:00:00','19:00:00','19:00:00','19:00:00','19:00:00','19:00:00','19:00:00'
union
select 'SBJAR','20:00:00','20:00:00','20:00:00','20:00:00','20:00:00','20:00:00','20:00:00'
union
select 'SBJAR','21:00:00','21:00:00','21:00:00','21:00:00','21:00:00','21:00:00','21:00:00'
union
select 'SBJAR','22:00:00','22:00:00','22:00:00','22:00:00','22:00:00','22:00:00','22:00:00'
union
select 'SBJAR','23:00:00','23:00:00','23:00:00','23:00:00','23:00:00','23:00:00','23:00:00'
union
select 'SBJAR','24:00:00','24:00:00','24:00:00','24:00:00','24:00:00','24:00:00','24:00:00'




insert into grade_grade (nm_ab_cli,hr_grade,dt_semana)
select 'ABCD','0:00:00' ,0
union
select 'ABCD','1:00:00' ,0
union
select 'ABCD','2:00:00' ,0
union
select 'ABCD','3:00:00' ,0
union
select 'ABCD','4:00:00' ,0
union
select 'ABCD','5:00:00' ,0
union
select 'ABCD','6:00:00' ,0
union
select 'ABCD','7:00:00' ,0
union
select 'ABCD','8:00:00' ,0
union
select 'ABCD','9:00:00' ,0
union
select 'ABCD','10:00:00',0
union
select 'ABCD','11:00:00',0
union
select 'ABCD','12:00:00',0
union
select 'ABCD','13:00:00',0
union
select 'ABCD','14:00:00',0
union
select 'ABCD','15:00:00',0
union
select 'ABCD','16:00:00',0
union
select 'ABCD','17:00:00',0
union
select 'ABCD','18:00:00',0
union
select 'ABCD','19:00:00',0
union
select 'ABCD','20:00:00',0
union
select 'ABCD','21:00:00',0
union
select 'ABCD','22:00:00',0
union
select 'ABCD','23:00:00',0
