import csv

def filter_columns(input_file, output_file_a, output_file_aaaa):
    with open(input_file, 'r', newline='') as infile, \
         open(output_file_a, 'w', newline='') as outfile_a, \
         open(output_file_aaaa, 'w', newline='') as outfile_aaaa:

        reader = csv.reader(infile)
        writer_a = csv.writer(outfile_a)
        writer_aaaa = csv.writer(outfile_aaaa)

        for row in reader:
            if 'A' in row:
                writer_a.writerow(row)
            if 'AAAA' in row:
                writer_aaaa.writerow(row)

# Kullanım örneği:
input_file = 'day-20230406.csv' #############################
output_file_a = 'day_20230406-A.csv' ############################################# 
output_file_aaaa = 'day_20230406-AAAA.csv' #######################################
############## her columna bakıyor bunu indeksle ayır
filter_columns(input_file, output_file_a, output_file_aaaa)
