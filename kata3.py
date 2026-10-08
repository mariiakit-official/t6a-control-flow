# pick one

# A: Location Codes (nested loop). Print the codes for 3 aisles × 4 shelves, one row per aisle.
# Expected first row: A1-S1 A1-S2 A1-S3 A1-S4


# B: Incident Validation (guard clauses). Using the incidents in kata3.py, 
# skip any with no branch or a severity outside 1–3, and print why.
# Expected: INC-1001 and INC-1004 are logged; INC-1002 and INC-1003 are skipped.

# Stretch: do the other Kata 3 option too.
for aisle in range (1,4):
    for shelves in range (1,5):
        #by default it print from new line, so the end will add space beetween the iteration , such as A1-S1 A1-S2 A1-S3 A1-S4
        print(f"A{aisle}-S{shelves}", end=" ")
    print()    

branch_name='DC-North'
incidents = [('INC-1001',branch_name,2),
             ('INC-1002',''),
             ('INC-1003','',5),
             ('INC-1004',branch_name,3)]


for i in range (0, len(incidents)):
    incident = incidents[i]
    if len(incident)> 2 and (incident[-1]<1 or incident[-1]>3):
        print(f"SKIPPED {incident[0]} : severity {incident[-1]} is not 1-3")
    elif incident[1]=='':
            print(f"SKIPPED {incident[0]} : missing branch")
    else:
        print(f"LOGGED {incident[0]} at {incident[1]} (severity{incident[-1]})")    
       
        