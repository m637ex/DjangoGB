from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Print 'Hello world!' to output." # -h --help - отобразится справка из консоли
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!') # self - указатель самого на себя
                                          # stdout - стандартный вывод
                                          # write - функция для записи в консоль
