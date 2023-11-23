import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker

def plot_graph(csv_filename):
    times = []
    download = []
    upload = []

    with open(csv_filename, "r") as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)

        for row in plots:
            times.append(row[0])
            download.append(float(row[1]))
            upload.append(float(row[2]))

    # print(times, "\n", download, "\n", upload)


    plt.figure(figsize=(10,5))

    # Plot download speed
    plt.plot(times, download, label='Download Speed (Mbps)', marker='o')

    # Plot upload speed
    plt.plot(times, upload, label='Upload Speed (Mbps)', marker='o')

    # Formatting the plot
    plt.xlabel('Time')
    plt.ylabel('Speed (Mbps)')
    plt.title('Internet Speed Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    plt.savefig('internet_speed_plot.png', bbox_inches='tight')

    # # Show the plot
    # plt.show()