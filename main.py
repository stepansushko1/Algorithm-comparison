import matplotlib.pyplot as plt
import time
import random
from copy import deepcopy

from numpy import log2


def selectionSort(arr):
    """ Sort the array with merge method """
    counter = 0
    for i in range(len(arr)):
        min_pos = i

        for j in range(i+1, len(arr)):
            counter += 1
            if arr[min_pos] > arr[j]:
                min_pos = j

        counter += 1
        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp

    return arr, counter


mergecounter = 0

def mergeSort(a):
    global mergecounter
    width = 1   
    n = len(a)                                         
    while (width < n):
        l=0;
        while (l < n):
            r = min(l+(width*2-1), n-1)
            m = (l+r)//2
            if (width>n//2):
                m = r-(n%width)
                mergecounter += 1  
            merge(a, l, m, r)
            l += width*2
        width *= 2
    return a, mergecounter
   
def merge(a, l, m, r):

    global mergecounter

    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        mergecounter += 1
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1
 
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1



def insertionSort(arr):
    counter = 0
    for i in range(len(arr)):
        temp = arr[i]
        hole_pos = i
        
        while(hole_pos > 0 and arr[hole_pos - 1] > temp):
            counter += 1
            arr[hole_pos] = arr[hole_pos - 1]
            hole_pos -= 1

        counter += 1
        arr[hole_pos] = temp
    
    return arr,counter

def shellSort(arr):
    counter = 0
    n = len(arr)
    gap = int(n/2)

    while gap > 0:

        for i in range(gap, n):
            elem = arr[i]
            j = i

            while j >= gap and arr[j - gap] > elem:
                counter += 1
                arr[j] = arr[j - gap]
                j -= gap

            counter += 1
            arr[j] = elem

        gap //= 2

    return arr, counter

# Functions for creating random sample arrays

def createRandomArray(number):
    arr = []
    for i in range(2**number):
        arr.append(random.randint(0,2**19))
    return arr

def createSortedArray(number):
    arr = createRandomArray(number)
    return sorted(arr)

def createReversedArray(number):
    arr = createRandomArray(number)
    return sorted(arr, reverse=1)


def createRepetativeArray(number):
    arr = []
    for i in range(2**number):
        arr.append(random.randint(1,3))
    return arr


def count_time(sample_array):
    """ Count time of working of each algorithm """

    copy1 = deepcopy(sample_array)
    copy2 = deepcopy(sample_array)
    copy3 = deepcopy(sample_array)
    copy4 = deepcopy(sample_array)


    start = time.time()
    a = selectionSort(copy1)
    end = time.time()

    start2 = time.time()
    b = insertionSort(copy2)
    end2 = time.time()
    
    start3 = time.time()
    c = mergeSort(copy3)
    end3 = time.time()

    start4 = time.time()
    d = shellSort(copy4)
    end4 = time.time()

    sel = "%s" % str(end - start)
    ins = "%s"% str(end2 - start2)
    merge = "%s" % str(end3 - start3)
    shell = "%s" % str(end4 - start4)

    return sel, ins, merge, shell, a[1], b[1], c[1], d[1]

def write_results(time, comperison_lst, switcher):
    """ 
    switcher: 0 - random arr, 1 - sorted arr, 2 - reversed arr, 3 - 1,2,3 arr 
    """
    way_name = ["Random Array","Sorted Array","Reversed Array","Repetative Array"]
    algorithms_names = ["Selection Sort", "Insertion Sort", "Merge Sort", "Shell Sort"]
    with open('results.txt', 'a') as file:
        for i in range(4):
            file.write(f"{algorithms_names[i]}, Comperison num: {comperison_lst[i]}, Time: {time[i]}, Experiment name: {way_name[switcher]}" + "\n")
        

def calculate_results(funct):
    """ """
    result_sel, result_ins, result_merge, result_shell = [], [], [], []
    result_sel_comp, result_ins_comp, result_merge_comp, result_shell_comp = [], [], [], []
    for j in range(9):
        temp_lst1 = []
        temp_lst1_comp = []
        for i in range(5):

            if funct == 1:
                random_array = createRandomArray(j+7)
            elif funct == 2:
                random_array = createReversedArray(j+7)
            elif funct == 3:
                random_array = createSortedArray(j+7)
            else:
                random_array = createRepetativeArray(j+7)

            time_lst = count_time(random_array)
            comparison_lst = time_lst[4:]
            time_lst = time_lst[:4]

            write_results(time_lst, comparison_lst, 0)

            for k in range(4):
                temp_lst1.append(float(time_lst[k]))
                temp_lst1_comp.append(comparison_lst[k])

        sel = (temp_lst1[0] + temp_lst1[4] + temp_lst1[8] + temp_lst1[12] + temp_lst1[16]) / 5
        ins = (temp_lst1[1] + temp_lst1[5] + temp_lst1[9] + temp_lst1[13] + temp_lst1[17]) / 5
        merge = (temp_lst1[2] + temp_lst1[6] + temp_lst1[10] + temp_lst1[14] + temp_lst1[18]) / 5
        shell = (temp_lst1[3] + temp_lst1[7] + temp_lst1[11] + temp_lst1[15] + temp_lst1[19]) / 5

        sel_comp = (temp_lst1_comp[0] + temp_lst1_comp[4] + temp_lst1_comp[8] + temp_lst1_comp[12] + temp_lst1_comp[16]) / 5
        ins_comp = (temp_lst1_comp[1] + temp_lst1_comp[5] + temp_lst1_comp[9] + temp_lst1_comp[13] + temp_lst1_comp[17]) / 5
        merge_comp = (temp_lst1_comp[2] + temp_lst1_comp[6] + temp_lst1_comp[10] + temp_lst1_comp[14] + temp_lst1_comp[18]) / 5
        shell_comp = (temp_lst1_comp[3] + temp_lst1_comp[7] + temp_lst1_comp[11] + temp_lst1_comp[15] + temp_lst1_comp[19]) / 5

        result_sel.append(sel)
        result_ins.append(ins)
        result_merge.append(merge)
        result_shell.append(shell)

        result_sel_comp.append(sel_comp)
        result_ins_comp.append(ins_comp)
        result_merge_comp.append(merge_comp)
        result_shell_comp.append(shell_comp)

    return [[result_sel, result_ins, result_merge, result_shell], [result_sel_comp, result_ins_comp, result_merge_comp, result_shell_comp]]




def grafik(res_time, res_comp):

    x = [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(x, res_time[0])
    plt.xlabel("Array size")
    plt.ylabel("Time")

    plt.plot(x, res_time[1])
    plt.plot(x, res_time[2])
    plt.plot(x, res_time[3])

    plt.legend(["Selection Sort", "Insertion Sort", "Merge Sort", "Shell sort"])

    plt.show()

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(x, res_comp[0])
    plt.plot(x, res_comp[1])
    plt.plot(x, res_comp[2])
    plt.plot(x, res_comp[3])
    plt.xlabel("Array size")
    plt.ylabel("Comprarison")
    
    plt.legend(["Selection Sort", "Insertion Sort", "Merge Sort", "Shell sort"])

    plt.show()



    
def main():

    output = calculate_results(1)
    grafik(output[0], output[1])
    output2 = calculate_results(2)
    grafik(output2[0], output2[1])
    output3 = calculate_results(3)
    grafik(output3[0], output3[1])
    output4 = calculate_results(4)
    grafik(output4[0], output4[1])   


if __name__ == "__main__":
    main()
