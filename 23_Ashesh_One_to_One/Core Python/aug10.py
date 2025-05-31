# Modes:
"""
Mode1   Name of the mode    Description                                         Mode2   Name of the mode
r       read                It opens the file for reading only.                 t       text mode               Default
                            Cursor is placed at the begining of the file.
                            Does not create the file if it does not exist.
                            Does not erase the content of the file.

w       write               Opens the file for writing only.                    b       binary mode
                            Creates the file if it does not exist.
                            Erase the entire content of the file at the time of opening.
                            Cursor is placed at the begining of the file.

a       append              Opens the file for writing only.
                            Creates the file if it does not exist.
                            Does not erase the content of the file.
                            Cursor is placed at the end of the file.

x       Exclusively         Opens the file for writing only.
        create              Creates the file if it does not exist.
                            Raises FileExistsError if the file already exists.
                            Cursor is placed at the begining of the file.
        
r+                          It opens the file for reading and writing both.
                            Cursor is placed at the begining of the file.
                            Does not create the file if it does not exist.
                            Does not erase the content of the file.

w+                          Opens the file for writing and reading both.
                            Creates the file if it does not exist.
                            Erase the entire content of the file at the time of opening.
                            Cursor is placed at the begining of the file.

a+                          Opens the file for writing and reading both.
                            Creates the file if it does not exist.
                            Does not erase the content of the file.
                            Cursor is placed at the end of the file.

"""
# work on a sample data using csv module