class HelloWorld:
    """
    Я не понимаю, зачем вы зашли сюда.
    Если вам действительно интересно посмотреть какие-либо мои проекты, то я Вас очень сильно обломал.
    Смотрите на этот "шедевральный" код. (ну типа я навичок, тока изучаю, тока хело ворлд выучил))))))
    Кто слишком расстроился, желаю всего наилучшего.
    """
    def __init__(self, helloworld):
        self.helloworld = helloworld
    
    def hello_world():
        return 'Hello world!'

if __name__ == "__main__":
    helloWorld = HelloWorld('Hello world!')
    print(helloWorld.hello_world)
    print(helloWorld.helloworld)