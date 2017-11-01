def sanitize(time_string):
    """Make all strings be in the same format"""

    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)

    return(mins + '.' + secs)

def process_file(filename):
    """Open and read file"""
    
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print("File error:" + str(ioerr))
        return(None)

james = process_file("james.txt")
julie = process_file("julie.txt")
mikey = process_file("mikey.txt")
sarah = process_file("sarah.txt")

james = (sorted(set([sanitize(each_james) for each_james in james])))
print(james[:3])
julie = (sorted(set([sanitize(each_julie) for each_julie in julie])))
print(julie[:3])
mikey = (sorted(set([sanitize(each_mikey) for each_mikey in mikey])))
print(mikey[:3])
sarah = (sorted(set([sanitize(each_sarah) for each_sarah in sarah])))
print(sarah[:3])
