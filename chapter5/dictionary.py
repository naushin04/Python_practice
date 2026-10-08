
marks = {   
    "Naushin": 90,
    "Tanay": 80,
    "Polok": 85
}

print(marks, type(marks))       
print(marks["Naushin"]) 
print(marks.keys())
print(marks.values())
marks.update({"Naushin":99, "Haraf":100})
print(marks)
print(marks.get("Naushin1"))    #prints none 
#print(marks["Naushin1"])        #returns an error
marks.pop("Naushin")
print(marks)