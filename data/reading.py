

df = pd.concat([pd.read_csv(f,  sep=';', encoding='latin1') for f in glob.glob('/content/drive/My Drive/Colab Notebooks/Roma/Inc_Roma_2019/csv_incidenti_*.csv')])
