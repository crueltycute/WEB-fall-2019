from django.db import models


class Computer(models.Model):
    country = models.CharField(max_length=32)
    IP_address = models.CharField(max_length=15)

    def __str__(self):
        return self.IP_address + ' (' + self.country + ')'


def get_computers():
    return Computer.objects.all()


class Browser(models.Model):
    name = models.CharField(max_length=32)
    engine = models.CharField(max_length=32)
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE)

    def __str__(self):
        return self.computer.IP_address + ' (' + self.computer.country + ')' \
               + ', ' + self.name + ' (' + self.engine + ')'


def get_browsers_by_computer(computer):
    browsers_of_computer = Browser.objects.filter(computer=computer)

    return browsers_of_computer
