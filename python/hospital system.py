Appointments = {}
patients = {}
doctors = {}


def ap():
    patient_id = int(input("Enter the id number of the patient :"))
    name = str(input("Please enter the name of patient :"))
    age = int(input("Please enter the age of the patient :"))
    deciec = str(input("please enter the ailment :"))
    if name in patients:
        print("This patient is already exist in the hospital!")
    elif name not in patients:
        patients[patient_id] = {"name": name, "age": age, "deciece": deciec}
        print("The patient has added!")


def rp():
    patient_id = int(input("Please enter the id of the patient :"))
    if patient_id in patients:
        del patients[patient_id]
        print("The patient has removed!")
    elif patient_id not in patients:
        print("The patient with this id doesn't exist!") 


def vp():
    nom = int(input("Please enter the id number of the patient :"))
    if nom in patients:
        print(patients[nom])
    else:
        print("This patient doesn't exist in the system!")


def vps():
    for x, y in patients.items():
        print(f"{x},{y}")


# ___________________________________________________________________

def ad():
    doc_id = int(input("Please enter the id of the doctor :"))
    name = str(input("Please enter the id of the doctor you want to add :"))
    deciece = str(input("Please enter the name of the specialty of the doctor :"))
    if name in doctors:
        print("This doctor is already exist in the system!")
    elif name not in doctors:
        doctors[doc_id] = {"name": name, "specialty": deciece}
        print("The doctor has added!")


def rd():
    doc_id = int(input("Please enter the id of the doctor:"))
    if doc_id in doctors:
        del doctors[doc_id]
        print("The doctor has removed!")
    elif doc_id not in doctors:
        print("This id number doesn't exist!")


def vd():
    nom=int(input("Enter the id number of the doctor :"))
    if nom in doctors:
        print(doctors[nom])
    else:
        print("This id number doesn't exist on the system!")


def vds():
    for x, y in doctors.items():
        print(f"{x}:{y}")


# ___________________________________________________________________


def aa():
    np = int(input("Please enter the id of the patient :"))
    nd = int(input("Please enter the id of the doctor :"))
    Appointments.update({np: nd})
    if np in patients and nd in doctors:
        appointment_id = int(input("Enter the appointment id number :"))
        Appointments[appointment_id] = {"patient id": np, "doctor id": nd}
        print("The Appointment has done!")
    else:
        print("This doctor cant heal this deciace!")


def ra():
    nom = int(input("Please enter the appointment number :"))
    if nom in Appointments:
        del Appointments[nom]
    elif nom not in Appointments:
        print("This appointment doesn't exist!")


def va():
    nom1 = int(input("Please enter the id number of the patient :"))
    nom2 = int(input("Please enter the id number of the doctor :"))
    Appointment_id = int(input(" Enter the id number of the appointment :"))
    print(Appointments[Appointment_id])


def vas():
    for x, y in Appointments.items():
        print(f"{x}:{y}")


# ___________________________________________________________________

print("hello to hospital system!")
while True:
    d = int(input(
        "1.Add a new patient\n2.Remove a previous patient\n3.View a patient\n4.View all patients\n5.Add a new "
        "doctor\n6.Remove a previous doctor\n7.View a doctor\n8.View all the doctors\n9.Add a appointment\n10.Remove "
        "a appointment\n11.View a appointment\n12.View all appointments""\n13.End the program\n"))
    if d == 1:
        while True:
            print("______________________________________")
            ap()
            a=str(input("Do you want to add another patient(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
                
    elif d == 2:
        while True:
            print("______________________________________")
            rp()
            a=str(input("Do you want to remove another patient(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break             
    elif d == 3:
        while True:
            print("______________________________________")
            vp()
            a=str(input("Do you want to view another patient(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
    elif d == 4:
        print("______________________________________")
        vps=()
        print("______________________________________")
    elif d == 5:
        while True:
            print("______________________________________")
            ad()
            a=str(input("Do you want to add another doctor(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
    elif d == 6:
        while True:
            print("______________________________________")
            rd()
            a=str(input("Do you want to remove another doctor(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
    elif d == 7:
        while True:
            print("______________________________________")
            vd()
            a=str(input("Do you want to view another doctor(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
    elif d == 8:
        print("______________________________________")
        vds()
        print("______________________________________")
    elif d == 9:
        while True:
            print("______________________________________")
            aa()
            a=str(input("Do you want to add another appointment(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
    elif d == 10:
        while True:
            print("______________________________________")
            ra()
            a=str(input("Do you want to remove another doctor(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
    elif d == 11:
        while True:
            print("______________________________________")
            ad()
            a=str(input("Do you want to view another doctor(yes/no):").lower())
            if a == "yes":
                continue
            else:
                print("______________________________________")
                break
    elif d == 12:
        print("______________________________________")
        vas()
        print("______________________________________")
    elif d== 13:
        print("______________________________________")
        break
    else:
        print("sorry but you can only enter (1/2/3/4/5/6/7/8/9/10/11/12/13)")
