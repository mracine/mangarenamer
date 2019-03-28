import argparse, os

PREFIX = None
SUFFIX = None

# NOTE: if the series starts with an '01' filename for instance,
# set this value to -1 to have the result start with '00'
OFFSET = 0

# Takes in a filtered filename consisting solely of an index integer
# as a string, and properly reindexes it according to any arguments
def reindex(indexStr):
    index = 0
    newStr = indexStr

    try:
        index = int(indexStr)
    except Exception:
        print(indexStr + " cannot be converted to int, skipping...")
        return indexStr

    index = index + OFFSET
    if index < 10:
        newStr = '00' + str(index)
    elif index < 100:
        newStr = '0' + str(index)
    else:
        newStr = str(index)

    return newStr

def sanitize_filename(f):    
    if PREFIX != None and PREFIX != '':
        f = f.split(PREFIX, 1)[1]
    if SUFFIX != None and SUFFIX != '':
        f = f.split(SUFFIX, 1)[0]
    return f

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mangarenamer: Use this script to rename image files of a manga or comic to prepare for a CBR or CBZ archive")

    # Starting offset (default 0)
    parser.add_argument('-o', '--offset', help="the number that the first file in this directory should be offset by")

    # Prefix to scrub (default empty)
    parser.add_argument('-P', '--prefix', help="the prefix to sanitize from the source filename")

    # Suffix to scrub (default empty)
    parser.add_argument('-S', '--suffix', help="the suffix to sanitize from the source filename")

    args = vars(parser.parse_args())
    OFFSET = int(args['offset'])
    PREFIX = args['prefix']
    SUFFIX = args['suffix']
    
    for dirpath, dirnames, filenames in os.walk(os.curdir):
        for f in filenames:
            # Use __file__ to get the name of this file
            # import __main__ as main and main.__file__ alternatively
            if f != __file__:
                filename, ext = os.path.splitext(f)
                newFilename = sanitize_filename(filename)
                newFilename = reindex(newFilename)
                newFilename = newFilename + ext

                if newFilename == f:
                    print("Skipping " + newFilename + " since no renaming is necessary...")
                else:
                    print("Renaming " + f + " to " + newFilename)
                    os.rename(f, newFilename)

