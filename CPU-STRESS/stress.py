import multiprocessing
import math as mt
from multiprocessing import Process
import time

def bad_func(benim):
    
    x = 1.0004

    while True:

        x = mt.sqrt(x**2)
        #print(benim)
        #time.sleep(3)
        pass

if __name__ == "__main__": 
        
        cekirdek_say =  multiprocessing.cpu_count()
        print("Cekirdek sayi: ", cekirdek_say)

        Process_List = []

        for count in range(cekirdek_say):

            P = Process(target=bad_func,args =('{}.PROSES CALISIYOR'.format(count + 1),))
            P.start()
            print('{}.PROSES OLUSTURULDU'.format(count + 1))
            Process_List.append(P)
            pass
             
        for count,pro_finish in enumerate(Process_List):
            print('{}.PROSES BITDI'.format(count + 1))
            pro_finish.join()
            pass


        



    
    