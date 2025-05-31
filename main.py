import asyncio
from energy_monitor import EnergyMonitor

async def main():
    monitor = EnergyMonitor()
    await monitor.analyze_data()

if __name__ == "__main__":
    asyncio.run(main())