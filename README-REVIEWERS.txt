App Store Review — Modbus TCP demo (macOS)

Goal
  Let the app connect to a real Modbus TCP server on the SAME Mac used for review,
  so all read/poll/traffic/log features can be exercised.

Step 1 — Start the demo server (Terminal)
  cd to the folder containing this file and run:

    python3 -m pip install --user pymodbus
    python3 run_modbus_demo_server.py

  The server listens on 0.0.0.0:5020 (no root / no port 502 privilege needed).

Step 2 — Open the sample project in the app
  Download and open (File → Open, or double-click if associated):

    ModbusTool-AppStoreReview.sample.modbus

  Connection is preset to:
    Host: 127.0.0.1
    Port: 5020

Step 3 — Verify features
  - Connection Setup: Connect
  - Read / Poll the row "Holding 0 (review)" — expected raw value 66 (0x0042)
  - Open Communication Traffic / log window
  - Save project (optional)

Support
  Email: 1159788905@qq.com
