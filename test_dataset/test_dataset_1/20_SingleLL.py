class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        def __init__(self, element, _next):      # initialize node's fields
            self._element = element               # reference to user's element
            self.__next = _next                     # reference to _next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element              # head of list

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        to_return = self._head._element
        self._head = self._head.__next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + "-->")
            curNode = curNode.__next
        result.append("None")
        return "".join(result)

    def __getitem__(self, k):
        tempNode = self._head
        for i in range(k):
            tempNode = tempNode.__next
        return tempNode._element

    def list_reverse(self):
        prev = None
        current = self._head 
        while (current is not None): 
            temp = current.next
            current.next = prev 
            prev = current 
            current = temp
        head = prev
        self._head = head

    def remove_all_occurance(self, value):
        cur = self._head
        pre = None
        
        while cur and cur.val == value:
            head = cur.next
            cur = head
            

        while cur: 
            while cur and cur.val != value:
                pre = cur
                cur = cur.next
            
            if cur == None:
                return head
            
            pre.next = cur.next
            cur = pre.next
        
        self._head = head
    
    def remove_nth_node_from_end(self, n):
        head = self._head
        #Remove the nth node from the END of the list, return head (the new list)
        #When removing the nth node from the END of the list, we need to connect the two detached lists
        #Goal: do in one pass
        
        if(head==None):
            return None

        #Loop through once, store all the nodes in a list
        #Just index the list and connect i-1 and i+1 nodes
        all_nodes = []
        
        tmp = head
        while(tmp!=None):
            all_nodes.append(tmp)
            tmp = tmp.next
            
        
        nth_node_i = len(all_nodes)-n
        
        nth_node_i_minus1 = -1
        nth_node_i_plus1 = -1
        
        if(nth_node_i-1<len(all_nodes) and nth_node_i-1>=0):
            nth_node_i_minus1 = nth_node_i-1

        if(nth_node_i+1<len(all_nodes) and nth_node_i+1>=0):
            nth_node_i_plus1 = nth_node_i+1
            
            
        if(nth_node_i_minus1!=-1 and nth_node_i_plus1!=-1):
            all_nodes[nth_node_i_minus1].next = all_nodes[nth_node_i_plus1]
            del all_nodes[nth_node_i]
        elif(nth_node_i==0):
            all_nodes[nth_node_i].next = None
            del all_nodes[nth_node_i]
        elif(nth_node_i==len(all_nodes)-1):
            all_nodes[nth_node_i_minus1].next = None
            del all_nodes[nth_node_i]
            
        if(len(all_nodes)>0):
            self._head = all_nodes[0]
        else:
            return


 
def main():
    print("----------------Testing __getitem__------------------")
    l1 = SingleLinkedList()
    l1.insert_from_head('good')
    l1.insert_from_head('nice')
    l1.insert_from_head('haha')
    l1.insert_from_head('hi')        

    print(l1)
    print("index 0 of l1:", l1[0])
    print("index 1 of l1:", l1[1])
    print("index 2 of l1:", l1[2])
    print("index 3 of l1:", l1[3])

    print("----------------Testing list_reverse------------------")
    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(i)
    print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
    l1.list_reverse()
    print(l1, "Expected: 0-->1-->2-->3-->4-->5-->6-->7-->8-->9-->None")


    print("-----------Testing remove_all_occurance-------------")
    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(6)
    print(l1)  # 6-->6-->6-->6-->6-->6-->6-->6-->6-->6-->None
    l1.remove_all_occurance(6)
    print(l1, "Expected: None")
    print()

    l1 = SingleLinkedList()
    for i in range(10):
        l1.insert_from_head(i % 2)
    print(l1)  # 1-->0-->1-->0-->1-->0-->1-->0-->1-->0-->None
    l1.remove_all_occurance(0)
    print(l1, "Expected: 1-->1-->1-->1-->1-->None")
    print()

    l1 = SingleLinkedList()
    l1.insert_from_head(0)
    print(l1)
    l1.remove_all_occurance(0)
    print(l1, "Expected: None")
    print()

    

"""if __name__ == '__main__':
    main()"""



