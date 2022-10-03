from datetime import datetime


def proclamer():
    print "[%s] Sam et Max, c'est bien" % datetime.now()


if __name__ == "__main__":
    proclamer()