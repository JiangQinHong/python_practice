#!/usr/bin/env python3
print("type integers, each followed by enter;or ^D or ^Z to finish")

total=0
count=0

while True:
    line=input("integer:")
    if line:
        try:
            number=int(line)
            total+=number
            count+=1
        except ValueError as err:
            print(err)
            continue
        except EOFError:
            break

if count:
    print("count=",count,"total=",total,"mean=",total/count)
