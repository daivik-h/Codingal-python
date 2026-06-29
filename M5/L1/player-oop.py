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
print(f"Let us welcome {p1.fname} playing his sixth world cup for {p1.country} he has had a great season at {p1.team} wining the saudi league he is {p1.age} yeat he is still breakin ankels out there his physic and hegth ohh top noch when you are {p1.height} meters tall no wonder players are scared of you scoring headers his salary uhh i wish i was him {p1.salary} is crazy mate and even after playin gthe beutifull game for his entire life he is the {p1.rank}th best in the world what a player man.")       