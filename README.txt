ENG (translated via Google)
WARNING! Some of the features listed in this README are not yet implemented!
This calculator is designed for mathematical calculations with memory.
Next to the entered numbers, the memory unit must be specified like this: <number> <unit> 
(for example, to specify 5 Megabytes, write "5MB").
In the future, all numbers indicating the amount of memory will be designated as objects of the User_number class.
The main units of measurement are bit ("b") and byte ("B").
Entering numbers without specifying a unit of measurement is only possible when using the multiplication ("*") and 
division ("/") operators as the second argument (in future versions, you can specify it as the first). 
The multiplication operation should look like this: 5 MB * 4 (in the current version, the expression 4 * 5 MB will 
cause an error). 
Division has the same syntax.
The following is a list of unit prefixes:
K-kilo-
M-mega-
G-Giga-
T-tera-
P-Peta-
E-EXA-
Z-Zetta-
Y-yotta-
A number of the User_number class has visible and invisible parts.
Visible number - the number that the calculator shows you. This number changes the unit prefix if the number exceeds 
1024 (if it is not a Yottabyte/Yottabit) or less than 1 (if it is not a byte/bit). The basic unit of measurement 
(bit / byte) does not change. If you need a different unit of measurement, use the command: <number> conv <unit> 
(not implemented!). This number does not participate in any mathematical operations.
An invisible number is an automatically calculated number of bits contained in the visible number. Unlike a visible 
number, this number is intended exclusively for mathematical operations and is not initially visible to the user. It is 
specified only after performing the operation in brackets.
It is important to note that when multiplying and dividing by floating-point numbers, the number of bits is rounded up.
In this version, the calculator is not able to perform operations with negative numbers.
In this version, the calculator can perform operations with multiple operators, but it does not support "()" brackets.
To perform an operation with numbers, use the command: <number 1> <unit 1> < operator> <number 2> <unit 2>.
The operation can be performed with different units, but it may return an error if the result of the operation is 
negative.
Rules for used operators:
+ and - only work if both numbers are specified as User_number
* and / only works if the first number is specified as User_number, and the second is a normal number (if you do on the 
contrary, the calculator will give an error).
to_HDD() and from_HDD() accept only 1 number, which is specified as User_number. These operators are converters from 
HDD memory to real memory (from_HDD()) and conversely (to_HDD()) (not implemented!).
The command syntax does not require numbers, operators, and units to be separated by spaces ("5 MB + 12.4 KB" = 
"5MB+12.4 KB"), but commands are case-sensitive ("5 MB" not = "5mB").