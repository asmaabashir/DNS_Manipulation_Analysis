from ripe.atlas.sagan import DnsResult, Result
import json
import requests as rq
import calendar, time
import csv
import time
import sys

def read_IDs_from_file(file_):
    msm_id_list,start_time_list = [],[]
    # 0.003sn
    with open(file_, 'r') as file:
        for line in file:
            data = json.loads(line)
            msm_id_list.append(data['msm_id'])
            start_time_list.append(data['ts'])
    return msm_id_list,start_time_list

def read_write_DNS_results(new_str,file_path,dir):
    with open(dir + "/" + file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for result in json.loads(new_str):
            my_dns_result = DnsResult(result)
            if my_dns_result.responses:
                abuf = my_dns_result.responses[0].abuf
                qbuf = my_dns_result.responses[0].qbuf
                if my_dns_result.responses[0].abuf.answers:
                    if my_dns_result.responses[0].abuf.answers[0].type == 'AAAA' or my_dns_result.responses[0].abuf.answers[0].type == 'A':
                        #  print("Measurement ID:" + str(id))
                        #print("Start Time:"+ str(start_time))
                        #print("Stop Time:" + str(stop_time))
                        #  print("Abuf:" + str(abuf))
                        abuf_answer = my_dns_result.responses[0].abuf.answers
                        #print("Abuf Answer:" + str(abuf_answer))
                        #print(type(my_dns_result.responses[0].abuf.answers[0]))
                        #  print(my_dns_result.responses[0].abuf.answers[0])
                        data2 = my_dns_result.responses[0].abuf.answers[0].raw_data
                        list2 = []
                        list2.append(str(my_dns_result.responses[0].abuf.answers[0].name))
                        list2.append(str(my_dns_result.responses[0].abuf.answers[0].ttl))
                        list2.append(str(my_dns_result.responses[0].abuf.answers[0].klass))
                        list2.append(str(my_dns_result.responses[0].abuf.answers[0].type))
                        list2.append(str(my_dns_result.responses[0].abuf.answers[0].address))
                        list2.append(str(my_dns_result.probe_id))
                        list2.append(str(my_dns_result.origin))
                        list2.append(str(my_dns_result.created_timestamp))
                        #list1.append(list2)
                        writer.writerow(list2)
                        
                        #  print("------------")
                        qbuf_answer = my_dns_result.responses[0].qbuf.answers
                        #print("Qbuf:" + str(qbuf))
                        #  print("---------------")
                    else:
                        print("Bulamadi")
            else:
                #print("my_dns_result.responses is empty, cannot access elements.")
                print("----------------------")

if __name__ == "__main__":
    t1 = time.time()
    msm_id_list,start_time_list = read_IDs_from_file('measurements_prev.jsonf')
    csv_file_path = "new-{i}-{id}-{start}-{stop}.csv"
    url = "https://atlas.ripe.net/api/v2/measurements/{id}/results/?start={start_time}&stop={stop_time}&format=json"

    i = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    j = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    dir = sys.argv[3] if len(sys.argv) > 3 else "out_default"

    id_list,start_time_list,stop_time_list = [], [], []

    with open("payload_recent_prev.txt", "r") as file:
        for line in file:
            str_ = line.split("-")
            id_list.append(int(str_[1]))
            start_time_list.append(str_[3]) 
            stop_time_list.append(str_[4].rstrip("\n"))
    #print(id_list)
    #print(len(id_list[i:j]))
    for ii in range(i,j):
        id = id_list[ii]
        start_time = start_time_list[ii]
        stop_time = stop_time_list[ii]
        new_url = url.format(id=id,start_time=start_time,stop_time=stop_time)
        new_res = rq.get(new_url)
        new_str = new_res.content.decode()
        #print(new_url,"len str:",len(new_str))
        read_write_DNS_results(new_str,csv_file_path.format(i=ii,id=id,start=start_time,stop=stop_time),dir)
    print(time.time()-t1,"saniye sürdü")
