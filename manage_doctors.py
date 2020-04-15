'''
lst = ["ID", "Department", "Doctor", "Patient Name", "Age", "Gender", "Address", "Mob. Number", "Room Number", "Patient Condition"]

lst = ["ID", "Department", "Doctor Name", "Mob. Number"]

lst = ["ID","Department", "Doctor", "Patient Name", "Age", "Gender"]

'''
from handling_csv_files import *
import pandas as pd
import csv

def admin_add_doctor():
	temp_lst = ['id']
	temp_lst.append( str(input("Enter Department: ")))
	temp_lst.append( str(input("Enter Doctor Name: ")))
	temp_lst.append( str(input("Enter Doctor Mobile Number: ")))
	
	temp_lst[0] = ( int(input("Enter Doctor ID: ")))

	#Saving the new elements
	flag,index = check_csv_id(temp_lst[0], 'doctors')
	# print("index " + str(index))
	if flag == 0:
		with open('doctors.csv', 'a', newline='') as file:
			wr = csv.writer(file)
			wr.writerow(temp_lst)
	else:
		print("This ID is already existed, ")




# #
def admin_delete_doctor(id, def_para=0):
	if (def_para != 0):
		delete_csv_row(id, 'patients')
	else:
		flag = delete_csv_row(id, 'doctors')
		if flag == True:
			print("doctors's Info has been deleted")
		else:
			print("This ID is not existed")




# #
def admin_edit_doctor_info(id):
	flag, index = check_csv_id(int(id), 'doctors')
	if flag == 1:
		print("ID is existed,")
		with open("doctors.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print(new_data)
		del data
		cpy_temp_data = new_data.copy()
		while True:
			msg = "\n0. Edit ID\n1. Edit Department\n3. Edit Doctor Name\n4. Mobile Number"
			print(msg)
			msg = "'s' for save\n'e' for exit"
			print(msg)
			user_choice = str(input("Enter your choice: "))
			user_choice = user_choice.lower()
			if user_choice == '0':
				x = int(input("old info: " + str(new_data[0]) +" Enter new: "))
				flag, index = check_csv_id(x, 'doctors')
				if (flag == 1):
					print("You can not assign this ID, because It's already taked !")
				else:
					new_data[0] = x
			elif user_choice == '1':
				x = str(input("old info: " + str(new_data[1]) +" Enter new: "))
				new_data[1] = x
			elif user_choice == '2':
				x = str(input("old info: " + str(new_data[2]) +" Enter new: "))
				new_data[2] = x
			elif user_choice == '3':
				x = str(input("old info: " + str(new_data[3]) +" Enter new: "))
				new_data[3] = x
			elif user_choice == '4':
				x = str(input("old info: " + str(new_data[4]) +" Enter new: "))
				new_data[4] = x
			elif user_choice == 's':
				#check if Admin didn't change nothing, 
				i, flg_data_not_same = 0, 0
				while i < len(new_data):
					if (str(new_data[i] != cpy_temp_data[i])):
						flg_data_not_same = 1
						break
					i += 1
				if (flg_data_not_same == 1):
					admin_delete_doctor(id,1)
					with open('doctors.csv', 'a', newline='') as file:
						wr = csv.writer(file)
						wr.writerow(new_data)
						print("Saving......")
				else:
					print("exit......")
			elif user_choice == 'e':
				break
			else: 
				pass
	else:
		print("The ID is not existed !!")




##
def admin_display_doctor(id):
	flag, index = check_csv_id(int(id), 'doctors')
	if flag == 1:
		print("ID is existed,")
		with open("doctors.csv") as file:
			data = list(csv.reader(file))
		#data[index+1][info]
		new_data = data[index+1]
		print(new_data)
		del data
	else:
		print("The ID is not existed !!")





######################################################
def admin_Manage_doctors():
	while True:
		msg = "\n1. Add new doctor\n2. Delete doctor Info\n3. Edit doctor Info\n4. Display doctor Info\n5. return to previous screen\n"
		print(msg)
		user_choice = str(input("Enter your choice: "))
		# user_choice = user_choice.lower()
		if user_choice == '1':
			#call: admin_add_doctor
			admin_add_doctor()

		elif user_choice == '2':
			#call : admin_delete_doctor(id)
			id = int(input("Enter doctor ID to delete: "))
			admin_delete_doctor(id)
			
		elif user_choice == '3':
			#call : admin_edit_doctor_info(id)
			id = int(input("Enter doctor ID to edit: "))
			admin_edit_doctor_info(id)
			
		elif user_choice == '4':
			#call : admin_display_doctor(id)
			id = int(input("Enter doctor ID to display: "))
			admin_display_doctor(id)
			pass
		elif user_choice == '5':
			#break
			break 
		else:
			#do nothing
			pass	
	return None	



