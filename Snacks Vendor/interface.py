#!/usr/bin/env python3
"""
Interactive console
"""
import sys
import cmd
import shlex #A lexical analyzer class for simple shell-like syntaxes.
from SnacksVendor import Vendor

class VendingCommand(cmd.Cmd):
   
    prompt = ("*DinDing* ")#print DingDing every time a command is called
    def do_quit(self, args): #determaine the command was quit
        return True
        

    def do_EOF(self, args):
   
        #EOF signal determines running termination, exit terminal/ cmd
   
        return True


    def do_buy(self, args):
        try:
            args = shlex.split(args)
            vendor.buy(args[0].title())
        except:
            print("** Please choose a snack **")


    def do_restock(self, args):
       #default values of the snacks
        vendor.restock()


    def do_money(self, args):
        #the vendor's profit
        vendor.value()


    # def do_add(self, args):
    #     #update the quanity when adding new snack
    #     item_dict = {
    #         'count': 1,
    #         'price': 0
    #     }

    #     try:
    #         args = shlex.split(args)
    #         item = args[0].title()
    #         vendor.add(item, item_dict)
    #     except:
    #         print("** Snack should have a name **")


    def do_check(self, args):
        #search for a snack
        try:
            args = shlex.split(args)
            item = args[0].title()
            if not vendor.find(item):
                print("Sorry, no {}s were found.".format(item))
        except:
            print("** I need the Snack name **")

    def do_blueprint(self, args):
        #return the blueprint of the snacks **default**
        vendor.blueprint()


    def do_inventory(self, args):
        #all the snacks and their details
        vendor.tell()


if __name__ == '__main__':
   
    #this will allow the program to keep running until the user writes "quit"
    # Creates size of hash table
    vendor = Vendor(5) #how many lines in the cmd to use to show the snacks details
    VendingCommand().cmdloop()
    #----------------cmdloop()----------------#
    # Performs an entire interactive session of line-oriented commands.
    # cmdloop starts by calling c .preloop( ),
    # then outputs string intro (c .intro, if intro is None).
    # Then c .cmdloop enters a loop. In each iteration of the loop,
    # cmdloop reads line s with s =raw_input( c .prompt).
    # When standard input reaches end-of-file,
    # cmdloop sets s ='EOF‘. If s is not 'EOF',
    # cmdloop preprocesses string s with s = c .precmd( s ),
    # then calls flag = c .onecmd( s ).
    # When onecmd returns a true value,
    # this is a tentative request to terminate the command loop.
    #  Now cmdloop calls flag = c .postcmd( flag,s ) to check if the loop should terminate.
    # If flag is now true, the loop terminates; otherwise another iteration of the loop executes.
    # If the loop is to terminate, cmdloop calls c .postloop( ), then terminates.
    # This structure of cmdloop is probably easiest to
    # understand by showing Python code equivalent to the method just described: