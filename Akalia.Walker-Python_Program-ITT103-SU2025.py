# importing module to use further down.

# Hospital Management System for handling patients', doctors and reservation info.

# CLASS: Person (parent class).
# represents a generic person with age, name, and gender.
class Person:
    def __init__(self, name, age, gender):
        # Initialize Person object with name, age, and gender attributes
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        # Display basic personal information
        print(f"Name:{self.name}, Age:{self.age}, Gender:{self.gender}")


# CLASS: Patient (inherits from the parent/super class Person)
# Represents a patient with name, age, gender, patient ID, and appointment list.
class Patient(Person):
    def __init__(self, name, age, gender, patient_id, appointment_list):
        # Call parent constructor to set name, age, gender
        Person.__init__(self, name, age, gender)
        # Unique patient ID
        self.patient_id = patient_id
        # List or reference to the patient's appointments
        self.appointment_id = appointment_list

    def display_info(self):
        # Display patient information including inherited personal info
        super().display_info()
        print(f"Patient ID: {self.patient_id}")


# CLASS: Doctor (inherits from Person)
# Represents a medical professional with a specialty and schedule
class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialty):
        # Initialize inherited attributes
        Person.__init__(self, name, age, gender)
        # Unique doctor ID
        self.doctor_id = doctor_id
        # Initialize the doctor's schedule: a dictionary with dates and hourly availability
        # False means the slot is free, True means booked
        self.schedule = {self.doctor_id: {
            '14/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '15/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '16/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '17/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False, 5: False},
            '18/07/2025': {9: False, 10: False, 11: False, 12: False, 1: False, 2: False, 3: False, 4: False,
                           5: False}}}
        # Doctor's medical specialty
        self.specialty = specialty

    def is_available(self, queried_day, queried_hour):
        # Check if the doctor is available at a specific date and hour
        for self.doctors_id, bookings in self.schedule.items():
            for schedule_days, schedule_hours in bookings.items():
                if queried_day == schedule_days:
                    for hour, value in schedule_hours.items():
                        if queried_hour == hour:
                            # If True, the slot is booked, so return False (not available)
                            if value:
                                # print(f"{hour}: Booked")
                                return False
                            else:
                                # print(f"{hour}: Available")
                                return True
        # If date or time not found, return None
        return None

    def view_schedule(self):
        # Print the full schedule for the doctor showing booked/available slots
        for doctors_id, bookings in self.schedule.items():
            for day, hours in bookings.items():
                print(day)
                for hour, value in hours.items():
                    if not value:
                        print(f"{hour}: Available")
                    else:
                        print(f"{hour}: Booked")


# CLASS: Appointment
# Represents an appointment with unique ID, patient, doctor, date, time, and status
class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time, status):
        # Initialize appointment attributes
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


