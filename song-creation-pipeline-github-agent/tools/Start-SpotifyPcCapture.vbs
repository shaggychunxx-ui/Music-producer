Set sh = CreateObject("WScript.Shell")
sh.CurrentDirectory = "C:\\Users\\shagg\\Documents\\GitHub\\Music-producer\\song-creation-pipeline-github-agent"
sh.Run """C:\\Users\\shagg\\AppData\\Local\\Programs\\Python\\Python312\\pythonw.exe"" ""C:\\Users\\shagg\\Documents\\GitHub\\Music-producer\\song-creation-pipeline-github-agent\\tools\\spotify_pc_capture.py"" loop", 0, False
