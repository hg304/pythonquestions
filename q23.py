gpa = 3.0
ais = float(input("Enter AIS threshold: "))

#AIS = 2.5 * (GPA / 4.0) * 100 + (test_score / 1600) * 100
#AIS/100 = 2.5 * (GPA / 4.0) + (test_score / 1600)
#1600 * (AIS/100) = 1600 * 2.5 * (GPA / 4.0) + test_score
#test_score = 1600 * (AIS/100) - 1600 * 2.5 * (GPA / 4.0)

print("Combinations that meet threshold:")
for i in range(int(gpa*10), 41):
    score = 1600 * (ais / 100) - 1600 * 2.5 * (float(i/10)/ 4.0)
    print(f"GPA: {str(float(i/10))}   Score: {str(score)}")