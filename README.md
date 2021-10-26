# TrashCanMonitor

Monitors your [`5G21-12W-A High-Speed Internet Gateway device`](https://www.t-mobile.com/support/public-files/attachments/T-Mobile%20High-Speed%20Internet%20Gateway%20End%20User%20Guide.pdf). Writes a log as a CSV (comma-separated values) file.

# Firmware Version

This software may need to be updated for newer gateway device firmware versions. It has been tested with version 1.2101.00.1609.

# Copyright

TrashCanMonitor &#169; Copyright 2021, [`Eric Bergman-Terrell`](https://www.ericbt.com)

# Links

* [`website`](https://www.ericbt.com/)
* [`GitHub repo`](https://github.com/EricTerrell/TrashCanMonitor)

# Quick Start

1. Install [`Python 3`](https://www.python.org/). TrashCanMonitor was developed and tested with Python version 3.9.1.
1. Install required modules: 
   1. Windows users: just run the install-modules.bat file in a command shell
   1. Otherwise, run the following commands in a command shell:
       1. python -m pip install dnspython
       1. python -m pip install dnspython3
       1. python -m pip install pythonping
       1. python -m pip install requests
1. In a command shell, navigate to the TrashCanMonitor source code folder.
1. python ./main.py {seconds between samples} {log (csv) file path, e.g. "c:\temp\trashcan-stats.csv"}

# License

[`GPL3`](https://www.gnu.org/licenses/gpl-3.0.en.html)

# Feedback

Please submit your feedback to TrashCanMonitor@EricBT.com.

# CSV File Imported into Spreadsheet

![`Spreadsheet`](https://ericbt.com/uploaded_images/trashcanspreadsheet.png "Spreadsheet")

# The Author's 5G21-12W-A

![`5G21-12W-A High-Speed Internet Gateway`](https://ericbt.com/uploaded_images/5G21-12W-A-SMALL.jpg "5G21-12W-A")
