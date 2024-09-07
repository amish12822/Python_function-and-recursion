"WAF to print the elements of a list in a single line. ( list is the parameter)"

list1 = ["Apple","Guava","Pineapple","Mango","Banana","Coconut","Cherry","Grapes"]
list2 = [ 2,4,5,6,2,3,4,5,3,32,32,4,4]

def litPrint(li2):
    count = 0
    while count<len(li2):
        print(li2[count],end=" ")

        count += 1

litPrint(list1)