l= int(input("Enter price : "))
b= int(input("Enter quantity: "))
a= int(l*b)
gst=a*0.05
total=a+gst
print(f"Total Bill = {a}")
print(f"GST (%5) = {gst}")
print(f"grand total = {total}")
M=int(input("Enter minutes: "))
h=M//60
m=M%60
s=m*60
print(f"{h} hours and {m} minutes and {s} seconds")
