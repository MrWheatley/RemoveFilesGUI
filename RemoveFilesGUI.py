# -*- coding: utf-8 -*-

import wx
import wx.xrc

# A very simple script to remove files if they
# have the specified keyword, coded by Suaj

import shutil, sys, os

# Main function

def main_func(keyword, directory, extract, k_r, verbose, ask):
    if extract:  # Create the sub-directory
        try:
            shutil.copytree(directory, f"{directory}/Extracted")
            if verbose:
                print("Creating sub-directory \"Extracted\"...")

        # The program could just try a different name, but that
        # name could also be used, and the next one too...

        # TO-DO: Ask for the user if the program should copy
        # the files to that directory or abort the operation

        except FileExistsError:
            print("The sub-directory \"Extracted\" already \
exists. Aborting...")
            sys.exit(0)
        else:  # Change the directory to the sub-directory
            directory = directory + "/Extracted"

    if verbose:
        print(f"Removing all files in {directory}...")

    conf = True  # Default value for the "ask" block

    for i in os.listdir(directory):
        if (keyword not in i and k_r == "k") \
        or (keyword in i and k_r == "r"):
            # Only if the value is an existing file
            if os.path.isfile(f"{directory}/{i}"):
                if ask:  # Ask for confirmation
                    conf = input(f"Remove {i}? [Y/n] ")
                    if conf.lower() in ["yes", "y"]:
                        conf = True
                    elif conf.lower() in ["no", "n"]:
                        conf = False
                        if verbose:
                            print("{i} will not be removed.")
                    # Y is the default option
                    else:
                        conf = True
                if conf:
                    if verbose:  # Verbose argument
                        print(f"Removing {i}... ", end='')
                    try:
                        os.remove(f"{directory}/{i}")
                    # This is to avoid the program collapsing
                    # if a single file raises an exception
                    except Exception as id:
                        print(f"""
An exception occurred.
Exception details: {id}
""")
                    else:
                        print("Done.")
            # TO-DO: Allow the deletion of files recursively
            elif os.path.isdir(f"{directory}/{i}"):
                if verbose:
                    print(f"{i} is a directory. Skipping...")
            else:  # It probably doesn't exist
                if verbose:
                    print(f"ERROR: {i} doesn't exist.")
    if verbose:
        print("Done.")

# Default option values, they are handled like this instead
# of putting them directly in the function in case the user
# changes them

extract = False
verbose = False
ask = False
k_r = "r"

# C-style loop because I forgot about the range() function lol

i = 1
while i < len(sys.argv):
    # Help option
    if sys.argv[i] in ["-h", "--help"]:
        print("""
Remove the files inside of a directory that have the
specified keyword in their names.
Usage:

Terminal$ python3 RemoveFiles.py [arguments] [keyword] [directory]

If your directory has spaces or special characters in its name,
use quotes:

\"directory with spaces\"

Arguments/Options:

-h, --help     Get information about the program.
-e, --extract  Copy the given directory and its files
               into a subdirectory and manipulate the
               files inside of it.
-k, --keep     Instead of removing the files, keep them
               and remove the ones that don't have the
               keyword in their names.
-r, --remove   Default value, the opposite of --keep.
-a, --ask      Ask before deleting a file.
-v, --verbose  Print the action being done.
        """)
        sys.exit(0)

    # Extract argument
    elif sys.argv[i] in ["-e", "--extract"]:
        extract = True

    # Keep argument
    elif sys.argv[i] in ["-k", "--keep"]:
        k_r = "k"

    # Remove argument (Default)
    elif sys.argv[i] in ["-r", "--remove"]:
        pass

    elif sys.argv[i] in ["-a", "--ask"]:
        ask = True

    # Verbose argument
    elif sys.argv[i] in ["-v", "--verbose"]:
        verbose = True

    # Invalid argument
    else:
        # It could be the directory
        if i == (len(sys.argv)-1):
            if not os.path.isdir(sys.argv[i]):
                print(f"The directory {sys.argv[i]} doesn't exist.")
                sys.exit(0)
        # Or it could be the keyword
        elif i == (len(sys.argv)-2):
            pass
        else:
            print(f"Invalid argument: \"{sys.argv[i]}\"")

    i += 1  # This is the increment value of the loop



###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,260 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 500,260 ), wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_dirPicker2 = wx.DirPickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.m_dirPicker2.SetMinSize( wx.Size( 999,-1 ) )

        bSizer4.Add( self.m_dirPicker2, 0, wx.ALL, 5 )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer7.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.keywordBox = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.keywordBox, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_checkBox_keep = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"keep", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_checkBox_keep, 0, wx.ALL, 5 )

        self.m_checkBox_extract = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"extract", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_checkBox_extract, 0, wx.ALL, 5 )

        self.m_checkBox_verbose = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"verbose", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_checkBox_verbose, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_button_execute = wx.Button( self.m_panel1, wx.ID_ANY, u"execute", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button_execute, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button_execute.Bind( wx.EVT_BUTTON, self.executeButton )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    directory = ""
    keyword = ""
    k_r = "r"
    extract = False
    verbose = False
    
    def executeButton( self, event ):
        directory = self.m_dirPicker2.GetPath()
        keyword = self.keywordBox.GetLineText(0)
        if self.m_checkBox_keep.IsChecked() == 1:
            k_r = "k"
        else:
            k_r = "r"


        if self.m_checkBox_extract.IsChecked() == 1:
            extract = True
        else:
            extract = False


        if self.m_checkBox_verbose.IsChecked() == 1:
            verbose = True
        else:
            verbose = False
        main_func(keyword, directory, extract, k_r, verbose, False)


app = wx.App(False)
frame = MyFrame1(None)
frame.Show(True)
app.MainLoop()
