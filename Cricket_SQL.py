import mysql.connector as sqltor
mycon = sqltor.connect(user = "root", passwd = "veeru2004", database = "cricket", host = "localhost")
cursor = mycon.cursor()
import math
import random
import matplotlib.pyplot as plt

def player_in_T20():
    cursor.execute("select name from player_t20")
    ar = []
    for i in cursor.fetchall():
        ar.append(i[0])
    return ar

def player_in_ODI():
    cursor.execute("select name from player_odi")
    ar = []
    for i in cursor.fetchall():
        ar.append(i[0])
    return ar

def player_in_TEST():
    cursor.execute("select name from player_test")
    ar = []
    for i in cursor.fetchall():
        ar.append(i[0])
    return ar

def team_in_TEST():
    cursor.execute("select team from team_test")
    ar = []
    for i in cursor.fetchall():
        ar.append(i[0])
    return ar

def team_in_ODI():
    cursor.execute("select team from team_odi")
    ar = []
    for i in cursor.fetchall():
        ar.append(i[0])
    return ar

def team_in_T20():
    cursor.execute("select team from team_t20")
    ar = []
    for i in cursor.fetchall():
        ar.append(i[0])
    return ar

def remove_c(s):
    s1 = ""
    if "(C)" in s:
        for i in range(0, len(s) - 3):
            s1 = s1 + s[i]
    else:
        s1 = s
    return s1

def remove_c_array(a):
    ar = []
    for i in a:
        ar.append(remove_c(i))
    return ar

Tests = []
for i in range(0, 276): #250 #275
    Tests.append(0)
for i in range(0, 36):
    Tests.append(1)
for i in range(0, 16):
    Tests.append(2)
for i in range(0, 5):
    Tests.append(3)
for i in range(0, 7):
    Tests.append(4)
for i in range(0, 4): #5
    Tests.append(5)
Tests.append(6)

ODI = []
for i in range(0, 65):
    ODI.append(0)
for i in range(0, 35):
    ODI.append(1)
for i in range(0, 17):
    ODI.append(2)
for i in range(0, 5):
    ODI.append(3)
for i in range(0, 7):
    ODI.append(4)
for i in range(0, 3):
    ODI.append(5)
for i in range(0, 3):
    ODI.append(6)

t20 = []
for i in range(0, 20):
    t20.append(0)
for i in range(0, 28):
    t20.append(1)
for i in range(0, 17):
    t20.append(2)
for i in range(0, 5):
    t20.append(3)
for i in range(0, 7):
    t20.append(4)
for i in range(0, 4):
    t20.append(5)
for i in range(0, 4):
    t20.append(6)


t10 = []
for i in range(0, 15):
    t10.append(0)
for i in range(0, 20):
    t10.append(1)
for i in range(0, 15):
    t10.append(2)
for i in range(0, 5):
    t10.append(3)
for i in range(0, 8):
    t10.append(4)
for i in range(0, 6):
    t10.append(5)
for i in range(0, 5):
    t10.append(6)

t20_target = []
for i in range(0, 19):
    t20_target.append(0)
for i in range(0, 23):
    t20_target.append(1)
for i in range(0, 16):
    t20_target.append(2)
for i in range(0, 4):
    t20_target.append(3)
for i in range(0, 8):
    t20_target.append(4)
for i in range(0, 7):
    t20_target.append(5)
for i in range(0, 7):
    t20_target.append(6)

t20_target_2 = []
for i in range(0, 28):
    t20_target_2.append(0)
for i in range(0, 30):
    t20_target_2.append(1)
for i in range(0, 14):
    t20_target_2.append(2)
for i in range(0, 4):
    t20_target_2.append(3)
for i in range(0, 6):
    t20_target_2.append(4)
for i in range(0, 3):
    t20_target_2.append(5)
for i in range(0, 4):
    t20_target_2.append(6)

t20_target_extreme = []
for i in range(0, 15):
    t20_target_extreme.append(0)
for i in range(0, 20):
    t20_target_extreme.append(1)
for i in range(0, 15):
    t20_target_extreme.append(2)
for i in range(0, 4):
    t20_target_extreme.append(3)
for i in range(0, 7):
    t20_target_extreme.append(4)
for i in range(0, 9):
    t20_target_extreme.append(5)
for i in range(0, 9):
    t20_target_extreme.append(6)

ODI_target = []
for i in range(0, 56):
    ODI_target.append(0)
for i in range(0, 50):
    ODI_target.append(1)
for i in range(0, 16):
    ODI_target.append(2)
for i in range(0, 5):
    ODI_target.append(3)
for i in range(0, 10):
    ODI_target.append(4)
for i in range(0, 7):
    ODI_target.append(5)
for i in range(0, 5):
    ODI_target.append(6)

ODI_target_2 = []
for i in range(0, 90):
    ODI_target_2.append(0)
for i in range(0, 40):
    ODI_target_2.append(1)
for i in range(0, 21):
    ODI_target_2.append(2)
for i in range(0, 5):
    ODI_target_2.append(3)
for i in range(0, 6):
    ODI_target_2.append(4)
for i in range(0, 2):
    ODI_target_2.append(5)
for i in range(0, 2):
    ODI_target_2.append(6)

def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum

def add_array(a1, a2):
    for i in range(0, len(a2)):
         a1.append(a2[i])
    return a1

def sum_int_without_X(a):
    s = 0
    for i in range(0, len(a)):
        if a[i] != 'X':
            s += int(a[i])
    return s

def sum_int_without_5(a):
    s = 0
    for i in range(0, len(a)):
        if a[i] != 5:
            s += int(a[i])
    return s

#remove s1 from s
def remove_str(s, s1):
    a = ""
    ind = s.index(s1)
    for i in range(0, ind):
        a = a + s[i]
    for i in range(ind + len(s1), len(s)):
        a = a + s[i]
    return a

def name_without_format(a):
    ar = ["T20", "ODI", "TEST"]
    s = ""
    for i in ar:
        if i in a:
            s = s + remove_str(a, i)
    if s == "":
        s = a
    return s

