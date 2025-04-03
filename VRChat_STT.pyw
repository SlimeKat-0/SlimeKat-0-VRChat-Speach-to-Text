import subprocess
from multiprocessing import Process, Pipe

def main():

    import os
    import sys
    import time
    import concurrent.futures
    from PySide6.QtWidgets import QApplication
    if os.name == "nt" and (3, 8) <= sys.version_info < (3, 99):
        from torchaudio._extension.utils import _init_dll_path
        _init_dll_path()

    from RealtimeSTT import AudioToTextRecorder
    from pythonosc import udp_client
    from ui_call import Widget
    from threading import Thread, Event
    from console import start_con  # Import the console function
    os.environ["QT_LOGGING_RULES"] = "qt.qpa.window=false"

    # Initialize the Qt application and open the UI window
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec()  # Wait for the UI window to close

    if hasattr(widget, 'ip') and hasattr(widget, 'port'):
        # Retrieve IP and port from the UI
        ip = widget.ip
        port = int(widget.port)
    else:
        sys.exit()

    print("System initializing, please wait")
    text2 = "System initializing, please wait"


    # Create a Pipe for communication
    parent_conn, child_conn = Pipe()

    # Start the console process
    console_process = Process(target=start_con, args=(child_conn,))
    console_process.start()

    stop_flag = Event()

    def check_for_termination():
        while not stop_flag.is_set():
            if parent_conn.poll(0.1):  # Check if there is data in the pipe
                message = parent_conn.recv()  # Receive the message from the pipe
                if message == "TERMINATE":
                    print("Termination signal received. Exiting application.")
                    stop_flag.set()
                    break


    def exit():
        if stop_flag.is_set():
            # Exit
            print("Exiting")
            parent_conn.close()  # Close the parent end of the pipe
            child_conn.close()  # Close the child end of the pipe
            if console_process.is_alive():
                console_process.terminate()
                console_process.join()
            if listener_thread.is_alive():
                print("Listener thread is still alive. Forcing exit.")
                listener_thread.join(timeout=1)  # Wait for the listener thread to finish
            print("Application exited cleanly.")
            executor.submit(os._exit(0))
            os._exit(0)

    # Start listening for updates in a separate thread
    listener_thread = Thread(target=check_for_termination, daemon=True)
    listener_thread.start()

    client = udp_client.SimpleUDPClient(ip, port)

    recorder = AudioToTextRecorder(
        spinner=False,
        silero_sensitivity=0.02,
        model="tiny.en",
        language="en",
        compute_type="float32"
        )

    print("Say something...")
    text2 = "Say somthing..."
    parent_conn.send(text2)

    
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            while not stop_flag.is_set():
                future = executor.submit(recorder.text)
                try:
                    # Wait for the result with a timeout of 5 seconds
                    text = future.result(timeout=5)
                    print("Sending: " + f"{text} ")
                    client.send_message("/chatbox/input", [text, True, True])
                    # Send the text to the console process
                    text2 = "Sent: " + text
                    parent_conn.send(text2)
                except concurrent.futures.TimeoutError:
                    print("Timeout")
                    time.sleep(0.5)
                    exit()

    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Stopping...")
        stop_flag.set()

    finally:
        exit()

            
if __name__ == '__main__':
    main()
