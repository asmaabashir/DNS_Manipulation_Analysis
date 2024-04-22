import csv

def split_csv(input_filename, a_filename, aaaa_filename):
    # Girdi ve çıktı dosyalarını aç
    with open(input_filename, 'r', encoding='utf-8') as input_file, \
         open(a_filename, 'w', newline='', encoding='utf-8') as a_file, \
         open(aaaa_filename, 'w', newline='', encoding='utf-8') as aaaa_file:

        # CSV okuyucu ve yazıcı oluştur
        csv_reader = csv.reader(input_file)
        csv_writer_a = csv.writer(a_file)
        csv_writer_aaaa = csv.writer(aaaa_file)

        # CSV dosyasının her bir satırını oku
        for row in csv_reader:
            # Satırın ilk sütunundaki değeri kontrol et
            if row[0] == 'A':
                # Satırı 'A' dosyasına yaz
                csv_writer_a.writerow(row)
            elif row[0] == 'AAAA':
                # Satırı 'AAAA' dosyasına yaz
                csv_writer_aaaa.writerow(row)

# Kullanım örneği:
# Dosya adlarını belirleyin
input_filename = 'merged_data_20240409-CNAME-RRSIG-filtered.csv'
a_filename = 'merged_data_A.csv'
aaaa_filename = 'merged_data_AAAA.csv'

# Fonksiyonu çağır
split_csv(input_filename, a_filename, aaaa_filename)