NewZealandT20 = "Finn Allen,Devon Conway,Kane Williamson(c),Glenn Phillips,Jimmy Neesham,Mark Chapman,Michael Santner,Ish Sodhi,Tim Southee,Lockie Ferguson,Trent Boult"
NewZealandODI = "Devon Conway,Rachin Ravindra,Kane Williamson(c),Daryl Mitchell,Tom Latham,Glenn Phillips,Mark Chapman,Mitchell Santner,Tim Southee,Trent Boult,Lockie Ferguson"
NewZealandTest = "Tom Latham,Devon Conway,Kane Williamson(c),Rachin Ravindra,Daryl Mitchell,Tom Blundell,Glenn Phillips,Trent Boult,Matt Henry,Tim Southee,Ben Sears"
NewZealandT20Women = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabelle Gaze,Rosemary Mair,Lea Tahuhu,Eden Carson,Fran Jonas"
NewZealandODIWomen = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabelle Gaze,Hannah Rowe,Jess Kerr,Molly Penfold,Fran Jonas"
NewZealandTestWomen = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabelle Gaze,Hannah Rowe,Jess Kerr,Molly Penfold,Fran Jonas"
AustraliaT20 = "Travis Head,Jake Fraser-McGurk,Mitchell Marsh(c),Glenn Maxwell,Marcus Stoinis,Matthew Wade,Tim David,Ashton Agar,Pat Cummins,Mitchell Starc,Adam Zampa"
AustraliaODI = "Travis Head,Jake Fraser-McGurk,Steve Smith,Marnus Labuchagne,Glenn Maxwell,Alex Carey,Mitchell Marsh,Pat Cummins(c),Mitchell Starc,Adam Zampa,Jason Behrendoff"
AustraliaTest = "Travis Head,Usman Khawaja,Marnus Labuchagne,Steve Smith,Mitchell Marsh,Cameron Green,Pat Cummins(c),Mitchell Starc,Nathan Lyon,Scott Boland,Josh Hazlewood"
AustraliaT20Women = "Alyssa Healy,Beth Mooney,Georgia Wareham,Tahlia McGrath(c),Ellyse Perry,Phoebe Litchfield,Ashleigh Gardner,Annabel Sutherland,Sophie Molineux,Megan Schutt,Darcie Brown"
AustraliaODIWomen = "Alyssa Healy,Beth Mooney,Georgia Wareham,Tahlia McGrath(c),Ellyse Perry,Phoebe Litchfield,Ashleigh Gardner,Annabel Sutherland,Sophie Molineux,Megan Schutt,Darcie Brown"
AustraliaTestWomen = "Beth Mooney,Phoebe Litchfield,Ellyse Perry,Tahlia McGrath,Jess Jonassen,Alyssa Healy(c),Ashleigh Gardner,Annabel Sutherland,Alan King,Kim Garth,Darcie Brown"
IndiaT20 = "Rohit Sharma(c),Abhishek Sharma,Virat Kohli,SKY,Rishabh Pant,Shivam Dube,Rinku Singh,Avesh Khan,Mayank Yadav,Yuzi Chahal,Jasprit Bumrah"
IndiaODI = "Rohit Sharma(c),Shubman Gill,Virat Kohli,Shreyash Iyer,SKY,Rinku Singh,Ravindra Jadeja,Jasprit Bumrah,Mohd Shami,Kuldeep Yadav,Mohd Siraj"
IndiaTest = "Rohit Sharma(c),Yashasvi Jaiswal,Shubman Gill,Virat Kohli,Sarfaraz Khan,Ravindra Jadeja,Rishabh Pant,Ravi Ashwin,Kuldeep Yadav,Jasprit Bumrah,Mohd Siraj"
IndiaT20Women = "Shafali Verma,Smriti Mandhana,Jemimah Rodrigues,Harmanpreet Kaur(c),Deepti Sharma,Richa Ghosh,Pooja Vastrakar,Arundhati Reddy,Shreyanka Patil,Radha Yadav,Renuka Singh"
IndiaODIWomen = "Shafali Verma,Smriti Mandhana,Dayalan Hemalatha,Harmanpreet Kaur(c),Jemimah Rodrigues,Richa Ghosh,Deepti Sharma,Pooja Vastrakar,Radha Yadav,Asha Sobhana,Renuka Singh"
IndiaTestWomen = "Shafali Verma,Smriti Mandhana,Shubha Satheesh,Jemimah Rodrigues,Harmanpreet Kaur(c),Richa Ghosh,Deepti Sharma,Pooja Vastrakar,Shen Rana,Renuka Singh,Rajeshwari Gayakwad"
EnglandODI = "Phil Salt,Zack Crawley,Joe Root,Harry Brook,Jos Buttler(c),Ben Stokes,Sam Curran,Chris Woakes,Adil Rashid,Reese Topley,Mark Wood"
EnglandT20 = "Phil Salt,Jos Buttler(c),Will Jacks,Liam Livingstone,Harry Brook,Ben Stokes,Sam Curran,Chris Woakes,Reese Topley,Adil Rashid,Mark Wood"
EnglandTest = "Zack Crawley,Ben Duckett,Joe Root,Harry Brook,Ben Stokes(c),Jamie Smith,Chris Woakes,Gus Atkinson,Jofra Archer,Ollie Robinson,Jack Leach"
EnglandT20Women = "Maia Bouchier,Danni Wyatt-Hodge,Alice Capsey,Nat Sciver-Brunt,Heather Knight(c),Amy Jones,Charlie Dean,Kate Cross,Sophie Ecclestone,Sarah Glenn,Lauren Bell"
EnglandODIWomen = "Tammy Beaumont,Maia Bouchier,Heather Knight(c),Nat Sciver-Brunt,Danni Wyatt-Hodge,Amy Jones,Alice Capsey,Charlie Dean,Sophie Ecclestone,Kate Cross,Lauren Bell"
EnglandTestWomen = "Maia Bouchier,Tammy Beaumont,Heather Knight(c),Nat Sciver-Brunt,Sophia Dunkley,Danni Wyatt-Hodge,Amy Jones,Sophie Ecclestone,Kate Cross,Lauren Filer,Lauren Bell"
SouthAfricaT20 = "Reeza Hendricks,QDK,Aiden Markram(c),Tristan Stubbs,Heinrich Klaasen,David Miller,Marco Jansen,Keshav Maharaj,Kagiso Rabada,Anrich Nortje,Tabraiz Shamsi"
SouthAfricaODI = "QDK,Temba Bavuma(c),Rassie van der Dussen,Aiden Markram,Heinrich Klaasen,David Miller,Marco Jensen,Gerald Coetzee,Keshav Maharaj,Kagiso Rabada,Tabraiz Shamsi"
SouthAfricaTEST = "Aiden Markram,Temba Bavuma(c),Tony de Zorzi,Keegan Petersen,David Bedingham,Kyle Verreynne,Marco Jansen,Gerald Coetzee,Kagiso Rabada,Nandre Burger,Anrich Nortje"
SouthAfricaT20Women = "Laura Wolvaardt(c),Tazmin Brits,Anneke Bosch,Marizanne Kapp,Nadine de Klerk,Chloe Tryon,Sune Luus,Annerie Dercksen,Sinalo Jafta,Nonkululeko Mlaba,Ayabonga Khaka"
SouthAfricaODIWomen = "Laura Wolvaardt(c),Tazmin Brits,Anneke Bosch,Sune Luus,Marizanne Kapp,Nadine de Klerk,Nondumiso Shangase,Mieke de Ridder,Masabata Klaas,Nonkululeko Mlaba,Ayabonga Khaka"
SouthAfricaTESTWomen = "Laura Wolvaardt(c),Anneke Bosch,Sune Luus,Marizanne Kapp,Delmari Tucker,Nadine de Klerk,Sinalo Jafta,Annerie Dercksen,Tumi Sekhukhune,Masabata Klaas,Nonkululeko Mlaba"
WestIndiesT20 = "Lendl Simmons,Evin Lewis,Chris Gayle,Nicholas Pooran,Shimron Hetmyer,Andre Russell,Keiron Pollard(c),Jason Holder,Obed McCoy,Fidal Edward,Hayden Walsh Jr."
WestIndiesODI = "Evin Lewis,Shai Hope,Darren Bravo,Shimron Hetmyer,Nicholas Pooran,Keiron Pollard(c),Jason Holder,Alzarri Joseph,Hayden Walsh Jr,Sheldon Cottrell,Oshane Thomas"
WestIndiesTest = "Kraigg Brathwaite(c),Keiran Powell,Nkrumah Bonner,Roston Chase,Jermaine Blackwood,Kyle Mayers,Jason Holder,Joshua Da Silva,Kemar Roach,Jomel Warrican,Jayden Seales"
WestIndiesT20Women = "Hayley Matthews(c),Qiana Joseph,Shemaine Campbelle,Stafanie Taylor,Deandra Dottin,Aaliyah Alleyne,Afy Fletcher,Chedean Nation,Zaida James,Ashmini Munisar,Karishma Ramharack"
WestIndiesODIWomen = "Hayley Matthews(c),Rashada Williams,Shemaine Campbelle,Stafanie Taylor,Chinelle Henry,Chedean Nation,Aaliyah Alleyne,Afy Fletcher,Zaida James,Karishma Ramharack,Shamilia Connell"
WestIndiesTestWomen = "Hayley Matthews(c),Rashada Williams,Shemaine Campbelle,Stafanie Taylor,Chinelle Henry,Chedean Nation,Aaliyah Alleyne,Afy Fletcher,Zaida James,Karishma Ramharack,Shamilia Connell"
RCB = "Devdutt Padikkal,Finn Allen,Virat Kohli,ABD,Glenn Maxwell(c),Mohd Azharuddin,Kyle Jamieson,Shahbaz Ahmed,Harshal Patel,Mohd Siraj,Yuzi Chahal"
MI = "QDK,Rohit Sharma(c),SKY,Ishan Kishan,Hardik Pandya,Keiron Pollard,Jimmy Neesham,Krunal Pandya,Rahul Chahar,Jaspreet Bumrah,Trent Boult"
RR = "Sanju Samson(c),Jos Butler,Yashasvi Jaiswal,Ben Stokes,Rahul Tewatia,Riyan Parag,Chris Morris,Jofra Archer,Shreyas Gopal,Kartik Tyagi,Chetan Sakaria"
SRH = "David Warner,Jonny Bairstow,Kane Williamson(c),Manish Pandey,Priyam Garg,Abdul Samad,Kedar Jadhav,Rashid Khan,Bhuvi Kumar,T Natarajan,Sandeep Sharma"
DC = "Prithvi Shaw,Shikhar Dhawan,Ajinkya Rahane,Shreyash Iyer,Rishabh Pant(c),Marcus Stoinis,Chris Woakes,Ravi Ashwin,Axar Patel,Anrich Nortje,Kagiso Rabada"
KXIP = "KL Rahul(c),Mayank Agarwal,Chris Gayle,Nicholas Pooran,Shah Rukh Khan,Deepak Hooda,Chris Jordan,Ravi Bishnoi,Murugan Ashwin,Jhye Richardson,Mohd Shami"
PeanutButter = "Peanut Butter(c),Peanut Sandwich,Peanut Pancake,Peanut Burger,Peanut Lasagne,Peanut Colada,Sergeant Peanut,Peanut Calculus,Square Peanut,Peanut Biryani,Peanut Rice"
DahliaXI = "Viral C(c),Harsha V,Akshit S,Ayush S,Bunny,Joshua L,Nikhil G,Anchit K,Devajya K,Aryan,Rishit"
SDS = "Viral C(c),Zehaan Naik,Aditya V,Ishi Jain,Nandini Bhattad,Raghav Govind,Subham Anand,Yash Bihany,Devansh Gupta,P Sarath,Priyanshu Gupta"
Beatles = "Paul McCartney,Ringo Starr,George Harrison,John Lennon(c),George Martin,Brian Epstein,Eleanor Rigby,Billy Shears,Geoff Emerick,Sergeant Pepper,Mr Kite"
WomenArtist = "Olivia Rodrigo(c),Sabrina Carpenter,Lana Del Rey,Leah Kate,Dua Lipa,Dasha,Adele,Katy Perry,Avril Lavigne,Linda Ronstadt,Tiffany Stringer"
ModernFamily = "Phil Dunphy(c),Luke Dunphy,Claire Dunphy,Cam Tucker,Jay Pritchett,Lily Tucker-Pritchett,Manny Delgado,Alex Dunphy,Mitchell Pritchett,Gloria Pritchett,Haley Dunphy"
print("Pre defined Teams - New Zealand, Australia, India, England, South Africa(SA), West Indies(WI), RCB, MI, RR, SRH, DC, KXIP, PeanutButter(PB), DahliaXI, Beatles, WomenArtist(WA), ModernFamily(MF), SDS")
Teams = [NewZealandT20, NewZealandODI, NewZealandTest, NewZealandT20Women, NewZealandODIWomen, NewZealandTestWomen, AustraliaODI, AustraliaT20, AustraliaTest, AustraliaODIWomen, AustraliaT20Women, AustraliaTestWomen, IndiaODI, IndiaT20, IndiaTest, IndiaODIWomen, IndiaT20Women, IndiaTestWomen, EnglandT20, EnglandODI, EnglandTest, EnglandT20Women, EnglandODIWomen, EnglandTestWomen, SouthAfricaT20, SouthAfricaODI, SouthAfricaTEST, SouthAfricaT20Women, SouthAfricaODIWomen, SouthAfricaTESTWomen, WestIndiesT20, WestIndiesODI, WestIndiesTest, WestIndiesT20Women, WestIndiesODIWomen, WestIndiesTestWomen, RCB, MI, RR, SRH, DC, KXIP, PeanutButter, DahliaXI, Beatles, WomenArtist, ModernFamily, SDS]
t = ["NZT20", "NZODI", "NZTEST", "NZWT20", "NZWODI", "NZWTEST", "AUSODI", "AUST20", "AUSTEST", "AUSWODI", "AUSWT20", "AUSWTEST", "INDODI", "INDT20", "INDTEST", "INDWODI", "INDWT20", "INDWTEST", "ENGT20", "ENGODI", "ENGTEST", "ENGWT20", "ENGWODI", "ENGWTEST", "SAT20", "SAODI", "SATEST", "SAWT20", "SAWODI", "SAWTEST", "WIT20", "WIODI", "WITEST", "WIWT20", "WIWODI", "WIWTEST", "RCB", "MI", "RR", "SRH", "DC", "KXIP", "PB", "DAHLIAXI", "BEATLES", "WA", "MF", "SDS"]
Te = input("Pre defined or Custom?(P/C) : ").upper()

