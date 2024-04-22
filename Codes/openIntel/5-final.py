

dir = "20240409" #########################################################################################
ind = [[6,11],[6,12]]
file1_prefix = ["day","day"]
file1_postfix = ["A_prev","AAAA_prev"] ###########################################################

file2_prefix = ["merged_data","merged_data"]
file2_postfix = ["A","AAAA"]  ######################################################################

for f in range(len(file1_prefix)):
    file1 = file1_prefix[f] + "_" + dir + "-" + file1_postfix[f] + ".csv"
    file2 = file2_prefix[f] + "_" + dir + "-" + file2_postfix[f] + ".csv"
    print(file1,file2)

    d1 = dict()
    d2 = dict()

    with open(file1, 'r',newline = '\n') as fp1:
        for row in fp1:
            line1 = row.strip().split(",")
            ii = ind[f][0]   # ip nin kaçıncı indis olduğu
            ip1 = line1[ii]
            d1[ip1] = line1
    print("len1",len(d1))
    with open(file2, 'r',newline = '\n') as fp2:
        for row in fp2:
            line2 = row.strip().split(",")
            ii = ind[f][1]
            ip2= line2[ii]
            d2[ip2] = line2
    print("len2",len(d2))
    #print(d2.keys())
    print("çakışan ip ler")
    common_keys = set(d1.keys()) & set(d2.keys())
    print(common_keys)
    
    with open("final_combined-" + file1_postfix[f] + ".csv","w") as out_file: ###################################################
        for ck in common_keys:
            data1 = d1[ck]
            data2 = d2[ck]
            out_file.write(str(data1) + str(data2) + "\n")
   
    """
    for k in d1.keys():
        print("araştırılan ip:",k)
        if k in d2.keys():
            print(k)
    """




    