import os
import datetime
import player

class SaveSystem():
  def __init__(self):
    self.savepath = "saves/"
    self.gamedir = os.path.abspath(".")

  def save(self, player):
    ### In case directory was deleted or it's the first time a save is done
    if not os.path.lexists("./saves/"):
      os.mkdir("saves")

    savetime = datetime.datetime.now() # Get a datetime instance
    filename = "save-{}-{}-{}.txt".format(savetime.day, savetime.month, savetime.year)
    l = [
      "user_id: {}\n".format(player.id),
      "save_time: {}:{}:{}\n".format(savetime.hour, savetime.minute, savetime.second),
      "user_score: {}\n".format(player.score),
      "---\n"
    ]

    if os.path.lexists("./saves/"+filename):
      finraw = open("./saves/"+filename, "rt", encoding="utf-8").read()
      fin = finraw.strip().split("\n")
      if len(fin) > 1:
        with open("./saves/"+filename, "at", encoding="utf-8") as fout:
          for data in l:
            fout.write(data)
    with open("./saves/"+filename, "wt", encoding="utf-8") as fout: # Fout -> File Out
      for data in l:
        fout.write(data)

  def load(self, player):
    if os.path.lexists("./saves/"):
      directory = os.fsencode("./saves/")

      loadtime = datetime.datetime.now() # Get a datetime instance
      to_load = None

      for file in os.listdir(directory):
          filename = os.fsdecode(file)
          file_name = filename.strip().split("-")
          if file_name[-1].endswith(".txt"):
            if int(file_name[2]) == loadtime.month:
              if int(file_name[1]) == loadtime.day:
                to_load = os.path.join(directory, file)
                break

      dataHold = {}

      with open(to_load, "rt", encoding="utf-8") as fin:
        fin_stripped = fin.read().strip().split("---")
        fin_grouped = [fi.strip().split("\n") for fi in fin_stripped]
        for block in fin_grouped:
          for data in block:
            if not data == "":
              status = data.strip().split(": ")
              if status[0] == "user_id":
                dataHold["id"] = status[1]
              elif status[0] == "user_score":
                dataHold["score"] = int(status[1])
              else:
                dataHold[status[0]] = status[1]

      if dataHold["id"] == player.id:
        player.set_score(dataHold["score"])