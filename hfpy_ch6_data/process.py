class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

    def add_time(self, time):
        self.times.append(time)

    def add_times(self, times):
        self.times.extend(times)

def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + "." + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            temp1 = data.strip().split(',')
            return(AthleteList(temp1.pop(0), temp1.pop(0), temp1))
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return(None)

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

james.append('1-22')
print(james.name + "'s fastest times are: " + str(james.top3()))

