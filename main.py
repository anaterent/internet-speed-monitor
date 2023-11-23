import monitor
import make_graph
import threading

def main():
    duration = 60 * 2  # For example, run for 2mins
    interval = 10  # Measure every 10 seconds
    csv_filename = "record.csv"

    # Start the speedtest in a separate thread
    speedtest_thread = threading.Thread(target=monitor.run_speedtest, args=(duration, interval, csv_filename))
    speedtest_thread.start()

    # Wait for the speedtest to complete
    speedtest_thread.join()

    # Once the speedtest is done, plot the graph
    make_graph.plot_graph(csv_filename)

if __name__ == "__main__":
    main()