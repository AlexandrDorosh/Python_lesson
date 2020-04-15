from subprocess import call
import os 
if __name__ == "__main__":
    downloader

class downloader():
    def menu(self):
        choice = int(
            input("1. Youtube single movie\n2. Youtube playlist\n0. Exit\n =====>>> "))
        return choice

    def download_youtybe_single_movie(self):
        movie_url = input("Enter movie URL => ")
        movie_info = "youtube-dl " + movie_url + " -F"
        # call("calc.exe", shell=False) калькулятор
        # call("mspaint.exe", shell=False) paint
        call(movie_info, shell=False)
        format = input("Enter format code : ")
        os.chdir("Downloads")
        download_command = "youtube-dl -f " + format + " " + movie_url + " -c"
        call(download_command, shell=False)
