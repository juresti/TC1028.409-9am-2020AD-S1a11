print("KPH \t MPH")
for kph in range(0,261,10):
    mph = kph * 0.6214
    print(f"{kph:.2f} \t {mph:.2f}")
    