# CLASS: HospitalSystem
# Main system class managing patients, doctors, and appointments
class HospitalSystem:
    def __init__(self):
        # Initialize lists to store patients, doctors, and appointments
        self.patients = []
        self.doctors = []
        self.appointments = []
        # Counters to generate unique IDs
        self.patient_count = 0
        self.doctor_count = 0
        self.appointment_count = 0

    def generate_id(self, object_type):
        # Generate unique ID strings based on object type
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

    def add_patient(self):
        # Loop to add one or more patients with input validation
        adding_patient = True
        while adding_patient:
            try:
                name = input('Please enter your name: ').strip()
                # Check that name is not empty and contains no digits
                if name == "" or any(char.isdigit() for char in name):
                    raise ValueError
                age = int(input('Please enter your age: '))
                #Age must be between 1 and 100
                if age < 1 or age > 100:
                    raise Exception('Invalid age!')
                gender = input('What is your gender (m/f): ').lower()
                # Gender must be 'm' or 'f'
                if gender != 'm' and gender != 'f':
                    raise ValueError
            except ValueError:
                # Handle invalid inputs by prompting again
                print('Invalid input')
            except:
                print('Invalid age!')
            else:
                # Create a Patient object and add it to the list
                patients_obj = Patient(name, age, gender, self.generate_id('patient'), self.appointments)
                self.patients.append(patients_obj)
                print(f'\nSuccessfully added patient {patients_obj.name} their ID is: {patients_obj.patient_id}')
                check = input('\n Do you want to add another patient? (y/n): ').lower()
                # Exit loop if user does not want to add more patients
                if check != 'y':
                    adding_patient: False
                    break

    def add_doctor(self):
        # Loop to add one or more doctors with input validation
        add_doc = True
        while add_doc:
            try:
                name = input('Please enter your name: ').strip()
                # Name validation: no digits allowed
                if name == "" or any(char.isdigit() for char in name):
                    raise ValueError
                age = int(input('Please enter your age: '))
                # Age must be between 1 and 100
                if age < 1 or age > 100:
                    raise Exception('Invalid age!')
                gender = input('Please enter your gender (m/f): ').lower()
                if gender != 'm' and gender != 'f':
                    raise ValueError
                speciality = input('What is your speciality? (Neurologist, Cardiologist, Urologist, Pediatrician): ').strip().lower()
                # Specialty must be one of the allowed list
                if speciality not in ['neurologist', 'cardiologist', 'urologist', 'pediatrician']:
                    raise ValueError
            except ValueError:
                print('Invalid input!')
            except:
                print('Invalid age!')
            else:
                # Availability input loop (though availability is not actually stored/used here)
                print('When are you available?')
                print('Enter done when finished')
                updating_schedule = True
                while updating_schedule:
                    time_slot = input('Time slot: ')
                    if time_slot == 'done':
                        break
                # Create a Doctor object and add it to the list
                doctors_obj = Doctor(name, age, gender, self.generate_id('doctor'), speciality)
                self.doctors.append(doctors_obj)
                print(f'\nSuccessfully added doctor {doctors_obj.name} their ID is: {doctors_obj.doctor_id}')
                check = input('\nWould you like to add another doctor? (y/n) :').lower()
                # Exit loop if user does not want to add more doctors
                if check != 'y':
                    add_doc = False
                    break

    def book_appointment(self):
        # Method to book an appointment between patient and doctor
        try:
            date = int(input(
                'Choose one of the following dates: \n 14/07/2025 - 1 \n 15/07/2025 - 2 \n 16/07/2025 - 3 \n 17/07/2025 - 4 \n 18/07/2025 - 5 \n : '))
            chosen_date = ''
            # Map numeric input to date string
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
            time = int(input(
                'Choose from one of the following time slots: \n 9 \n 10 \n 11 \n 12 \n 1 \n 2 \n 3 \n 4 \n 5 \n : '))
            doctor_name = input("What is the doctor's name?: ")
            patient_name = input("What is the patient's name?: ")
        except ValueError:
            # Catch invalid numeric inputs
            print('Invalid input')
        else:
            # Check doctor availability and book if free
            for doctor in self.doctors:
                if doctor_name == doctor.name:
                    availability = doctor.is_available(chosen_date, time)
                    if availability:
                        print(' \nThe doctor is available, setting appointment')
                        # Mark time slot as booked
                        doctor.schedule[doctor.doctor_id][chosen_date][time] = True
                        # Create and add appointment to list
                        appointment_obj = Appointment(self.generate_id('appointment'), patient_name, doctor_name,
                                                      chosen_date, time, 'confirmed')
                        self.appointments.append(appointment_obj)
                        print(f'Your appointment ID is: {appointment_obj.appointment_id}')
                    else:
                        print(' \nThe time slot you chose is not available')

    def cancel_appointment(self):
        # Cancel an existing appointment by freeing the doctor's slot and removing appointment
        for appointment in self.appointments:
            for doctor in self.doctors:
                if doctor.name == appointment.doctor:
                    # Mark the doctor's slot as available again
                    doctor.schedule[doctor.doctor_id][appointment.date][appointment.time] = False
                    print(
                        f'The appointment - {appointment.appointment_id} of {appointment.patient} on {appointment.date} at '
                        f'{appointment.time} has been cancelled.')
                    # Remove the appointment from the list
                    self.appointments.remove(appointment)

    def generate_bill(self):
        # Generate a bill receipt for an appointment by ID
        appointment_id = input("Enter Appointment ID for billing: ")
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                    try:
                        # Print formatted bill details
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
                        # Handle invalid fee input
                        print("Invalid fee entered.")
            else:
                print("Appointment not found.")

    def view_patients(self):
        # View patient profile by patient ID
        patient_id = input("Enter Patient's ID: ").strip()
        for patient in self.patients:
            if patient_id == patient.patient_id:
                # Print patient details
                print(f'\nName: {patient.name} \nAge: {patient.age} \nGender: {patient.gender.upper()}')
            else:
                print("Invalid ID. Patient not found!")

    def view_doctors(self):
        # View doctor profile and schedule by doctor ID
        doctor_id = input("Enter Doctor's ID: ").strip()
        for doctor in self.doctors:
            if doctor_id == doctor.doctor_id:
                # Print doctor details and schedule
                print(f'Name: \n{doctor.name} \nAge: {doctor.age} \nGender: {doctor.gender.upper()}')
                print('Schedule:')
                doctor.view_schedule()
            else:
                print("Invalid ID. Doctor not found!")

    # === MAIN MENU ===
    def main_menu(self):
        # Main interactive menu loop for the hospital system
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
                # Handle invalid menu options
                print("Invalid option. Please try again.")

# Create an instance of HospitalSystem and start the main menu loop
hospital = HospitalSystem()
hospital.main_menu()
