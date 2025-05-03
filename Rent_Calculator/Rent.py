
rent = int(input('Enter your flat rent ='))
food = int (input('Enter the amount of food order='))
electricity_spend = int (input('Enter the total of electricuty spend='))
charge_per_unit= int (input('Enter the charge per unit='))
number_of_person = int (input('Enter the number of person ='))

total_bill = (charge_per_unit) * (electricity_spend)

output = ( rent + food + total_bill) // number_of_person

print(f'Each person will pay = ',output)

