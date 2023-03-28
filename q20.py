rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("<table>")
for i in range(rows):
    print("<tr>", end = " ")
    for j in range(cols):
        print("<td> c </td>", end = " ")

    print("</tr>")
print("</table>")