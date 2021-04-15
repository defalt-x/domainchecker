import requests
from multiprocessing.dummy import Pool as ThreadPool

active_trash = [] 
maxThreads = 15
pool = ThreadPool(maxThreads)
inp = input('Domains: ')

with open(r'' + inp, 'r') as file:
    urls = file.read().splitlines()

def ask (url):
    url = url + '.com'
    try:
        r = requests.get(url, timeout = 1)
        sc = r.status_code
        if sc == 200:
            f = open('working_results.txt', 'a')
            f.write(f'{url} \n')
            active_trash.append(url)
            f.close()
        else:
            pass                
    except:
        pass
    pool.close()
    
results = pool.map(ask, urls)
pool.join()
print('+ See results /working_results.txt |', len(active_trash), '/', len(urls), )
