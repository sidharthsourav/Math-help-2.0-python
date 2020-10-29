import cmath

def Quadratic_eqation(a,b,c):

    a=int(a)
    b=int(b)
    c=int(c)
    equation='Equation: {0}x^2 + {1}x + {2} = 0'.format(a,b,c)
    Discriminant=pow(b,2)-(4*a*c)
    if Discriminant==0:
        statement="Roots are real and equal."
        root=-b/(2*a)
        return(equation,root,root,statement)
    elif Discriminant>0:
        statement="Roots are real and unequal."
        root1=(-b+cmath.sqrt(Discriminant))/(2*a)
        root2=(-b-cmath.sqrt(Discriminant))/(2*a)
        return(equation,root1,root2,statement)

    elif Discriminant<0:
        statement="Roots are Complex."
        root1=(-b+cmath.sqrt(Discriminant))/(2*a)
        root2=(-b-cmath.sqrt(Discriminant))/(2*a)
        root1=format(root1,".2f")
        root2=format(root2,".2f")
        return(equation,root1,root2,statement)