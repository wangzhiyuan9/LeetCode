class aogroud:
    def split_data(self,path,size):
        import pandas as pd 
        import numpy as np
        data = pd.read_excel(path,header=None,usecols=[0])
        data['sort'] = np.random.rand(data.shape[0])
        data = data.sort_values(by='sort').reset_index()[[0]]
        head = 'https://www.bing.com/search?q='
        data[0] = data[0].apply(lambda x:head+str(x))
        low = 0
        for i in range(1,size[2]//2+1):
            data[low:low+size[0]].to_csv('F:/output/{}.txt'.format(i*2-1),header=None,index=None)
            low+=size[0]
            if i*2 == size[2]:
                data[low:].to_csv('F:/output/{}.txt'.format(i*2),header=None,index=None)
            else:
                data[low:low+size[1]].to_csv('F:/output/{}.txt'.format(i*2),header=None,index=None)
                low+=size[1]

    def make_dir(self,n):
        import os
        for i in range(1,n+1):
            os.mkdir('F:/ww/wzy{}'.format(i))


    def rename_dir(self):
        import os 
        s = input().split()
        print(s)
        for i,j in enumerate(s):
            os.rename("F:/ww/wzy{}".format(i+1),"F:/ww/{}".format(j))
    

    def move_file(self,start,end):
        import shutil
        import numpy as np
        a = np.arange(start,end+1)
        j = 0
        for i in range(1,(end-start+1)//2+1):
            shutil.move('D:/火车采集器V9.21/Data/{}/SpiderResult.db3'.format(a[j]),'F:/ww/wzy{}/1.db3'.format(i))
            j+=1
            shutil.move('D:/火车采集器V9.21/Data/{}/SpiderResult.db3'.format(a[j]),'F:/ww/wzy{}/2.db3'.format(i))
            j+=1
