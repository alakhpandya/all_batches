up = ["up1", "up2"]
lp = ["lp1", "lp2"]

# final_list = [("up1", "lp1"), ("up2", "lp2")]
final_list = zip(up, lp)
for x, y in final_list:
    print(x, y)