#-------------Why  inerface.py--------------#
#the interface to the vending machine class
#-------------------------------------------#





#----------------import sys----------------#
"""
When an import statement is executed, the standard builtin __import__()
unction is called. Other mechanisms for invoking the\
import system (such as importlib.import_module()) may choose to
bypass __import__() and use their own solutions to implement import semantics.

When a module is first imported, Python searches for the module and if found,
it creates a module object 1, initializing it. If the named module cannot be found,
a ModuleNotFoundError is raised. Python implements various strategies to search for the
named module when the import machinery is invoked. These strategies can be modified and
extended by using various hooks described in the sections below.

Changed in version 3.3: The import system has been updated to fully implement
the second phase of PEP 302. There is no longer any implicit import machinery
 - the full import system is exposed through sys.meta_path. In addition
  native namespace package support has been implemented (see PEP 420).
"""
#-------------------------------------------#






#----------------import cmd----------------#
"""
third party module,The Cmd class provides a simple framework for writing line-oriented command interpreters.
These are often useful for test harnesses, administrative tools,
and prototypes that will later be wrapped in a more sophisticated interface.
** class cmd.Cmd(completekey='tab', stdin=None, stdout=None) **
A Cmd instance or subclass instance is a line-oriented interpreter framework.
There is no good reason to instantiate Cmd itself; rather, it’s useful as a
superclass of an interpreter class you define yourself in order to inherit Cmd’s
methods and encapsulate action methods.

"""
#-------------------------------------------#




import sys
import cmd
import shlex #A lexical analyzer class for simple shell-like syntaxes.

class Vendor():
    #snacks will be implemente as a hash table
    def __init__(self, size):
        """
        Initializes Vendor class

        Attributes:
            snacks list [list]: The hash map containing (size) snacks
            size[int]: Number of snacks in hash map
        """
        #initialize empty hash map // when the code runs first time we need to run interface.py
        self.buckets = [None] * size #right down is why the .buckets
        self.size = size
        """
        A hash table is typically implemented by creating
        a variable numberof""" #buckets
        """that will contain your data and
        indexing this data by hashing their"""#keys.
        """The"""#hash value
        """ of the key
        will determine the correct"""#bucket
        """to be used for that particular piece of data.
        """


    def get_hash(self, key):
        
        ####This is an optional way of hashing, we can use any method we want
        ####Here is a user-defined hashing method with some built in methods lie str() and ord()


        #Returns the  key and value that indicates bucket , the bucket represents a snack
        total = 0
        # adds ascii value of key string, modulo by size to produce hash
        #How? The ord() function returns an integer representing the Unicode character (ascii value).
        for aCharacter in str(key):
            total += ord(aCharacter)
            #every snack will get an id/ hash that is unique, How?
            #for a given snack, we get the ascii code of each character in it's name, and sum them together
            #then return the value modulus the size of the snack name
        return total % self.size


    def add(self, key, values={}):
        #we need it to add the dfault snacks on the first run
        
        hash_key = self.get_hash(key)
        item = [key, values]

        # If empty? -nothing added-
        if self.buckets[hash_key] is None:
            self.buckets[hash_key] = [item]
        else:
            # do a traverse on the snacks in the hash table (the buckets)
            for pair in self.buckets[hash_key]:
                if pair[0] == key:
                    # this is to increase the quantity of a snack
                    total_count = pair[1].get('count') + values.get('count')
                    pair[1]['count'] = total_count
                    return True
            #if a given snack is not stored
            return False
            return True


    def buy(self, key):
        #will update the quantity of the snacks

        #get the snack through it's id/hash
        hash_key = self.get_hash(key)
        bucket = self.buckets[hash_key] 

        #if found:
        if bucket:
            for i in range(0, len(bucket)):
                print(bucket[i][0])
                        #[i][0] : price
                if bucket[i][0] == key:
                    print("thanks for buying {} for ${:.2f}".format(bucket[i][0], bucket[i][1].get("price")))
                        ##[i][1] : quantity
                    bucket[i][1].update({"count": bucket[i][1].get("count") - 1})


    def tell(self):
        """
        Describes items in hash
        """
        flag = None #that's why we imported -sys-
        #searches the sys.path for the named module and executes its contents as the __main__ module.
        # When the -m flag is used with a command on the command-line interface,
        # followed by a <module_name>, it allows the module to be executed as an executable file.
        for val in self.buckets:
            if val:
                flag = 1
                for i in range(len(val)):
                    count = val[i][1].get("count", "not available")
                    item = val[i][0]
                    price = val[i][1].get("price")
                    if not price:
                        price = 0

                    if val[i][1].get("count") > 1:
                        print("You have {0} {1}s only. {1}s priced ${2:.2f}".format(count, item.title(), price)) 
                    else:
                        print("You got {0} {1} only. {1}s priced ${2:.2f}".format(count, item.title(), price))
                        #The title () function in python is the Python String Method
                        # which is used to convert the first character in each word to
                        # Uppercase and remaining characters to Lowercase in the string and returns a new string.
        
        if not flag:
            print("we ran out, no snack is available")

    def find(self, key):
        #check if the given snack exists
        hash_key = self.get_hash(key)
        bucket = self.buckets[hash_key]

        if bucket:
            for i in range(0, len(bucket)):
                if bucket[i][0] == key:
                    print("{}s cost ${:.2f}.".format(bucket[i][0], bucket[i][1].get("price")))
                    return True
        else:
            return False

    def value(self):
        #to show the cost of all the snacks in the vendor
        totalCurrentSnacksCost = 0
        for val in self.buckets:
            if val:
                for i in range(len(val)):
                    totalCurrentSnacksCost += val[i][1].get("price") * val[i][1].get("count")
        print("I got a total of ${:.2f} that is the cost of all the Snacks I got".format(totalCurrentSnacksCost))


    def restock(self):
        self.add("Chips", {"count": 10, "price": 1.00})
        self.add("Chocolate", {"count": 10, "price": 1.50})
        self.add("Popsicle", {"count": 10, "price": 0.50})
        self.add("Biscuits", {"count": 10, "price": 2.50})
        self.add("Drops", {"count": 10, "price": 0.30})
        self.add("Gum", {"count": 10, "price": 1.00})
        self.add("Cake", {"count": 10, "price": 3.75})
        self.add("Candy", {"count": 10, "price": 0.50})


    def blueprint(self):
        for val in self.buckets:
            print(val)

if __name__ == '__main__':
    vendor = Vendor(5) #how many lines in the cmd to use to show the snacks details