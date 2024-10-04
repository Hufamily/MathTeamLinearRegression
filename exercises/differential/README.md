# Breakdown
If you have already done the previous exercises in ```MathTeamLinearRegression/exercises/fitting/```, you can use these programs as examples of how to use scipy to plot differential equations.

```SimpleHarmonicOscillator.py``` is a good place to start. It plots out the equation, dy/dt = -k*y.

Then you can take a look at some of the other oscillator programs(Essentially the same thing, but with additional terms), or look at ```PredatorPrey``` which plots out the Lotka Voltera equations.

```GravityAnimation.py``` demonstrates a way to visualize integration across 2 different variables.

```ProblemAEcosystem.py``` was the program I wrote for HiMCM 2023, about Dandelion populations. It is essentially a more convoluted form of the Lotka Voltera equations. One mistake I made in this program is that I manually set the fit parameters due to lack of data, but you should combine these functions with your fitting functions to fit your differential equations to data.

```Simple Derivative.py``` was just an example of how you can use a matrix to get an approximation of the derivative of a vector, but it could be useful if you have the data without a function to find the derivative analytically.
