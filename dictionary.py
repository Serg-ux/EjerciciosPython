myfamily={
    "child1" : {
        "name":"Emily",
        "year": 2004
    },
     "child2" : {
        "name":"Tobias",
        "year": 2007
    },
     "child3" : {
        "name":"Linus",
        "year": 2011
    }
}
x=myfamily["child3"]
y=x.get("year")
print(y)