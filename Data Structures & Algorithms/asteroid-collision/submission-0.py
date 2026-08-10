from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulate asteroid collisions using a stack.

        Positive values move right, negative values move left.
        Only asteroids moving toward each other (right vs left) can collide.
        """
        if not asteroids:
            return []

        stack: List[int] = []

        for asteroid in asteroids:
            # A collision is only possible when:
            # - the last asteroid in the stack is moving right (stack[-1] > 0)
            # - the current asteroid is moving left (asteroid < 0)
            while stack and asteroid < 0 < stack[-1]:

                # Determine which asteroid is larger.
                # diff < 0  : current asteroid is larger (stack top explodes)
                # diff > 0  : stack top is larger (current asteroid explodes)
                # diff == 0 : both explode
                diff: int = asteroid + stack[-1]

                if diff < 0:
                    # Current asteroid (moving left) is larger.
                    # Remove the smaller right-moving asteroid.
                    stack.pop()
                elif diff > 0:
                    # Stack top asteroid wins.
                    # Current asteroid is destroyed.
                    asteroid = 0
                else:
                    # Same size: both are destroyed.
                    asteroid = 0
                    stack.pop()

                # If current asteroid is gone, stop checking collisions.
                if asteroid == 0:
                    break

            # Only push asteroid if it still exists after collision checks.
            if asteroid != 0:
                stack.append(asteroid)

        return stack
