
import psycopg2
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

try:
    # Conexão com o banco
    conexao = psycopg2.connect(
        host= os.getenv('hospedgem'),
        database=os.getenv('banco_dados'),
        user=os.getenv('usuario'),
        password=os.getenv('senha'),
        port=os.getenv('porta')
    )

    # Cria o cursor para executar comandos SQL
    cursor = conexao.cursor()

    sql = """-- consultar todos os Órgãos Públicos que publicam por conta própria ou não
SELECT
    usuario.id,
    usuario.nomerazaosocial,
    usuario.cpfcnpj AS usuarioCpfCnpj,
    --naturezajuridica.nome,
	--naturezajuridica.descricao,
    SUM(CASE WHEN usuario.cpfcnpj = orgao.cnpj THEN 1 ELSE 0 END) AS totalComprasPublicacaoPropria,
    SUM(CASE WHEN usuario.cpfcnpj != orgao.cnpj THEN 1 ELSE 0 END) AS totalComprasPublicacaoEmNomeOutroOrgao,
    SUM(CASE WHEN usuario.cpfcnpj = orgao.cnpj THEN 1 ELSE 0 END) + SUM(CASE WHEN usuario.cpfcnpj != orgao.cnpj THEN 1 ELSE 0 END) AS totalPublicacoes,
    (SELECT
			naturezajuridica.nome
		FROM
			PNCP_VBL.orgao AS orgao
			INNER JOIN PNCP_VBL.naturezajuridica as naturezajuridica ON orgao.naturezajuridica = naturezajuridica.id
		WHERE
			orgao.cnpj = usuario.cpfcnpj) as naturezajuridica
FROM
    PNCP_VBL.compra AS compra
    INNER JOIN PNCP_VBL.orgao AS orgao ON compra.orgaoid = orgao.id
    INNER JOIN PNCP_VBL.usuario AS usuario ON compra.usuarioid = usuario.id
    --INNER JOIN PNCP_VBL.naturezajuridica as naturezajuridica ON orgao.naturezajuridica = naturezajuridica.id
--WHERE
    --compra.excluido = FALSE
GROUP BY
    usuario.id,
    usuario.nomerazaosocial,
    usuario.cpfcnpj
    --naturezajuridica.nome,
    --naturezajuridica.descricao
--HAVING
	 --SUM(CASE WHEN usuario.cpfcnpj = orgao.cnpj THEN 1 ELSE 0 END) > 0
	 --SUM(CASE WHEN usuario.cpfcnpj != orgao.cnpj THEN 1 ELSE 0 END) > 0
ORDER BY
	naturezajuridica DESC
	--usuario.id ASC
   -- usuario.nomerazaosocial ASC
	--totalPublicacoes ASC
--    totalComprasPublicacaoPropria ASC,
--    totalComprasPublicacaoTerceiro ASC
"""



  

    cursor.execute(sql)
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

except Exception as e:
    print(f"Erro ao conectar ou executar comandos: {e}")

finally:
    # Fechar a conexão
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()
