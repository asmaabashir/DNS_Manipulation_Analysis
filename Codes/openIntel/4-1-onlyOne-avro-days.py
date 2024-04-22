import csv
from datetime import datetime
#Bu kod bulduğumuz tüm manipüle edilmiş dataları tarihlerine göre sıralıyor, hangi günde ne kadar veri varsa buluyor ortalamasını yazıyor
def epoch_to_date(epoch):
    return datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d')

input_file = "birlestir.csv"
output_file = "day-by-day-all_manipulated.csv"
# Manuel olarak day-by-day'i csv'ler içine aktar
date_data = {}
skipped_rows_count = 0
total_data_count = 0

with open(input_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    with open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Gün', 'Epoch Time', 'Diğer Veriler']) # Başlık satırını yaz

        for row in csv_reader:
            if len(row) != 8:  # Satırın boyutu 8'den farklıysa atla
                skipped_rows_count += 1
                continue

            try:
                epoch_time = int(row[7])
                date = epoch_to_date(epoch_time)
                csv_writer.writerow([date, epoch_time] + row[:7] + row[8:]) # Tarih, Epoch zamanı ve diğer verileri yeni CSV dosyasına yaz

                # Her gün için veri miktarını takip et
                if date in date_data:
                    date_data[date] += 1
                else:
                    date_data[date] = 1
                total_data_count += 1
            except Exception as e:
                print(f"Hata oluştu: {e}. Satır: {row}")

# En çok veri olduğu günü bul
if date_data:
    max_date = max(date_data, key=date_data.get)
    max_count = date_data[max_date]

    print("En çok veri olduğu gün:", max_date)
    print("Veri miktarı:", max_count)
else:
    print("Dosyada işlenebilir veri bulunamadı.")

print("Atlanan satır sayısı:", skipped_rows_count)

# Her gün kaç tane veri olduğunu ve ortalama günlük veri miktarını hesapla
if total_data_count > 0:
    print("\nHer gün veri miktarı:")
    for date, count in date_data.items():
        print(date, ":", count)

    average_daily_data = total_data_count / len(date_data)
    print("Ortalama günlük veri miktarı:", average_daily_data)
else:
    print("Dosyada işlenebilir veri bulunamadı.")
