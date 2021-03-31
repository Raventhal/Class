import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
root = tk.Tk()
root.withdraw()

 

def write_slogan():
    #print("Tkinter is easy to use!")
    output=3

def One():
    l= "Cloud Computing 101: The cloud is a part of everyday life. For companies everywhere, it’s become an ideal solution for their technology needs. With its ability to scale, on-demand solutions, and flexible pricing, companies can focus on bringing their ideas to life rather than buying and managing servers.What does this mean for your career? If you’re interested in a job in technology, knowledge of cloud computing is essential. Start with Cloud Computing 101 to build a foundation and grow your expertise."
    def printout():
        messagebox.showinfo("AWS Career Path: Cloud Computing 101", l)
    printout()
    
def Two():
    l= "Application Developers are behind the apps that people use every day, from travel to shopping to connecting with the world. They work on all aspects of app development, from identifying requirements to building prototypes to continuously making improvements. If you like collaborating with multiple teams and owning the development work to bring web and mobile apps to life, check out the Application Developer Pathway today."
    def printout():
        messagebox.showinfo("AWS Career Path: Application Developer", l)
    printout()
def Three():
    l= "Cloud Support Associates use their expertise in cloud computing and AWS solutions to answer customer questions and solve technology challenges every day.If you’re curious, excited by the future of cloud computing, and enjoy working directly with customers, get started with the Cloud Support Associate Pathway today."
    def printout():
        messagebox.showinfo("AWS Career Path: Cloud Support Associate", l)
    printout()
def Four():
    l= "Cloud Support Engineers work with companies every day to help them move their technology to the cloud and solve different types of technical challenges. They’re also the voice of the customer and provide feedback on customer needs when working with engineering teams to develop new features. Start this pathway today if you like the idea of developing your cloud computing expertise to help customers find solutions to complex issues."
    def printout():
        messagebox.showinfo("AWS Career Path: Cloud Support Engineer", l)
    printout()
def Five():
    l= "As the world becomes more connected, security will continue to be a foundational element of technology. Cybersecurity Specialists use their expertise to identify security risks and protect computer systems, networks, applications, and data. Dive into the Cybersecurity Specialist Pathway if you’re interested in the skills needed to keep technology and data safe today and in the future."
    def printout():
        messagebox.showinfo("AWS Career Path: Cybersecurity Specialist", l)
    printout()
def Six():
    l= "Data Integration Specialists develop creative solutions to combine data from multiple locations into one place. This enables businesses look at the big picture to understand how to improve and develop new products. If you’re excited by the idea of helping companies grow through data integration and automation, start building your skills with the Data Integration Specialist Pathway."
    def printout():
        messagebox.showinfo("AWS Career Path: Data Integration Specialist", l)
    printout()
def Seven():
    l= "Data Scientists analyze large amounts of data to identify opportunities, inform business strategies, and solve customer challenges. They work with experts to develop and automate processes, metrics, and long-term, scalable solutions. If you have strong quantitative and analytical skills and enjoy diving into data to uncover patterns and solutions, explore the Data Scientist Pathway to grow your expertise."
    def printout():
        messagebox.showinfo("AWS Career Path: Data Scientist", l)
    printout()
def Eight():
    l= "DevOps Engineers are the first line of defense to tackle software application issues that could disrupt the customer experience. They work behind the scenes with different teams to identify, implement, and monitor software applications, as well as identify ways to automate manual processes. If you’re a problem solver who enjoys working with multiple technologies, explore the DevOps Engineer Pathway today to learn more."
    def printout():
        messagebox.showinfo("AWS Career Path: DevOps Engineers", l)
    printout()
def Nine():
    l= "Machine Learning Scientists create the products of the future. They collaborate with subject matter experts, design algorithms, and develop predictive data models that result in new features and enhancements that delight customers.If you have a passion for diving deep into data and software development and want to shape the customer experiences of tomorrow, get started with the Machine Learning Scientist Pathway today."
    def printout():
        messagebox.showinfo("AWS Career Path: Machine Learning Scientist", l)
    printout()
def Ten():
    l= "Software Development Engineers are versatile. They can build groundbreaking customer features or develop the backend infrastructures that support them. They are creative and passionate about using software engineering principles to solve challenges across a wide array of technologies.If you enjoy coding and software applications and want to work in a fast-paced, collaborative environment, get started with the Software Development Engineer Pathway today."
    def printout():
        messagebox.showinfo("AWS Career Path: Software Development Engineer", l)
    printout()
def Eleven():
    l= "Solutions Architects use their knowledge of the latest cloud computing technologies to work with customers to build innovative AWS cloud infrastructures and solve technical challenges.Get started today to learn about the unique mix of technical, leadership, and communication skills Solutions Architects use to develop customer strategies and solutions."
    def printout():
        messagebox.showinfo("AWS Career Path: Solutions Architect", l)
    printout()
def Twelve():
    l= "Web Development Engineers design, build, and improve websites and features that stand out for their innovation and accessibility. They work with different teams to understand customer needs to ensure they’re creating the right experience. If you’re interested in learning more about the skills you need to develop the next cutting-edge web experience, dive into the Web Development Engineer Pathway today."
    def printout():
        messagebox.showinfo("AWS Career Path: Web Development Engineer", l)
    printout()



root = tk.Tk()
root.title("AWS Educate: Career Paths")
frame = tk.Frame(root)
frame.configure(bg='black')

frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red", 
                   command=quit)
button.grid(row=0,column=1)
button2 = tk.Button(frame,
                   text="Cloud Computing 101", width=30, 
                   command=One)
button2.grid(row=1,column=1)
button3 = tk.Button(frame, 
                   text="    Application Developer    ", width=30,
                   command=Two)
button3.grid(row=1,column=2)
button4 = tk.Button(frame,
                   text="   Cloud Support Associate   ", width=30,
                   command=Three)
button4.grid(row=1,column=3)
button5 = tk.Button(frame,
                   text="   Cloud Support Engineer    ", width=30,
                   command=Four)
button5.grid(row=2,column=1)
button6 = tk.Button(frame,
                   text="  Cybersecurity Specialist   ", width=30,
                   command=Five)
button6.grid(row=2,column=2)
button6 = tk.Button(frame,
                   text=" Data Integration Specialist ", width=30,
                   command=Six)
button6.grid(row=2,column=3)
button7 = tk.Button(frame,
                   text="       Data Scientist        ", width=30,
                   command=Seven)
button7.grid(row=3,column=1)
button8 = tk.Button(frame,
                   text="       DevOps Engineer       ", width=30,
                   command=Eight)
button8.grid(row=3,column=2)
button9 = tk.Button(frame,
                   text=" Machine Learning Scientist  ", width=30,
                   command=Nine)
button9.grid(row=3,column=3)
button10 = tk.Button(frame,
                   text="Software Development Engineer", width=30,
                   command=Ten)
button10.grid(row=4,column=1)
button11 = tk.Button(frame,
                   text="     Solution Architect      ", width=30,
                   command=Eleven)
button11.grid(row=4,column=2)
button12 = tk.Button(frame,
                   text="   Web Development Engineer  ", width=30,
                   command=Twelve)
button12.grid(row=4,column=3)

root.mainloop()
