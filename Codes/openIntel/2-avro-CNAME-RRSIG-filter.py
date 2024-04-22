import csv

def remove_rows(input_filename, output_filename):
    with open(input_filename, newline='') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if len(row) > 1:  # Satır boş değilse
                if row[2].strip() in ("CNAME", "RRSIG"):
                    continue  # "CNAME" veya "RRSIG" varsa bu satırı atla
                if "A" in row[0] and row[11].strip():  # İlk indekste "A" varsa ve 11. indeks doluysa
                    writer.writerow(row)
                elif "AAAA" in row[0] and row[12].strip():  # İlk indekste "AAAA" varsa ve 12. indeks doluysa
                    writer.writerow(row)


# Ana işlem
input_file = "merged_data_20230406.csv" ############################################################
output_file = "merged_data_20230406-CNAME-RRSIG-filtered.csv" #################################################
column_index = 10  # 11. indeksi kontrol edecek

remove_rows(input_file, output_file)
print("Boş satırlar ve 'CNAME' satırları kaldırıldı.")

