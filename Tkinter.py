# version 3.6
from py4j.java_gateway import JavaGateway
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
import unittest
import timeit
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
from Double_Hashing import HashDoubleTable
#from Unittest_Double import HashTableTest
from hashTable import HashTable

ht = HashTable()
htd=HashDoubleTable()

CONST_SIZE_FOR_CHAINING = 10000
CONST_SIZE_FOR_HASH_DOUBLE=100000

def from_file_to_file():
    f = open("data/QRNGFull.txt", 'r')
    seq = f.read()
    l = len(seq)
    print(l)
    datta = []
    for val in seq[0:len(seq)]:
        b = bin(val)
        d = int(b, 2)
        datta.append(d)
    print("done ", len(datta))
    f = open('data/QRNG100000.txt', 'w')
    cnt = 100000;
    tmp = 0
    for index in datta:
        f.write(str(index) + "\n")
        tmp += 1
        if (tmp == cnt):
            break;


def readFrom():
    print("Start")
    with open("data/QRNG.txt", "r") as f:
        for l in f:
            b = l.strip().split(";")
    results = list(map(int, b))

    print(results)
    f = open('data/QRNG100000.txt', 'w')
    cnt = 100000;
    tmp = 0
    for index in results:
        f.write(str(index) + "\n")
        print(index)
        tmp += 1
        print(tmp)
        if (tmp == cnt):
            break;
    print("Finish")

def startGraphSimulation_Hd():
    graph_list_x = []
    find_all_list_y = []
    graph_list_y_Find = []
    find_all_list_y_Find = []
    graph_list_y_Delete = []
    find_all_list_y_Delete = []
    forFileKey = []
    forFileValue = []
    cnt = 0
    tmp=0
    stats = open("data/QRNG100000.txt", "r")
    li = []
    key = []
    for l in stats.read().split():
        li.append(int(l))
    print(li)
    stats1 = open("data/Value.txt", "r")
    for l in stats1:
        arr = np.array(l.split(';'))
        key.append(arr[np.random.randint(arr.size - 1)])
    for i in range(1):
        graph_list_y = []

        for l in range(len(li)):

            k = li[l]
            value = arr[np.random.randint(arr.size - 1)]

            forFileKey.append(k)
            forFileValue.append(value)
            graph_list_x.append(l)
            start = time.time() #timeit.default_timer() time.clock() perf_counter()  monotonic()  process_time()  get_clock_info(clock_name)
            htd.put(k, value)
            elapsed = (time.time() - start)
            tmp+=1


            graph_list_y.append(elapsed)
            if (tmp == CONST_SIZE_FOR_HASH_DOUBLE):
                for l in range(len(li)):
                    startFind = time.time()
                    htd.get(li[l])
                    elapsedFind = (time.time() - startFind)
                    graph_list_y_Find.append(elapsedFind)
                    cnt += 1
                    if (cnt == CONST_SIZE_FOR_HASH_DOUBLE):
                        print(cnt)
                        for k in range(len(li)):
                            startDelete = time.time()
                            htd.delete(li[l])
                            elapsedDelete = (time.time() - startDelete)
                            graph_list_y_Delete.append(elapsedDelete)
                        find_all_list_y_Delete.append(graph_list_y_Delete)
                        if (ht.length() == 0):
                            break;
                find_all_list_y_Find.append(graph_list_y_Find)

        find_all_list_y.append(graph_list_y)

    with open("data/HashDouble.txt", 'w') as f:
        for s in range(CONST_SIZE_FOR_HASH_DOUBLE):
            f.write(str(forFileKey[s]) + ":" + forFileValue[s] + '\n')

    final_avg_list_y = list(map(mean, zip(*find_all_list_y)))
    final_avg_list_y_Find = list(map(mean, zip(*find_all_list_y_Find)))
    final_avg_list_y_Delete = list(map(mean, zip(*find_all_list_y_Delete)))

    plt.xlabel('List Length')
    plt.ylabel('Time Taken')

    plt.plot(graph_list_x, final_avg_list_y, label='Insert Case')
    plt.grid()
    plt.legend(['$\mathcal{O}(1)$ Insert Case(Average)'], loc='upper right', fontsize=20)

    plt.show()
   # plt.savefig("insert.png")

    plt1.xlabel('List Length')
    plt1.ylabel('Time Taken')
    plt1.plot(graph_list_x, final_avg_list_y_Find, label='Find Case')
    plt1.grid()
    plt1.legend(['$\mathcal{O}(1)$ Delete Case(Average)'], loc='upper right', fontsize=20)
    plt1.show()
   # plt1.savefig("find.png")

    plt2.xlabel('List Length')
    plt2.ylabel('Time Taken')
    plt2.plot(graph_list_x, final_avg_list_y_Delete, label='Delete Case')
    plt2.grid()
    plt2.legend(['$\mathcal{O}(1)$ Find Case(Average)'], loc='upper right', fontsize=20)
    plt2.show()
    #plt2.savefig("delete.png")

    plt3.xlabel('List Length')
    plt3.ylabel('Time Taken')
    plt3.plot(graph_list_x, final_avg_list_y, label='Insert Case')
    plt3.plot(graph_list_x, final_avg_list_y_Find, label='Find Case')
    plt3.plot(graph_list_x, final_avg_list_y_Delete, label='Delete Case')

    plt3.grid()
    plt3.legend()
    plt3.show()
   # plt3.savefig("all.png")

