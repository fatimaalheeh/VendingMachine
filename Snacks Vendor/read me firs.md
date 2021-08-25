### Start:
1. use VS code, download python extension, you also need python to be installed on your system
2. first command is: restock as the inventory is empty by default
3. second command: inventory
4. you can write: start: to see the architecture of the snacks in the vending machine
### other commands:


|   **Command**  |   **Description**   |  **Syntax**  |
| -------------- | --------------------- | ---------------------|
| `buy <item>` | Purchase item from machine. Item count will reflect change |buy snackName|
| `check <item>` | Checks price and quantity of an item |check snackName|
| `price <item>` | Changes the price of an item |price snackName newPrice|
| `start` | Prints the hash table schems |start|
| `inventory` | Prints the vending machine inventory |inventory|
| `money` | Prints total value of vending machine items |money|
| `restock` | Restocks the vending machine |restock|
| `quit` | Exits the program |quit|


#### A use Case 
```
$ ./interface.py 
interdace.py is the fuile to run
*DinDing* restock
*DinDing* inventory
You have 10 Drops  's only. Dropss priced $0.30
You have 10 Popsicle  's only. Popsicles priced $0.50
You have 10 Gum  's only. Gums priced $1.00
You have 10 Chips  's only. Chipss priced $1.00
You have 10 Chocolate  's only. Chocolates priced $1.50
*DinDing* restock
*DinDing* inventory
You have 20 Drops  's only. Dropss priced $0.30
You have 20 Popsicle  's only. Popsicles priced $0.50
You have 20 Gum  's only. Gums priced $1.00
You have 20 Chips  's only. Chipss priced $1.00
You have 20 Chocolate  's only. Chocolates priced $1.50
*DinDing* buy Chocolate
Chocolate
thanks for buying Chocolate for $1.50
*DinDing* money
I got a total of $84.50 that is the cost of all the Snacks I got
*DinDing* check Drops 
Dropss cost $0.30.
*DinDing* money
I got a total of $84.50 that is the cost of all the Snacks I got
*DinDing* quit

