# Python implementation of Binary Tree for Managing School Library Operations.

# Global Support Variable used for list operations
ls = []


class bookNode:
    """
    A class used to represent Binary Tree
    ...
    Attributes
    ----------
    bkID : Unique Book ID that needs to be inserted in the Binary Tree
    avCntr: Available counts of each unique book
    chkOutCntr: A variable to store total number of checkouts of the book
    Methods
    -------
    __init__ : self
        Object constructor of class bookNode
    readBookList(self, bkID, availCount):
        A Binary Tree constructor reading every line from inputsPS6.txt file
    printBooks(self, bkNode):
        :returns all the nodes in the Binary Tree
    findBook(self, eNode, bkID):
    :return availability of the books for checkout
    getNode(self, eNode, bkID):
    :return the node of the given book id
    chkInChkOut(self, bkID, inOut):
    process check in or checkout operation for the given book id based on inOut
    getTopBooks(self, bkNode):
    :returns top three most checkedout books
    notIssued(self, bkNode):
    :returns list of all the books that was never checked out
    stockout(self, bkNode)
    :returns list of all the books that are not availabel(out of stock)
    """

    def __init__(self, bkID, availCount):
        """

        :param bkID: Unique ID of the book that needs to be inserted in the Node
        :param availCount: Available count of the book that needs to be inserted in the Node
        """
        self.bookID = bkID
        self.avCntr = availCount
        self.chkOutCntr = 0
        self.left = None
        self.right = None

    def readBookList(self, bkID, availCount):
        """

        :param bkID: Unique Book ID that needs to be inserted in the Node of Binary Tree
        :param availCount: Available counts of corresponding books
        :return:
        """
        # Initializing the root node with the first entry in input file
        node = bookNode(bkID, availCount)
        if self is None:
            self = node
            print(self.avCntr)
        # In case of duplicate entries found, instead of creating a new node
        # Available count is incremented
        elif self.bookID == node.bookID:
            self.avCntr = self.avCntr + availCount
        # If root node already exists, continue with this routine
        else:
            # If the root book id is less than new book id
            # create a right node
            if self.bookID < node.bookID:
                if self.right is None:
                    self.right = node
                else:
                    self.right.readBookList(bkID, availCount)
            # If root node book id is greater than new node id
            # create a left node
            else:
                if self.left is None:
                    self.left = node
                else:
                    self.left.readBookList(bkID, availCount)

    def printBooks(self, bkNode):
        """

        :param bkNode: Root Node to begin traverse
        :return: All the nodes in pre-order
        """
        if bkNode:
            # First recur on left child
            self.printBooks(bkNode.left)
            # then print the bkID of node
            ls.append(str(bkNode.bookID) + "," + str(bkNode.avCntr))
            # now recur on right child
            self.printBooks(bkNode.right)
            return ls

    def findBook(self, eNode, bkID):
        """

        :param eNode: The root node to begin the search from
        :param bkID: The book id that needs to be searched
        :return: Availability of the book for checkout.
        """
        if eNode:
            if eNode.bookID == bkID:
                if eNode.avCntr > 0:
                    return "Book id {} is available for checkout".format(bkID)
                else:
                    return "All copies of book id {} have been checked out".format(bkID)
            elif eNode.bookID < bkID:
                return self.findBook(eNode.right, bkID)
            else:
                return self.findBook(eNode.left, bkID)
        else:
            return "Book id {} does not exist.".format(bkID)

    def getNode(self, eNode, bkID):
        """

        :param eNode: Root node to begin the traverse
        :param bkID: Book ID whose node to be found
        :return: Returns the node of the given book id
        """
        if eNode:
            if eNode.bookID == bkID:
                return eNode

            elif bkID < eNode.bookID:
                # First recur on left child
                return self.getNode(eNode.left, bkID)
            else:
                # now recur on right child
                return self.getNode(eNode.right, bkID)
        else:
            return None

    def chkInChkOut(self, bkID, inOut):
        """

        :param bkID: Unique book id
        :param inOut: (checkin / checkout): instructions of the process to be performed
        :return: None
        """
        try:
            if inOut == 'checkout':
                node = self.getNode(self, bkID)
                check_availability = self.findBook(node, bkID)
                if 'is available for checkout' in check_availability:
                    node.chkOutCntr = node.chkOutCntr + 1
                    node.avCntr = node.avCntr - 1
            else:
                node = self.getNode(self, bkID)
                node.avCntr = node.avCntr + 1
        except:
            return 'Book {} not available.'.format(bkID)

    def getTopBooks(self, bkNode):
        """

        :param bkNode: Root node to begin the traverse from
        :return: Top 3 books that have been checked out most
        """
        if bkNode:
            self.getTopBooks(bkNode.left)
            ls.append((bkNode.chkOutCntr, (bkNode.bookID, bkNode.avCntr)))
            ls.sort()
            self.getTopBooks(bkNode.right)
            result = [i[1] for i in ls[-3:][::-1]]
            return "Top Books1: {},{}\n " \
                   "Top Books2: {},{}\n " \
                   "Top Books3: {},{}\n".format(result[0][0], result[0][1],
                                                result[1][0], result[1][1],
                                                result[2][0], result[2][1])

    def notIssued(self, bkNode):
        """

        :param bkNode: Root node to begin traverse from
        :return: Books that have never been checked out
        """
        if bkNode:
            self.notIssued(bkNode.left)
            ls.append((bkNode.chkOutCntr, (bkNode.bookID, bkNode.avCntr)))
            ls.sort()
            self.notIssued(bkNode.right)
            result = [i[1][0] for i in ls if i[0] == 0]
            for ids in result:
                self.deleteNode(bkNode, ids)
            return result

    def stockout(self, bkNode):
        """

        :param bkNode: Root node to begin the traverse from
        :return: All book IDs with 0 availability
        """
        if bkNode:
            self.stockout(bkNode.left)
            ls.append((bkNode.avCntr, (bkNode.bookID, bkNode.avCntr)))
            ls.sort()
            self.stockout(bkNode.right)
            result = [i[1][0] for i in ls if i[0] == 0]
            return set(result)

    def isstockout(self, bkNode):
        """

        :param bkNode: Root node to begin the traverse from
        :return: True If at all any books are availabile
        """
        if bkNode:
            return bool(self.stockout(bkNode) != [])

    def deleteDeepest(self, bkNode, d_node):
        q = []
        q.append(bkNode)
        while (len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def deleteNode(self, bkNode, bkID):
        if bkNode == None:
            return None
        if bkNode.left == None and bkNode.right == None:
            if bkNode.bookID == bkID:
                return None
            else:
                return bkNode
        key_node = None
        q = []
        q.append(bkNode)
        while (len(q)):
            temp = q.pop(0)
            if temp.bookID == bkID:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x = temp.bookID
            y = temp.avCntr
            z = temp.chkOutCntr
            self.deleteDeepest(bkNode, temp)
            key_node.bookID = x
            key_node.avCntr = y
            key_node.chkOutCntr = z
        return bkNode


def main():
    """
    :return: implement all the modules of bookNode class as per the instructions from promptsPS6.txt file
    """
    
    output = open('./outputPS6.txt', 'a')
    with open('./inputsPS6.txt', 'r') as inpf:
        firstLine = inpf.readline()
        if not firstLine:
            print('Input file is empty ! Please add some books and their available counts in inputsPS6.txt',
                  file=output)
        else:
            if ',' in firstLine:
                firstLine.replace(" ", "")
                bkId, availCount = firstLine.split(",")
                root = bookNode(int(bkId), int(availCount))
                counter = 1
                for i, line in enumerate(inpf.readlines()):
                    counter = counter + 1
                    if ',' in line:
                        line.replace(" ", "")
                        bkId, availCount = line.split(",")
                        root.readBookList(int(bkId), int(availCount))
                    else:
                        return
            else:
                return
    with open('./promptsPS6.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if ':' in line:
                proc, bkid = line.split(':')
                if proc.lower() == 'findbook':
                    print(root.findBook(root, int(bkid)), file=output)
                elif proc.lower() in ['checkin', 'checkout']:
                    root.chkInChkOut(int(bkid), proc.lower())
            proc = line.lower()
            if 'listtop' in proc or 'gettop' in proc:
                print('Top Books:', file=output)
                print(root.getTopBooks(root), file=output)
                ls.clear()
            if 'notissued' in proc:
                print('List of books not issued:', file=output)
                for i in root.notIssued(root):
                    print(i, file=output)
                ls.clear()
            if 'print' in proc:
                root.printBooks(root)
                print('There are a total of {} book titles in the library.'.format(len(ls)),
                      file=output)
                for node in ls:
                    print(node, file=output)
                ls.clear()
    if root.isstockout(root):
        print('All available copies of the below books have been checked out:', file=output)
        for i in root.stockout(root):
            print(i, file=output)
            # root.deleteNode(root, i)
            ls.clear()
        # root.printBooks(root)
        # print('After deleting the Nodes with 0 Available count there are {} books:'.format(len(ls))
        #       , file=output)
        # for node in ls:
        #     print(node, file=output)
        # ls.clear()


if __name__ == "__main__":
    main()