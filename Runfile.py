from FrontEnd import FrontEnd
from BackEnd import BackEnd
from SQLdatabase import SQLdatabase
def main():
    SQ = SQLdatabase()
    SQ.Table()
    SQ.insertBLOB(1, "Temperature", "Temperature.png", "Temperature.html")
    print(SQ[1856])
    FE = FrontEnd()

if __name__ == "__main__":
    main()
