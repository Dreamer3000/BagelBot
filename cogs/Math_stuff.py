import discord
from discord.ext import commands
import sys,os
import matplotlib.pyplot as plt
import numpy as np
#from scipy.integrate import odeint

master = "/Users/justinbeutel/Desktop/Python_Programs_2020/Discord_bot_Stuff"
codex = ["sin", "cos", "tan","cot", "csc", "sec", "log", "exp", "ln"]

client = commands.Bot(command_prefix = "$")
class Math(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        # functions in a class need this to function
        print("Ready to Integrate")
    
    @commands.command(aliases = ["Log"], help = "Finds the log of a number")
    async def log(self, ctx, arg1):
        try:
            answer = np.log10(int(arg1))
            await ctx.send("The log of " + arg1 + " is " + str(answer))
            
        except:
            await ctx.send("An error occured, please check your input or contact the Head Pastiere")
            await ctx.send(str(sys.exc_info()[0]))
            await ctx.send(str(sys.exc_info()[1]))
    
    @commands.command(aliases = ["NaturalLog", "LN"], help = "Finds the natural log of a numebr")
    async def ln(self, ctx, arg1):
        
        try:
            answer = np.log(int(arg1))
            await ctx.send("The natural log of " + arg1 + " is " + str(answer))
            
        except:
            await ctx.send("An error occured, please check your input or contact the Head Pastiere")
            await ctx.send(str(sys.exc_info()[0]))
            await ctx.send(str(sys.exc_info()[1]))
    
    @commands.command(aliases = ["EXP", "Power"], help = "Raises numbers to a given power")
    async def exp(self, ctx, *args):
        answer = 0
        counter = 0
        try:
            
            for i in range(0, len(args)):
                if counter == 0:
                    answer = float(args[i]) ** 1.0
                    counter += 1
                   
                else:
                    answer = answer ** float(args[i])
                    counter += 1
                  
            await ctx.send("Your answer is: " + str(answer))
            
        except:
            await ctx.send("An error occured, please check your input or contact the Head Pastiere")
            await ctx.send(str(sys.exc_info()[0]))
            await ctx.send(str(sys.exc_info()[1]))

    @commands.command(help = "Takes in 12 arguments, and solves for x,y and z. Refer to $Cramer_help for a tutorial")
    async def cramer(self, ctx, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
    
        D_extended = [[float(arg1), float(arg2), float(arg3), float(arg1), float(arg2)],
                 [float(arg5), float(arg6), float(arg7), float(arg5), float(arg6)],
                 [float(arg9), float(arg10), float(arg11), float(arg9), float(arg10)]]
    
        D_normal1 = (D_extended[0][0] * D_extended[1][1] * D_extended[2][2]) + (D_extended[0][1] * D_extended[1][2] * D_extended[2][3]) + (D_extended[0][2] * D_extended[1][3] * D_extended[2][4])
        D_normal2 = (D_extended[0][2] * D_extended[1][1] * D_extended[2][0]) + (D_extended[0][3] * D_extended[1][2] * D_extended[2][1]) + (D_extended[0][4] * D_extended[1][3] * D_extended[2][2])
        D_determ = D_normal1 - D_normal2
    
        Dx_extended = [[float(arg4), float(arg2), float(arg3), float(arg4), float(arg2)],
                  [float(arg8), float(arg6), float(arg7), float(arg8), float(arg6), float(arg7)],
                  [float(arg12), float(arg10), float(arg11), float(arg12), float(arg10)]]
    
        Dx1 = (Dx_extended[0][0] * Dx_extended[1][1] * Dx_extended[2][2]) + (Dx_extended[0][1] * Dx_extended[1][2] * Dx_extended[2][3]) + (Dx_extended[0][2] * Dx_extended[1][3] * Dx_extended[2][4])
        Dx2 = (Dx_extended[0][2] * Dx_extended[1][1] * Dx_extended[2][0]) + (Dx_extended[0][3] * Dx_extended[1][2] * Dx_extended[2][1]) + (Dx_extended[0][4] * Dx_extended[1][3] * Dx_extended[2][2])
        Dx_determ = Dx1 - Dx2
    
        Dy_extended = [[float(arg1), float(arg4), float(arg3),float(arg1), float(arg4)],
                  [float(arg5), float(arg8), float(arg7), float(arg5), float(arg8)],
                  [float(arg9), float(arg12), float(arg11), float(arg9), float(arg12)]]
    
        Dy1 = (Dy_extended[0][0] * Dy_extended[1][1] * Dy_extended[2][2]) + (Dy_extended[0][1] * Dy_extended[1][2] * Dy_extended[2][3]) + (Dy_extended[0][2] * Dy_extended[1][3] * Dy_extended[2][4])
        Dy2 = (Dy_extended[0][2] * Dy_extended[1][1] * Dy_extended[2][0]) + (Dy_extended[0][3] * Dy_extended[1][2] * Dy_extended[2][1]) + (Dy_extended[0][4] * Dy_extended[1][3] * Dy_extended[2][2])
    
        Dy_determ = Dy1 - Dy2
    
        Dz_extended = [[float(arg1), float(arg2), float(arg4), float(arg1), float(arg2)],
                  [float(arg5), float(arg6), float(arg8), float(arg5), float(arg6)],
                  [float(arg9), float(arg10), float(arg12), float(arg9), float(arg10)]]
    
        Dz1 = (Dz_extended[0][0] * Dz_extended[1][1] * Dz_extended[2][2]) + (Dz_extended[0][1] * Dz_extended[1][2] * Dz_extended[2][3]) + (Dz_extended[0][2] * Dz_extended[1][3] * Dz_extended[2][4])
        Dz2 = (Dz_extended[0][2] * Dz_extended[1][1] * Dz_extended[2][0]) + (Dz_extended[0][3] * Dz_extended[1][2] * Dz_extended[2][1]) + (Dz_extended[0][4] * Dz_extended[1][3] * Dz_extended[2][2])
    
        Dz_determ = Dz1 - Dz2
    
        X = Dx_determ / D_determ
        Y = Dy_determ / D_determ
        Z = Dz_determ / D_determ
    
        await ctx.send("We have solved your equations")
        await ctx.send("X is equal to " + str(X) + ", Y is equal to " + str(Y) + ", and Z is equal to " + str(Z))
 

    @commands.command(help = "In-depth explanation of how to use $cramer")
    async def Cramer_help(self,ctx):
        await ctx.send("$cramer takes in 12 arguments: the coefficients and answers of your 3 equation system, row by row.")
        await ctx.send("""For example:
2x + 3y -9z = 12
5x + 100y -4z = 0
-34x + 8y + 32x = -3087

You should type '$cramer 2 3 -9 12 5 100 -4 0 34 8 32 -3087'""")
        
    @commands.command(aliases = ["Ordinary", "ODE"], help = "Plots an Ordinary Differential Equation")
    async def ode(self, ctx, *args):
        
        def od(x,t):
            
            equation = args[0]
            equation2 = args[0]
            print(equation)
            print(type(equation))
            print(equation2)
            
            pass
        pass
    
    #@commands.command
    
    @commands.command(aliases = ["Standard_Deviation", "SD"], help = ("Finds the standard deviation of a set of data. Type in as many data points as you wish."))
    async def standard_deviation(self, ctx, *args):
        temp = []
        total = 0
        for i in range(len(args)):
            total += float(args[i])
            temp.append(args[i])
      
        counter = 0
        print("test 1")
        for i in range(len(temp)):
           
            counter += (float(str(args[i])) - (total/len(temp)) ) ** 2.0
            
        answer = (counter / len(temp)) ** 0.5
            
        await ctx.send("The standard deviation of your datapoints is: " + str(answer))
        
    @commands.command(aliases = ["chi_squared", "CHI_Sqaured", "Chi"], help = ("Finds the chi squared value of a dataset, with unlimited points and only 1 expected value. This version only supports 1 expected value."))
    async def Chi_Squared(self, ctx, *args):
        await ctx.send("Notice: This Chi Squared only supports one expected value")
        temp = []
        counter = 0
                  
        for i in range(len(args)):
            temp.append(args[i])
        print(temp)
        expected = temp[-1]
        print(expected)

        for i in range(len(temp)-1):
            
            counter += ((float(temp[i]) - float(expected)) ** 2) / float(expected)
            print(float(temp[i]))
            print(counter)
            
 
       
        await ctx.send("The Chi Squared of your datapoints is: " + str(counter))
    
    
    @commands.command(aliases = ["Permutation"], help = ("Calculates the number of permutations of 'n' objects taken 'r' at a time. Takes in arguments n and r"))
    async def permutation(self, ctx, arg1, arg2):
        
        def fact(n):
            answer = 1
            for i in range(1, n+1):
                answer = answer * i
        
            return answer
        
        n = fact(int(arg1))
        print(n)
        print(fact(int(arg1) - int(arg2)))
        
        answer = n / fact(int(arg1) - int(arg2))
        await ctx.send("The number of permutations according to your data is: " + str(answer))


    @commands.command(aliases = ["Combination"], help = ("Calculates the number of combinations of 'n' objects taken 'r' at a time. Takes in arguments n and r"))
    async def combination(self, ctx, arg1, arg2):

        def fact(n):
            answer = 1
            for i in range(1, n+1):
                answer = answer * i
        
            return answer
        
        n = fact(int(arg1))
        answer = n / (fact(int(arg1) - int(arg2)) * fact(int(arg2)))
        
        await ctx.send("The number of combinations for your data is: " + str(answer))
    
    @commands.command(aliases = ["Plot", "P"], help = ("Plot a graph or a function based on user input. Insert the x boundries and the function."))
    async def plot(self, ctx, *args):
        
        os.chdir(master)
        A = False
            
        global codex
        y = []
        if len(args) > 2:
            x1 = int(args[0]) 
            x2 = int(args[1])
            
        x = np.linspace(x1,x2, abs(x1) + abs(x2))   
        func = args[len(args)-1]
            
        if str(func) in codex:
                A = True
                if str(func) == "csc":
                    
                    for i in x:
                        y.append(1 / np.sin(x[int(i)]))
                        
                elif str(func) == "cot":
                    for i in x:
                        y.append(np.cos(x[int(i)]) / np.sin(x[int(i)]))
                    
                elif str(func) == "sec":
                    for i in x:
                        y.append(1 / np.cos(x[int(i)]))
                
                elif str(func) == "log":
                    for i in x:
                        y.append(np.log10(x[int(i)]))
                
                elif str(func) == "ln":
                    for i in x:
                        y.append(np.log(x[int(i)]))
                
                elif str(func) == "exp":
                    for i in x:
                        y.append(np.exp(x[int(i)]))
                
                elif str(func) == "sin":
                    
                    for i in x:
                        y.append(np.sin(x[int(i)]))
                        print(len(x))
                        print(len(y))
                    
                elif str(func) == "cos":
                    for i in x:
                        y.append(np.cos(x[int(i)]))
                
                elif str(func) == "tan":
                    for i in x:
                        y.append(np.sin(x[int(i)]) / np.cos(x[int(i)]) )
    
                
        if A == False:
            for i in x:
                y.append(x[int(i)] ** func)
            
        
        print(y)
        
      
        plt.plot(x,y ,'b--')
        plt.grid(True)
        plt.title(f'{ctx.message.author}\'s Graph')
        plt.savefig(fname='plot')
        #print(os.path.dirname(os.path.realpath('plot.png')))
        with open("plot.png","rb") as tacos:
            t = discord.File(tacos, filename = "plot.png")
        await ctx.send(file = t)
        plt.clf()
        os.remove('plot.png')
        
        
        
        
        
    @commands.command(aliases = ["Pythag", "pythagoras", "pythag", "pg"], help = "Takes in 3 arguments, 2 numbers and what side you're looking for (a,b or c). For example: $Pythag 10 14 a")
    async def Pythagoras(self,ctx, arg1, arg2, arg3):
    
        if arg3.lower() == "c":
            answer = (int(arg1) ** 2 + int(arg2) ** 2) ** (1/2)
            await ctx.send("Your answer is " + str(answer))
        
        else:
            if int(arg1) > int(arg2):
                answer = (int(arg1) ** 2 - int(arg2) ** 2) ** (1/2)
                await ctx.send("Your answer is " + str(answer))
            
            elif int(arg2) > int(arg1):
                answer = (int(arg2) ** 2 - int(arg1) ** 2) ** (1/2)
                await ctx.send("Your answer is " + str(answer))
    
    @commands.command(help = "Will tell you the average of however many arguments you pass it, for example: $mean 1 87 52")
    async def mean(self, ctx, *args):
    
        length = len(args)
        counter = 0
        for i in args:
            counter += int(i)
        await ctx.send("The mean of your numbers is " + str(counter /len(args)))
        
    @commands.command(aliases = ["Solve", "S"], help = ("Finds the roots of an equation, supplied with the exponents of your equation. The last term should be the answer to the equation, and the second to last is the constant (type 0 if there's no constant)"))
    
    async def solve(self, ctx, *args):
      
        lower = np.linspace(0, -1000000000000)
        upper = np.linspace(1,10000000000001)
        terms = [x for x in args]
        answer = terms[len(terms)-1]
        constant = float(terms[len(terms) - 2])
        constant = constant - float(answer)
        results = []
        print(terms)
        print("hi 1")
        temp = 0
        a = 0
        b = 0
        x = True
        test = 0.000000000000001
        for d in range(len(lower)):
            if d == 0:
                for i in range(len(terms) - 2):
                    a = lower[d] ** float(terms[i])
                    b = upper[d] ** float(terms[i])
                    print("hi 1.5")
                    print(a)
                    print(b)
                a += constant
                b += constant
                print("hi 1.6")
                print(a)
                print(b)
                if a == float(answer):
                    results.append(a)
                elif b == float(answer):
                    results.append(b)
                else:
                    if abs(a) < abs(b):
                        temp = a
                        
                    else:
                        temp = b
                      
            else:
                print("hi 1.7")
                for i in range(len(terms) - 2):
                    a =  lower[d] ** float(terms[i])
                    b = upper[d] ** float(terms[i])
                a += constant
                b += constant
                print(a)
                print(b)
                print("hi 1.8")
                if a == float(answer):
                    results.append(a)
                elif b == float(answer):
                    results.append(b)
                else:
                    if abs(a) < temp and abs(a) < abs(b):
                        temp = a
                        a = 0
                        b = 0
                    elif abs(b) < temp and abs(b) < abs(a):
                        temp = b
                        a = 0
                        b = 0
                    elif abs(a) > temp and abs(b) > temp:
                        break
        print("hi 2")
        print(results)
        if results[0] == float(answer):
            pass
        
        else:
            print("hi 2.1")
            
            while x == True:
                print("hi 2.3")
                if temp < test:
                    results.append(b)
                    break
                else:
                    print("hi 3")
                    div = temp / 2
                    for i in range(len(terms) - 2):
                        print("hi 4")
                        a += temp ** float(terms[i])
                        b += div ** float(terms[i])
                    print("hi 5")
                    a += constant
                    b += constant
                    if a == float(answer):
                        results.append(a)
                        break
                    elif b == float(answer):
                        results.append(b)
                        break
                    else:
                        if abs(a) < abs(b):
                            temp = a
                        else:
                            temp = b
        
        await ctx.send("The answer(s) to your equation should be: ")
        for i in range(len(results)):
            await ctx.send(str(results[i]))
                
                 
    

def setup(client):
    
    client.add_cog(Math(client))