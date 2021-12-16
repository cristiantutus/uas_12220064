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
    st.write("""# main page""") #menampilkan main page
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

    nation_txt = st.text_input('Masukan Nama Negara :')
    dm = pd.read_csv('data/produksi_minyak_mentah.csv')
    df_js = pd.read_json('data/kode_negara_lengkap.json')
    arr = []
    for i in list(dm['kode_negara']) :
        if i not in list(df_js['alpha-3']) :
            arr.append(i)
    for i in arr :
        dm = dm[dm.kode_negara != i]

    if nation_txt:
        for nation in data_n:
            if nation['name'] == str(nation_txt):
                # Untuk jawaban 1
                st.text("Data Negara Yang Di Tunjukan : ")
                st.text("Kode Negara : " + nation['alpha-3'])

                data_produksi = dm[dm["kode_negara"].isin([nation['alpha-3']])]["produksi"].tolist()

                st.text("Chart Untuk Kode Negara => {}".format(nation['alpha-3']))
                            
                chart_data = pd.DataFrame(
                    data_produksi, 
                    columns=[nation['alpha-3']]
                )
                st.line_chart(chart_data)
                chart_data
                
                # Untuk jawaban 1 b
                year_data = dm[dm["kode_negara"].isin([nation['alpha-3']])]["tahun"].tolist()

                in_tahun = st.selectbox('Masukan Tahun ', year_data)
                st.text("Chart Pertahun Untuk Kode Negara => {} Pada Tahun {}".format(nation['alpha-3'], in_tahun))

                d_tahun = dm[dm["tahun"].isin([in_tahun])]["produksi"].tolist()

                chart_tahunan = pd.DataFrame(
                    d_tahun,
                    columns=[in_tahun]
                )

                st.line_chart(chart_tahunan)
                chart_tahunan

                # Untuk jawaban 1 c
                st.text("Chart Pertumbuhan Untuk Kode Negara => {} Pada Tahun {}".format(nation['alpha-3'], in_tahun))
                d_pertum = dm[dm["kode_negara"].isin([nation['alpha-3']])]["produksi"].tolist()                

                chart_pertum = pd.DataFrame(
                    d_pertum,
                    columns=[nation['alpha-3']]
                )
                
                sort_pertum = chart_pertum.sort_values(by=[nation['alpha-3']], ascending=False)

                st.line_chart(sort_pertum)
                sort_pertum

                # Untuk jawaban 1 d
                df_year = dm.loc[dm['tahun'] == in_tahun]
                df_year.sort_values(by=['produksi'], ascending=False, inplace=True)
                df_year.reset_index(drop=True, inplace=True)
                df2 = dm
                df2.sort_values(by=['produksi'], ascending=False, inplace=True)
                df2.reset_index(drop=True, inplace=True)
                if st.button('Lihat info 1'):
                    if(len(df_year) > 0) :
                        max_nat = df_year.head(1)
                        max_nat_code = str(max_nat["kode_negara"][0])
                        nat_info = df_js.loc[df_js['alpha-3'] == max_nat_code]
                        nat_info.reset_index(drop=True, inplace=True)
                        st.write("Informasi nation dengan jumlah produksi terbesar pada tahun", str(in_tahun))
                        if(len(nat_info) > 0) :
                            res = [[str(nat_info['name'][0]), str(max_nat_code), str(nat_info['region'][0]), str(nat_info['sub-region'][0])]]
                            res = pd.DataFrame(res, columns=['Nama nation', 'Kode nation', 'Region ', 'Sub-region'])
                            res
                        else :
                            st.write("Informasi nation kurang lengkap selain kode nation")
                            st.write("Kode nation : ", str(max_nat_code))
                        max_nat_all_year = df2.head(1)
                        max_nat_all_year_code = str(max_nat_all_year["kode_negara"][0])
                        nat_all_year_info = df_js.loc[df_js['alpha-3'] == max_nat_all_year_code]
                        nat_all_year_info.reset_index(drop=True, inplace=True)
                        st.write("Informasi nation dengan jumlah produksi terbesar keseluruhan tahun")
                        if(len(nat_all_year_info) > 0) :
                            res2 = [[str(nat_all_year_info['name'][0]), str(max_nat_all_year_code), str(nat_all_year_info['region'][0]), str(nat_all_year_info['sub-region'][0])]]
                            res2 = pd.DataFrame(res2, columns=['Nama nation', 'Kode nation', 'Region ', 'Sub-region'])
                            res2
                        else :
                            st.write("Informasi nation kurang lengkap selain kode nation")
                            st.write("Kode nation : ", str(max_nat_all_year_code))
                if st.button('Lihat info 2'):
                    df2 = dm.loc[dm['produksi'] > 0]
                    df2.sort_values(by=['produksi'], inplace=True)
                    df2.reset_index(drop=True, inplace=True)
                    df_year = df2.loc[df2['tahun'] == in_tahun]
                    df_year.sort_values(by=['produksi'], inplace=True)
                    df_year.reset_index(drop=True, inplace=True)
                    if(len(df_year) > 0) :
                        min_nat = df_year.head(1)
                        min_nat_code = str(min_nat["kode_negara"][0])
                        nat_info = df_js.loc[df_js['alpha-3'] == min_nat_code]
                        nat_info.reset_index(drop=True, inplace=True)
                        st.write("Informasi nation dengan jumlah produksi terkecil pada tahun", str(in_tahun))
                        if(len(nat_info) > 0) :
                            res = [[str(nat_info['name'][0]), str(min_nat_code), str(nat_info['region'][0]), str(nat_info['sub-region'][0])]]
                            res = pd.DataFrame(res, columns=['Nama nation', 'Kode nation', 'Region ', 'Sub-region'])
                            res
                        else :
                            st.write("Informasi nation kurang lengkap selain kode nation")
                            st.write("Kode nation : ", str(min_nat_code))
                        min_nat_all_year = df2.head(1)
                        min_nat_all_year_code = str(min_nat_all_year["kode_negara"][0])
                        nat_all_year_info = df_js.loc[df_js['alpha-3'] == min_nat_all_year_code]
                        nat_all_year_info.reset_index(drop=True, inplace=True)
                        st.write("Informasi nation dengan jumlah produksi terkecil keseluruhan tahun")
                        if(len(nat_all_year_info) > 0) :
                            res2 = [[str(nat_all_year_info['name'][0]), str(min_nat_all_year_code), str(nat_all_year_info['region'][0]), str(nat_all_year_info['sub-region'][0])]]
                            res2 = pd.DataFrame(res2, columns=['Nama nation', 'Kode nation', 'Region ', 'Sub-region'])
                            res2
                        else :
                            st.write("Informasi nation kurang lengkap selain kode nation")
                            st.write("Kode nation : ", str(min_nat_all_year_code))
                if st.button('Lihat info 3'):
                    df2 = dm.loc[dm['produksi'] == 0]
                    df2.sort_values(by=['kode_negara'], inplace=True)
                    df2.reset_index(drop=True, inplace=True)
                    df2_uniq = df2.kode_negara.unique()
                    df_year = df2.loc[df2['tahun'] == in_tahun]
                    df_year.sort_values(by=['kode_negara'], inplace=True)
                    df_year.reset_index(drop=True, inplace=True)
                    df_year_uniq = df_year.kode_negara.unique()
                    if(len(df_year) > 0) :
                        res = [[0, 0, 0, 0] for i in range(len(df_year_uniq))]
                        for i in range(len(res)) :
                            code = str(df_year_uniq[i])
                            nat_info = df_js.loc[df_js['alpha-3'] == code]
                            nat_info.reset_index(drop=True, inplace=True)
                            res[i][0] = str(nat_info['name'][0])
                            res[i][1] = str(df_year_uniq[i])
                            res[i][2] = str(nat_info['region'][0])
                            res[i][3] = str(nat_info['sub-region'][0])
                        st.write("Informasi nation dengan jumlah produksi nol pada tahun ", str(in_tahun))
                        res = pd.DataFrame(res, columns=['Nama nation', 'Kode nation', 'Region ', 'Sub-region'])
                        res
                        res2 = [[0, 0, 0, 0] for i in range(len(df2_uniq))]
                        for i in range(len(res2)) :
                            code = str(df2_uniq[i])
                            nat_info = df_js.loc[df_js['alpha-3'] == code]
                            nat_info.reset_index(drop=True, inplace=True)
                            res2[i][0] = str(nat_info['name'][0])
                            res2[i][1] = str(df2_uniq[i])
                            res2[i][2] = str(nat_info['region'][0])
                            res2[i][3] = str(nat_info['sub-region'][0])
                        st.write("Informasi nation dengan jumlah produksi nol pada seluruh tahun ")
                        res2 = pd.DataFrame(res2, columns=['Nama nation', 'Kode nation', 'Region ', 'Sub-region'])
                        res2
