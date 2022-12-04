"""
P = []
Q = []
terms = int(input("Enter number of terms"))
for i in range(terms) :
  p = int("Enter True/False")
  P.append(p)

for i in range(terms) :
  q = int("Enter True/False")
  Q.append(q)
"""

P = [True, True, False , False , True , True]
Q = [False, True, True , False , True , False]
print(P)
print(Q)

length = len(P)
P_New = []
for i in range (0, length) :
  P_element = 1 - P[i]
  P_New.append(P_element)

C = []
for i in range(0, length) :
  element = P_New[i] + Q[i]
  if element == 0:
    C.append(False)
  else:
    C.append(True)

print(f"Final List = {C}")
count = 0
for i in range(0, length) :
  if C[i] == 0:
    count = count + 1

if count == 0:
  print("It is a Tautology")

elif count == length:
  print("It is a Contradiction")

else :
  print("It is a Satisfiabilty")