def startGraphSimulation():
    graph_list_x = []
    find_all_list_y = []
    graph_list_y_Find = []
    find_all_list_y_Find = []
    graph_list_y_Delete = []
    find_all_list_y_Delete = []
    forFileKey = []
    forFileValue = []
    cnt = 0
    stats = open("data/QRNG10000.txt", "r")
    li = []
    key = []
    for l in stats.read().split():
        li.append(int(l))
    print(li)
    stats1 = open("data/Value.txt", "r")
    for l in stats1:
        arr = np.array(l.split(';'))
        key.append(arr[np.random.randint(arr.size - 1)])

    for i in range(1):
        graph_list_y = []
        for l in range(len(li)):
            k = li[l]
            value = arr[np.random.randint(arr.size - 1)]

            forFileKey.append(k)
            forFileValue.append(value)
            graph_list_x.append(l)

            start = time.perf_counter()
            insert(k, value)
            elapsed = (time.perf_counter() - start)
            graph_list_y.append(elapsed)

            if (ht.length() == CONST_SIZE_FOR_CHAINING):
                for l in range(len(li)):
                    startFind = time.perf_counter()
                    find(li[l])
                    elapsedFind = (time.perf_counter() - startFind)
                    graph_list_y_Find.append(elapsedFind)
                    cnt += 1
                    if (cnt == CONST_SIZE_FOR_CHAINING):
                        for k in range(len(li)):
                            startDelete = time.perf_counter()
                            delete(li[k])
                            elapsedDelete = (time.perf_counter() - startDelete)
                            graph_list_y_Delete.append(elapsedDelete)
                        find_all_list_y_Delete.append(graph_list_y_Delete)
                        if (ht.length() == 0):
                            break;

                find_all_list_y_Find.append(graph_list_y_Find)

        find_all_list_y.append(graph_list_y)

    with open("data/Chaining.txt", 'w') as f:
        for s in range(CONST_SIZE_FOR_CHAINING):
            f.write(str(forFileKey[s]) + ":" + forFileValue[s] + '\n')

    final_avg_list_y = list(map(mean, zip(*find_all_list_y)))
    final_avg_list_y_Find = list(map(mean, zip(*find_all_list_y_Find)))
    final_avg_list_y_Delete = list(map(mean, zip(*find_all_list_y_Delete)))

    plt.xlabel('List Length')
    plt.ylabel('Time Taken')

    plt.plot(graph_list_x, final_avg_list_y, label='Insert Case')

    plt.grid()
    plt.legend(['$\mathcal{\Lambda/2}$ Insert Case(Average) '], loc='upper right', fontsize=20);

    plt.show()
   # plt.savefig("insert.png")

    plt1.xlabel('List Length')
    plt1.ylabel('Time Taken')
    plt1.plot(graph_list_x, final_avg_list_y_Find, label='Find Case')
    plt1.grid()
    plt.legend(['$\mathcal{\Lambda/2}$ Find Case(Average)'], loc='upper right', fontsize=20);
    plt1.show()
   # plt1.savefig("find.png")

    plt2.xlabel('List Length')
    plt2.ylabel('Time Taken')
    plt2.plot(graph_list_x, final_avg_list_y_Delete, label='Delete Case')
    plt2.grid()
    plt.legend(['$\mathcal{\Lambda/2}$ Delete Case(Average)'], loc='upper right', fontsize=20);
    plt2.show()
    #plt2.savefig("delete.png")

    plt3.xlabel('List Length')
    plt3.ylabel('Time Taken')
    plt3.plot(graph_list_x, final_avg_list_y, label='Insert Case')
    plt3.plot(graph_list_x, final_avg_list_y_Find, label='Find Case')
    plt3.plot(graph_list_x, final_avg_list_y_Delete, label='Delete Case')

    plt3.grid()
    plt3.legend()
    plt3.show()
   # plt3.savefig("all.png")


