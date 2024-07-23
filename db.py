import sqlite3

conn = sqlite3.connect('nokia.db')
cursor = conn.cursor()

# Create the Makkah_5g table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Makkah_5g (
    Id INTEGER PRIMARY KEY,  
    Phone INTEGER,          
    Bin_Time_Stamp TEXT,   
    Latitude REAL,       
    Longitude REAL,        
    Nemo_Data_Connection_Attempt_HTTP INTEGER,  
    Nemo_Data_Connection_Success INTEGER,       
    Nemo_Data_Connection_Disconnect INTEGER,   
    Nemo_Data_Transfer_Fail_HTTP INTEGER,       
    Nemo_Data_Connection_Dropped INTEGER,      
    Data_Throughput_RLC_DL_Throughput_kbps REAL,   
    Serving_Channel_Info_DL_EARFCN INTEGER,    
    Serving_Cell_Info_Serving_PCI INTEGER,     
    RSRP_d_Bm_Dominant_RSRP_d_Bm REAL,          
    Common_Protocol TEXT,                       
    Serving_RS_Info_NR_Best_SS_RSRP REAL,     
    Serving_RS_Info_NR_Best_SS_SINR REAL,      
    Data_Throughput_NR_PDCP_Downlink_Throughput_Mbps REAL,  
    NR_Best_Serving_PCI_for_Selected_Set_199 INTEGER,  
    NR_ARFCN_199 INTEGER,                     
    NR_PDSCH_MCS_Index_for_CW0_199 INTEGER,  
    NR_PDSCH_Modulation_for_CW0_199 TEXT,      
    GSM_Cell_Identity_GSM_Serving_Cell_Id INTEGER,  
    Serving_RS_Info_Serving_RSRP_d_Bm REAL,   
    Serving_RS_Info_Serving_RS_CINR_d_B REAL,  
    Serving_RS_Info_Serving_RSRQ_d_B REAL,     
    Audio_Quality_POLQA_Downlink_MOS_POLQA_SWB REAL,  
    Data_Throughput_Physical_DSCH_Throughput_kbps REAL,  
    PCell_Strongest_Serving_PCell_Avg_DL_PRB REAL,   
    FiveG_NR_NR_Best_SS_RSRP REAL,             
    FiveG_NR_NR_PDCP_Downlink_Throughput_Mbps REAL, 
    FiveG_NR_NR_Best_SS_SINR REAL,             
    NR_ARFCN_SCG_PS_Cell INTEGER,            
    NR_Best_Serving_PCI_for_Selected_Set_SCG_PS_Cell INTEGER, 
    Common_Metrics_Band_Info TEXT,            
    Common_Metrics_Protocol TEXT               
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS CLUSTERS (
    SELECT AVG(Longitude), AVG()            
);
''')


conn.commit()
conn.close()

print("table created")