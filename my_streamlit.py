import streamlit as st
import pandas as pd 
import numpy as np 
import json

f = open('data/kode_negara_lengkap.json')
data_n = json.load(f)

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Dataframe','Jumlah Produksi Minyak')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Utama""") #menampilkan halaman utama
elif option == 'Dataframe':
    st.write("""## Dataframe""") #menampilkan judul halaman dataframe

    #membuat dataframe dengan pandas yang terdiri dari 2 kolom dan 4 baris data
    df = pd.DataFrame({
        'Column 1':[1,2,3,4],
        'Column 2':[10,12,14,16]
    })
    df #menampilkan dataframe
elif option == 'Jumlah Produksi Minyak':
    st.write("""## Jumlah Produksi Minyak""") #menampilkan judul halaman 

    txt_negara = st.text_input('Masukan Nama Negara :')

    if txt_negara:
        for negara in data_n:
            if negara['name'] == str(txt_negara):
                st.text("Data Negara Yang Di Tunjukan : ")
                st.text("Kode Negara : " + negara['alpha-3'])

                dm = pd.read_csv('data/produksi_minyak_mentah.csv')
                
                data_produksi = dm[dm["kode_negara"].isin([negara['alpha-3']])]["produksi"].tolist()

                st.text("Chart Untuk Kode Negara => {}".format(negara['alpha-3']))
                            
                chart_data = pd.DataFrame(
                    data_produksi, 
                    columns=[negara['alpha-3']]
                )
                st.line_chart(chart_data)
                chart_data
                
                data_tahun = dm[dm["kode_negara"].isin([negara['alpha-3']])]["tahun"].tolist()

                in_tahun = st.selectbox('Masukan Tahun ', data_tahun)

                st.text("Chart Pertahun Untuk Kode Negara => {} Pada Tahun {}".format(negara['alpha-3'], in_tahun))

                d_tahun = dm[dm["tahun"].isin([in_tahun])]["produksi"].tolist()

                chart_tahunan = pd.DataFrame(
                    d_tahun,
                    columns=[in_tahun]
                )

                st.line_chart(chart_tahunan)
                chart_tahunan

                st.text("Chart Pertumbuhan Untuk Kode Negara => {} Pada Tahun {}".format(negara['alpha-3'], in_tahun))
                d_pertum = dm[dm["kode_negara"].isin([negara['alpha-3']])]["produksi"].tolist()                

                chart_pertum = pd.DataFrame(
                    d_pertum,
                    columns=[negara['alpha-3']]
                )
                
                sort_pertum = chart_pertum.sort_values(by=[negara['alpha-3']], ascending=False)

                st.line_chart(sort_pertum)
                sort_pertum

                st.write("Data Lengkap Negara :")

                st.text("Nama Negara : {}".format(negara['name']))
                st.text("Kode Negara : {}".format(negara['alpha-3']))
                st.text("Region dan Sub Region : {}, {} \n".format(negara['region'], negara['sub-region']))

                st.text("======================================================================================")
                st.text("Produksi Terkecil : {}".format(chart_data.min()))
                st.text("Produksi Terkecil Keseruhan : ")
                sort_pertum2 = chart_pertum.sort_values(by=[negara['alpha-3']], ascending=True)

                st.line_chart(sort_pertum2)
                sort_pertum2
