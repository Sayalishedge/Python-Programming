age=int(input("enetr age"))
income=float(input("enetr income"))
if age<=25 and income <20000:
    licinstallment=5000
    medicalinssurance=4567
elif age<=25 and income <40000 :
    licinstallment=7000
    medicalinssurance=4580
elif age<=35 and income <40000 :
    licinstallment=7500
    medicalinssurance=5580
else:
    licinstallment=9000
    medicalinssurance=5600
print("lic installment : ",licinstallment)
print("medical inssurance: ",medicalinssurance)
