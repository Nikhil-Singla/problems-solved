class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        last = asteroids[-1]
        for i in asteroids:
            if i > mass:
                return False
            mass += i

            if mass >= last:
                return True

        return True