import asyncio
import pandas as pd
import numpy as np

class EnergyMonitor:

    def __init__(self, days=7):
        self.days = days
        self.df = self.generation_data()


    def generation_data(self):
        rng_arr = np.random.randint(100, 1001, self.days)
        data = {'Day': [f"День {i + 1}" for i in range(self.days)],
                'Consumption': rng_arr}
        return pd.DataFrame(data)

    def average_value(self):
        avg = self.df['Consumption'].mean()
        print(f"Среднее потребление электроэнергии: {avg}")

    async def display_data(self):
        for _,row in self.df.iterrows():
            await asyncio.sleep(0.5)
            print(f"День: {row['Day']}, Потребление: {row['Consumption']}")

    def peak_consumption(self):
        peak = self.df[
            self.df['Consumption'] > 500
        ]
        return peak

    async def analyze_data(self):
        await self.display_data()
        self.average_value()
        peak = self.peak_consumption()
        print("\n Пик потребления электроэнергии (>500кВт/ч):")
        for _,row in peak.iterrows():
            await asyncio.sleep(0.5)
            print(f"День: {row['Day']}, Потребление: {row['Consumption']}")
        self.df.to_csv('energy_data.csv', index=False)
        print("Данные сохранены в energy_data.csv")