"""
Make a list of national holidays in The Netherlands (assume current year). 
Write a program that reads a month and day from the user. 
If the month and day match one of the holidays in the list then your program should display the holiday’s name. 
Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.
"""

holidays = {
    "2022-01-01": "Nieuwjaarsdag",
    "2022-04-15": "Goede vrijdag",
    "2022-04-17": "Pasen (eerste Paasdag)",
    "2022-04-18": "Pasen (tweede Paasdag)",
    "2022-04-27": "Koningsdag",
    "2022-05-05": "Bevrijdingsdag",
    "2022-05-26": "Hemelvaartsdag",
    "2022-06-05": "Pinksteren (eerste pinksterdag)",
    "2022-06-06": "Pinksteren (tweede pinksterdag)",
    "2022-12-24": "Kerstmis (eerste Kerstdag)",
    "2022-12-25": "Kerstmis (tweede Kerstdag)",
}

month = input("Month: ")
print(month)
day = input("Day: ")
print(day)

# if date in holidays:
#     print("Feestdag:", holidays[date])
# else:
#     print("Geen feestdag")
