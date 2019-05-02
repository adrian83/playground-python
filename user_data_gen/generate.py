
import sys
import random

names = ["Muhammad","Oliver","Noah","Harry","Leo","George","Jack","Charlie","Freddie","Arthur","Alfie","Henry","Oscar","Theo","Archie","Jacob","Joshua","James","Ethan","Thomas","William","Logan","Lucas","Jackson","Max","Isaac","Finley","Adam","Alexander","Teddy","Mason","Harrison","Elijah","Daniel","Elliot","Joseph","Arlo","Dylan","Liam","Sebastian","Hunter","Rory","Reuben","Luca","Benjamin","Albie","Tommy","Finn","Samuel","Caleb"]
surnames = ["Smith","Jones","Williams","Taylor","Brown","Davies","Evans","Wilson","Thomas","Johnson","Roberts","Robinson","Thompson","Wright","Walker","White","Edwards","Hughes","Green","Hall","Lewis","Harris","Clarke","Patel","Jackson","Wood","Turner","Martin","Cooper","Hill","Ward","Morris","Moore","Clark","Lee","King","Baker","Harrison","Morgan","Allen","James","Scott","Phillips","Watson","Davis","Parker","Price","Bennett","Young","Griffiths"]

names_count = len(names)
surnames_count = len(surnames)

def rand_name():
    return names[random.randint(0,names_count-1)]

def rand_surname():
    return surnames[random.randint(0,surnames_count-1)]

def create_email(name, surname):
    return "{0}_{1}@domain_{2}.com".format(name, surname, random.randint(0,100)).lower()

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("provide number of records")
        exit(1)
    
    if not sys.argv[1].isdigit():
        print("number of records must be an integer")
        exit(1)

    records = int(sys.argv[1]) 

    #print("{0}".format(records))


    for i in range(1, records+1):
        name = rand_name()
        surname = rand_surname()
        email = create_email(name, surname)
        print("{0},{1},{2},{3}".format(i,name,surname, email))


    

