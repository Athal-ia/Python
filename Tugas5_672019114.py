import sys
from fuzzywuzzy import fuzz 
import pandas as pd

df = pd.read_csv('room_type.csv')
df.head()

def main():
   menu()

def menu():
    print(30 * "=" , "MENU" , 30 * "=")
    
    choice = input("""
1. Ratio
2. Partial Ratio
3. Token Set Ratio
4. Partial Token Set Ratio
5. Lihat data yang serupa
6. Lihat data yang sama
7. Exit

Pilihan: """)

    if choice == "1":
        ratio()
        menu()
    elif choice == "2":
        pr()
        menu()
    elif choice == "3":
        tsr()
        menu()
    elif choice == "4":
        ptsr()
        menu()
    elif choice == "5":
        serupa()
        menu()
    elif choice == "6":
        sama()
        menu()
    elif choice == "7":
        sys.exit
    else:
        print("Input salah")
        menu()

def ratio():
   kt1 = (input("Masukkan kata 1 : "))
   kt2 = (input("Masukkan kata 2 : "))
   
   ratio = fuzz.ratio(kt1, kt2)
   print("Rasio dari", kt1, "dan", kt2, "adalah", ratio)
   
   if (ratio > 80):
       print("Tinggi")
       print("\n")
      
   elif (ratio >= 50):
       print("Cukup")
       print("\n")
       
   else:
       print("Rendah")
       print("\n")   
    
def pr():
   kt1 = (input("Masukkan kata 1 : "))
   kt2 = (input("Masukkan kata 2 : "))
   ratio = fuzz.partial_ratio(kt1.lower(), kt2.lower())
   print("Rasio partial dari", kt1, "dan", kt2, "adalah", ratio)
   
   if (ratio > 80):
       print("Tinggi")
       print("\n")
      
   elif (ratio >= 50):
       print("Cukup")
       print("\n")
       
   else:
       print("Rendah")
       print("\n")

def tsr():
   kt1 = (input("Masukkan kata 1 : "))
   kt2 = (input("Masukkan kata 2 : "))
   ratio = fuzz.token_set_ratio(kt1, kt2)
   print("Token set rasio dari", kt1, "dan", kt2, "adalah", ratio)
   
   if (ratio > 80):
       print("Tinggi")
       print("\n")
      
   elif (ratio >= 50):
       print("Cukup")
       print("\n")
       
   else:
       print("Rendah")
       print("\n")

def ptsr():
   kt1 = (input("Masukkan kata 1 : "))
   kt2 = (input("Masukkan kata 2 : "))
   ratio = fuzz.partial_token_set_ratio(kt1, kt2)
   print("Partial token set rasio dari", kt1, "dan", kt2, "adalah", ratio)
   
   if (ratio > 80):
       print("Tinggi")
       print("\n")
      
   elif (ratio >= 50):
       print("Cukup")
       print("\n")
       
   else:
       print("Rendah")
       print("\n")

def serupa():
   print(20 * "=" , "Lihat Data Serupa" , 15 * "=")
   print(df.head)
   print(20 * "=" , "Data Serupa" , 15 * "=")
    
   def get_ratio(row):
       name = row['Expedia']
       name1 = row['Booking.com']
       return fuzz.partial_ratio(name, name1)
   print(df[df.apply(get_ratio, axis = 1) > 85])
   print("\n")

def sama():
   print(15 * "=" , "Lihat Data Sama" , 15 * "=")
   print(df.head)
   print(15 * "=" , "Data Sama" , 15 * "=")
    
   def ratio2(row):
       name = row['Booking.com']
       name1 = row['Expedia']
       return fuzz.ratio(name, name1)
   x = len(df[df.apply(ratio2, axis = 1) > 99]) / len(df)
   print(x)
   print(df[df.apply(ratio2, axis = 1) > 99])
   print("\n")

main()