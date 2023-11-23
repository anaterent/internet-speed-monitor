import speedtest
import datetime
import csv
import time

def run_speedtest(duration, interval, csv_filename):
    s = speedtest.Speedtest(secure=True)
    start_time = time.time()
    threshold = 7.0 

    with open(csv_filename, mode="w", newline='') as speedcsv:
        csv_writer = csv.DictWriter(speedcsv, fieldnames=["time", "downspeed", "upspeed"])
        csv_writer.writeheader()
        while time.time() - start_time < duration:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            downspeed = round((round(s.download()) / 1048576), 2)
            upspeed = round((round(s.upload()) / 1048576), 2)
            csv_writer.writerow(
                {"time": time_now, "downspeed": downspeed, "upspeed": upspeed}
            )
            if downspeed < threshold or upspeed < threshold:
                print(f"Warning: Low internet speed detected at {time_now}!")
            print(f"Download Speed: {downspeed} Mbps, Upload Speed: {upspeed} Mbps")

            time.sleep(interval)

