def selection_sort(lst):
    l = len(lst)
    for i in range(l):
        min_ind = i
        for j in range(i+1, l):
            if lst[j] < lst[min_ind]:
                min_ind = j
        lst[i], lst[min_ind] = lst[min_ind], lst[i]

def partition(seq, start, end):
    pivot_ind = start
    pivot_val = seq[pivot_ind]
    i = start + 1
    j = end - 1

    #scanning from both side, until we met element a > pivot_val from left side
    #and element b < pivot_val from right side,
    #then switch both element and move pointers
    #we must set  pointerLeft <= pointerRight, the equal is very import
    #so that when they overlapped, we still make pointer move one more time, and then we know 
    #we can swap pivot and the final pointer
    while i <= j :
        while i <= j  and seq[i] <= pivot_val:
            i += 1
        while i <= j and  pivot_val <= seq[j]:
            j -= 1
        if i < j:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
            j -= 1
    seq[pivot_ind], seq[j] = seq[j], pivot_val
    return j

def quick_sort_recursive(seq, start, end):
    if start >= end -1:
        return 
    
    pivot = partition(seq, start, end)
    quick_sort_recursive(seq, start, pivot)
    quick_sort_recursive(seq, pivot+1, end)

def quick_sort(seq):
    quick_sort_recursive(seq, 0, len(seq))
        
def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1
    while i < mid:
        lst.append(seq[i])
        i += 1
    #ignore
    # while j < stop:
    #    lst.append(seq[j])
    #     j += 1
    #since the next code will have the same effect
    
    for i in range(len(lst)):
        seq[start+i] = lst[i]

def merge_sort_recursively(seq, start, end):
    #if len(seq) == 0 or 1
    if start >= end -1:
        return 
    mid = (start + end) // 2
    merge_sort_recursively(seq, start, mid)
    merge_sort_recursively(seq, mid, end)
    merge(seq, start, mid, end)

def merge_sort(seq):
    merge_sort_recursively(seq, 0, len(seq))

def insert_sort(seq):
    #    j  i  
    #[a, b, c, d, e]
    # i always point to the start of unsorted seq
    # j always point to the end of the sorted seq
    # compare seq[i] and seq[j]
    # key = seq[i]
    # if seq[j] > key then we move seq[j] to the next position
    # and move j to the previous element
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > key:
            seq[j+1]  = seq[j]
            j -= 1
        seq[j+1] = key
        

#only for non-negative integer, only for known bound array
def count_sort(seq, upbound):
    helper = [0] * upbound
    for e in seq:
        helper[e] += 1
    j = 0
    for i in range(upbound):
        while helper[i] != 0:
            seq[j] = i
            helper[i] -= 1
            j += 1

#for uniform distributed sequence
def bucket_sort(seq):
    slot_num = len(seq)
    arr = [[] for i in range(slot_num)]
    #dispatch elements uniformly to each bucket, 
    #in perfect situation, if those elements are uniformly distributed
    #then each bucket will have just one elements
    #then we could know the time plexcity will just be O(n)
    for e in seq:
        arr[int(slot_num*e)].append(e)
    
    #sort each bucket
    for b in arr:
        insert_sort(b)
    
    k = 0
    for b in arr:
        for e in b:
            seq[k] = e
            k += 1
            

def num_of_digits(n):
    l = 1
    while n > 9:
        n = n / 10
        l += 1
    return l
#compare each digits of the integer
def radix_sort(seq):
    #max element
    max_ele = max(seq)
    #number of digits of max element
    nd = num_of_digits(max_ele)
    #from least significant to the most significant
    c = 0
    while nd > c:
        #counter array for digits
        helper = [0]*10
        for  e in seq:
            helper[(e // pow(10, c)) % 10] += 1
        for i in range(1, 10):
            helper[i] += helper[i-1]
        res = [0]*len(seq)
        for k in range(len(seq)-1, -1, -1):
            res[helper[(seq[k] // pow(10, c)) % 10] -1] =  seq[k]
            helper[(seq[k] // pow(10, c)) % 10] -= 1
        c += 1
        for j in range(len(seq)):
            seq[j] = res[j]
    
def bubble_sort(seq):
    for i in range(len(seq)):
        swapped = False
        for j in range(0, len(seq) - i-1):
            if seq[j] > seq[j+1]:
                seq[j+1], seq[j] = seq[j], seq[j+1]
                swapped = True
        if not swapped:
            break
    
    
if __name__ == '__main__':
    lst = [3,2,1,5,4]
    selection_sort(lst)
    print(lst)
    lst = [3,2,1,5,4, 2, 7]
    merge_sort(lst)
    print(lst)
    lst = [3,2,1,5,4, 5, 9]
    quick_sort(lst)
    print(lst)
    lst =  [3,1,2,4,8,7]
    insert_sort(lst)
    print(lst)
    lst = [3,2,1,1,0,4,6,5]
    count_sort(lst, 7)
    print(lst)
    lst = [3,2,1,5,6,7,89,4,8]
    bubble_sort(lst)
    print(lst)
    lst = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
    bucket_sort(lst)
    print(lst)
    lst = [3,2,10,6,2,58,2,1,0,5,4]
    radix_sort(lst)
    print(lst)
 

