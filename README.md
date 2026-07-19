# Holiday Cost Calculator

## Project Description

The Holiday Cost Calculator is a Python program that calculates the total cost of a holiday based on the user's travel details.

The program asks the user to enter:

- The city they will be flying to
- The number of nights they will stay in a hotel
- The number of days they will hire a car

It then calculates:

- The flight cost
- The hotel cost
- The car rental cost
- The total holiday cost

The available destinations are:

- Cape Town
- OR Tambo
- PE

## Functions Used

The program contains the following functions:

- hotel_cost() – Calculates the total hotel cost.
- plane_cost() – Returns the flight cost for the selected destination.
- car_rental() – Calculates the total car rental cost.
- holiday_cost() – Calculates the complete holiday cost.

## How to Run the Program

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

python holiday.py


## Example Output

Available cities:
Cape Town
OR Tambo
PE

Enter a city you will be flying to: Cape Town
Enter the number of nights you will be staying in a hotel: 3
Enter the number of days you will be hiring a car for: 2

------ HOLIDAY SUMMARY ------
Destination    : Cape Town
Hotel stay     : 3 nights
Car rental     : 2 days
Flight cost    : R1,500.00
Hotel cost     : R2,400.00
Car rental cost: R2,400.00
-----------------------------
Total holiday cost: R6,300.00
