#!/usr/bin/python3

import requests
import os
import time
from multiprocessing import Pool

def run(i):
    #https://apd-383dad6ba0dd2d2b3411e33af7e8eb8c.v.smtcdns.com/vipts.tc.qq.com/A3yQfNpU4NYXHblbrSITBSY8auG0sKvP8V0GxfwPL-yA/uwMROfz2r5zAoaQXGdGnC2df644E7D3uP8M8pmtgwsRK9nEL/XwSeuVOm4SWeqqvlpH_mJLucpBeahm2u3XNeZ0505BfTz4Q6cX7BmO9MB4AS_YsyqNJbc6yFD6EDbloigu38q8EZbBnQ5APU-t1X5nn2yOVTetIvQ_0Cyw6P6KyqwOjuOgBwXdl0qyB0IyrJXp6xFURpMpQO2unvbfAu6dECpoQ/021_r0027q5k46f.321002.1.ts
    #https://dadi-yun.com/20190513/7598_765af90a/800k/hls/b644d276996000011.ts
    #https://dadi-bo.com/20181217/3w2Xz5ul/800kb/hls/lRuThN4226013.ts
    #https://dadi-yun.com/20190213/70_8ba8656c/800k/hls/6ce7fdd2e7c000000.ts
    #https://youku.com-bilibili.com/20180925/8189_02de1e86/800k/hls/1a16968a776000.ts
    #https://dadi-bo.com/20190103/wa7v0ZYH/800kb/hls/AlBd8932000.ts
    #https://lajiao-bo.com/20190501/wQBAnEH1/600kb/hls/V4biL32k5059000.ts
    # https://cdn.lhav41.com/video/m3u8/202001/04/8b2c0fffe35c/0001.ts
    url = 'https://cdn.lhav41.com/video/m3u8/202001/04/8b2c0fffe35c/0%03d.ts'%i
    # url = 'https://d1v-h.phncdn.com/hls/videos/202003/14/292761081/,720P_4000K,480P_2000K,240P_400K,_292761081.mp4.urlset/seg-%01d-f1-v1-a1.ts'%i
    print("开始下载："+url)
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; LENW8; 4399Box.1067)"}
    r = requests.get(url, headers = headers)
    with open('./mp4/2{}'.format(url[-4:]),'wb') as f:
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