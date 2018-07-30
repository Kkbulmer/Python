import pandas as pd
import teradata
import difflib
import itertools
import password

udaExec = teradata.UdaExec(appName="Source",version="1.0",logConsole=False)
conn_s = udaExec.connect(method="odbc",dsn="CLAIM_TERADATA_DEV",username=password.username,password=password.password)

print("Connection established")


sql="""SELECT CLM_NBR, CLM_DOM_CD, DATA_EFF_STRT_TS, DATA_EFF_STRT_DT,
		DATA_EFF_END_TS,
		DATA_EFF_END_DT,
		ETL_EFF_END_TS,
		DATA_SRC_CD,
		DATA_SRC_CREAT_TS,
		DATA_SRC_LST_UPDT_TS,
		ETL_RUN_CREAT_ID,
		ETL_RUN_UPDT_ID,
		ON_PRM_LS_IND,
		APPL_COV_CD,
		MALPR_TYP_CD,
		LIAB_PERS_INJ_IND,
		SUIT_ATTY_LVL_IND,
		CLM_SEV_IND,
		POL_ENTY_NBR,
		POLHLDR_STR_NM,
		POLHLDR_CTY_NM,
		POLHLDR_ST_CD,
		POLHLDR_PST_CD,
		POLHLDR_PST_5_CD,
		POLHLDR_PST_4_CD,
		POLHLDR_CONSL_ADDR_UID,
		POL_ENTY_LOC_DESC_TXT,
		LIAB_BLD_DAM_IND,
		LIAB_OTHR_DAM_IND,
		LIAB_VEH_DAM_IND,
		UNINS_OR_UNDINSD_CD,
		NOL_BLD_DAM_AMT,
		CM_LS_DT,
		OCCUR_RPT_DT,
		INSD_PRM_HABTL_CD,
		LIAB_PERS_INJ_COL_CD,
		CLMT_OBTN_DAM_EST_IND,
		APL_COL_CD,
		THRD_PTY_PDAM_IND,
		LIAB_CLM_AT_INTK_FIRE_IND
FROM	CLAIM_DW_SBOXV.APL_NOL_CLAIM_LIAB WHERE CLM_NBR in ('B360215','B366596','B9M0751','DJ61380','B369996','DPL0103','POSH121','B377880','B360912','D6P2130','B373974')"""



#Pulling data from Teradata and saving the data into a file
def create_results_file(x):
    processed_s =  pd.read_sql(x, conn_s)
    df1=pd.DataFrame(processed_s)
    df1.to_csv('Results data.txt',header=False, sep='\t', index=False,)
    print("Results data has been created")

#Compares the expected output.txt against the Results data.txt and generates a HTML file with differences
def compare_files():
    expected_output = open('expected output.txt','r')
    results_data = open('Results data.txt','r')
    find_differences = difflib.HtmlDiff().make_file(expected_output,results_data,'Expected output.txt','Results data.txt',charset='utf-8')
    write_html = open('difference.html','w')
    write_html.write(find_differences)
    write_html.close()
    print("HTML file is created")

#Finds the row where the mismatch occurred and prints the row number
def row_of_mismatch():
    with open('expected output.txt') as file1, open('Results data.txt') as file2:
        for row, (row1, row2) in enumerate(itertools.zip_longest(file1, file2)):
            if row1 != row2:
                print ('Mismatch in row : {0}'.format(row + 1))
                

#create_results_file(sql)
compare_files()
row_of_mismatch()