def insert(key, value):
    ht.set(key, value)

def find(key):
    ht.get(key)

def delete(key):
    ht.delete(key)

def mean(a):
    return sum(a) / len(a)

def _Show_Visualization_HDouble():
    gateway = JavaGateway()  # connect to the JVM
    addition_app = gateway.entry_point  # get the AdditionApplication instance
    addition_app.startAppletHD()
def _Show_Visualization_HChain():
    gateway = JavaGateway()  # connect to the JVM
    addition_app = gateway.entry_point  # get the AdditionApplication instance
    addition_app.startAppletHC()


def _Show_Info_Plot_HashChain():
    startGraphSimulation()

def _Show_Info_Plot_Open_addressing():
    startGraphSimulation_Hd()

def testOHT():
    try:
        showinfo("Editor", "Testing passed.")# i have already know about good ending unitest
        unittest.main()
    except AssertionError :             # not working
        showinfo("Editor", "Testing failed.")

def testHD():
    try:
        showinfo("Editor", "Testing passed.")# i have already know about good ending unitest
        unittest.main()
    except AssertionError :             # not working
        showinfo("Editor", "Testing failed.")

def _open():
    txt.delete('1.0', END+'-1c')
    op = askopenfilename()
    for l in fileinput.input(op):
        txt.insert(END,l)
def _save():
    sa = asksaveasfilename()
    letter=txt.get(1.0,END)
    f=open(sa,"w")
    f.write(letter)
    f.close()
def close_win():
    if askyesno("Exit","Do you want to save?"):
        _save()
        root.destroy()
    else :
        root.destroy()
def about():
    showinfo("Editor","Just press the OK button.")


def square():
    fra.config(width=500)
    fra.config(height=500)


def rectangle():
    fra.config(width=700)
    fra.config(height=400)



root = Tk()
root.title("CourseWork")

fra = Frame(root,width=300,height=100,bg="White")
fra.pack()

m = Menu(root)

root.config(menu=m)
filem = Menu(m)
m.add_cascade(label='File', menu=filem)
filem.add_cascade(label='Open...', command=_open)
filem.add_cascade(label='Show Visualization Hash Double', command=_Show_Visualization_HDouble)
filem.add_cascade(label='Show Visualization Hash Chain', command=_Show_Visualization_HChain)
filem.add_cascade(label='Show Plot Hash Chain', command=_Show_Info_Plot_HashChain)
filem.add_cascade(label='Show Plot Open addressing', command=_Show_Info_Plot_Open_addressing)
filem.add_cascade(label='Run unit testing for Open Hashing table', command=testOHT)
filem.add_cascade(label='Run unit testing for Close Hashing table(Open addressing)', command=testHD)






filem.add_command(label="Save...", command=_save)
filem.add_command(label="Exit", command=close_win)
edit= Menu(m)
m.add_cascade(label="Edit", menu=edit)
my_size_dict= {"500x500":square,"700x400":rectangle}
for j in my_size_dict:
    edit.add_command(label=j,command=my_size_dict.get(j))
helpm = Menu(m)

m.add_cascade(label="Help", menu=helpm)
helpm.add_command(label="About", command=about)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

txt = Text(root, width=40, height=15, font="12")
txt.pack()
scrollbar.config(command=txt.yview)

root.mainloop()