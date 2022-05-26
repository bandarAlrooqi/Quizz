import sqlite3

# You can create a new database by changing the name within the quotes
conn = sqlite3.connect('Quizz.db')
c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - Science
c.execute('''CREATE TABLE SCIENCE
             ([Question] text, [C1] text, [C2] text, [C3] text, [C4] text, [Answer] text)''')

# Create table - Technology
c.execute('''CREATE TABLE Technology
             ([Question] text, [C1] text, [C2] text, [C3] text, [C4] text, [Answer] text)''')

# Create table - History
c.execute('''CREATE TABLE History
              ([Question] text, [C1] text, [C2] text, [C3] text, [C4] text, [Answer] text)''')

# Create table - Geography
c.execute('''CREATE TABLE Geography
              ([Question] text, [C1] text, [C2] text, [C3] text, [C4] text, [Answer] text)''')

c.execute(
    '''INSERT INTO SCIENCE(Question,C1,C2,C3,C4,Answer) VALUES('What is another name for Vitamin K?','Nicotinic acid','Riboflavin','Thiamine','2 Methyl-1','2 Methyl-1') ''')
c.execute(
    '''INSERT INTO SCIENCE(Question,C1,C2,C3,C4,Answer) VALUES('Identify India first indigenous Satellite Launch Vehicle (SLV):',
     'SLV-1','PSLV','SLV-3','GSLV','SLV-3') ''')
c.execute(
    '''INSERT INTO SCIENCE(Question,C1,C2,C3,C4,Answer) VALUES('Which hormone controls blood pressure?','Vasopressin','Oestrogen','Oxytocin','Testosterone','Vasopressin') ''')
c.execute(
    '''INSERT INTO SCIENCE(Question,C1,C2,C3,C4,Answer) VALUES('How do biocides work?','Control the multiplication of insects','Kill the insects','Manage the original form of material','Control the bacteria','Control the bacteria') ''')
c.execute(
    '''INSERT INTO SCIENCE(Question,C1,C2,C3,C4,Answer) VALUES('What is the actual name of our Moon','Solaris','Selene','Luna','Luka','Luna') ''')

c.execute(
    '''INSERT INTO Technology(Question,C1,C2,C3,C4,Answer)
     VALUES('Which one of the following is a coding language also known as a term for coffee?','Java','Joe','CoffeeBean','None of the above','Java') ''')
c.execute(
    '''INSERT INTO Technology(Question,C1,C2,C3,C4,Answer)
    VALUES('Which was the world first successful electronic computer?','PARAM','CRAY-1','Pascaline','ENIAC (Electronic Numerical Integrator And Computer)','ENIAC (Electronic Numerical Integrator And Computer)') ''')
c.execute(
    '''INSERT INTO Technology(Question,C1,C2,C3,C4,Answer)
     VALUES('How is the quality of a printer measured?','Alphabet per strike','Words per Inch','Strike per Inch','Dots per Inch','Dots per Inch') ''')
c.execute(
    '''INSERT INTO Technology(Question,C1,C2,C3,C4,Answer)
    VALUES('Number of bit used by the IPv6 address:','32bit','64bit','128bit','256bit','128bit') ''')
c.execute(
    '''INSERT INTO Technology(Question,C1,C2,C3,C4,Answer)
    VALUES('Which of the following is not an operating system?','DOS','macOS','Python','Linux','Python') ''')

c.execute(
    '''INSERT INTO History(Question,C1,C2,C3,C4,Answer)
    VALUES('In which decade was the SPICE simulator introduced:','1962','1972','1982','1992','1972') ''')
c.execute(
    '''INSERT INTO History(Question,C1,C2,C3,C4,Answer)
    VALUES('Who started the construction of the Colosseum in Rome?','Nero','Titus','Octavian','Vespasian','Vespasian') ''')
c.execute(
    '''INSERT INTO History(Question,C1,C2,C3,C4,Answer)
    VALUES('Who was the first woman in space?','Sunitha Williams','Valentina Tereshkova','Masida namisha','Tamara Press','Valentina Tereshkova') ''')
c.execute(
    '''INSERT INTO History(Question,C1,C2,C3,C4,Answer)
    VALUES('Who was the last Emperor of Rome?','Nero','Caeser','Romulus Augustulus','Julius','Romulus Augustulus') ''')
c.execute(
    '''INSERT INTO History(Question,C1,C2,C3,C4,Answer)
    VALUES('Who wrote the first history book?','Herodotus','Euclid','Julius Caesar','Aristotle','Herodotus') ''')

c.execute(
    '''INSERT INTO Geography(Question,C1,C2,C3,C4,Answer)
    VALUES('Which one is the largest ocean in the World?','Indian','Pacific','Atlantic','Arctic','Pacific') ''')
c.execute(
    '''INSERT INTO Geography(Question,C1,C2,C3,C4,Answer)
    VALUES('Dead Sea is located between which two countries?','Jordan and Sudan','Jordan and Palastain','UAE and Egypt','Saudi Arabia and UAE','Jordan and Palastain') ''')
c.execute(
    '''INSERT INTO Geography(Question,C1,C2,C3,C4,Answer)
    VALUES('Which one is the largest producer of tea in the World?','China','Sri Lanka','India','Kenya','China') ''')
c.execute(
    '''INSERT INTO Geography(Question,C1,C2,C3,C4,Answer)
    VALUES('Earth day is celebrated on?','September 17','February 16','April 4','April 22','April 22') ''')
c.execute(
    '''INSERT INTO Geography(Question,C1,C2,C3,C4,Answer)
    VALUES('Which country gifted the (Statue of Liberty) to USA in 1886?','French','Canada','Brazil','Saudi Arabia','French') ''')

conn.commit()
