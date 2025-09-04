cname=input("Enetr the consumer name:")
cnum=input("Enter the consumer number:")
pmr=float(input("Enter the present month bill: "))
lmr=float(input("Enter last month bill: "))
tu=pmr-lmr
total=3.80*tu
print(f" Consumer name:{cname} \n consumer_number:{cnum} \n Present_month_bill:{pmr} \n last_month_bill:{lmr} \n bill:{total}")
bill=0
if tu<=50:
    bill=tu*3.8
elif tu<=100:
    bill=50*3.8+(tu-50)*4.2
elif tu<=200:
    bill=50*3.8+100*4.2+(tu-100)*5.1
elif tu<=300:
    bill=50*3.8+100*4.2+150*5.1+(tu-200)*6.3
else:
    bill=50*3.8+100*4.2+150*5.1+200*6.3+(tu-300)*7.5
print(bill)
    