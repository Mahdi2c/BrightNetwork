# BrightNetwork
During my internship in BrightNetwork I created a path finding algorithm, that goes from point A to point B, while avoiding and going round any obstacles

### How does my path finding algorithm work?

-First the algorithm checks if the finish coordinate is further left, or further right. <br>
-If its further left, it will go 1 square left (provided there is no obstacle), if it is further right it will go 1 square right. <br>
-Afterward it goes in that direction, it will check if it is stepping on an obstacle, if it is, it will go back to its starting point. <br>
-This means the algorithm now learns that there is an obstacle in that direction, so now it will choose whether to go up or down. <br>
-It will now instead check if it can move up or down. <br>
-The same process for the left and right algorithm, is then used for the up and down algorithim. <br>
-This whole algorithm is placed in a while loop, so it will eventually find its path. <br>

![alt text](https://github.com/Mahdi2c/storage/blob/master/BrightNetwork/1.jpg)

Here is an example run.

First all the obstacle locations are printed out, and then the start and finish line are also shown.  

The algorithm then finds its path from (3,2) to (9,9)

Diagram of the track:

![alt text](https://github.com/Mahdi2c/storage/blob/master/BrightNetwork/2.jpg)
