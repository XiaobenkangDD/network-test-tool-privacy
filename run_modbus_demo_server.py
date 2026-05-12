#!/usr/bin/env python3
"""
Minimal Modbus TCP holding-register demo server for App Review / local testing.
Listens on 0.0.0.0:5020 (non-privileged port; avoids macOS root requirement for port 502).

Usage (from this directory):
  python3 -m pip install --user pymodbus
  python3 run_modbus_demo_server.py

Then open the sample project ModbusTool-AppStoreReview.sample.modbus in the app
and connect to 127.0.0.1:5020 (already set in the file).
"""
from __future__ import annotations

try:
    from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
    from pymodbus.server import StartTcpServer
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "Missing dependency: pymodbus\n"
        "Install with: python3 -m pip install --user pymodbus\n"
        f"Import error: {e}"
    ) from e


def main() -> None:
    # pymodbus maps FC03 address 0 to internal offset 1; index 0 is unused padding.
    # Holding register 0 therefore reads values[1] == 0x0042 (66 decimal).
    hr = ModbusSequentialDataBlock(0, [0, 0x0042] + [0] * 126)
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0] * 128),
        co=ModbusSequentialDataBlock(0, [0] * 128),
        hr=hr,
        ir=ModbusSequentialDataBlock(0, [0] * 128),
    )
    context = ModbusServerContext(slaves=store, single=True)
    addr = ("0.0.0.0", 5020)
    print(f"Modbus TCP demo server listening on {addr[0]}:{addr[1]} (FC03 holding address 0 → value 66 / 0x0042)")
    print("Press Ctrl+C to stop.")
    StartTcpServer(context=context, address=addr)


if __name__ == "__main__":
    main()
