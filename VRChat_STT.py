if __name__ == '__main__':

    import os
    import sys
    import pyautogui
    import random
    import time
    import asyncio
    from PySide6.QtWidgets import QApplication
    if os.name == "nt" and (3, 8) <= sys.version_info < (3, 99):
        from torchaudio._extension.utils import _init_dll_path
        _init_dll_path()

    from RealtimeSTT import AudioToTextRecorder
    from pythonosc import udp_client
    from googletrans import Translator
    from uicall import Widget
    os.environ["QT_LOGGING_RULES"] = "qt.qpa.window=false"
    # Initialize the Qt application and open the UI window
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec()  # Wait for the UI window to close

    # Retrieve IP and port from the UI
    ip = widget.ip
    port = int(widget.port)

    client = udp_client.SimpleUDPClient(ip, port)

    print("System initializing, please wait")

    recorder = AudioToTextRecorder(
        spinner=False,
        silero_sensitivity=0.02,
        model="tiny.en",
        language="en",
        compute_type="float32"
        )

    print("Say something...")
    
    async def translate_text(text):
        async with Translator() as translator:
            return await translator.translate(text, dest='ar')

    try:
        while (True):
            text = recorder.text()
            print("Sending: " + f"{text} ")
            client.send_message("/chatbox/input", [text, True, True])
            #result = asyncio.run(translate_text(text))
            #print("Sending (translated): " + f"{result.text} ")
            #client.send_message("/chatbox/input", [result.text, True, True])

    except KeyboardInterrupt:
        print("Exiting application due to keyboard interrupt")