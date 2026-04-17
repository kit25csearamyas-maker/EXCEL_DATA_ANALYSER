from openpyxl import Workbook

# Create workbook
wb = Workbook()
ws = wb.active

# Add headings
ws.append(["S.No", "Name", "Department", "Subject", "Register No", "Marks"])

# Add data
ws.append([1, "Ramya", "CSE", "Maths", 101, 95])
ws.append([2, "Ravi", "CSE", "Maths", 102, 78])
ws.append([3, "Arun", "CSE", "Maths", 103, 45])

# Save file
wb.save("data.xlsx")

print("Excel file created successfully!")
