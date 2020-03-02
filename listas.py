hall=11.25
kit=18
liv=20
bed=20
bath=9.5
home=["hall",hall,"kitchen",kit,"living room",liv,"bed",bed,"bath",bath]
print(home)

home[4]="chill zone"
home[-1]=10.5
home_ext= home + [["poolhouse",24.5],["garage",12]]

home_extt= home_ext.remove(["poolhouse",24.5])
print(home_ext      )

myNumber = '1.89099'

result = myNumber.index('.')
value = [result +1]
print (value)
