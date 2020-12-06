def eligible_for_vote(consider_age):
    age=int(input("enter the age"))
    if age >=consider_age:
        print("you are eligible")
    else:
        print("not eligible")
   
eligible_for_vote(18)