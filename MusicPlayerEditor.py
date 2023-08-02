import os
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_song = None
        self.is_playing = False

    def add_song_to_playlist(self, song_path):
        if os.path.exists(song_path):
            self.playlist.append(song_path)
            print(f"Added {os.path.basename(song_path)} to the playlist.")
        else:
            print("Song not found. Please provide a valid path.")

    def play(self):
        if not self.is_playing and self.playlist:
            self.current_song = pygame.mixer.Sound(self.playlist[0])
            self.current_song.play()
            self.is_playing = True
            print("Now playing:", os.path.basename(self.playlist[0]))

    def pause(self):
        if self.is_playing:
            pygame.mixer.pause()
            self.is_playing = False
            print("Paused.")

    def stop(self):
        if self.is_playing:
            pygame.mixer.stop()
            self.is_playing = False
            print("Stopped.")

    def show_playlist(self):
        if self.playlist:
            print("Current Playlist:")
            for idx, song in enumerate(self.playlist, start=1):
                print(f"{idx}. {os.path.basename(song)}")
        else:
            print("Playlist is empty.")

    def quit(self):
        pygame.mixer.quit()
        pygame.quit()
        print("Music player editor has been closed.")

if __name__ == "__main__":
    player = MusicPlayer()

    while True:
        print("\nMusic Player Editor Menu:")
        print("1. Add Song to Playlist")
        print("2. Play")
        print("3. Pause")
        print("4. Stop")
        print("5. Show Playlist")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            song_path = input("Enter the path of the song: ")
            player.add_song_to_playlist(song_path)
        elif choice == "2":
            player.play()
        elif choice == "3":
            player.pause()
        elif choice == "4":
            player.stop()
        elif choice == "5":
            player.show_playlist()
        elif choice == "6":
            player.quit()
            break
        else:
            print("Invalid choice. Please try again.")
