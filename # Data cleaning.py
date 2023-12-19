# Data cleaning task

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

updated_medical_data = medical_data.replace("#", "$")

# Counting the number of records
num_records = 0
for record in updated_medical_data:
  if "$" in record:
    num_records += 1
print("there are {} medical records in the data".format(num_records))

# Spliting the string into a clean list of lists
medical_data_split = updated_medical_data.split(";")
medical_records = []
for record in medical_data_split:
    medical_records.append(record.split(","))
medical_records_clean = []
for record in medical_records:
  record_clean = []
  medical_records_clean.append(record_clean)
  for item in record:
    record_clean.append(item.strip())
print(medical_records_clean)

# Capitalising names
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])

# Lists by data category
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

# Printing data for each patient
for i in range(0, len(names)):
  print("{}, aged {} and with a BMI of {} has an insurance cost of {}".format(names[i], ages[i], bmis[i], insurance_costs[i]))

# BMI analysis
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
print(average_bmi)
