from datetime import datetime, timedelta
import pandas as pd

stupci = ['ID', 'ADRESA', 'DATUM_ISTEKA', 'IME_I_PREZIME']
csv_file_path = 'Popis.csv'
df = pd.read_csv(csv_file_path, names=stupci, header=0)


df['DATUM_ISTEKA'] = pd.to_datetime(df['DATUM_ISTEKA'], format='%d.%m.%Y.', dayfirst=True)

time_now = datetime.now()

next_sixty_days = time_now + timedelta(days=60)

korisnici_sa_upozorenjem = df[df['DATUM_ISTEKA'] <= next_sixty_days]

print('Korisnicima kojima će se u sljedećih 60 dana isteći prešutno produljeni ugovori: ')
print(korisnici_sa_upozorenjem)