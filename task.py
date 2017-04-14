# coding=utf-8
import numpy as np

#решение в лоб, которое приходит в голову в первую очередь
def find_clusters_1(a):
    result=[]
    current_cluster=[]
    for x in a:
        if len(current_cluster)!=0:
            if(x!=current_cluster[-1]+1):
                result.append(current_cluster)
                current_cluster=[]
        current_cluster.append(x)
    if len(current_cluster)!=0:
        result.append(current_cluster)
    return result

def find_clusters_2(a):
    array_a=np.array(a);
    shifted_a=np.copy(array_a)
    shifted_a[1:]=array_a[:-1]
    delta=array_a-shifted_a
    index_delta=np.where(delta!=1)
    index_delta=index_delta[0]
    index_delta=np.append(index_delta, len(a))
    result=[]
    for i in range(len(index_delta)-1):
        result.append(a[index_delta[i]:index_delta[i+1]])
    return result

def main():
    a=[1,2,3,5,6,8,9,12]
    print find_clusters_1(a)
    print find_clusters_2(a)

if __name__=="__main__":
    main()

