SELECT * FROM new_hrdb.employee;
#Number of employess who left the company
Use new_hrdb;
SELECT count(*) as attritioncount
FROM employee WHERE Attrition = 'Yes';

#Avg rate of employees frequently travel for business
SELECT avg(DailyRate)
FROM employee WHERE BusinessTravel ='Travel_Frequently';

# How many employees are satisfied with their job involvement
SELECT COUNT(*) FROM employee
WHERE JobInvolvement>3;
 SELECT JobInvolvement,  count(EmployeeNumber) FROM employee
 GROUP BY JobInvolvement;
 #867 people are satisfied
 
 # Give Overall average rating of employee
 SELECT avg(performanceRating) FROM employee;
 
 SELECT column_name
FROM information_schema.columns
WHERE table_name = 'employee' AND table_schema = 'new_hrdb';



