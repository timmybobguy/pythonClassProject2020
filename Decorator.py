from pieChart import CreatePieChart
import re


class PieChart:

    def operation(self, name, regex):
        pass

    def generatePieChart(self):
        pass


class ConcretePieChart(PieChart):

    def __init__(self, file, file_data):
        self._file = file
        self._file_data = file_data
        self._labels = []
        self._sizes = []

    def operation(self, name, regex):
        self._labels.append(name)
        matches = re.finditer(regex, self._file_data, re.MULTILINE)
        num = 0
        for _ in matches:
            num += 1
        self._sizes.append(num)

    def generatePieChart(self):
        for label in self._labels:
            print(label)
        for size in self._sizes:
            print(size)
        pie = CreatePieChart(self._labels, self._sizes, self._file)
        pie.generate_pie_chart()


class Decorator(PieChart):

    _component: PieChart = None

    def __init__(self, component: PieChart) -> None:
        self._component = component

    @property
    def component(self) -> PieChart:

        return self._component

    def operation(self, name, regex):
        return self._component.operation(name, regex)

    def generatePieChart(self):
        return self._component.generatePieChart()


class ConcreteDecoratorClasses(Decorator):

    def __init__(self, component: PieChart):
        super().__init__(component)
        self.component.operation("Classes", r"class")


class ConcreteDecoratorFunctions(Decorator):

    def __init__(self, component: PieChart):
        super().__init__(component)
        self.component.operation("Functions", r"def")


class ConcreteDecoratorAttributes(Decorator):

    def __init__(self, component: PieChart):
        super().__init__(component)
        self.component.operation("Attributes", r"self.*=")


def client_code(component: PieChart) -> None:

    component.generatePieChart()


if __name__ == "__main__":

    filePath = "C:/Users/TimDesk/PycharmProjects" \
               "/pythonClassProject2020/ppp_cmd.py"
    fileTest = open(filePath, 'r')
    fileData = fileTest.read().replace('\n', '')

    simple = ConcretePieChart(fileTest, fileData)
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorClasses(simple)
    decorator2 = ConcreteDecoratorFunctions(decorator1)
    # decorator3 = ConcreteDecoratorClasses(decorator2)
    client_code(decorator2)
