import csv
#istediğim tarihe göre filtreleme yapıyor, csv oluşturuyor.
def filter_csv_by_date(input_file, output_file, target_date):
    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        filtered_rows = [row for row in reader if row[0].startswith(target_date)]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_rows)

input_file = "day-by-day-all_manipulated.csv"  # CSV dosyasının adı 
output_file = "day-20240409.csv"  # Filtrelenmiş CSV dosyasının adı #############################################
target_date = input("Filtrelemek istediğiniz tarihi girin (örneğin 2024-03-20): ")  # Filtrelenecek tarih

filter_csv_by_date(input_file, output_file, target_date)
print("Filtreleme işlemi tamamlandı. Sonuçlar '{}' dosyasına kaydedildi.".format(output_file))