def is_series():
    n = input("Series/Single : ")
    return n.upper()

def names():
    n2 = input("Home Team : ").upper()
    n1 = input("Visiting Team : ").upper()
    array = [n1, n2]
    return array

names = names()

def name_to_team(n):
    ar = []
    for i in range(0, len(t)):
        if t[i] == n:
            ar = Teams[i]
    return ar

def team():
    T1 = []
    T2 = []
    if Te == "P":
        if names[0] and names[1] in t:
            T1 = name_to_team(names[0])
            T2 = name_to_team(names[1])
        if names[0] not in t and names[1] in t:
            T2 = name_to_team(names[1])
            T1 = input("Team not predefined. Enter " + names[0] + " team : ")
        if names[1] not in t and names[0] in t:
            T1 = name_to_team(names[0])
            T2 = input("Team not predefined. Enter " + names[1] + " team : ")
        if names[0] not in t and names[1] not in t:
            T1 = input("Team not predefined. Enter " + names[0] + " team : ")
            T2 = input("Team not predefined. Enter " + names[1] + " team : ")
    elif Te == "C":
        T1 = input("Enter " + names[0] + " team : ")
        T2 = input("Enter " + names[1] + " team : ")
    array = [T1, T2]
    return array

te = team()

def Team_array():
    T1 = te[0].upper().split(",")
    T2 = te[1].upper().split(",")
    return [T1, T2]

teams = Team_array()

def lineup():
    print("The batting lineup is out, and...")
    print(names[0] + " - " + str(teams[0]))
    print(names[1] + " - " + str(teams[1]))

def types():
    n = input("T10/T20/ODI/Test/Custom : ")
    return n.upper()

def balls(t):
    if t == "CUSTOM":
        n = int(input("Number of balls : "))
        return n
    if t == "T10":
        n = 60
        return n
    if t == "T20":
        n = 120
        return n
    if t == "ODI":
        n = 300
        return n


