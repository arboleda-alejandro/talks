import os
import time
import concurrent.futures
import math
import subprocess
import argparse

#Argument parsing
parser = argparse.ArgumentParser(description="Arguments for script")
parser.add_argument('--parallel_execution', default='false', help="Value for parallel execution (defaul is 'false')")
args = parser.parse_args()
parallel_execution = args.parallel_execution

#Config values
sites_dict = {'www.elespectador.com':'Colombia',
              'www.eleconomista.com.mx': 'Mexico',
              'www.publimetro.cl': 'Chile',
              'www.nytimes.com': 'USA'}
probes_number = 15
threads_percentage = 50


def ping_site1(site, country):
    print(f'\nPinging site from: {country}')
    os.system(f'ping -c {probes_number} {site}')


def ping_site2(site, country):
    print(f'\nPinging site from: {country}')
    process = subprocess.Popen(['ping', '-c', str(probes_number), site], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()#wait ping to finish
    if stderr:
        print(f"Error pinging {site}: {stderr.decode()}")
    else:
        print(stdout.decode())


def ping_site3(site, country):
    """Función para hacer ping a un sitio web y mostrar el país."""
    print(f'\nPinging site from: {country}')
    # we use subprocess.popen to avoid locks in execution
    process = subprocess.Popen(
        ['ping', '-c', str(probes_number), site],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # asyncronous read of the output
    for line in process.stdout:
        print(line.decode(), end='')
    for line in process.stderr:
        print(line.decode(), end='')
    process.wait()  # waits until process finishes


def get_max_threads():
    return os.cpu_count()

def calculate_threads_to_use(max_threads, threads_percentage):
    return math.ceil(max_threads * threads_percentage / 100)


############## Sequential execution ##################

if parallel_execution == 'false':
    t1_sequential = time.time()
    for site in sites_dict.keys():
        print(f'\npinging site from: {sites_dict.get(site)}')
        os.system(f'ping -c {probes_number} {site}')
    t2_sequential = time.time()
    print(f'\nTotal execution time - Sequential: {t2_sequential-t1_sequential} seconds')


############## Parallel Execution ##############
else:
    #Get max threads available
    max_threads = get_max_threads()
    #Get threads to use for this execution
    threads_to_use = calculate_threads_to_use(max_threads, threads_percentage)
    #Pings execution in Parallel
    t1_parallel = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_to_use) as executor:
        futures = []
        for site, country in sites_dict.items():
            #Send ping task to get executed
            futures.append(executor.submit(ping_site3, site, country))
        #Wait all tasks to finish
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Esperar que la tarea termine, puede manejar excepciones si es necesario
    t2_parallel = time.time()
    print(f'\nTotal execution time - Parallel: {t2_parallel - t1_parallel} segundos')
