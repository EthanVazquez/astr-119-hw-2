example_dict = {
	"class" : "astro 119" ,
	"prof"  : "Brant" ,
	"awesome" : 10

}

print(type(example_dict))


course = example_dict["class"]
print(course)



example_dict["awesome"] += 1

print(example_dict)


for x in example_dict.keys():
	print(x,example_dict[x])