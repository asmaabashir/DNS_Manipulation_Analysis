import os
import glob
import csv
from avro.datafile import DataFileReader
from avro.io import DatumReader
#Bu kod, belirli gün için indirdiğin openIntel dosyası içerisindeki avro dosyalarından "A" ve "AAAA" olanları filtreleyerek merged_data_20230714.csv
#"A" ve "AAAA" olanları filtreleyerek merged_data_[tarih (yil-ay-gun)].csv içerisine yazıyor



# ÇALIŞMA SIRASI 1"
def find_avro_files(directory):
    avro_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".avro"):
                avro_files.append(os.path.join(root, file))
    return avro_files

def merge_avro_to_csv_filtered(avro_files, csv_filename):
    total_A_count = 0
    total_AAAA_count = 0

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for avro_file in avro_files:
            with open(avro_file, 'rb') as f:
                reader = DataFileReader(f, DatumReader())
                for record in reader:
                    if record['query_type'] == "A" or record['query_type'] == "AAAA":
                        csv_writer.writerow(record.values())
                        if record['query_type'] == "A":
                            total_A_count += 1
                        elif record['query_type'] == "AAAA":
                            total_AAAA_count += 1
                reader.close()

    return total_A_count, total_AAAA_count

def generate_csv_from_avro(directory_path, csv_output_filename):
    avro_files = find_avro_files(directory_path)
    total_A_count, total_AAAA_count = merge_avro_to_csv_filtered(avro_files, csv_output_filename)
    print("Toplam A kaydı sayısı:", total_A_count)
    print("Toplam AAAA kaydı sayısı:", total_AAAA_count)

directory_path = "C:\\Users\\emres\\Desktop\\VSCode\\openIntel\\20240410" ##########################################
csv_output_filename = "merged_data_20240410.csv"                     ##########################################

generate_csv_from_avro(directory_path, csv_output_filename)
