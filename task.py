# coding=utf-8

#
# ЕСЛИ БУДЕТЕ ЗАПУСКАТЬ НА PYTHON 3+, уберите вон ту строчку
#Это для красивого вывода, т.к. на 2 питоне я не нашел как исопльзовать атирубы end и sep
from __future__ import  print_function
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

#тут решил попробовать использовать возможности NumPy
def find_clusters_2(a):
    array_a=np.array(a)
    shifted_a=np.copy(array_a)
    #сдвинули на 1 вправо
    shifted_a[1:]=array_a[:-1]
    #считаем разность  в каждой точке
    delta=array_a-shifted_a
    #берем индексы, где разница не 1, это будут началы новых кластеров
    index_delta=np.where(delta!=1)
    index_delta=index_delta[0]
    #для общности решения
    index_delta=np.append(index_delta, len(a))
    result=[]
    for i in range(len(index_delta)-1):
        result.append(a[index_delta[i]:index_delta[i+1]])
    return result


#чтобы вид был по ТЗ
#
# Есть список [1,2,3,5,6,8,9,12]. Числа всегда идут по возрастанию.
# Необходимо разбить этот список на кластеры с непрерывными последовательностями.
# В данном случае в результате должно получиться [[1-3], [5-6], [8-9], [12]]
# Можно написать несколько реализаций этой задачи и определить наиболее эффективный метод.
def good_view(result):
    print ('[',end='')
    for i in result[:-1]:
        print ('[',end='')
        if len(i)>1:
            print (i[0],'-',i[-1],end='', sep='')
        else:
            print (i[0],end='')
        print ('], ',end='')
    print ('[',end='')
    if len(result[-1])>1:
        print (result[-1][0],'-', result[-1][-1],end='', sep='')
    else:
        print (result[-1][0],end='')
    print (']]',end='\n')

def main():
    a=[-1,0,1,2,3,5,6,8,9,12,23,24,25,101,102,103,104]
    good_view( find_clusters_1(a))
    good_view( find_clusters_2(a))


if __name__=="__main__":
    main()

