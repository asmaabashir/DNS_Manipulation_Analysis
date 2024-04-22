from ripe.atlas.sagan import DnsResult, Result
import json
import requests as rq
import calendar, time
import csv
import time

def read_IDs_from_file(file_):
    msm_id_list,start_time_list = [],[]
    # 0.003sn
    with open(file_, 'r') as file:
        for line in file:
            data = json.loads(line)
            msm_id_list.append(data['msm_id'])
            start_time_list.append(data['ts'])
    return msm_id_list,start_time_list

if __name__ == "__main__":
    csv_file_path = "new-{i}-{id}-{day_no}-{start}-{stop}.csv"
    url = "https://atlas.ripe.net/api/v2/measurements/{id}/results/?start={start_time}&stop={stop_time}&format=json"
    msm_id_list,start_time_list = read_IDs_from_file('measurements_new.jsonf')
    lst = []
    delta_day, max_day = 5, 5
    i = 1
    start_time = 1712620800
    for id,start in zip(msm_id_list,start_time_list):
        print(i,id,start)
        iday = 5
        #start_time = start
        while(iday <= max_day):
            stop_time = start_time + (3600*24*delta_day)
            print(i,id,iday,start_time,stop_time)
            csv_file_path.format(i=i,id=id,day_no=iday,start=start_time,stop=stop_time)
            url.format(id=id,start_time=start_time,stop_time=stop_time)
            lst.append("-".join([str(i),str(id),str(iday),str(start_time),str(stop_time)]))
            #print("-".join([str(i),str(id),str(iday),str(start_time),str(stop_time)]))
            #new_res = rq.get(new_url)
            #new_str = new_res.content.decode()
            iday+=5
            #start_time = stop_time
        i+=1
    with open("payload_recent_new.txt", "w") as file:
        for item in lst:
            file.write(f"{item}\n")
    