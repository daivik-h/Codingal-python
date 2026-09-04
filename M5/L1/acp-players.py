class Player:
    def __init__(self,fname,country,team,age,height,salary,rank):
        self.fname = fname
        self.country = country
        self.team = team
        self.age = age 
        self.height = height
        self.salary = salary
        self.rank = rank
p1 = Player("Cristiano Ronaldo dos Santos Aveiro","Portugal","Al nassr",41,1.87,"4 million$(perweek)",4) 
p2 = Player("Lionel Andrés Messi Cuccitini","Argentina","Inter miami",38,1.70,"230,769$(perweek)",2) 
p3 = Player ("Neymar da Silva Santos Júnior","Brazil","Santos",34,1.75,"38.000$(perweek)",18)
print(f"Let us welcome {p1.fname} playing his sixth world cup for {p1.country} he has had a great season at {p1.team} wining the saudi league he is {p1.age} yeat he is still breakin ankels out there his physic and hegth ohh top noch when you are {p1.height} meters tall no wonder players are scared of you scoring headers his salary uhh i wish i was him {p1.salary} is crazy mate and even after playin gthe beutifull game for his entire life he is the {p1.rank}th best in the world what a player man.")
print(f"Let us welcome {p2.fname} playing his fourth world cup for {p2.country} he has had a great season at {p2.team} wining the paulistão league he is {p1.age} yeat he is still breakin ankels out there his physic and hegth ohh top noch when you are {p2.height} meters tall no wonder players are scared of you scoring skill goals his salary uhh i wish i was him {p2.salary} is crazy mate and even after playin the beutifull game for his entire life he is the {p2.rank} best in the world what a player man.")
print(f"Let us welcome {p3.fname} playing his sixth world cup for {p3.country} he has had a great season at {p3.team} wining the mls cup he is {p3.age} yeat he is still breakin ankels out there his physic and hegth ohh top noch when you are {p3.height} meters tall no wonder players are scared of you scoring solo goals his salary uhh i wish i was him {p3.salary} is crazy mate and even after playin gthe beutifull game for his entire life he is the {p3.rank}nd best in the world what a player man.")