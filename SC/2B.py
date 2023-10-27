def mccullock_pitts_andnot(A,B):
    w1=1
    w2=-1
    threshold=0
    weighted_sum=w1*A+w2*B
    output=1 if weighted_sum>threshold else 0
    return output
input_A=int(input("Enter the value of A (0 or 1): "))
input_B=int(input("Enter the value of B (0 or 1): "))
if input_A in (0,1) and input_B in (0,1):
    result=mccullock_pitts_andnot(input_A,input_B)
    print(f"ANNOT({input_A},{input_B})={result}")
else:
    print("Invalid input.Please enter 0 or 1 for A and B.")
