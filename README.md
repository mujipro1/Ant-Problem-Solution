# ANT Problem

### Problem Statement

Luca, an eminent ant researcher, took two photos a short time apart at
a group of ants on the move. Unfortunately the photos came out wrong, and you can't
distinguish the direction in which the ants were oriented: they are just black dots.
Considering A the vector of the positions Ai of the ants (in one dimension) in the
first photo, and B the vector of the Bi positions of the ants (in one dimension) in the
second photo, we want to understand, scrolling K from 1 to N (the number of ants) how many there are the K for which precisely K ants moved from left to right (hence theirs
position has increased).

For example, having vectors

    A = 3 8 10 13 17
    B = 4 7 18 19 20

then K can be equal to either 3:

    3 -> 18
    13 -> 19
    17 -> 20

but also a 4:

    3 -> 4
    10 -> 18
    13 -> 19
    17 -> 20

and no other configuration with a different K is possible. So the answer is 2.
Write an algorithm which, given the vectors A and B, returns the number of possible different Ks.


### Solution:
Instead of going towards iterative approach, that was failing
continuously, I went for the mathematical approach. After a bit of
focus and some testing on paper, i found that there exists a mathematical
formula that can solve the algorithm directly, here's a description
of the formula:

    K = K_max - K_min + 1

where K_max is a counter that is increased by 1 only if any ith term of 
vector B is greater than or equal to the ith term of vector A, that is 

        K_max++ if A[i] >= B[i]

and K_min is the number of elements of vector B that are greater in 
value to the last element of A, 

        K_min = no of indexes in B > A[N] (last element)

E.g : if A = [1,2,3,4,5] and B=[3,4,5,6,7], then the last element of A is 5
and there are 2 elements in B greater than 5, so K_min is 2.

Lets look at the given example of professor:

    A = [3, 8, 10, 13, 17]
    B = [4, 7, 15, 18, 19]

Here K_min is 3, i.e 3 elements in B are greater from A[N] (N is length of vector)
and K_max is 4 i.e 4 elements of A are smaller in values to their corresponding values in B.


### Description
Now, how does the approach works, K_min actually represents the minimum configuration or value of K possible, in this case 3, and K_max represents maximum number of values of K possible, that is 4 in this case, after a lot of testing and hit and trial, it has been found that all possible values between K_min and K_max will be a possible configuration and exist in all cases, so we dont need to iterate over all of these values, instead by simply finding K_min and K_max, we can find the final value of K using the formula. 


**_Algorithm developed by Mujtaba Shafqat_**