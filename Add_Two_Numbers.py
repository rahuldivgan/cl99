# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.lis1 = self.sll_to_list(l1)
        self.lis2 = self.sll_to_list(l2)
        self.num1 = self.lis_to_num(self.lis1)
        self.num2 = self.lis_to_num(self.lis2)
        #print self.num1, ', ', self.num2
        ret= self.num_to_lis(self.num1+self.num2)
        ret.reverse()
        print ret
        rl = self.list_to_sll(ret)
        #print rl, rl.val, rl.next
        return rl
    
    def list_to_sll(self, lis):
        init = prev = ListNode(lis[0])
        cnt=0
        for i in lis:
            if cnt>0:
                cur = ListNode(i)
                prev.next=cur
                prev = cur
            cnt+=1
            
        return init
    
    def lis_to_num(self, lis):
        num=0
        for i in range(len(lis)):
            num+=lis[i]*pow(10,i) #also reverses
        return num
            
    def num_to_lis(self, num):
        list_from_num=[]
        temp_num = num
        num_len=1
        while temp_num/10 != 0:
            num_len+=1
            temp_num = temp_num/10        
        for i in range(num_len):
            dig = num/pow(10, (num_len-(i+1)))
            list_from_num.append(dig)
            num = num - dig*pow(10, (num_len-(i+1)))
            
        return list_from_num
    
    def sll_to_list(self, l):
        node = l
        cnt=1
        ret_l=[]

        while node.next != None:
            cnt+=1
            ret_l.append(node.val)
            node = node.next

        ret_l.append(node.val)

        return ret_l
