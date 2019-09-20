# enter the schedule you need
class Stack:

    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items)-1]

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

class schedule:
    def enterschdule():
        k = 1
        while True:

            s = input('do you want to study today?(y/n):')
            if s.lower() == 'y':
                schedule.setschdule()
                break
            elif s.lower() == 'n':
                print('ok, goodbye')
                break
            else:
                print('wrong input, please enter y/n!')


    def setschdule():
            change = True
            decision = 0
            while decision==0:
                s2 = input('Do you want to change secdule right now?(y/n):')
                if s2.lower() == 'n':
                    change = False
                    decision +=1
                elif s2.lower() == 'y':
                    decision += 1
                else:
                    print('wrong order, please enter y or n!')
                    continue

            if change==True:
                i=0
                works = list()
                f = open('schedule.txt','w')
                for i in range(0,99):
                    w = input('please enter mission'+str(i)+' or enter q to quit: ')
                    works.append(w)

                    if works[i].lower() == 'q':
                        break

                print(*works, sep = "\n")
                # i=0
                f.writelines(["%s\n" % work  for work in works])
                f.close()
                print('schedule has updated')

            else:
                f = open('schedule.txt','r')
                print('Today missions are following below: ')
                content = f.read()
                print(content)



def main():
    i = input('please press enter to start the program')
    schedule.enterschdule()

main()
