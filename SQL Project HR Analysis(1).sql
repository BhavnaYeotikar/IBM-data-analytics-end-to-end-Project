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

# Find the maximum and minimum monthly income of employees.
SELECT MAX(MonthlyIncome) AS MaxMonthlyIncome, MIN(MonthlyIncome) AS MinMonthlyIncome
FROM employee;

#List the unique job roles and the number of employees in each role.
SELECT JobRole, COUNT(*) AS EmployeeCount
FROM employee
GROUP BY JobRole;

#Identify the employee with the highest daily rate.
SELECT *
FROM employee
ORDER BY DailyRate DESC
LIMIT 1;

#Find the top 5 departments with the highest average monthly income among employees:
SELECT Department, AVG(MonthlyIncome) AS AvgMonthlyIncome
FROM employee
GROUP BY Department
ORDER BY AvgMonthlyIncome DESC
LIMIT 5;

#Calculate the employee turnover rate (attrition rate) for each department:
SELECT Department, 
       COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END) / COUNT(*) AS TurnoverRate
FROM employee
GROUP BY Department;

/*List the employees who have spent more than 5 years in their current role and have not received
 a promotion in the last 3 years:*/
 SELECT *
FROM employee
WHERE YearsInCurrentRole > 5
AND EmployeeNumber NOT IN (
    SELECT EmployeeNumber
    FROM employee
    WHERE YearsSinceLastPromotion <= 3
);









