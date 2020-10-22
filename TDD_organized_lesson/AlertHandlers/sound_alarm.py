import winsound


class SoundAlarm:
    def handle_alert(self, alert):
        if(alert.level >= 3):
            frequency = 200  # Set Frequency To 2500 Hertz
            duration = 200  # Set Duration To 1000 ms == 1 second
            for _ in range(5):
              winsound.Beep(frequency, duration)
              winsound.Beep(frequency*2, duration)