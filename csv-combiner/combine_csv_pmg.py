import pandas as pd
import os
import sys


def is_command_valid(arg):
    if len(arg) <= 1:
        print('Error: No command input')
        return False

    cmdlst = arg[1:]

    for files in cmdlst:
        if not os.path.exists(files):
            print('Error: File not found:' + files)
            return False
        if os.stat(files).st_size == 0:
            print('Error: The following file is empty:' + files)
            return False
    return True


def combine_csv(arg):

    dfsize = 10 ** 6
    df_list = []

    if is_command_valid(arg):
        cmdlst = arg[1:]

        for files in cmdlst:
            for df in pd.read_csv(files, chunksize=dfsize):
                filename = os.path.basename(files)
                df['filename'] = filename
                df_list.append(df)
        header = True

        for df in df_list:
            print(df.to_csv(index=False, header=header,
                  line_terminator='\n', chunksize=dfsize))
            header = False
    else:
        return


combine_csv(sys.argv)
