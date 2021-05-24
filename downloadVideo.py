#!/usr/bin/python3

import requests
import os
import time
from multiprocessing import Pool

def run(i):
    
    url = 'https://*********seg-%01d.ts'%i
    print("开始下载："+url)
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; LENW8; 4399Box.1067)"}
    r = requests.get(url, headers = headers)
    with open('./mp4/3{}'.format(url[-6:]),'wb') as f:
        f.write(r.content)

def merge (t,cmd):
    time.sleep(t)
    res = os.popen(cmd)
    print(res.read())



if __name__ == '__main__':
    if not os.path.exists('./mp4'):
        os.mkdir('./mp4')
    local_path = './mp4/'
    if not os.path.exists(local_path):
        try:
            os.mkdir(local_path)
        except:
            pass
    # 创建进程池，执行10个任务
    pool = Pool(10)
    for i in range(10):
        pool.apply_async(run, (i+1,)) #执行任务
    pool.close()
    pool.join()
    #调用合并
    merge(5,"copy /b mp4\\*.ts mp4\\new16.ts")
    print('ok！处理完成')
