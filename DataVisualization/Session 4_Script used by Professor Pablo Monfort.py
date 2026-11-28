###########################
# RECAP
###########################
### WEEK 1
# VARIABLES: 
    - Numerical: float or int - + - * / **
                                import math
                                math.sqrt(100)
                                math.pi
                                math.sin(90)
    - String:    text           s.lower(), s.upper()
                                len(s), s[0], s[0:5]
    - Boolean:   True / False    
# IF ELIF ELSE 
# LOOPS: FOR AND WHILE

### WEEK 2
# LISTS
people = [34,2435,346,346,14,12]
people = ["Omer","Pablo","Asbil"]
people[0]
people[0:5]
for i in people:
    .....
people.append("new")
people.remove("deleting element")
len(people)
# SETS
people = {"","",""}
people.union(otherPeople)
people.intersection(otherPeople)


###########################
# REGULAR EXERCISES:
###########################
# EXERCISE 1. Identify the students failing the exam (less than 5)
st = ["Yasir - 9","Hana - 8","Bilal - 10","Maha - 3","Abbas - 4"]
for i in st:
    if float(i[-2:]) <5:
        print(i)
    
# EXERCISE 2. Given our next clients, show the following info:
# Q1. How many clients are there in Spain
# Q2. Amount of total clients in Europe
# Q3. Who are the premium clients in Spain
# Q4. Who are the premium clients in Europe
sp = ["SP1","SP2","SP3"]
pt = ["PT1","PT2","PT3","PT4","PT5"]
sa = ["SA1","SA2"]
eg = ["EG1","EG2","EG3"]
pr = ["SP3","PT1","PT2","EG1","EG3"]

# Q1. LISTS: remove, append, len, for, ...
print(len(sp))
# Q2. 
print(len(sp) + len(pt))
# Q3. 
sp2 = set(sp)
pr2 = set(pr)
sp2.intersection(pr2)
# Q4. Premium european clients:
pt2 = set(pt)
eu = sp2.union(pt2)
eu.intersection(pr2)       # Who they are
len(eu.intersection(pr2))  # How many

# EXERCISE 3
sale1 = "20260923, Wed, 14:08:00, 100"
sale2 = "20260730, Tue, 08:10:12, 5"
sale3 = "20260916, Wed, 16:12:10, 20"
# s.lower(), s.upper(), s[0], s[4:8], s.count("...")
# len(s), +
# Q1. How many sales took place on Wednesdays?
(sale1 + sale2 + sale3).count("Wed")
# Q2. How many sales took place in June or July?
sale1[4:6].count("06") + sale1[4:6].count("07")
etc
# Q3. How many sales took place from 10:00:00 to 10:59:59 AM?
(sale1 + sale2 + sale3).count(" 10:")
# Q4. How much money did we get?
# OPTION 1: using .split(","). Try for yourself!!!
float(sale1.split(",")[-1]) and sum the other ones...
# OPTION 2:
float(sale1[24:]) + 
float(sale2[24:]) + 
float(sale3[24:])









###########################
# ADVANCED EXERCISES:
###########################
# PANDAS:   data analysis
# PLOTNINE: data visualization
# SEABORN:  data visualization
# BS4:      web scraping
# FOLIUM:   maps, geolocated info
import folium
m = folium.Map()
folium.Marker(location=[0,0]).add_to(m)
folium.Marker(location=[20,30],popup="Yasir's house").add_to(m)
m.save("My first map.html")







