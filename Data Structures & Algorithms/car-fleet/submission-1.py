class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(key=lambda x:x[0], reverse=True)
        print(cars)

        fleets=0
        x=float('-inf')
        for car in cars :
            time= (target-car[0])/car[1]
            if time>x:
                x=time
                fleets+=1
            # else:
            #     x=time
        return fleets