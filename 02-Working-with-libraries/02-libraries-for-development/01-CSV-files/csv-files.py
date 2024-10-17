import csv

def read_csv_file(file_name, doPrint = False):
    with open(file_name, newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(filereader) # skip header
        if(doPrint):
            for row in filereader:
                print('Id: ' + row[0] + ' Club: ' + row[1] + ' League: ' + row[2])
        return filereader

def read_csv_file_exception(file_name):
    try:
        csvfile = open(file_name, newline='') 
        clubreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in clubreader:
            print('Id: ' + row[0] + ' Club: ' + row[1] + ' League: ' + row[2])
    except FileNotFoundError:
        print('File not found')

def extract_column_names(file_name):
    with open(file_name) as csv_file:
        # reading the csv file using DictReader
        csv_reader = csv.DictReader(csv_file)
    
        # converting the file to dictionary
        # by first converting to list, then converting the list to dict
        dict_from_csv = dict(list(csv_reader)[0])
    
        # making a list from the keys of the dict
        list_of_column_names = list(dict_from_csv.keys())
    
        # displaying the list of column names
        print("List of column names : ", list_of_column_names)
        return list_of_column_names
    
def get_league_data_for_club(clubid):
    # TODO
    return False


csv_file = 'data/bundesliga_clubs.csv'
read_csv_file_exception(csv_file+'2')

extract_column_names(csv_file)
read_csv_file(csv_file, True)

print("Club with ID 1, plays in league: " + str(get_league_data_for_club(1)))

