import matplotlib.pyplot as plt


class CreatePieChart:

    def __init__(self, label, size, file):
        self.__labels = label
        self.__sizes = size
        self.__file = file

    def generate_pie_chart(self):
        fig1, ax1 = plt.subplots()
        ax1.pie(self.__sizes,  labels=self.__labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title(self.__file.name)
        plt.show()
