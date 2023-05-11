# ByteElevate
This Python script creates a text file with a user-defined size and prompts for a file name. It displays CPU and RAM usage, elapsed time, and file size. Once the file is generated, it waits for the user to press Enter before exiting.

The script imports the required modules: os, random, string, time, psutil, and colorama. colorama is used to add color to the console output.

The script then initializes the colorama module to allow the use of color in the console output.

The script displays a welcome message to the user, explaining what the program does.

The script prompts the user to enter a filename for the output text file. If the user enters an empty string, it displays an error message and asks again until a valid name is provided.

The script prompts the user to enter the desired size of the output text file in bytes. If the user enters a non-numeric value or a negative number, it displays an error message and asks again until a valid size is provided.

The script then creates a new file with the given name and generates random data of the specified size using the random.choices() method from the random module. If the size is negative, it generates a string of null bytes instead.

The script writes the generated data to the file using the open() function and the write() method.

The script prints out the elapsed time taken to create the file, as well as the RAM usage and CPU usage during the process using the time, psutil, and os modules.

Finally, the script displays a message informing the user that the file has been successfully created and waits for the user to press enter to exit.
