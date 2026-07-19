# Available cities
print("Available cities:")
print("Cape Town")
print("OR Tambo")
print("PE")
print()

# User inputs
city_flight = input ( "Enter a city you will be flying to: "                             ).lower()
num_nights  = int ( input ( "Enter the number of nights you will be staying in a hotel: "))
rental_days = int ( input ( "Enter the number of days you will be hiring a car for: "    ))


# Hotel cost function
def hotel_cost ( num_nights ):
    """
    Calculate the total hotel cost based on the number of nights.
    """
    cost_per_night = 800
    return num_nights * cost_per_night


# Plane cost function
def plane_cost ( city_flight ):
    """
    Return the flight cost for the selected destination.
    """

    if city_flight == "cape town":
        return 1500

    elif city_flight == "or tambo":
        return 1200

    elif city_flight == "pe":
        return 800

    else:
        return 0


# Car rental function
def car_rental ( rental_days ):
    """
    Calculate the total car rental cost based on the number of days.
    """
    rental_per_day = 1200
    return rental_days * rental_per_day


# Holiday cost function
def holiday_cost ( num_nights, city_flight, rental_days ):
    """
    Calculate the total holiday cost by combining
    hotel, flight, and car rental costs.
    """

    total_holiday_cost = (
        hotel_cost ( num_nights )
        + plane_cost ( city_flight )
        + car_rental ( rental_days )
    )

    return total_holiday_cost


# Check city validity
if plane_cost ( city_flight ) == 0:

    print ( "Invalid city selected. Please choose Cape Town, OR Tambo, or PE." )

else:

    holiday = holiday_cost (
        num_nights,
        city_flight,
        rental_days
    )

    print ( "\n------ HOLIDAY SUMMARY ------" )
    print ( f"Destination    : {city_flight.title() }" )
    print ( f"Hotel stay     : {num_nights } nights"   )
    print ( f"Car rental     : {rental_days} days"     )
    print ( f"Flight cost    : R{plane_cost (city_flight):,.2f}" )
    print ( f"Hotel cost     : R{hotel_cost (num_nights):,.2f}"  )
    print ( f"Car rental cost: R{car_rental (rental_days):,.2f}" )
    print ( "-----------------------------" )
    print ( f"Total holiday cost: R{holiday:,.2f}" )
    