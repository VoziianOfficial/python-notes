from abc import ABC, abstractmethod


class MusicPlayer(ABC):

    @abstractmethod
    def play_song(self, song):
        pass


class SpotifyPlayer(MusicPlayer):
    def play_song(self, song):
        print(f"Playing {song} on Spotify")


class RadioPlayer(MusicPlayer):
    def play_song(self, song):
        print(f"Playing {song} on Radio")


class LocalPlayer(MusicPlayer):
    def play_song(self, song):
        print(f"Playing {song} from local files")


players = [SpotifyPlayer(), RadioPlayer(), LocalPlayer()]

for player in players:
    player.play_song("Hello")


spotify = SpotifyPlayer()
radio = RadioPlayer()
local = LocalPlayer()


# О - OCP этот метод нарушается если нам приходится лезть в music сервис и добавлять очередной if и elif, соответственно elif, и не один,
# но если сделать наследование класса MusicPlayer, то этот метод будет работать.

# L - LSP этот метод нарушается если дочерний класс имеет тот же метот как и родительский но не может его реализовать правильно!


class MusicDevice(ABC):

    @abstractmethod
    def play_song(self, song):
        pass

    @abstractmethod
    def record_song(self, song):
        pass

    @abstractmethod
    def connect_bluetooth(self):
        pass


class SpotifyPlayer(MusicDevice):

    def play_song(self, song):
        print(f"Playing {song} on Spotify")

    def record_song(self, song):
        print("Spotify can't record songs")

    def connect_bluetooth(self):
        print("Connected to Bluetooth")


class VoiceRecorder(MusicDevice):

    def play_song(self, song):
        print("Recorder doesn't play songs")

    def record_song(self, song):
        print(f"Recording {song}")

    def connect_bluetooth(self):
        print("Recorder has no Bluetooth")


# I - ISP метод нарушаетс если дочерние классы реализовуют методы которые есть уродителя хотя они дочернему классу не нужны!
# В таком случает что бы не нарушать этот метод лучше разбить общий большой интерфейс то есть род класс на несколько маленьких!

from abc import ABC, abstractmethod


class Playable(ABC):

    @abstractmethod
    def play_song(self, song):
        pass


class Recordable(ABC):

    @abstractmethod
    def record_song(self, song):
        pass


class BluetoothConnectable(ABC):

    @abstractmethod
    def connect_bluetooth(self):
        pass


class SpotifyPlayer(Playable, BluetoothConnectable):

    def play_song(self, song):
        print(f"Playing {song} on Spotify")

    def connect_bluetooth(self):
        print("Connected to Bluetooth")


class VoiceRecorder(Recordable):

    def record_song(self, song):
        print(f"Recording {song}")


# ===========================================
class SpotifyPlayer:
    def play_song(self, song):
        print(f"Playing {song} on Spotify")


class MusicService:
    def __init__(self):
        self.player = SpotifyPlayer()

    def start(self, song):
        self.player.play_song(song)


# D — DIP нарушается, когда один общий класс слишком жёстко привязан к конкретному другому классу. Тогда добавить или заменить другую реализацию становится сложно.

# Чтобы это исправить, мы создаём общий абстрактный класс, например MusicPlayer, в котором есть обязательный метод play_song().

# Потом создаём дочерние классы SpotifyPlayer, RadioPlayer, YouTubePlayer, LocalPlayer, и каждый по-своему реализует play_song().

# А MusicService уже не создаёт внутри себя конкретно SpotifyPlayer. Он просто получает player снаружи:


class MusicPlayer(ABC):
    @abstractmethod
    def play_song(self, song):
        pass


class SpotifyPlayer:
    def play_song(self, song):
        print(f"Playing {song} on Spotify")


class MusicService:
    def __init__(self, player):
        self.player = player

    def start(self, song):
        self.player.play_song(song)
