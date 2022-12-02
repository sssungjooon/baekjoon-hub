import sys
 
 
n=int(sys.stdin.readline())
 
word_list=[]
while (n>0):
    n-=1
    word_list.append(list(sys.stdin.readline().strip()))
 
#길이비교후
#길이같으면 글자비교
def mergeSort(li):
    if len(li)<=1:
        return li
    mid=len(li)//2
 
    left=li[:mid]
    right=li[mid:]
 
    left1=mergeSort(left)
    right1=mergeSort(right)
 
    return merge(left1,right1)
 
def merge(left,right):
 
    i=0#왼쪽
    j=0#오른쪽
 
    arr=[]
 
    while i<len(left) and j<len(right):
        if len(left[i])<len(right[j]):#한쪽이 더길면
            arr.append(left[i])
            i+=1
        elif len(left[i])==len(right[j]):#길이가 같을때
            for c in range(len(left[i])):#길이만큼 반복함
                if left[i][c]<right[j][c]:#각 단어비교
                    arr.append(left[i])
                    i+=1
                    break
                elif left[i][c]>right[j][c]:
                    arr.append(right[j])
                    j+=1
                    break
                if c == len(left[i])-1:  # 끝까지 비교해 두단어가 같다면
                    arr.append(left[i])
                    i += 1
                    break
 
        else:
            arr.append(right[j])
            j+=1
 
 
    while i<len(left):
        arr.append(left[i])
        i+=1
    while j<len(right):
        arr.append(right[j])
        j+=1
 
    return arr
 
 
 
word_list=mergeSort(word_list)
before=""#이전단어
for i in range(len(word_list)):
    if before==word_list[i]:#같은 단어라면 건너뛴다.
        continue
    for j in range(len(word_list[i])):
        print(word_list[i][j],end="")
    print()
    before=word_list[i]
