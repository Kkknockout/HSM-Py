# Hospital Management System for handling patients', doctors and reservation info.
# Person class (parent class).
# represents a generic person with age, name, and gender.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name:{self.name}, Age:{self.age}, Gender:{self.gender}")

# Patient class (inherits from the parent/super/main class Person)
# Represents a patient with name, age, gender, patient ID, and appointment list.
class Patient(Person):
    def __init__(self, name, age, gender, patient_id, appointment_list):
        Person.__init__(self, name, age, gender)
        self.patient_id = patient_id
        self.appointment_id = appointment_list

    def display_info(self):
        super().display_info()
        print(f"Patient ID: {self.patient_id}")

# Doctor class (inherits from the parent/main class Person)
# Represents a medical professional with a name, age, gender, specialty and schedule.
class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialty):
        Person.__init__(self, name, age, gender)
        self.doctor_id = doctor_id
        # Initialize the doctor's schedule; a multifaceted dictionary with dates and hourly availability.
        # False means the slot is free, True means booked.
        self.specialty = specialty
        self.schedule = {self.doctor_id: {
            '14/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '15/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '16/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '17/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '18/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False}}}


# Checking if the doctor is available at a specific date and hour

    def is_available(self, queried_day, queried_hour):
        for doctors_id, bookings in self.schedule.items():
            for schedule_days, schedule_hours in bookings.items():
                if queried_day == schedule_days:
                    for hour, value in schedule_hours.items():
                        if queried_hour == hour:
                            return not value
        return None


    def view_schedule(self):
     # Displaying the full schedule for the doctor showing booked/available slots
        for doctors_id, bookings in self.schedule.items():
            for day, hours in bookings.items():
                print(day)
                for hour, value in hours.items():
                    print(f"{hour}: {'Booked' if value else 'Available'}")


# Class for Appointment
# Represents an appointment with unique ID, patient, doctor, date, time, and status.

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = status

    def confirm(self):
# Confirm the appointment by setting status
        self.status = 'confirmed'

    def cancel(self):
# Cancel the appointment by setting status
        self.status = 'cancelled'

# Class for the HospitalSystem which is the main system class managing patients, doctors, and appointments
class HospitalSystem:
    def __init__(self):
# Initialize lists to store patients, doctors, and appointments.
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.patient_count = 0
        self.doctor_count = 0
        self.appointment_count = 0

    def generate_id(self, object_type):
 # Generate unique ID strings based on the object type.
        user_id = ''
        if object_type == 'doctor':
            self.doctor_count += 1
            user_id = 'D' + str(self.doctor_count)
            return user_id
        elif object_type == 'patient':
            self.patient_count += 1
            user_id = 'P' + str(self.patient_count)
            return user_id
        elif object_type == 'appointment':
            self.appointment_count += 1
            user_id = 'A' + str(self.appointment_count)
            return user_id
        else:
            print('Object type not valid')
        return None


# Loops to add one or more patients with input validation
    def add_patient(self):
        adding_patient = True
        while adding_patient:
            try:
                name = input('Please enter your name: ').strip()
                if name == "" or any(char.isdigit() for char in name):
                    raise ValueError
                age = int(input('Please enter your age: '))
                if age < 1 or age > 100:
                    raise Exception('Invalid age!')
                gender = input('What is your gender (m/f): ').lower()
                if gender != 'm' and gender != 'f':
                    raise ValueError
            except ValueError:
    # Handle invalid inputs by prompting again
                print('Invalid input')
            except:
                print('Invalid age!')
            else:
                # Creates a Patient object and add it to the list
                patients_obj = Patient(name, age, gender, self.generate_id('patient'), self.appointments)
                self.patients.append(patients_obj)
                print(f'\nSuccessfully added patient {patients_obj.name} their ID is: {patients_obj.patient_id}')
                check = input('\n Do you want to add another patient? (y/n): ').lower()
 # Exit loop if user does not want to add more patients.
                if check != 'y':
                    adding_patient = False 
                    break

    def add_doctor(self):
 # Loops to add one or more doctors.
        add_doc = True
        while add_doc:
            try:
                name = input('Please enter your name: ').strip()
                if name == "" or any(char.isdigit() for char in name):
                    raise ValueError
                age = int(input('Please enter your age: '))
                if age < 1 or age > 100:
                    raise Exception('Invalid age!')
                gender = input('Please enter your gender (m/f): ').lower()
                if gender != 'm' and gender != 'f':
                    raise ValueError
                speciality = input('What is your speciality? (Neurologist, Cardiologist, Urologist, Pediatrician): ').strip().lower()
                if speciality not in ['neurologist', 'cardiologist', 'urologist', 'pediatrician']:
                    raise ValueError
            except ValueError:
                print('Invalid input!')
            except:
                print('Invalid age!')
            else:
                print('When are you available?')
                print('Enter done when finished')
                updating_schedule = True
                while updating_schedule:
                    time_slot = input('Time slot: ')
                    if time_slot == 'done':
                        break
# Creates a Doctor object and add it to the list.
                doctors_obj = Doctor(name, age, gender, self.generate_id('doctor'), speciality)
                self.doctors.append(doctors_obj)
                print(f'\nSuccessfully added doctor {doctors_obj.name} their ID is: {doctors_obj.doctor_id}')
                check = input('\nWould you like to add another doctor? (y/n) :').lower()
 # Exit loop if user does not want to add more doctors
                if check != 'y':
                    add_doc = False
                    break


    def book_appointment(self):
# Method to book an appointment between patient and doctor.
        try:
            date = int(input(
                'Choose one of the following dates: \n 14/07/2025 - 1 \n 15/07/2025 - 2 \n 16/07/2025 - 3 \n 17/07/2025 - 4 \n 18/07/2025 - 5 \n : '))
            chosen_date = ''
            if date == 1:
                chosen_date = '14/07/2025'
            elif date == 2:
                chosen_date = '15/07/2025'
            elif date == 3:
                chosen_date = '16/07/2025'
            elif date == 4:
                chosen_date = '17/07/2025'
            elif date == 5:
                chosen_date = '18/07/2025'
            else:
                print('Invalid input')
                raise ValueError
            time = int(input('Choose from one of the following time slots: \n 9 \n 10 \n 11 \n 12 \n 1 \n 2 \n 3 \n 4 \n 5 \n : '))
            doctor_name = input("What is the doctor's name?: ")
            patient_name = input("What is the patient's name?: ")
        except ValueError:
            print('Invalid input')
        else:
      # Check doctor availability and book if free
            for doctor in self.doctors:
                if doctor_name == doctor.name:
                    availability = doctor.is_available(chosen_date, time)
                    if availability:
                        print(' \nThe doctor is available, setting appointment')
                        doctor.schedule[doctor.doctor_id][chosen_date][time] = True
                      # Create and add appointment to list
                        appointment_obj = Appointment(self.generate_id('appointment'), patient_name, doctor_name,
                                                      chosen_date, time, 'confirmed')
                        self.appointments.append(appointment_obj)
                        print(f'Your appointment ID is: {appointment_obj.appointment_id}')
                        return
                    else:
                        print(' \nThe time slot you chose is not available')
                        return
            print("Doctor not found.")

    def cancel_appointment(self):
 # Cancels an existing appointment by freeing the doctor's slot and removing the appointment
        appointment_id = input("Enter appointment ID to cancel: ").strip()
        for appointment in self.appointments[:]:  # iterates over a copy to allow removal
            if appointment.appointment_id == appointment_id:
                for doctor in self.doctors:
                    if doctor.name == appointment.doctor:
                        doctor.schedule[doctor.doctor_id][appointment.date][appointment.time] = False
                self.appointments.remove(appointment)
                print(f'Appointment {appointment_id} cancelled.')
                return
        print("Appointment not found.")

    def generate_bill(self):
# Generates a bill receipt for an appointment by ID
        appointment_id = input("Enter Appointment ID for billing: ")
        found = False
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                found = True
                try:
                    # Prints a formatted bill with details.
                    print("\n--- WALKS-WOOD HOSPITAL BILL RECEIPT ---")
                    print(f"Appointment ID: {appointment_id}")
                    print(f"Patient: {appointment.patient}")
                    print(f"Doctor: {appointment.doctor}")
                    print(f"Date: {appointment.date}, Time: {appointment.time}:00")
                    print("Consultation Fee: JMD $3000")
                    # Prompt for extra fees such as medication or tests
                    extra = float(input("Enter extra service fee (tests, medication): "))
                    total = 3000 + extra
                    print(f"Total Amount: JMD ${total}")
                    print("-------------------------------------\n")
                except ValueError:
                    print("Invalid fee entered.")
        if not found:
            print("Appointment not found.")

    def view_patients(self):
# View patient's profile by patient ID
        patient_id = input("Enter Patient's ID: ").strip()
        for patient in self.patients:
            if patient_id == patient.patient_id:
# Print patient's details.
                print(f'\nName: {patient.name} \nAge: {patient.age} \nGender: {patient.gender.upper()}')
                return
        print("Invalid ID. Patient not found!")

    def view_doctors(self):
# View doctor's profile and schedule by doctor ID
        doctor_id = input("Enter Doctor's ID: ").strip()
        for doctor in self.doctors:
            if doctor_id == doctor.doctor_id:
# Print doctor's details and schedule.
                print(f'\nName: {doctor.name} \nAge: {doctor.age} \nGender: {doctor.gender.upper()}')
                print('Schedule:')
                doctor.view_schedule()
                return
        print("Invalid ID. Doctor not found!")


# Main interactive menu loop for the hospital system.
    def main_menu(self):
        while True:
            print("\n--- WALKS-WOOD HOSPITAL MANAGEMENT SYSTEM ---")
            print("1. Add Patient")
            print("2. Add Doctor")
            print("3. Book Appointment")
            print("4. Cancel Appointment")
            print("5. Generate Bill")
            print("6. View Patient Profile")
            print("7. View Doctor Schedule")
            print("8. Exit")
            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.add_doctor()
            elif choice == "3":
                self.book_appointment()
            elif choice == "4":
                self.cancel_appointment()
            elif choice == "5":
                self.generate_bill()
            elif choice == "6":
                self.view_patients()
            elif choice == "7":
                self.view_doctors()
            elif choice == "8":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


# Create an instance of HospitalSystem and runs the system.
hospital = HospitalSystem()
hospital.main_menu()
