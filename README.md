# BrightNetwork
BrightNetwork task that was done during the internship duration - the task was to create a path finding algorithim

### How does my path finding algorithm work?

-First the algorithm checks if the finish coordinate is further left, or further right. 
-If its further left, it will go 1 square left (provided there is no obstacle), if it is further right it will go 1 square right
-Afterward it goes in that direction, it will check if is stepping on an obstacle, if it is, it will go back to its starting point.
-This means the algorithm now learn there is an obstacle in that direction, so now it will choose whether to go up or down.
-It will now instead check if it can move up or down.
-The same process for left and right, is then used for the up and down algorithim.
-This whole algorithm is placed in a while loop, so it will eventually find its path.

![alt text](https://github.com/Mahdi2c/storage/blob/master/BrightNetwork/1.jpg)

Here is an example run.

First all the obstacle locations are printed out, and then the start and finish line are also shown.  

The algorithm then finds its path from (3,2) to (9,9)
