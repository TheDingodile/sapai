from pyinstrument import Profiler
import main  # Import your main script

def profile_main():
    profiler = Profiler()
    profiler.start()

    # Call the function you want to profile
    main.timing_test()

    profiler.stop()

    # Display the report in the console
    print(profiler.output_text(unicode=True, color=True))
    
    # Save the report to an HTML file
    with open("performance_report.html", "w") as f:
        f.write(profiler.output_html())

if __name__ == "__main__":
    profile_main()