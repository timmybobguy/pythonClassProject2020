from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
import os
import subprocess


class Builder(ABC):

    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_svg(self) -> None:
        pass

    @abstractmethod
    def produce_fig(self) -> None:
        pass

    @abstractmethod
    def produce_dot(self) -> None:
        pass


class ConcreteBuilderPyReverse(Builder):

    def __init__(self, input_file) -> None:
        self._work_dir = os.path.dirname(input_file)
        self._file = input_file[len(self._work_dir) + 1:]
        self._product = ProductPyReverse(self._file, self._work_dir)

    @property
    def product(self) -> ProductPyReverse:
        product = self._product
        return product

    def produce_svg(self) -> None:
        self._product.add("pyreverse {0} -o svg -p diagram".format(self._file))

    def produce_fig(self) -> None:
        self._product.add("pyreverse {0} -o fig -p diagram".format(self._file))

    def produce_dot(self) -> None:
        self._product.add("pyreverse {0} -o dot -p diagram".format(self._file))


class ProductPyReverse:

    def __init__(self, file, work_dir) -> None:
        self.commands = []
        self._file = file
        self._work_dir = work_dir

    def add(self, part: Any) -> None:
        self.commands.append(part)

    def list_commands(self) -> None:
        print(f"Product commands: {', '.join(self.commands)}", end="")

    def run_commands(self):
        for command in self.commands:
            print("input_dir:{0} input_file:{1}"
                  .format(self._work_dir, self._file))
            print("command:" + command)
            subprocess.run(command, cwd=self._work_dir, shell=True)


class Director:

    def __init__(self, file_type_array) -> None:
        self._builder = None
        self._file_type_array = file_type_array

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, build: Builder) -> None:

        self._builder = build

        for fileType in self._file_type_array:

            if fileType == "svg":
                self.build_svg_product()
            elif fileType == "dot":
                self.build_dot_product()
            elif fileType == "fig":
                self.build_fig_product()
            else:
                print(" You only have 3 options which are"
                      " svg, dot and fig in the file types")

    def build_svg_product(self) -> None:
        self.builder.produce_svg()

    def build_dot_product(self) -> None:
        self.builder.produce_dot()

    def build_fig_product(self) -> None:
        self.builder.produce_fig()

    def build_full_product(self) -> None:
        self.builder.produce_svg()
        self.builder.produce_fig()
        self.builder.produce_dot()


if __name__ == "__main__":
    testArray = ["fig", "dot"]
    director = Director(testArray)
    builder = ConcreteBuilderPyReverse("C:/Users/TimDesk/PycharmProjects' \
    '/pythonClassProject2020/Builder.py")
    director.builder = builder

    builder.product.run_commands()

    # print("Standard product: ")
    # director.build_svg_product()
    # builder.product.list_commands()
    #
    # print("\n")
    #
    # director.build_full_product()
    # builder.product.list_commands()
    #
    # print("\n")
    #
    # builder.produce_svg()
    # builder.produce_dot()
    # builder.product.list_commands()
    # builder.product.run_commands()