def wickets(a):
    n = len(a) - 1
    return n

wicket = wickets(teams[0])

def balls_array(b, w, a):    #b is balls, w is wickets
    array = []
    while array.count(5) < w and len(array) < b:
        array.append(a[random.randint(0, len(a) - 1)])
        if array.count(5) == w or len(array) == b:
            break
    return array

def total(a):
    total = sum_array(a) - 5*a.count(5)
    return total

def indexes(a, n):
    ar = []
    for i in range(0, len(a)):
        if a[i] == n:
            ar.append(i)
    return ar
# a = [Hello, World, Don, Kon]
# a1 = [1, 6, 3, 4, 2, 5, 6, 4, 5]
def partnership(a, a1, r): # a is array of players, a1 is array of balls_output, r is Runs/Balls array(how he scored runs)
    a2 = a.copy()
    a3 = r
    di = dict(zip(a2, a3))
    for i in range(0, len(a1) - 1):
        if a1[i] % 2 == 0:
            L = di[a2[0]]
            L.append(a1[i])
            di[a2[0]] = L
            a2 = a2
        if a1[i] % 2 == 1:
            L = di[a2[0]]
            L.append(a1[i])
            di[a2[0]] = L
            a2 = a2[::-1]
    if a1 == []:
        di = dict(zip(a2, a3))
        return di
    if a1[-1] == 5:
        L = di[a2[0]]
        L.append('X')
        di[a2[0]] = L
    if a1[-1] != 5:
        L = di[a2[0]]
        L.append(a1[-1])
        di[a2[0]] = L
    return di

def split_1(a, n):
    ar = []
    ar1 = indexes(a, n)
    if len(ar1) == 0:
        ar.append(a)
    elif len(ar1) > 0:
        if a[0] != n:
            ar.append(a[:ar1[0] + 1])
            for i in range(0, len(ar1) - 1):
                ar.append(a[ar1[i] + 1 : ar1[i + 1] + 1])
        if a[0] == n:
            ar.append([n])
            for i in range(0, len(ar1) - 1):
                ar.append(a[ar1[i] + 1 : ar1[i + 1] + 1])
        if a[-1] != n:
            ar.append(a[ar1[-1] + 1 : len(a) + 1])
    if len(ar) < wickets(te[0]):
        for i in range(0, wickets(te[0]) - len(ar)):
            ar.append([])
    return ar

def append_dict(D1, D2):
    for d in D2.keys():
        if d in D1.keys():
            L = D1[d]
            L1 = D2[d]
            L = add_array(L, L1)
            D1[d] = L
    return D1

def empty_arrays(n):
    a = []
    for i in range(0, n):
        a.append([])
    return a


# a is array of players, a11 is array of balls_output, r is Runs/Balls array
def partnerships(a, a11, r):
    di = dict(zip(a, r))
    f = add_array(split_1(a11, 5), empty_arrays(len(a) - 1 - a11.count(5)))
    Opening_Partnership = partnership([a[0], a[1]], f[0], [[], []])
    if a11[0] == 5:
        Opening_Partnership = {a[0] : ['X'], a[1] : []}
    di = append_dict(di, Opening_Partnership)
    for i in range(2, len(a)):
        p1 = a[i]
        p2 = ''
        for j in range(0, i):
            if 'X' not in di[a[j]]:
                p2 = a[j]
        r1 = [[], []]
        p = partnership([p1, p2], f[i - 1], r1)
        di = append_dict(di, p)
    return di

