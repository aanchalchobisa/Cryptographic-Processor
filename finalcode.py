global PC
global inpc
global branch
global zero
global mem2reg
global regwr
global memwr
global regdest
global alucontrol
global alusrc
global t
global x
inpc=0
pcn =0
PC=-1
t=0
global b
b="ABCD"

#module for mux
def mux(a,b,control):
    if control==0:
        c= a
    else:
        c= b
    return(c)

#module to add two the pc branch address
def adder(a,b):                 
    c= a+b
    return(c)

#module of the reading the instruction code of hex format
def instr(a):
        
    for i in instrmem:
        if a == i:
            print(a)
            print(i)
            print(instrmem[i])
            #a=bin(int(instrmem[i],16))

            x=int(instrmem[i],16)
            a=bin(x)
            a=a[2:]
            c=a.zfill(16)
    return(c)

#module of the control unit to generate signals according to opcode recieved
def control_unit(op):
                        #control unit 16
    if op==0: #add
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
    
    elif op==1: #sub
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
    elif op==2:  #mul
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
    elif op==3: #xor
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
   
    elif op==4:  #And
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
   
    elif op==5:    #or
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
    
    elif op==6:  #load
        mem2reg=1
        memwr=0
        branch=0
        alusrc=1
        regdest=0
        regwr=0
        alucontrol=op
    
    elif op==7:   #store
        mem2reg=0
        memwr=1
        branch=0
        alusrc=1
        regdest=5
        regwr=0
        alucontrol=op
    elif op==8:   #Branch Zero
        mem2reg= 5
        memwr=0
        branch=1
        alusrc=0
        regdest= 5
        regwr=0
        alucontrol=op
    elif op==9:   #Branch equal
        mem2reg= 5
        memwr=0
        branch=1
        alusrc=0
        regdest= 5
        regwr=0
        alucontrol=op
 
    elif op==10:   #Branch positive
        mem2reg= 5
        memwr=0
        branch=1
        alusrc=0
        regdest= 5
        regwr=0
        alucontrol=op
    
    elif op==11:   #Branch Negative
        mem2reg= 5
        memwr=0
        branch=1
        alusrc=0
        regdest= 5
        regwr=0
        alucontrol=op
   
    elif op==12:     #Jump and Link
        mem2reg= 5
        memwr=0
        branch=1
        alusrc=0
        regdest= 5
        regwr=0
        alucontrol=op
   
    elif op==13:    #Load Immediate
        mem2reg= 0
        memwr=0
        branch=0
        alusrc=1
        regdest=0
        regwr=1
        alucontrol=op
    
    elif op==14:     #modulo addition
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
    elif op==15:      #modulo multiplication
        mem2reg=0
        memwr=0
        branch=0
        alusrc=0
        regdest=1
        regwr=1
        alucontrol=op
                        
    return(mem2reg,memwr,branch,alusrc,regdest,regwr,alucontrol)
	
#alu defined
#module for alu operation to perform the operation and give the alu result
def alu(a,b,control):   
    if control==0:   #add
        c=a+b
        z=0
    elif control==1:        #sub
        c=a-b
        if c<=0:
            c=0
        z=0
    elif control==2:        #mul
        c=a*b
        z=0
    elif control==3:        #Xor
        c= a^b
        z=0
    elif control==4:        #And
        c=a&b
        z=0
    elif control==5:        #Or
        c=a|b
        z=0
    elif control==6:        #Load
       c=a+b
       z=0
    elif control==7:        #store
        c=a+b
        z=0
    elif control==9:        #Branch equal
        if a==b:
            c=0
        else:
            c=1
        if c==0:
            z=1
        else:
            z=0
    elif control==8:        #Branch Zero
        if a==0:
            c=1
        else:
            c=0
        if c==1:
            z=1
        else:
            z=0
    elif control==10:       #Branch Positive
        if a>=1:
            c=1
            z=0
        else:
            c=0
            z=0
    elif control==11:       #Branch Negative
        if a<b:
            c=1
            z=0
        else:
            c=0
            z=0
    elif control==12:       #Jump
            c=a
            z=0
    elif op==13:                #Load Immediate
            c=int(RD[4:12],base=2)
            z=0
    elif control==14:           #Modulo addition
            c=a+b
            c=c%65536
            z=0
    elif control==15:           #Modulo Multiplication
            if a==0:
                a=65536
            if b==0:
                b=65536
            c= (a*b)%65537
            if c==65536:
                c=0
            z=0
    return (c,z)



#register file module

def reg_file(a1,a2):
    a=regfile[a1]
    b=regfile[a2]
    return(a,b)


#module for shifter used in the PC calculation
def shifter(a):
    c= a* 2
    return(c)
i=0

#Instruction to decrypt the instruction hex code file
instrm= open("code.txt", "r")
instrmem = dict(enumerate(line.strip() for line in instrm))
InstCount=len(instrmem)


#Instruction to decrypt  the data hex code file
datamem = open("data.txt", "r")
print(datamem)
data = dict(enumerate(line.strip() for line in datamem))
print("data",data)


#the  16 bitregister file to store the variables
from array import array
regfile=array('i',[0]*16)


#output array
from array import array
output=array('i',[0]*65)


zero=0
branch=0


# Defining the main module or Implementing The IDEA Code
while (i<InstCount):
    """PCplus4=adder(PC,1)
    PCbranch= adder(inpc,PCplus4)
    PCsrc= branch & zero
    pcn= mux(PCplus4,PCbranch,PCsrc)"""
    PC=i

    RD= instr(PC)
    #print("value of instruction file\n", RD)
   #control unit function defined
    rd=RD[0:4]

    op = int(rd,base=2)
    print("opcode is %s\n" %op)

    if op>=0:
        t=t+1
    print("clock cycles: %d"%t)

    (mem2reg,memwr,branch,alusrc,regdest,regwr,alucontrol) = control_unit(op)   #control unit output

    a1= int(RD[4:8],2)  #rs
    a2= int(RD[8:12],2)      #rt
    a3= int(RD[12:],2)      #rd
    #print("rs, rt,rd",a1,a2,a3)

#register file
    (RD1,RD2)= reg_file(a1,a2)
   # print("output of register module, RD1 and RD2",RD1,RD2)
   
    if op==13:       #for load Immediate instruction
        Imm=int(RD[4:12],base=2)
    else:
        Imm=int(RD[8:12],base=2)

    srcB= mux(RD2,Imm,alusrc)
    #print(srcB)
    inpc= shifter(RD)
    srcA=RD1

    (aluresult,zero)= alu(srcA,srcB,alucontrol)

    A= aluresult
    print("Aluresult:%d" %A)

    if op==6:  #for load instruction
        if(type(b)==type(aluresult)):
            A=int(aluresult,16)
        else:
            A=aluresult
            regfile[a3]=int(data[A],16)
    else:
        if(regwr==1):
            print ("A:",A)
            regfile[a3]=A
        else:
            print("A",A)
    print("regfile",regfile)
    wd=int(RD2)
    A=aluresult
    print(memwr)
    if memwr==1:
        #A=i
        data[A]=hex(regfile[a3])[2:]
       
        print("datai",data[A])
        output[A]= int(data[A],base=16)
        print("output",output[A])
        print("A",A)
        print("data", data)

    if op==10:
        if aluresult==1:
            i=a3
        else:
            i=PC+1
    else:
            i=PC+1
    #print("pc",PC)
    #PC module

print("regfile",regfile)
print("output",data)
