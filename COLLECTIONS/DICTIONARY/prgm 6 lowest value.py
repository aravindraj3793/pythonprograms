dic={
    "physics":50,
    "Maths":30,
    "science":40
}

#out=lowest score subject name
print(min(dic,key=dic.get))