def partnership_shares(a, w):
    ar = split_1(a, 5)
    wi = a.count(5)
    for i in range(0, len(ar)):
        if len(ar[i]) > 0:
            print("Partnership for wicket number " + str(i + 1) + " : " + str(sum_int_without_5(ar[i])) + " off " + str(len(ar[i])) + " balls.")
    s = 0
    b = 0
    print("")
    print("Fall of Wickets - ")
    print("")
    if wi == 0:
        print("None fell.")
        print()
        return
    for i in range(0, wi):
        if len(ar[i]) > 0:
            s += sum_int_without_5(ar[i])
            b += len(ar[i])
            print(str(s) + "/" + str(i + 1) + "  (" + str(b//6) + "." + str(b%6) + " Overs)")
    print()
"""
    if wi == 10:
        i = 9
        s += sum_int_without_5(ar[i])
        b += len(ar[i])
        print(str(s) + "/" + str(i + 1) + "  (" + str(b // 6) + "." + str(b % 6) + " Overs)")
"""











def split(a, n):
    ar = []
    ar1 = indexes(a, n)
    if len(ar1) == 0:
        ar = a
    elif len(ar1) > 0:
        if a[0] != n:
            ar.append(a[:ar1[0]])
            for i in range(0, len(ar1) - 1):
                ar.append(a[ar1[i] + 1 : ar1[i + 1]])
        if a[0] == n:
            ar.append([])
            for i in range(0, len(ar1) - 1):
                ar.append(a[ar1[i] + 1 : ar1[i + 1]])
        if a[-1] != n:
            ar.append(a[ar1[-1] + 1 : len(a) + 1])
    return ar

def array_score(a, w):
    ar = []
    spl = split(a, 5)
    if a.count(5) == w:
        for i in range(0, w):
            ar.append(str(sum_array(spl[i])) + "(" + str(len(spl[i]) + 1) + ")")
    if 0 < int(a.count(5)) < int(w):
        for i in range(0, a.count(5)):
            ar.append(str(sum_array(spl[i])) + "(" + str(len(spl[i]) + 1) + ")")
        ar.append(str(sum_array(a[indexes(a, 5)[-1] + 1:len(a)])) + "(" + str(len(a[indexes(a, 5)[-1] + 1:len(a)])) + ")")
        for i in range(0, w - a.count(5) - 1):
            ar.append('-')
    if a.count(5) == 0:
        ar.append(str(sum_array(a)) + "(" + str(len(a)) + ")")
        for i in range(0, w - 1):
            ar.append('-')
    return ar

def score_players(a1, a, w): # a1 is players names, a is balls_array, w is wickets
    if a.count(5) >= w:
        arr = []
        k = indexes(a, 5)[w - 1]
        for i in range(0, k + 1):
            arr.append(a[i])
        a = arr
    if a.count(5) < w:
        a = a
    r = empty_arrays(len(a1))
    d = partnerships(a1, a, r)
    d1 = dict(zip(a1, r))
    for p in d.keys():
        runs = sum_int_without_X(d[p])
        balls = len(d[p])
        d1[p] = [runs, balls]
    return d1

def array_score_from_dict(a1, a, w):
    d = score_players(a1, a, w)
    ar = []
    for j in d.keys():
        ar.append(str(d[j][0]) + "(" + str(d[j][1]) + ")")
    return ar

def array_score_1(a, w):
    ar = []
    spl = split(a, 5)
    if a.count(5) == w:
        for i in range(0, w):
            ar.append((str(sum_array(spl[i])),str(len(spl[i]) + 1)))
    if 0 < int(a.count(5)) < int(w):
        for i in range(0, a.count(5)):
            ar.append((str(sum_array(spl[i])), str(len(spl[i]) + 1)))
        ar.append((int(sum_array(a[indexes(a, 5)[-1] + 1:len(a)])), int(len(a[indexes(a, 5)[-1] + 1:len(a)]))))
        for i in range(0, w - a.count(5) - 1):
            ar.append(('-', '-'))
    if a.count(5) == 0:
        ar.append((int(sum_array(a)), int(len(a))))
        for i in range(0, w - 1):
            ar.append(('-', '-'))
    return ar

def replace(a, n1, n2): #n1 to be replaced
    arr = a.copy()
    f = indexes(a, n1)
    for i in f:
        arr[i] = n2
    return arr

def stats_array_score(a):
    arr = array_score_1(a, wicket)
    for i in range(0, a.count(('-', '-'))):
        arr = replace(arr, ('-', '-'), (0, 0))
    arr1 = []
    arr2 = []
    for i in range(0, len(arr)):
        if arr[i] != ('-', '-'):
            arr1.append(int(arr[i][0]))
            arr2.append(int(arr[i][1]))
        if arr[i] == ('-', '-'):
            arr1.append(0)
            arr2.append(0)
    return [arr1, arr2]

def batting_second(a, n):
    ar = []
    if total(a) <= n:
        ar = a
    if total(a) > n:
        for i in range(0, len(a)):
            if total(a[:i]) <= n and total(a[:i + 1]) > n:
                ar = a[:i + 1]
    return ar

def toss():
    d = {}
    n1 = input(str(names[0]) + "'s call : Heads or Tails (H/T) : ")
    C = ["H", "T"]
    n2 = random.randint(0, 1)
    b = ["BAT", "BOWL"]
    if n1.upper() == C[n2]:
        n3 = input(names[0] + " wins the toss and chooses to : ").upper()
        while n3 not in b:
            n3 = input(names[0] + " wins the toss and chooses to : ").upper()
        else:
            d[names[0]] = n3.upper()
            d[names[1]] = b[1 - b.index(n3.upper())]
    if n1.upper() != C[n2]:
        n4 = input(names[1] + " wins the toss and chooses to : ").upper()
        while n4 not in b:
            n4 = input(names[1] + " wins the toss and chooses to : ").upper()
        else:
            d[names[1]] = n4.upper()
            d[names[0]] = b[1 - b.index(n4.upper())]
    ar = []
    T = names
    if d[T[0]] == "BAT":
        ar.append(T[0])
        ar.append(T[1])
    if d[T[0]] == "BOWL":
        ar.append(T[1])
        ar.append(T[0])
    return ar

def Test(a, w):
    w1 = 0
    ar = []
    while w1 < w:
        f = random.randint(0, len(a) - 1)
        ar.append(a[f])
        if a[f] == 5:
            w1 += 1
        if a[f] != 5:
            w1 += 0
    return ar

def remove_common(L):
    l = L.copy()
    L1 = []
    for i in l:
        if i not in L1:
            L1.append(i)
        if i in L1:
            pass
    return L1

def max_dict(d):
    a = max(d.values())
    v = ""
    for i in d.keys():
        if d[i] == a:
            v = i
    return v

#U = type()
def many_zero(n):
    L = []
    for i in range(0, n):
        L.append(0)
    return L

def cut_list(L, n):
    L1 = []
    for i in range(0, n):
        L1.append(L[i])
    return L1

def add_dict(D1, D2):
    D = D1.copy()
    for i in D2.keys():
        D[i] = D2[i]
    return D

def dict_arrange(d):
    d1 = list(d.values())
    d1.sort()
    de = d1[::-1]
    ar = []
    for i in range(0, len(d1)):
        for j in d:
            if d[j] == de[i]:
                ar.append(j)
    return ar

def runs_stats(D):
    L = dict_arrange(D)
    L = remove_common(L)
    for i in range(0, len(L)):
        print(str(i + 1) + ") " + str(L[i]) + " - " + str(D[L[i]]) + " runs")
    print()

def avg_stats(D):
    L = dict_arrange(D)
    L = remove_common(L)
    for i in range(0, len(L)):
        print(str(i + 1) + ") " + str(L[i]) + " - " + str(D[L[i]]))
    print()

def high_score_stats(D):
    L = dict_arrange(D)
    L = remove_common(L)
    L = cut_list(L, 15)
    for i in range(0, len(L)):
        print(str(i + 1) + ") " + str(L[i]) + " - " + str(D[L[i]]))
    print()

def impact_stats(D):
    L = dict_arrange(D)
    L = remove_common(L)
    L = cut_list(L, 20)
    for i in range(0, len(L)):
        print(str(i + 1) + ") " + str(L[i]) + " - " + str(round(D[L[i]], 2)))
    print()

def strike_rate(D1, D2): # D1 is runs, D2 is balls dict
    D3 = {}
    for i in D1:
        if D2[i] >= 20:
            D3[i] = round((D1[i] * 100/float(D2[i])), 2)
        if D2[i] < 20:
            pass
    return D3

def strike_rate_1(D1, D2):
    D3 = {}
    for i in D1:
        if D2[i] != 0:
            D3[i] = round((D1[i] * 100 / float(D2[i])), 2)
        if D2[i] == 0:
            D3[i] = 0
    return D3

def addendum(L, s):
    L1 = []
    for i in range(0, len(L)):
        L1.append(L[i] + str(s))
    return L1

def strike_rate_stats(D):
    L = dict_arrange(D)
    L = remove_common(L)
    for i in range(0, len(L)):
        print(str(i + 1) + ") " + str(L[i]) + " - " + str(D[L[i]]))
    print()

def y_axis(a):
    p = []
    for i in range(0, len(a)):
        p.append(total(a[:i + 1]))
    return p


D7 = dict(zip(te[0].upper().split(",") + te[1].upper().split(","), many_zero(2 * wicket + 2)))
#print(D7)
d = {name_without_format(names[0]) : 0, name_without_format(names[1]) : 0}
def scorecard(b, U, d, D4, D10, D15, D_avg, k):
#    type = U
    w = wicket
    a3 = []
    a4 = []
    if U == "TEST":
        a3 = Tests
    if U == "ODI":
        a3 = ODI
    if U == "T20":
        a3 = t20
    if U == "T10":
        a3 = t10
    if U == "CUSTOM":
        if b <= 90:
            a3 = t10
        if 90 < b <= 180:
            a3 = t20
        if 180 < b < 600:
            a3 = ODI
        if b >= 600:
            a3 = Tests
#    b = 0
    a1 = []
    a2 = []
    if U != "TEST" and U != "ODI" and U != "T20":
#        b = balls(U)
        a1 = balls_array(b, w, a3)
        a2 = balls_array(b, w, a3)
    if U == "TEST":
        a1 = Test(a3, w)
        a2 = Test(a3, w)
    if U == "ODI":
        b = 300
        a1 = balls_array(b, w, a3)
        if total(a1) > 300:
            a2 = balls_array(b, w, ODI_target)
        if total(a1) < 235:
            a2 = balls_array(b, w, ODI_target_2)
        else:
            a2 = balls_array(b, w, a3)
    if U == "T20":
        b = 120
        a1 = balls_array(b, w, t20)
        if total(a1) >= 174 and total(a1) < 200:
            a2 = balls_array(b, w, t20_target)
        if total(a1) >= 200:
            a2 = balls_array(b, w, t20_target_extreme)
        if total(a1) <= 135:
            a2 = balls_array(b, w, t20_target_2)
        else:
            a2 = balls_array(b, w, t20)
    r = []
    for i in range(0, w + 1):
        r.append([])
    Names = names # name of team
    Teams = teams # players of team
    D = dict(zip(Names, Teams))
    a2 = batting_second(a2, total(a1))
    Bat_Score_1 = array_score_from_dict(Teams[0], a1, w)
#    print(Bat_Score_1)
    Bat_Score_2 = array_score_from_dict(Teams[1], a2, w)
#    print(Bat_Score_2)
    y1 = y_axis(a1)
    y2 = y_axis(a2)
    balls1 = []
    balls2 = []
    for i in range(0, len(y1)):
        balls1.append(i)
    for j in range(0, len(y2)):
        balls2.append(j)
    T = toss()
    if T[0] == Names[0]:
        D = D
    if T[0] == Names[1]:
        Names = Names[::-1]
        Teams = Teams[::-1]
        D = dict(zip(Names, Teams))
    all_players = Teams[0] + Teams[1]
    if U == "T20":
        if Names[0] or Names[1] not in team_in_T20():
                cursor.execute("select no from team_{}".format(U))
                n = len(cursor.fetchall())
                for i in [Names[0], Names[1]]:
                    if i not in team_in_T20():
                        n += 1
                        cursor.execute("insert into team_{} (No, Team, Highest_Score) values ({}, '{}', 0)".format(U, n, i))
                        mycon.commit()
        for i in remove_c_array(all_players):
            cursor.execute("select no from player_{}".format(U))
            n = len(cursor.fetchall())
            if i not in player_in_T20():
                n += 1
                cursor.execute("insert into player_{} (No, Name, Matches) values ({}, '{}', {})".format(U, n, i, 1))
                mycon.commit()
            else:
                cursor.execute("update player_{} set Matches = Matches + 1 where Name = '{}'".format(U, i))
                mycon.commit()
    if U == "ODI":
        if Names[0] or Names[1] not in team_in_ODI():
                cursor.execute("select no from team_{}".format(U))
                n = len(cursor.fetchall())
                for i in [Names[0], Names[1]]:
                    if i not in team_in_ODI():
                        n += 1
                        cursor.execute("insert into team_{} (No, Team, Highest_Score) values ({}, '{}', 0)".format(U, n, i))
                        mycon.commit()
        for i in remove_c_array(all_players):
            cursor.execute("select no from player_{}".format(U))
            n = len(cursor.fetchall())
            if i not in player_in_ODI():
                n += 1
                cursor.execute("insert into player_{} (No, Name, Matches) values ({}, '{}', {})".format(U, n, i, 1))
                mycon.commit()
            else:
                cursor.execute("update player_{} set Matches = Matches + 1 where Name = '{}'".format(U, i))
                mycon.commit()
    if U == "TEST":
        if Names[0] or Names[1] not in team_in_TEST():
                cursor.execute("select no from team_{}".format(U))
                n = len(cursor.fetchall())
                for i in [Names[0], Names[1]]:
                    if i not in team_in_TEST():
                        n += 1
                        cursor.execute("insert into team_{} (No, Team, Highest_Score) values ({}, '{}', {})".format(U, n, i, 0))
                        mycon.commit()
        for i in remove_c_array(all_players):
            cursor.execute("select no from player_{}".format(U))
            n = len(cursor.fetchall())
            if i not in player_in_TEST():
                n += 1
                cursor.execute("insert into player_{} (No, Name, Matches) values ({}, '{}', {})".format(U, n, i, 1))
                mycon.commit()
            else:
                cursor.execute("update player_{} set Matches = Matches + 1 where Name = '{}'".format(U, i))
                mycon.commit()

    P1 = partnerships(Teams[0], a1, r)
    r = []
    for i in range(0, w + 1):
        r.append([])
    P2 = partnerships(Teams[1], a2, r)
    Not_Outs_1 = []
    Not_Outs_2 = []
    for i in P1.keys():
        if P1[i] != []:
            if str(P1[i][-1]) != 'X':
                Not_Outs_1.append(i)
            if str(P1[i][-1]) == 'X':
                D_avg[i] += 1
    for i in P2.keys():
        if P2[i] != []:
            if str(P2[i][-1]) != 'X':
                Not_Outs_2.append(i)
            if str(P2[i][-1]) == 'X':
                D_avg[i] += 1
#    score_players(player_list, ball_array, wickets) - returns player_name : [run, ball]
    Player_Score_Dict_1 = score_players(Teams[0], a1, w)
 #   print(Player_Score_Dict_1)
    Player_Score_Dict_2 = score_players(Teams[1], a2, w)

    Runs_array_1 = []
    Balls_array_1 = []
    Runs_array_2 = []
    Balls_array_2 = []
    for j in Teams[0]:
        Runs_array_1.append(Player_Score_Dict_1[j][0])
        Balls_array_1.append(Player_Score_Dict_1[j][1])
    for j in Teams[1]:
        Runs_array_2.append(Player_Score_Dict_2[j][0])
        Balls_array_2.append(Player_Score_Dict_2[j][1])

    D1 = dict(zip(Teams[0], Runs_array_1))
    D2 = dict(zip(Teams[1], Runs_array_2))
    D6 = dict(zip(Teams[0], Balls_array_1))
    D8 = dict(zip(Teams[1], Balls_array_2))
    D9 = add_dict(D6, D8) # balls of all
    D3 = add_dict(D1, D2) # score of all
    D12 = dict(zip(addendum(Teams[0], " - Match " + str(k + 1)), Runs_array_1))
    D13 = dict(zip(addendum(Teams[1], " - Match " + str(k + 1)), Runs_array_2))
    D14 = add_dict(D12, D13)
    for i in D14:
        D15[i] = D14[i]

    for i in D3.keys():
        D4[i] = int(D4[i]) + int(D3[i])


    for i in D9:
        D10[i] += int(D9[i])

    print("")
    print("-----------------------------------------------")
    print(T[0] + (30 - len(T[0]))*" " + "Score" + 8 * " " + "S/R")
    print("-----------------------------------------------")
    for i in range(0, len(Teams[0])):
        s = str(Runs_array_1[i]) + "(" + str(Balls_array_1[i]) + ")"
        if s != "0(0)" and Teams[0][i] not in Not_Outs_1:
            print(Teams[0][i] + (30 - len(Teams[0][i])) * " " + s + (13 - len(s)) * " " + str(round(100 * Runs_array_1[i]/float(Balls_array_1[i]))))
            if U in ["T20", "ODI", "TEST"]:
                cursor.execute("update player_{} set Outs = Outs + 1 where Name = '{}'".format(U, remove_c(Teams[0][i])))
                cursor.execute("update player_{} set Highest = 0 where Name = '{}' and Highest is NULL".format(U, remove_c(Teams[0][i])))
                mycon.commit()
        if s != "0(0)" and Teams[0][i] in Not_Outs_1:
            print(Teams[0][i] + "*" + (29 - len(Teams[0][i])) * " " + s + (13 - len(s)) * " " + str(round(100 * Runs_array_1[i]/float(Balls_array_1[i]))))
            if U in ["T20", "ODI", "TEST"]:
                cursor.execute("update player_{} set Not_Outs = Not_Outs + 1 where Name = '{}'".format(U, remove_c(Teams[0][i])))
                cursor.execute("update player_{} set Highest = 0 where Name = '{}' and Highest is NULL".format(U, remove_c(Teams[0][i])))
                mycon.commit()
        if s == "0(0)":
            print(Teams[0][i] + (30 - len(Teams[0][i])) * " " + "-" + 12 * " " + "-")
        if U in ["TEST", "ODI", "T20"]:
            cursor.execute("update player_{} set Runs = Runs + {} where Name = '{}'".format(U, Runs_array_1[i], remove_c(Teams[0][i])))
            mycon.commit()
            if 50 <= Runs_array_1[i] < 100:
                cursor.execute("update player_{} set 50s = 50s + 1 where Name = '{}'".format(U, remove_c(Teams[0][i])))
                mycon.commit()
            if 100 <= Runs_array_1[i] < 200:
                cursor.execute("update player_{} set 100s = 100s + 1 where Name = '{}'".format(U, remove_c(Teams[0][i])))
                mycon.commit()
        if U in ["TEST", "ODI"] and Runs_array_1[i] >= 200:
            cursor.execute("update player_{} set 200s = 200s + 1 where Name = '{}'".format(U, remove_c(Teams[0][i])))
            mycon.commit()
        if U in ["TEST", "ODI", "T20"]:
            cursor.execute("update player_{} set Balls = Balls + {} where Name = '{}'".format(U, Balls_array_1[i], remove_c(Teams[0][i])))
            cursor.execute("update player_{} set Highest = {} where Name = '{}' and Highest < {}".format(U, Runs_array_1[i], remove_c(Teams[0][i]), Runs_array_1[i]))
            mycon.commit()
            cursor.execute("update player_{} set Strike_Rate = Runs/(Balls) * 100 where Name = '{}' and Balls != 0".format(U, remove_c(Teams[0][i])))
            cursor.execute("update player_{} set Avg = Runs/(Outs) where Name = '{}' and Outs != 0".format(U, remove_c(Teams[0][i])))
            cursor.execute("update player_{} set Avg = Runs where Name = '{}' and Outs = 0".format(U, remove_c(Teams[0][i])))
            mycon.commit()
    print("-----------------------------------------------")
#    print("")
    print(Names[0] + " score = " + str(total(a1)) + "/" + str(a1.count(5)) + " in " + str(len(a1)//6) + "." + str(len(a1)%6) + " overs")
    print("Run Rate = " + str(round(total(a1) * 6/float(len(a1)), 2)))
 #   print("")
    print("-----------------------------------------------")
    print("")
    p1 = input("Partnerships ? : ")
    if p1.upper() == "P" or p1.upper() == "Y":
        partnership_shares(a1, w)
    if p1.upper() != "P" or "Y":
        pass
    p = input("Continue? : ")
    print("")
    print("-----------------------------------------------")
    print(T[1] + (30 - len(T[1]))*" " + "Score" + 8 * " " + "S/R")
    print("-----------------------------------------------")


    for i in range(0, len(Teams[1])):
        if p.upper() !=  "N":
            s = str(Runs_array_2[i]) + "(" + str(Balls_array_2[i]) + ")"
            if s != "0(0)" and Teams[1][i] not in Not_Outs_2:
                print(Teams[1][i] + (30 - len(Teams[1][i])) * " " + s + (13 - len(s)) * " " + str(round(100 * Runs_array_2[i]/float(Balls_array_2[i]))))
                if U in ["TEST", "ODI", "T20"]:
                    cursor.execute("update player_{} set Outs = Outs + 1 where Name = '{}'".format(U, remove_c(Teams[1][i])))
                    cursor.execute("update player_{} set Highest = 0 where Name = '{}' and Highest is NULL".format(U, remove_c(Teams[1][i])))
                    mycon.commit()
            if s != "0(0)" and Teams[1][i] in Not_Outs_2:
                print(Teams[1][i] + "*" + (29 - len(Teams[1][i])) * " " + s + (13 - len(s)) * " " + str(round(100 * Runs_array_2[i]/float(Balls_array_2[i]))))
                if U in ["TEST", "ODI", "T20"]:
                    cursor.execute("update player_{} set Not_Outs = Not_Outs + 1 where Name = '{}'".format(U, remove_c(Teams[1][i])))
                    cursor.execute("update player_{} set Highest = 0 where Name = '{}' and Highest is NULL".format(U,remove_c(Teams[1][i])))
                    mycon.commit()
            if s == "0(0)":
                print(Teams[1][i] + (30 - len(Teams[1][i])) * " " + "-" + 12 * " " + "-")
            if U in ["TEST", "ODI", "T20"]:
                cursor.execute("update player_{} set Runs = Runs + {} where Name = '{}'".format(U, Runs_array_2[i], remove_c(Teams[1][i])))
                mycon.commit()
                if 49 < Runs_array_2[i] < 100:
                    cursor.execute("update player_{} set 50s = 50s + 1 where Name = '{}'".format(U, remove_c(Teams[1][i])))
                    mycon.commit()
                if 100 <= Runs_array_2[i] < 200:
                    cursor.execute("update player_{} set 100s = 100s + 1 where Name = '{}'".format(U, remove_c(Teams[1][i])))
                    mycon.commit()
            if U in ["TEST", "ODI"] and Runs_array_2[i] >= 200:
                cursor.execute("update player_{} set 200s = 200s + 1 where Name = '{}'".format(U, remove_c(Teams[1][i])))
                mycon.commit()
            if U in ["TEST", "ODI", "T20"]:
                cursor.execute("update player_{} set Balls = Balls + {} where Name = '{}'".format(U, Balls_array_2[i], remove_c(Teams[1][i])))
                cursor.execute("update player_{} set Highest = {} where Name = '{}' and Highest < {}".format(U, Runs_array_2[i], remove_c(Teams[1][i]), Runs_array_2[i]))
                mycon.commit()
                cursor.execute("update player_{} set Strike_Rate = Runs/(Balls) * 100 where Name = '{}' and Balls != 0".format(U, remove_c(Teams[1][i])))
                cursor.execute("update player_{} set Avg = Runs/(Outs) where Name = '{}' and Outs != 0".format(U, remove_c(Teams[1][i])))
                cursor.execute("update player_{} set Avg = Runs where Name = '{}' and Outs = 0".format(U, remove_c(Teams[1][i])))
                mycon.commit()
    print("-----------------------------------------------")
 #   print("")
    print(Names[1] + " score = " + str(total(a2)) + "/" + str(a2.count(5)) + " in " + str(len(a2)//6) + "." + str(len(a2)%6) + " overs")
    print("Run Rate = " + str(round(total(a2) * 6/float(len(a2)), 2)))
 #   print("")
    print("-----------------------------------------------")
    if U in ["TEST", "ODI", "T20"]:
        cursor.execute("update team_{} set Highest_score = {} where Team = '{}' and Highest_score < {}".format(U, total(a1), Names[0], total(a1)))
        cursor.execute("update team_{} set Highest_score = {} where Team = '{}' and Highest_score < {}".format(U, total(a2), Names[1], total(a2)))
        mycon.commit()
    if total(a1) > total(a2):
        print("")
        print(str(Names[0]) + " wins by " + str(total(a1) - total(a2)) + " runs")
        print("")
        print("Player of the Match - " + str(max_dict(D1)) + "(" + str(Names[0]) + ")" + " - " + str(D1[max_dict(D1)]) + " runs")
        if U in ["TEST", "ODI", "T20"]:
            cursor.execute("update player_{} set MOTM = MOTM + 1 where Name = '{}'".format(U, remove_c(str(max_dict(D1)))))
            cursor.execute("update team_{} set Win = Win + 1 where Team = '{}'".format(U, Names[0]))
            cursor.execute("update team_{} set Loss = Loss + 1 where Team = '{}'".format(U, Names[1]))
            mycon.commit()
        d[Names[0]] = d[Names[0]] + 1
    if total(a1) < total(a2):
        print("")
        print(str(Names[1]) + " wins by " + str(w - a2.count(5)) + " wickets")
        print("")
        print("Player of the Match - " + str(max_dict(D2)) + "(" + str(Names[1]) + ")" + " - " + str(D2[max_dict(D2)]) + " runs")
        if U in ["TEST", "ODI", "T20"]:
            cursor.execute("update player_{} set MOTM = MOTM + 1 where Name = '{}'".format(U, remove_c(str(max_dict(D2)))))
            cursor.execute("update team_{} set Win = Win + 1 where Team = '{}'".format(U, Names[1]))
            cursor.execute("update team_{} set Loss = Loss + 1 where Team = '{}'".format(U, Names[0]))
            mycon.commit()
        d[Names[1]] = d[Names[1]] + 1
    if total(a1) == total(a2):
        print("It's a Draw!!!")
        print("")
        print("Player of the Match - " + str(max_dict(dict(zip((max_dict(D1), max_dict(D2)), (D1[max_dict(D1)], D2[max_dict(D2)]))))))
        if U in ["TEST", "ODI", "T20"]:
            cursor.execute("update player_{} set MOTM = MOTM + 1 where Name = '{}'".format(U, remove_c(str(max_dict(dict(zip((max_dict(D1), max_dict(D2)), (D1[max_dict(D1)], D2[max_dict(D2)]))))))))
            cursor.execute("update team_{} set Draw = Draw + 1 where Team = '{}' or Team = '{}'".format(U, Names[0], Names[1]))
            mycon.commit()
    p2 = input("Partnership ? : ")
    if p2.upper() == "P" or p2.upper() == "Y":
        partnership_shares(a2, w)
    if p2.upper() != "P" or "Y":
        pass
    """
    p3 = input("Graph ? :")
    if p3.upper() == "G" or p3.upper() == "Y":
        plt.plot(balls1, y1)
        plt.plot(balls2, y2)
        plt.legend([names[0], names[1]])
        plt.show()
    if p3.upper() != "G" or p3.upper() != "Y":
        pass
    """
D16 = {}

def cricket():
    s = is_series()
    ty = types()
    b = balls(ty)
    names[0] = name_without_format(names[0])
    names[1] = name_without_format(names[1])
    if s == "SINGLE" or "":
        D5 = dict(zip(te[0].upper().split(",") + te[1].upper().split(","), many_zero(2 * wicket + 2)))
        D11 = dict(zip(te[0].upper().split(",") + te[1].upper().split(","), many_zero(2 * wicket + 2)))
        D12 = dict(zip(te[0].upper().split(",") + te[1].upper().split(","), many_zero(2 * wicket + 2)))
        scorecard(b, ty, d, D5, D11, D16, D12, 0)

    else:
        D5 = dict(zip(te[0].upper().split(",") + te[1].upper().split(","), many_zero(2 * wicket + 2)))
        D11 = dict(zip(te[0].upper().split(",") + te[1].upper().split(","), many_zero(2 * wicket + 2)))
        D12 = dict(zip(te[0].upper().split(",") + te[1].upper().split(","), many_zero(2 * wicket + 2)))
        n = int(input("No. of matches : "))
        for i in range(0, n):
            scorecard(b, ty, d, D5, D11, D16, D12, i)
            if i < n - 1:
                print("")
                if d[names[0]] > d[names[1]]:
                    print(names[0] + " leads " + str(n) + " match series by " + str(d[names[0]]) + " - " + str(d[names[1]]))
                    print("")
                if d[names[1]] > d[names[0]]:
                    print(names[1] + " leads " + str(n) + " match series by " + str(d[names[1]]) + " - " + str(d[names[0]]))
                    print("")
                if d[names[0]] == d[names[1]]:
                    print(str(n) + " match series is tied at " + str(d[names[0]]) + " - " + str(d[names[1]]))
                    print("")
            if i == n - 1:
                print("")
                if d[names[0]] > d[names[1]]:
                    print(names[0] + " wins " + str(n) + " match series by " + str(d[names[0]]) + " - " + str(d[names[1]]))
                    if ty in ["TEST", "ODI", "T20"]:
                        cursor.execute("update team_{} set Series_Win = Series_Win + 1 where Team = '{}'".format(ty, names[0]))
                        cursor.execute("update team_{} set Series_Loss = Series_Loss + 1 where Team = '{}'".format(ty, names[1]))
                        mycon.commit()
                if d[names[1]] > d[names[0]]:
                    print(names[1] + " wins " + str(n) + " match series by " + str(d[names[1]]) + " - " + str(d[names[0]]))
                    if ty in ["TEST", "ODI", "T20"]:
                        cursor.execute("update team_{} set Series_Win = Series_Win + 1 where Team = '{}'".format(ty, names[1]))
                        cursor.execute("update team_{} set Series_Loss = Series_Loss + 1 where Team = '{}'".format(ty, names[0]))
                        mycon.commit()
                if d[names[0]] == d[names[1]]:
                    print(str(n) + " match series is drawn at " + str(d[names[0]]) + " - " + str(d[names[1]]))
                print("")

        strikerate = strike_rate(D5, D11)
        strikerate1 = strike_rate_1(D5, D11)
        list1 = [""]
        average = {}
        for i in D12.keys():
            if D12[i] == 0:
                average[i] = round(D5[i])
            if D12[i] > 0:
                if D5[i] >= n * 14:
                    average[i] = round(D5[i] / float(D12[i]))
        average1 = {}
        for i in D12.keys():
            if D12[i] == 0:
                average1[i] = round(D5[i])
            if D12[i] > 0:
                average1[i] = round(D5[i] / float(D12[i]))
        D_mots = {}
        for i in D5.keys():
            if ty == "T20":
                D_mots[i] = D5[i] + average1[i]/float(5) + 1.5 * strikerate1[i]
            if ty == "TEST":
                D_mots[i] = D5[i] + average1[i] /float(5)
            else:
                D_mots[i] = D5[i] + average1[i] /float(5) + strikerate1[i]
        f = max_dict(D_mots)
        if f in teams[0]:
            print("Player of the Series - " + f + "(" + str(names[0]) + ")" + " - " + str(D5[f]) + " runs with an average of " + str(average[f]) + " striking at " + str(strikerate[f]))
            if ty in ["TEST", "ODI", "T20"]:
                cursor.execute("update player_{} set MOTS = MOTS + 1 where Name = '{}'".format(ty, remove_c(f)))
                mycon.commit()
        if f in teams[1]:
            print("Player of the Series - " + f + "(" + str(names[1]) + ")" + " - " + str(D5[f]) + " runs with an average of " + str(average[f]) + " striking at " + str(strikerate[f]))
            if ty in ["TEST", "ODI", "T20"]:
                cursor.execute("update player_{} set MOTS = MOTS + 1 where Name = '{}'".format(ty, remove_c(f)))
                mycon.commit()
        print("")
        s = input("Stats(Highest Impact Points/Most Runs/Highest Strike rates/Highest Individual Scores/All)(R/S/H/A) : ").upper()

        while s not in list1:
            if s == "R":
                print("")
                print("Most Runs - ")
                runs_stats(D5)
            if s == "S":
                print("")
                print("Highest Strike Rates - ")
                strike_rate_stats(strikerate)
            if s == "H":
                print("")
                print("Highest Individual Scores - ")
                high_score_stats(D16)
            if s == "AVG":
                print("")
                print("Averages - ")
                avg_stats(average)
            if s == "I":
                print("")
                print("Impact Points - ")
                impact_stats(D_mots)

            if s == "A":
                print("Impact Points - ")
                impact_stats(D_mots)

                print("Most Runs - ")
                runs_stats(D5)

                print("Averages - ")
                avg_stats(average)

                print("Highest Individual Scores - ")
                high_score_stats(D16)

                print("Highest Strike Rates - ")
                strike_rate_stats(strikerate)
                break
            s = input("Stats(Most Runs/Highest Strike rates/Highest Individual Scores/All)(R/S/H/A) : ").upper()

#print(team_in_T20())
cricket()
