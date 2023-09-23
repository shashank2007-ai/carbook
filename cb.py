import random

print('                                  WELCOME TO CAR BOOKING/SELLING/RENTING SYSTEM')
print('          _______            -           __                                ______--------___   ')
print('         //  ||\ \         --          ~( @\   \                          /|             / |   ')
print('   _____//___||_\ \___    ---   _________]_[__/_>________      o___________|_\__________/__|   ')
print('  }  _          _    \         /  ____ \ <>     |  ____  \    ]|___     |  |=   ||  =|___  |   ')
print('  |_/ \________/ \___|        =\_/ __ \_\_______|_/ __ \__D   //   \\    |  |____||_///   \\|  ')
print(' ___\_/________\_/______  ________(__)_____________(__)____   |  X  |\--------------/|  X  |\   ')
print('                                                               \___/                  \___/   ')
print("WELCOME TO OUR NO.1 CAR RESALE AND BOOKING SITE!! ENJOY 10% OFF ON YOUR FIRST REGISTRATION")
U_name=input("Enter your name:")
res=input("Enter your state of residence:")
ph_no=int(input("Enter your phone number:"))
email=input("Enter your E-Mail:")
print("Would you like to recieve daily update on your E-Mail"
      "answer in 'yes' or 'no'")
input("")
def otttp():
  otp=random.randint(1000,9999)
  print("your OTP is :",otp)
  ottp=int(input("Enter the OTP sent on your mobile:"))
  if otp==ottp:
    print("OTP verified")
  else:
    print("incorrect otp")
    otttp()
otttp()
print('Choose mode\nBuy\t\tSell\t\tRent')
mode = input('')
print('Enter Car Class\nSUV\t\tSEDAN\t\tSPORTS\t\tLUXURY')
t_suv=('Audi Q3','BMW X5','Tata Safari','Mahindra Thar','Ford Ecosport','Land Rover','Mercedes G Class','Kia Sonet','Toyota Fortuner','Nissan Magnite')
t_sedan=('Audi A4','Nissan Altima','Mercedes Benz','Skoda Slavia','Swift Dezire','BMW M340I','Hyundai Aura','Volvo S90','Toyota Camry','Jaguae XF')
t_sports=('Chevolet Camaro','Chevolet Corvette','Ford Mustang','Mclaren Artura','Porche 911','Pagani Zonda R','Toyota Supra','Audi TT',"Mazda Furai")
t_luxury=('Rolls Royce-Phantom','BMW 2 Series Gran Coupe','MG Gloster','Mercedes-Benz A-Class Limousine','Toyota Fortuner Legender','BMW (modified)','Aston Martin','Beast','Bentley')
def Cartype():
  a = input('')
  return a
cartype=Cartype()
def SUV():
  print('choose car to see more details (use option number or first word )')
  print('available Cars:-\n 1. Audi Q3 \t 2. BMW X5 \t 3. Tata Safari \t 4. Mahindra Thar \t 5. Ford Ecosport \n 6. Land rover \t 7. Mercedes G Class \t 8. Kia Sonet \t9. Toyota Fortuner \t10. Nissan Magnite')
  Suv_option=int(input(''))
  print(t_suv.index(Suv_option))
def Sedan():
  print('choose car to see more details (use option no or first word of car)')
  print('available Cars:-\n 1. Audi A4 \t 2. Nissan Altima \t 3. Mercedes Benz \t 4. Skoda Slavia \t5. Swift Dezire \n 6. BMW M340I \t 7. Hyundai Aura \t8. Volvo S90 \t9. Toyota Camry \t10. Jaguar XF')
  sedan_option=int(input(''))
  print(t_suv.index(sedan_option))
def sports():
  print("choose car to see more details (use option no or first word of car)")
  print("available cars:-\n 1.Chevolet Camaro \t 2 .Chevolet Corvette \t 3.Ford Mustang \t 4.Mclaren Artura \t 5.Porche 911 \t 6.Pagani Zonda R \t 7.Toyota Supra \t 8.Audi TT \t 9:Mazda Furai}")
  sports_option=int(input(''))
  print(t_sports.index(1))
def luxury():
  print("choose car to see more details (use option no or first word of car)")
  print("available cars:-\n 1.Rolls Royce-Phantom \t 2 .BMW 2 Series Gran Coupe \t 3.MG Gloster \t 4.Mercedes-Benz A-Class Limousine \t 5.Toyota Fortuner Legender \t 6.BMW (modified) R \t 7.Aston Martin \t 8.Beast \t 9:Bentley}")
  luxury_option=int(input(''))
  print(t_luxury.index(luxury_option))
if cartype == 'SUV' or cartype == 'suv':
  SUV()
  print("Ex-showroom price >> 17 Lakh"
        "On-Road price >> 18.5 Lakh")
elif cartype == 'SEDAN' or cartype == 'sedan':
  Sedan()
  print("Ex-showroom price >> 10 Lakh"
        "On-Road price >> 11 Lakh")
elif cartype == 'SPORTS' or cartype == 'sports':
  sports()
  print("Ex-showroom price >> 25 Lakh"
        "On-Road price >> 27 Lakh")
elif cartype == 'LUXURY' or cartype == 'luxury':
  luxury()
  print("Ex-showroom price >> 55 Lakh"
        "On-Road price >> 60.15 Lakh")







