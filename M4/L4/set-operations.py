
set1 = {2,3,4,8}
set2 = {2,5,8,21,4}

user_choice = int(input("Please choose a number 1-4: \n1.Union\n2.Intersection\n3.Difference\n4.Symmetric Difference\n:"))

if user_choice == 1 :
    print(f"Ok The Union of set 1 and 2 is:{set1.union(set2)}")

elif user_choice == 2 :
    print(f"Ok The Intersection of set 1 and 2 is:{set1.intersection(set2)}")

elif user_choice == 3 :
    print(f"Ok The Difference of set 1 and 2 is:{set1.difference(set2)}")

elif user_choice == 4 :
    print(f"Ok The Symmetric Difference of set 1 and 2 is:{set1.symmetric_difference(set2)}")
