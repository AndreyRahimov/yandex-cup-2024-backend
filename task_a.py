from decimal import Decimal, getcontext

# Set the precision to 20 decimal places (you can adjust this)
getcontext().prec = 10

patients = {}
total_temp = Decimal(0)  # Running sum of temperatures
patient_count = 0  # Number of patients

while True:
    request = input().split()

    match request[0]:
        case "-":
            patient_id = request[1]

            if patient_id in patients:
                # Subtract the removed patient's temperature from the total
                total_temp -= patients[patient_id]
                # Decrease the patient count
                patient_count -= 1
                del patients[patient_id]

        case "?":
            # Calculate the average only if there are patients
            if patient_count > 0:
                avg_temp = total_temp / Decimal(patient_count)

            else:
                avg_temp = Decimal(0)  # Avoid division by zero

            print(avg_temp, flush=True)

        case "!":
            break

        case _:
            patient_id, temperature = request[1], Decimal(request[2])

            if patient_id in patients:
                # Update the total with the new temperature (subtract the old one, add the new one)
                total_temp = total_temp - patients[patient_id] + temperature

            else:
                # Add the new patient's temperature
                total_temp += temperature
                patient_count += 1

            patients[patient_id] = temperature
